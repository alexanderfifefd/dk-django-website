from dataclasses import dataclass
from datetime import date
from pathlib import Path

import frontmatter
from pydantic import ValidationError

from pages.models import Member
from pages.sources.errors import IngestReport
from pages.sources.articles.schema import ArticleFrontmatter
from pages.sources.markdown import render_markdown
from pages.sources.validation import format_validation_error


@dataclass(frozen=True)
class ArticleRecord:
    slug: str
    title: str
    date: date
    author_username: str
    system_slug: str | None
    summary: str
    body_html: str


def load_all_articles(
    blog_dir: Path,
    members: dict[str, Member],
    system_slugs: set[str],
    report: IngestReport,
) -> list[ArticleRecord]:
    if not blog_dir.is_dir():
        return []

    records: list[ArticleRecord] = []
    for path in sorted(blog_dir.glob("*.md")):
        record = _load_article(path, members, system_slugs, report)
        if record is not None:
            records.append(record)

    return records


def _load_article(
    path: Path,
    members: dict[str, Member],
    system_slugs: set[str],
    report: IngestReport,
) -> ArticleRecord | None:
    label = f"blog/{path.name}"
    parsed = frontmatter.load(path)

    try:
        frontmatter_data = ArticleFrontmatter.model_validate(parsed.metadata)
    except ValidationError as exc:
        report.add(label, format_validation_error(exc))
        return None

    if frontmatter_data.draft:
        return None

    if frontmatter_data.author not in members:
        report.add(label, f"unknown author {frontmatter_data.author!r}")
        return None

    if frontmatter_data.system and frontmatter_data.system not in system_slugs:
        report.add(label, f"unknown system {frontmatter_data.system!r}")
        return None

    return ArticleRecord(
        slug=path.stem,
        title=frontmatter_data.title,
        date=frontmatter_data.date,
        author_username=frontmatter_data.author,
        system_slug=frontmatter_data.system,
        summary=frontmatter_data.summary,
        body_html=render_markdown(parsed.content),
    )
