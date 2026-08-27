# Datakollektivet — CSS structure (prototype 15)

Fork of [prototype 14](../14-design-elements/) — same pages and visual language; this prototype refactors **how CSS is organised** (files, tokens, load order) without re-opening design exploration.

**Project docs:** `docs/projects/15-css-structure/`

## Quick start

From this directory:

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py load_articles      # optional — dev middleware syncs on first request too
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/ — **Component catalog:** http://127.0.0.1:8000/design-lab/

## What changed from prototype 14

The CSS refactor landed 2026-08-27 (same visual language, new structure):

- **Six-file layer split** — `tokens → base → layout → components → pages` (+ `catalog.css` on the catalog route only). Load order and placement rules in `static/css/README.md`.
- **Token system** — palette + semantic layers in `tokens.css`; the only file with hex.
- **Generic names** — `btn` / `card` / `panel` replace `btn-nt` / `panel-nt` / `win-nt`; `hero--inverted` replaces `hero--night`; legacy rounded `.btn` deleted.
- **Component catalog** — `/design-lab/` rebuilt storybook-style (foundations, buttons, cards, panel, forms, chrome, content patterns).
- **Design tweaks** — article lists are cards, forms use sunken-bevel fields, the stripe also closes the page bottom, nav first-letter marks are HTML spans.

Reasoning in `docs/projects/15-css-structure/`; prototype 14 design decisions remain in `docs/projects/14-design-elements/`.

## Layout

Same as prototype 14 — see `prototypes/14-design-elements/README.md` for articles, loaders, and language conventions.
