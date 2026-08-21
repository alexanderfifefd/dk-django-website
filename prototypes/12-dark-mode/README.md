# Datakollektivet — dark mode (prototype 12)

Fork of [prototype 11](../11-site-design/) with the dark brand palette applied in CSS. Same routes,
templates, and content — only visual tokens differ.

**Project docs:** `docs/projects/12-dark-mode/`

## Quick start

From this directory:

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py load_articles      # optional — dev middleware syncs on first request too
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

Compare with prototype 11 (`prototypes/11-site-design/`) for dark vs light palette on the same pages.

## Content loading

Same as prototype 11 — articles live in `content/articles/` and sync into sqlite. In `DEBUG`, markdown
is re-loaded on every request. Manual sync:

```bash
uv run python manage.py load_articles
```

See `prototypes/10-first-version/README.md` for article frontmatter and layout detail.

## What changed from prototype 11

- `static/css/site.css` — charcoal background, cream text, mint / peach / terracotta accents
- Logo PNGs → `logo-dark-theme.png` / `logo-dark-theme-small.png` in header and footer
- Everything else is unchanged (copied from prototype 11 at fork time)

## Layout

Same as prototype 10/11 — see `prototypes/10-first-version/README.md` for articles, loaders, and language
conventions.
