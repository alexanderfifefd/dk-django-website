"""Articles under ``content/articles/*.md``."""

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from pages.models import Article, Member, System, Initiative
from pages.sources.common import (
    SyncResult,
    abort_if,
    format_validation_error,
    member_cache,
    render_markdown,
    require_members,
)


class ArticleFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    date: dt.date
    author: str
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


@dataclass(frozen=True)
class ArticleRecord:
    slug: str
    meta: ArticleFrontmatter
    body_html: str


def load_articles(
    articles_dir: Path,
    members: dict[str, Member],
    system_slugs: set[str],
    initiative_slugs: set[str],
    errors: list[str],
) -> list[ArticleRecord]:
    records = []
    if not articles_dir.is_dir():
        return records

    for path in sorted(articles_dir.glob("*.md")):
        record = _load_article(path, members, system_slugs, initiative_slugs, errors)
        if record is not None:
            records.append(record)

    return records


def _load_article(
    path: Path,
    members: dict[str, Member],
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

    if meta.author not in members:
        errors.append(f"{label}: unknown author {meta.author!r}")
        return None

    if meta.system and meta.system not in system_slugs:
        errors.append(f"{label}: unknown system {meta.system!r}")
        return None

    if meta.initiative and meta.initiative not in initiative_slugs:
        errors.append(f"{label}: unknown initiative {meta.initiative!r}")
        return None

    return ArticleRecord(slug=path.stem, meta=meta, body_html=render_markdown(parsed.content))


def sync_articles(records: list[ArticleRecord], members: dict[str, Member]) -> SyncResult:
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
            Article.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "date": record.meta.date,
                    "author": members[record.meta.author],
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
    system_slugs = set(System.objects.values_list("slug", flat=True))
    initiative_slugs = set(Initiative.objects.values_list("slug", flat=True))
    errors: list[str] = []
    records = load_articles(
        settings.CONTENT_DIR / "articles",
        members,
        system_slugs,
        initiative_slugs,
        errors,
    )
    abort_if(errors, "sync_articles")

    if flush:
        Article.objects.all().delete()

    return sync_articles(records, members)
