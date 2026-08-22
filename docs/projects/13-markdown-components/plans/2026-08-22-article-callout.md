# Plan: article callout shortcode

**Project:** `markdown-components`
**Discussion:** [article-callout.md](../discussions/article-callout.md)
**Prototype:** `prototypes/13-markdown-components/`
**Status:** planned (2026-08-22)

## Goal

Article link card in markdown — slug in, title + summary from ORM at render time.

## Approach

See [article-callout.md](../discussions/article-callout.md) for the ingest-vs-render decision.

1. Ingest handler — validate slug, emit `data-article-slug` placeholder
2. `shortcodes/live/` or `resolve_live_shortcodes()` — ORM lookup, emit card HTML
3. Wire in `article_detail` view or `|resolve_shortcodes` filter
4. CSS `.article-callout`
5. Showcase section in `markdown-features.md`
6. Optional: `validate_articles` command for slug checks at CI

## Verify

- `/articles/markdown-features/` shows live title/summary
- Target frontmatter edit updates card without re-syncing linking articles
- Unknown slug behaviour documented and implemented

## Depends on

- [2026-08-22-shortcode-package-split.md](./2026-08-22-shortcode-package-split.md) — complete

## Outcome

Not started. Ingest-only prototype reverted 2026-08-22.
