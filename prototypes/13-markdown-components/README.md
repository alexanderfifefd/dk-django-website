# Datakollektivet — markdown components (prototype 13)

Fork of [prototype 11](../11-site-design/) with ingest-time article shortcodes: callout, CTA banner, and
syntax-highlighted code. Same routes and palette — article authoring gains reusable components.

**Project docs:** `docs/projects/13-markdown-components/`

## Quick start

From this directory:

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py load_articles      # optional — dev middleware syncs on first request too
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/articles/markdown-features/ for the authoring reference.

## Content loading

Articles live in `content/articles/` and sync into sqlite. In `DEBUG`, markdown is re-loaded on every
request. Manual sync:

```bash
uv run python manage.py load_articles
```

## Author syntax

See `content/articles/markdown-features.md` and
`docs/projects/13-markdown-components/discussions/v1-component-syntax.md`.

| Component | Syntax |
| --- | --- |
| Callout | `:::callout type="note"` … `:::` (`note`, `warning`, `tip`) |
| CTA banner | `:::cta` with YAML: `header`, `subheader`, `button`, `url` |
| Highlighted code | Standard ` ```python ` fenced blocks (Pygments via `codehilite`) |

Article callout is planned (render-time) — see `docs/projects/13-markdown-components/discussions/article-callout.md`.

Shortcodes expand to static HTML when `load_articles` runs. The article template still uses
`{{ article.body_html|safe }}` — no render pass.

## What changed from prototype 11

- `public/loaders/shortcodes/` — package with registry (`callout`, `cta`) and expand engine
- `public/loaders/common.py` — shortcode pre-process + `codehilite`
- `static/css/site.css` — callout, article CTA, highlight token colors
- `content/articles/markdown-features.md` — showcase / style guide article

## Layout

Same as prototype 11 — see `prototypes/10-first-version/README.md` for templates, loaders, and language
conventions.
