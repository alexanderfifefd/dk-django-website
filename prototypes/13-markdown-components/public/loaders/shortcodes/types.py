"""Types shared by the shortcode engine and components."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class Block:
    name: str
    header: str
    body: str


@dataclass(frozen=True)
class Context:
    label: str
    render_markdown: Callable[[str], str]


RenderFn = Callable[[Block, Context], str]
