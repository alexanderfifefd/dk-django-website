"""Blog posts as markdown files.

The filesystem is the source of truth: every non-draft ``.md`` file in
``CONTENT_DIR/blog/`` is a post, and its filename is its slug. Files are
read and parsed on every request — deliberately uncached, so edits show
up on reload and we find out what the naive approach costs.
"""

import datetime
from dataclasses import dataclass, field

import frontmatter
import markdown
from django.conf import settings

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty"]


@dataclass
class Post:
    slug: str
    title: str
    date: datetime.date
    tags: list[str] = field(default_factory=list)
    summary: str = ""
    body_html: str = ""


def _blog_dir():
    return settings.CONTENT_DIR / "blog"


def _parse_file(path):
    """Parse one markdown file into a Post, or None for drafts."""
    parsed = frontmatter.load(path)
    if parsed.get("draft", False):
        return None

    date = parsed.get("date")
    if isinstance(date, datetime.datetime):
        date = date.date()
    if not isinstance(date, datetime.date):
        # Undated files still deserve a page; mtime beats crashing.
        date = datetime.date.fromtimestamp(path.stat().st_mtime)

    return Post(
        slug=path.stem,
        title=parsed.get("title", path.stem.replace("-", " ").title()),
        date=date,
        tags=list(parsed.get("tags", [])),
        summary=parsed.get("summary", ""),
        body_html=markdown.markdown(parsed.content, extensions=MARKDOWN_EXTENSIONS),
    )


def all_posts():
    """All non-draft posts, newest first."""
    blog_dir = _blog_dir()
    if not blog_dir.is_dir():
        return []
    posts = [_parse_file(path) for path in sorted(blog_dir.glob("*.md"))]
    return sorted((p for p in posts if p is not None), key=lambda p: p.date, reverse=True)


def get_post(slug):
    """One post by slug, or None if missing or draft."""
    path = (_blog_dir() / f"{slug}.md").resolve()
    # The slug URL converter already forbids path separators; this is a
    # second line of defence against ever serving files outside content/.
    if not path.is_file() or _blog_dir().resolve() not in path.parents:
        return None
    return _parse_file(path)
