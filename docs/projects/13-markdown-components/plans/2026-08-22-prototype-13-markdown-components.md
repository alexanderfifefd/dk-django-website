# Plan: prototype 13 — markdown components

**Project:** `markdown-components`
**Discussions:** `docs/projects/13-markdown-components/discussions/`
**Prototype:** `prototypes/13-markdown-components/`
**Status:** built (2026-08-22)

## Goal

Prove that a small set of article components can live in git-authored markdown and expand to static HTML at
sync time — without a render pass or JavaScript.

## Approach

Fork `prototypes/11-site-design/` → `prototypes/13-markdown-components/`.

| Area | Change |
|---|---|
| `public/loaders/common.py` | Shortcode pre-processor + highlighted code extension |
| `public/loaders/shortcodes.py` | New — parse `:::callout`, `:::cta`; Pydantic validation |
| `static/css/site.css` | `.callout-*`, `.article-cta`, code highlight colors |
| `content/articles/markdown-features.md` | Showcase article |
| `pyproject.toml` (repo root) | Add `pygments` if using `codehilite` |

Article detail template unchanged — still `{{ article.body_html|safe }}`.

## Build order

1. Fork prototype 11; update README pointer to this project
2. Implement shortcode parser (callout, CTA) — unit-friendly pure functions first
3. Wire into `render_markdown()` or `_load_article()` pipeline; fail sync on validation errors
4. Add Pygments / `codehilite`; style highlighted blocks
5. Write showcase article covering base markdown + all three components
6. Manual pass in browser on `/articles/markdown-features/`

## Verify

From `prototypes/13-markdown-components/`:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py load_articles
uv run python manage.py runserver
```

- `/articles/markdown-features/` renders callouts, CTA, and highlighted code
- Invalid shortcode in any article shows load error (middleware or command)
- Prototype 11 unchanged

## Success criteria

- Author syntax matches [v1-component-syntax.md](../discussions/v1-component-syntax.md)
- All expansion happens before `body_html` is written to sqlite
- Showcase article is sufficient for a new contributor to learn authoring without reading Python
- No new URL routes or template tags required for v1

## Open follow-ups

- Article callout — render-time; see [article-callout.md](../discussions/article-callout.md)
- Quote pull-styling vs plain blockquote
- Timeline block (same ingest pattern)
- Figure + caption (blocked on media/assets project)
- Port components to prototype 12 dark palette when design catches up
- Render-time expansion for POST forms inside articles
