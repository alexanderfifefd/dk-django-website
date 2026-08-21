# Prototype 01 — markdown pages

Can markdown files on disk be the content layer? Parsed per request — no database sync.

**Project docs:** `docs/projects/01-markdown-pages/`

## Quick start

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Content loading

No sync command. Blog posts are read from `content/blog/*.md` on each request.
