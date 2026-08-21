# Prototype 06 — site UI

Present systems, members, articles, and updates — authored content synced from git to the ORM.

**Project docs:** `docs/projects/06-site-ui/`

## Quick start

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Content loading

In `DEBUG`, content is re-synced from `content/` on **every request** — no manual step needed for
local browsing. To sync explicitly (or if `DEBUG` is off):

```bash
uv run python manage.py sync_content
```

Use `--flush` to wipe derived rows and rebuild from scratch.
