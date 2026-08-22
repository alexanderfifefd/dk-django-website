"""Registered shortcode handlers."""

from public.loaders.shortcodes import callout, cta
from public.loaders.shortcodes.types import RenderFn

HANDLERS: dict[str, RenderFn] = {
    "callout": callout.render,
    "cta": cta.render,
}
