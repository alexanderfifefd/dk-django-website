"""Articles under ``content/articles/*.md``."""

import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import frontmatter
from django.conf import settings
from django.db import transaction
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator

from public.models import Article
from public.loaders.common import SyncResult, abort_if, format_validation_error, render_markdown


class ArticleFrontmatter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    date: dt.date
    author: str
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


def load_articles(articles_dir: Path, errors: list[str]) -> list[ArticleRecord]:
    records = []
    if not articles_dir.is_dir():
        return records

    for path in sorted(articles_dir.glob("*.md")):
        record = _load_article(path, errors)
        if record is not None:
            records.append(record)

    return records


def _load_article(path: Path, errors: list[str]) -> ArticleRecord | None:
    label = f"articles/{path.name}"

    parsed = frontmatter.load(path)
    try:
        meta = ArticleFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        errors.append(f"{label}: {format_validation_error(exc)}")
        return None

    if meta.draft:
        return None

    return ArticleRecord(slug=path.stem, meta=meta, body_html=render_markdown(parsed.content))


def sync_articles(records: list[ArticleRecord]) -> SyncResult:
    with transaction.atomic():
        for record in records:
            Article.objects.update_or_create(
                slug=record.slug,
                defaults={
                    "title": record.meta.title,
                    "date": record.meta.date,
                    "author": record.meta.author,
                    "summary": record.meta.summary,
                    "body_html": record.body_html,
                },
            )

        removed, _ = Article.objects.exclude(
            slug__in=[record.slug for record in records]
        ).delete()

    return SyncResult(upserted=len(records), removed=removed)


def run_sync_articles(*, flush: bool = False) -> SyncResult:
    errors: list[str] = []
    records = load_articles(settings.CONTENT_DIR / "articles", errors)
    abort_if(errors, "sync_content")

    if flush:
        Article.objects.all().delete()

    return sync_articles(records)
