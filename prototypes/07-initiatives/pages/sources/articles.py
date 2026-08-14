"""Articles under ``content/articles/*.md``."""

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator, model_validator

from pages.models import Article, Group, Member, System, Initiative
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    group_cache,
    member_cache,
    render_markdown,
    require_members,
)


class ArticleFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    date: dt.date
    author: str | None = None
    author_group: str | None = None
    system: str | None = None
    initiative: str | None = None
    summary: str = ""
    draft: bool = False

    @field_validator("date", mode="before")
    @classmethod
    def _accept_yaml_datetime(cls, value: object) -> object:
        if isinstance(value, dt.datetime):
            return value.date()
        return value

    @model_validator(mode="after")
    def _author_or_group(self) -> "ArticleFrontmatter":
        if not self.author and not self.author_group:
            raise ValueError("author or author_group is required")
        return self


@dataclass(frozen=True)
class ArticleRecord:
    slug: str
    meta: ArticleFrontmatter
    body_html: str


def load_articles(
    articles_dir: Path,
    members: dict[str, Member],
    groups: dict[str, Group],
    system_slugs: set[str],
    initiative_slugs: set[str],
    errors: list[str],
) -> list[ArticleRecord]:
    records = []
    if not articles_dir.is_dir():
        return records

    for path in sorted(articles_dir.glob("*.md")):
        record = _load_article(path, members, groups, system_slugs, initiative_slugs, errors)
        if record is not None:
            records.append(record)

    return records


def _load_article(
    path: Path,
    members: dict[str, Member],
    groups: dict[str, Group],
    system_slugs: set[str],
    initiative_slugs: set[str],
    errors: list[str],
) -> ArticleRecord | None:
    label = f"articles/{path.name}"

    parsed = frontmatter.load(path)
    try:
        meta = ArticleFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    if meta.draft:
        return None

    if meta.author and meta.author not in members:
        errors.append(f"{label}: unknown author {meta.author!r}")
        return None

    if meta.author_group and meta.author_group not in groups:
        errors.append(f"{label}: unknown author_group {meta.author_group!r}")
        return None

    if meta.system and meta.system not in system_slugs:
        errors.append(f"{label}: unknown system {meta.system!r}")
        return None

    if meta.initiative and meta.initiative not in initiative_slugs:
        errors.append(f"{label}: unknown initiative {meta.initiative!r}")
        return None

    return ArticleRecord(slug=path.stem, meta=meta, body_html=render_markdown(parsed.content))


def sync_articles(
    records: list[ArticleRecord],
    members: dict[str, Member],
    groups: dict[str, Group],
) -> SyncResult:
    with transaction.atomic():
        for record in records:
            system = (
                System.objects.get(slug=record.meta.system) if record.meta.system else None
            )
            initiative = (
                Initiative.objects.get(slug=record.meta.initiative)
                if record.meta.initiative
                else None
            )
            author = members[record.meta.author] if record.meta.author else None
            author_group = (
                groups[record.meta.author_group] if record.meta.author_group else None
            )
            Article.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "date": record.meta.date,
                    "author": author,
                    "author_group": author_group,
                    "system": system,
                    "initiative": initiative,
                    "summary": record.meta.summary,
                    "body_html": record.body_html,
                },
            )

        removed, _ = Article.objects.exclude(
            slug__in=[record.slug for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_articles(*, flush: bool = False) -> SyncResult:
    require_members()

    members = member_cache()
    groups = group_cache()
    system_slugs = set(System.objects.values_list("slug", flat=True))
    initiative_slugs = set(Initiative.objects.values_list("slug", flat=True))
    errors: list[str] = []
    records = load_articles(
        settings.CONTENT_DIR / "articles",
        members,
        groups,
        system_slugs,
        initiative_slugs,
        errors,
    )
    abort_if(errors, "sync_articles")

    if flush:
        Article.objects.all().delete()

    return sync_articles(records, members, groups)
