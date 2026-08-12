# Plan: prototype 06 — site UI

**Project**: `site-ui`
**Discussion**: `docs/projects/site-ui/discussions/ui-without-ingest.md` (original),
`docs/projects/site-ui/discussions/orm-pivot-for-ui-queries.md` (current)
**Context**: `docs/organizational-context.md`
**Prototype directory**: `prototypes/06-site-ui/`
**Status**: active — UI and content work continuing

## Goal

A UI-focused prototype of the collective homepage. Real markdown content on disk, templates we can
redesign freely. Authored nouns only — no forge sync, no identity plumbing.

## Content model

```
content/
  members/
    groups.yaml           # group slug → title (board, maintainers)
    <nick>.md             # name, role, groups, bio body
  systems/<slug>/
    system.md             # title, summary, teamlead, admins; body = marketing page
    updates.json          # [{date, kind, message}, ...]
  articles/<slug>.md      # title, date, author, optional system, summary, draft
```

Member filename = lowercase nick (canonical slug). Org `role` and `groups` are collective-level;
`teamlead` / `admins` on each system are system-level accountability.

## Architecture (current)

- **Models:** `Group`, `Member`, `System`, `Article` in `pages/models.py`
- **Ingest:** `pages/sources/` — one module per collection; `sync_content` runs groups → members →
  systems → articles
- **Dev freshness:** `ContentSyncMiddleware` calls `sync_content` on every request (DEBUG)
- **Views:** ORM queries with `select_related` / `prefetch_related`

First-time setup:

```bash
uv sync
cd prototypes/06-site-ui
uv run python manage.py migrate
uv run python manage.py runserver
```

## Scope

**Done**

- All pages: home, systems, members, articles (index + detail)
- Real member and system data; org groups and roles
- Members index shows org role/groups + systems led/administered
- One article (`building-the-collective-homepage.md`)
- ORM pivot; `pages/content.py` removed

**In progress / next**

- UI design — layout, typography, hierarchy (CSS still prototype 03 baseline)
- Member bios, system copy, updates, more articles
- Group/role presentation polish
- Home page composition

**Out**

- Forge issues/PRs, `identities` map, external fixtures
- Admin, auth, pagination, search, deployment, production sync policy

## How we know it worked

- `migrate`, `runserver` — middleware syncs; edit content, reload, change appears
- Sync errors show readable HTML error page in dev
- System detail: team, updates, related articles
- Member detail: role, groups, systems led/administered, articles
- Members index: role, groups, system roles inline

## Outcome

**Phase 1 (2026-08-12):** Per-request parsing prototype validated page inventory and content shapes.
Real production data loaded.

**Phase 2 (2026-08-12):** ORM restored with dev auto-sync. Groups (`groups.yaml` + member frontmatter)
and org roles added. Manual query layer removed.

## Considerations when resuming

- **Docs vs code:** `ui-without-ingest.md` records the original bet; architecture is now in
  `orm-pivot-for-ui-queries.md`.
- **UI is the remaining work** — data path is settled enough to focus on templates and CSS.
- **Forge presentation** is a follow-up once authored-noun UI stabilises; templates here are the base.
- **Case-sensitive slugs:** member files must be lowercase; careful on macOS renames.
- **Do not delete `db.sqlite3` casually** — it rebuilds from content, but migrate is still required on
  fresh checkout.
