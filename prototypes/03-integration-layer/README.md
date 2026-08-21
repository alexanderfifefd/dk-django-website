# Prototype 03 — integration layer

Collections, relationships, and mixed sources (git + external JSON) via separate sync commands.

**Project docs:** `docs/projects/03-integration-layer/`

## Quick start

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py sync_members
uv run python manage.py sync_systems
uv run python manage.py sync_articles
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Content loading

Run in order — later commands validate FKs against earlier ones:

```bash
uv run python manage.py sync_members    # external/members.json
uv run python manage.py sync_systems    # content/systems/
uv run python manage.py sync_articles   # content/blog/
```

Re-run the relevant command after editing source files.
