# Datakollektivet — site design (prototype 11)

Fork of [prototype 10](../10-first-version/) with the warm brand palette applied in CSS. Same routes,
templates, and content — only visual tokens differ.

**Project docs:** `docs/projects/11-site-design/`

## Quick start

From this directory:

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

Compare with prototype 10 (`prototypes/10-first-version/`) to see palette vs generic blue tokens.

Header chrome: single peach rule under sticky header. Home dividers use the same `--rule-peach`.

## What changed from prototype 10

- `static/css/site.css` — cream background, espresso text, sage / peach / clay accents
- Everything else is unchanged (copied from prototype 10 at fork time)

## Layout

Same as prototype 10 — see `prototypes/10-first-version/README.md` for articles, loaders, and language
conventions.
