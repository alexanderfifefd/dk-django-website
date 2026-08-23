"""Small helpers for article sync."""

from dataclasses import dataclass

import markdown
from django.core.management.base import CommandError
from pydantic import ValidationError

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty"]


def render_markdown(text: str) -> str:
    return markdown.markdown(text, extensions=MARKDOWN_EXTENSIONS)


def format_validation_error(exc: ValidationError) -> str:
    parts = []
    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"]) or "value"
        parts.append(f"{location}: {error['msg']}")
    return "; ".join(parts)


def abort_if(errors: list[str], command: str) -> None:
    if errors:
        raise CommandError(f"{command} aborted, nothing written:\n  " + "\n  ".join(errors))


@dataclass(frozen=True)
class SyncResult:
    upserted: int
    removed: int
