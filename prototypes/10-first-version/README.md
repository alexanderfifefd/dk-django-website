# Datakollektivet — public site

Django homepage for Datakollektivet. Articles are markdown files in git; everything else is
server-rendered HTML templates. One app (`public`) holds all visitor-facing code.

## Quick start

From this directory (Python env setup is TBD when this repo stands alone; today it uses the parent
monorepo’s shared `uv` environment):

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

In `DEBUG`, article markdown is re-synced from disk on every request — edit a file in
`content/articles/`, reload the browser, and the change appears. You can also sync manually:

```bash
uv run python manage.py load_articles
```

## Project layout

```
config/                 # Django project settings and root URLs
public/                 # single app — all public-site code
  loaders/              # git-owned markdown → ORM sync
  templates/public/
    layouts/            # pages extend base.html
    partials/           # header, footer — included by base
    articles/
    join/
  views.py
  models.py
  middleware.py
content/articles/       # article markdown (authoring layer)
static/                 # CSS, logos
```

A future logged-in area is expected to be a separate Django app (e.g. `portal`), not more apps
inside `public`.

## Adding articles

Create or edit `content/articles/<slug>.md`:

```yaml
---
title: Example post
date: 2026-08-21
author: Alex
summary: Optional deck line shown in lists.
draft: false
---

Body markdown here.
```

- **Slug** — filename without `.md`; becomes the URL `/articles/<slug>/`.
- **`draft: true`** — file is skipped on sync; useful for work in progress.
- **`author`** — plain string for now (no member profiles in this version).

Invalid frontmatter aborts sync with an error page in dev.

## How it works

Markdown in `content/articles/` is the source of truth authors edit. On each request in dev (or via
`load_articles`), loaders validate frontmatter, render markdown to HTML, and upsert an `Article` row in
sqlite. Views query the ORM like any Django app. Static pages (home, about, join) are template HTML
only — not markdown files.

## Language

**Do not mix languages across the human/machine boundary.**

| Language | Written by | Used for |
|---|---|---|
| **English** | Machines | Code, comments, commit messages, template/UI copy, article content in git |
| **Norwegian** | Humans | Human-facing prose where Norwegian is the intentional voice |

Pick one language per artifact. If user-visible copy is English, keep it English throughout that
page or post; do not blend in Norwegian strings (or the reverse).
