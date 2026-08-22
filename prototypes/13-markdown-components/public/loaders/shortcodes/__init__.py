"""Expand article shortcodes before markdown runs."""

from __future__ import annotations

from collections.abc import Callable

from public.loaders.shortcodes.engine import expand_shortcodes as _expand_shortcodes
from public.loaders.shortcodes.types import Context


def expand_shortcodes(
    text: str,
    *,
    label: str,
    render_markdown: Callable[[str], str],
) -> tuple[str, list[str]]:
    ctx = Context(label=label, render_markdown=render_markdown)
    return _expand_shortcodes(text, ctx)
