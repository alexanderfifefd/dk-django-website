"""Find ``:::name`` fences and dispatch to registered handlers."""

from __future__ import annotations

import re

from public.loaders.shortcodes.errors import ShortcodeError
from public.loaders.shortcodes.registry import HANDLERS
from public.loaders.shortcodes.types import Block, Context

BLOCK_RE = re.compile(
    r"^:::(\w+)([^\n]*)\n([\s\S]*?)^:::\s*$",
    re.MULTILINE,
)


def expand_shortcodes(text: str, ctx: Context) -> tuple[str, list[str]]:
    errors: list[str] = []
    parts: list[str] = []
    last_end = 0

    for match in BLOCK_RE.finditer(text):
        parts.append(text[last_end : match.start()])
        block = Block(match.group(1), match.group(2).strip(), match.group(3))

        try:
            handler = _handler(block.name)
            parts.append(handler(block, ctx))
        except ShortcodeError as exc:
            errors.append(f"{ctx.label}: {exc}")
            parts.append(match.group(0))

        last_end = match.end()

    parts.append(text[last_end:])
    return "".join(parts), errors


def _handler(name: str):
    try:
        return HANDLERS[name]
    except KeyError as exc:
        allowed = ", ".join(sorted(HANDLERS))
        raise ShortcodeError(f"unknown shortcode {name!r} (expected one of {allowed})") from exc
