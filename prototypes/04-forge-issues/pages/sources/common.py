"""Small helpers shared by every source module."""

from dataclasses import dataclass

import markdown
from django.core.management.base import CommandError
from pydantic import ValidationError

from pages.models import Member

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty"]


def render_markdown(text: str) -> str:
    return markdown.markdown(text, extensions=MARKDOWN_EXTENSIONS)


def format_validation_error(exc: ValidationError) -> str:
    """One readable line per problem, e.g. ``admins.1: Input should be a valid string``."""
    parts = []
    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"]) or "value"
        parts.append(f"{location}: {error['msg']}")
    return "; ".join(parts)


def abort_if(errors: list[str], command: str) -> None:
    if errors:
        raise CommandError(f"{command} aborted, nothing written:\n  " + "\n  ".join(errors))


def require_members() -> None:
    if not Member.objects.exists():
        raise CommandError("no members in the database — run sync_members first")


def member_cache() -> dict[str, Member]:
    return {member.username: member for member in Member.objects.all()}


@dataclass(frozen=True)
class SyncResult:
    upserted: int
    removed: int
