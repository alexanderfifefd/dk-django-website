# Prototype 04 — forge issues

Does the ingest pattern extend to a forge's HTTP API?

**Project docs:** `docs/projects/04-forge-issues/`

## Quick start

```bash
uv sync                                    # once, from the monorepo root
uv run python manage.py migrate
uv run python manage.py sync_members
uv run python manage.py sync_systems
uv run python manage.py sync_issues      # optional — needs network
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Content loading

Git-owned content:

```bash
uv run python manage.py sync_members
uv run python manage.py sync_systems
```

Forge issues and pull requests (optional — calls the configured Forgejo API; set `FORGEJO_TOKEN` if
required):

```bash
uv run python manage.py sync_issues
```
