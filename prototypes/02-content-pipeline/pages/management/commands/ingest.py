"""Sync ``content/blog/*.md`` into the Post table.

Files are the source of truth; the table is derived. A run is a full sync:
new files insert, changed files update, and rows whose files are gone (or
turned draft) are deleted. Validation is strict — any bad file aborts the
whole run and the database is left untouched.
"""

import datetime

import frontmatter
import markdown
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from pages.models import Post

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty"]
ALLOWED_KEYS = {"title", "date", "tags", "summary", "draft"}
REQUIRED_KEYS = {"title", "date"}


def parse_file(path):
    """Return a dict of Post fields, or None for drafts.

    Raises ValueError listing every problem in the file.
    """
    parsed = frontmatter.load(path)
    meta = parsed.metadata
    errors = []

    if unknown := set(meta) - ALLOWED_KEYS:
        errors.append(f"unknown keys: {', '.join(sorted(unknown))}")
    if missing := REQUIRED_KEYS - set(meta):
        errors.append(f"missing required keys: {', '.join(sorted(missing))}")

    date = meta.get("date")
    if isinstance(date, datetime.datetime):
        date = date.date()
    if "date" in meta and not isinstance(date, datetime.date):
        errors.append(f"date is not a YAML date (unquoted YYYY-MM-DD): {meta['date']!r}")

    title = meta.get("title")
    if "title" in meta and not isinstance(title, str):
        errors.append(f"title is not a string: {title!r}")

    summary = meta.get("summary", "")
    if not isinstance(summary, str):
        errors.append(f"summary is not a string: {summary!r}")

    tags = meta.get("tags", [])
    if not (isinstance(tags, list) and all(isinstance(t, str) for t in tags)):
        errors.append(f"tags is not a list of strings: {tags!r}")

    draft = meta.get("draft", False)
    if not isinstance(draft, bool):
        errors.append(f"draft is not a boolean: {draft!r}")

    if errors:
        raise ValueError("; ".join(errors))
    if draft:
        return None

    return {
        "slug": path.stem,
        "title": title,
        "date": date,
        "tags": tags,
        "summary": summary,
        "body_html": markdown.markdown(parsed.content, extensions=MARKDOWN_EXTENSIONS),
    }


class Command(BaseCommand):
    help = "Sync content/blog/*.md into the Post table. Files are the source of truth."

    def add_arguments(self, parser):
        parser.add_argument(
            "--flush", action="store_true", help="Delete every post first and rebuild from scratch."
        )

    def handle(self, *args, flush, **options):
        blog_dir = settings.CONTENT_DIR / "blog"
        paths = sorted(blog_dir.glob("*.md")) if blog_dir.is_dir() else []

        posts, errors = [], []
        for path in paths:
            try:
                fields = parse_file(path)
            except ValueError as exc:
                errors.append(f"{path.name}: {exc}")
            else:
                if fields is not None:
                    posts.append(fields)

        if errors:
            raise CommandError("ingest aborted, nothing written:\n  " + "\n  ".join(errors))

        with transaction.atomic():
            if flush:
                Post.objects.all().delete()
            slugs = [fields["slug"] for fields in posts]
            for fields in posts:
                Post.objects.update_or_create(slug=fields["slug"], defaults=fields)
            removed, _ = Post.objects.exclude(slug__in=slugs).delete()

        self.stdout.write(self.style.SUCCESS(f"Ingested {len(slugs)} posts, removed {removed}."))
