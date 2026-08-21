# Prototype 05 — git identity

Link member profiles to forge activity via git-backed identity assertions in frontmatter.

**Project docs:** `docs/projects/05-git-identity/`

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

Forge issues and pull requests, matched to members by `identities.forgejo` (optional — network;
`FORGEJO_TOKEN` if required):

```bash
uv run python manage.py sync_issues
```
