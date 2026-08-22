# Plan: shortcode package split

**Project:** `markdown-components`
**Discussion:** [shortcode-registry.md](../discussions/shortcode-registry.md)
**Prototype:** `prototypes/13-markdown-components/`
**Status:** complete (2026-08-22)

## Goal

Replace single `shortcodes.py` with a registry-based package — one module per ingest shortcode.

## Done

- `public/loaders/shortcodes/` package with `engine`, `registry`, `callout`, `cta`
- Import path unchanged: `from public.loaders.shortcodes import expand_shortcodes`

## Verify

```bash
cd prototypes/13-markdown-components
uv run python manage.py load_articles
```

- All articles load; callouts and CTA render
- Unknown `:::foo` fails sync with clear error

## Outcome

Complete. Reasoning: [shortcode-registry.md](../discussions/shortcode-registry.md).
