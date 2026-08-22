"""``:::cta`` — banner with header, subheader, button, and url."""

from __future__ import annotations

import html

from pydantic import BaseModel, ConfigDict, ValidationError

from public.loaders.shortcodes.errors import ShortcodeError, parse_yaml_mapping, validation_message
from public.loaders.shortcodes.types import Block, Context


class CtaFields(BaseModel):
    model_config = ConfigDict(extra="forbid")

    header: str
    subheader: str
    button: str
    url: str


def render(block: Block, ctx: Context) -> str:
    del ctx  # static HTML — no markdown body
    fields = _cta_fields(block.body)
    return (
        f'<aside class="article-cta">'
        f'<h2 class="article-cta-header">{html.escape(fields.header)}</h2>'
        f'<p class="article-cta-subheader">{html.escape(fields.subheader)}</p>'
        f'<p><a class="btn btn-primary" href="{html.escape(fields.url, quote=True)}">'
        f"{html.escape(fields.button)}</a></p>"
        f"</aside>"
    )


def _cta_fields(body: str) -> CtaFields:
    data = parse_yaml_mapping(body, name="cta")
    try:
        return CtaFields.model_validate(data)
    except ValidationError as exc:
        raise ShortcodeError(f"cta: {validation_message(exc)}") from exc
