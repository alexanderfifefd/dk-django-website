"""Small helpers for article sync."""

from dataclasses import dataclass

import markdown
from django.core.management.base import CommandError
from pydantic import ValidationError

from public.loaders.shortcodes import expand_shortcodes

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "smarty", "codehilite"]

MARKDOWN_EXTENSION_CONFIGS = {
    "codehilite": {
        "guess_lang": False,
        "no_classes": False,
        "linenums": False,
    },
}


def markdown_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWN_EXTENSION_CONFIGS,
    )


def render_markdown(text: str, *, label: str = "article") -> tuple[str, list[str]]:
    expanded, errors = expand_shortcodes(
        text,
        label=label,
        render_markdown=markdown_to_html,
    )
    if errors:
        return "", errors
    return markdown_to_html(expanded), []


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
