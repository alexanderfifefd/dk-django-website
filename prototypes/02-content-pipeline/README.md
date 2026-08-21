# Prototype 02 — content pipeline

Who owns the path from markdown file to page? A management command ingests files into the ORM.

**Project docs:** `docs/projects/02-content-pipeline/`

## Quick start

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py ingest
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Content loading

```bash
uv run python manage.py ingest
```

Syncs `content/blog/*.md` into the `Post` table. Re-run after editing markdown on disk.
