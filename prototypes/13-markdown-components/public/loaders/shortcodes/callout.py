"""``:::callout type="note"`` — styled aside with markdown body."""

from __future__ import annotations

import re

from public.loaders.shortcodes.errors import ShortcodeError
from public.loaders.shortcodes.types import Block, Context

TYPE_RE = re.compile(r"""type=["']?(\w+)["']?""")
CALLOUT_TYPES = frozenset({"note", "warning", "tip"})


def render(block: Block, ctx: Context) -> str:
    kind = _callout_type(block.header)
    inner = ctx.render_markdown(block.body.strip())
    return f'<aside class="callout callout-{kind}" role="note">{inner}</aside>'


def _callout_type(header: str) -> str:
    match = TYPE_RE.search(header)
    if not match:
        raise ShortcodeError("callout: missing type= attribute")

    kind = match.group(1)
    if kind not in CALLOUT_TYPES:
        allowed = ", ".join(sorted(CALLOUT_TYPES))
        raise ShortcodeError(f"callout: type must be one of {allowed}")
    return kind
