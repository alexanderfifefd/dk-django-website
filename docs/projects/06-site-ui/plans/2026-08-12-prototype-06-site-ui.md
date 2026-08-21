# Plan: prototype 06 — site UI

**Project**: `site-ui`
**Discussion**: `docs/projects/06-site-ui/discussions/ui-without-ingest.md` (original),
`docs/projects/06-site-ui/discussions/orm-pivot-for-ui-queries.md` (current)
**Context**: `docs/organizational-context.md`
**Prototype directory**: `prototypes/06-site-ui/`
**Status**: paused — UI baseline validated (2026-08-12)

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
    system.md             # title, summary, stage, url, teamlead, admins; body = marketing page
    updates.json          # [{date, kind, message}, ...]
  articles/<slug>.md      # title, date, author, optional system, summary, draft
static/
  css/site.css
  img/logo-light-theme.png
```

Member filename = lowercase nick (canonical slug). Org `role` and `groups` are collective-level;
`teamlead` / `admins` on each system are system-level accountability.

System **`stage`**: `suggestion` | `development` | `production` — lifecycle, not runtime state.

System **`url`**: optional; hostname or full URL for the live service (normalised to `https://` at sync).

## Architecture (current)

- **Models:** `Group`, `Member`, `System`, `Article` in `pages/models.py` (`System.stage` in
  `0002_system_stage`; `System.url` in `0003_system_url`)
- **Ingest:** `pages/sources/` — one module per collection; `sync_content` runs groups → members →
  systems → articles
- **Dev freshness:** `ContentSyncMiddleware` calls `sync_content` on every request (DEBUG)
- **Views:** ORM queries with `select_related` / `prefetch_related`
- **Templates:** `base.html` includes `includes/header.html` and `includes/footer.html`

First-time setup:

```bash
uv sync
cd prototypes/06-site-ui
uv run python manage.py migrate
uv run python manage.py runserver
```

## Scope

**Done**

- All core pages: home, systems, members, articles (index + detail), about, join
- Real member and system data; org groups and roles; board on about page
- Home: hero, systems, latest articles, join CTA
- Header: split nav, centred logo; footer: three-column layout (pages / about / newsletter)
- Article layouts: byline, deck, system badge on index/home/detail
- System detail: header-band metadata (stage, url, team), full-width body, updates, related articles
- Systems index: stage badge and external URL (replaces teamlead line)
- ORM pivot; `pages/content.py` removed
- Listmonk added as `stage: suggestion` system idea
- System URLs for Keycloak, Loomio, Forgejo, Website

**Paused / resume later**

- Typography and visual design polish
- Member bios, system copy, authored updates, more articles
- Group/role presentation beyond current inline text
- Wire up join form and footer newsletter (or link to Listmonk when real)

**Out**

- Forge issues/PRs, `identities` map, external fixtures
- Admin, auth, pagination, search, deployment, production sync policy
- Media in markdown, template tags in markdown — tracked as open questions in `docs/projects/index.md`

## How we know it worked

- `migrate`, `runserver` — middleware syncs; edit content, reload, change appears
- Sync errors show readable HTML error page in dev
- System detail: stage/url/team metadata, updates, related articles
- Member detail: role, groups, systems led/administered, articles
- Members index: role, groups, system roles inline
- All routes smoke-tested: `/`, `/systems/`, `/members/`, `/articles/`, `/about/`, `/join/`

## Outcome

**Phase 1 (2026-08-12):** Per-request parsing prototype validated page inventory and content shapes.
Real production data loaded.

**Phase 2 (2026-08-12):** ORM restored with dev auto-sync. Groups (`groups.yaml` + member frontmatter)
and org roles added. Manual query layer removed.

**Phase 3 (2026-08-12):** UI baseline session — site chrome (logo, header/footer partials, wider layout),
static pages (about, join), home and article layout passes, system `stage` field and detail layout,
Listmonk suggestion, docs updated. Prototype paused here; authored-noun presentation is good enough to
layer forge/identity work onto later.

**Phase 3 follow-up (2026-08-12):** System `url` field — optional hostname in frontmatter, normalised at
sync, shown on systems index and detail. Four production URLs added to content.

## Considerations when resuming

- **Docs vs code:** `ui-without-ingest.md` records the original bet; architecture is in
  `orm-pivot-for-ui-queries.md`; **current UI state** is in `overview.md`.
- **Forge presentation** is a follow-up once more authored content exists; templates here are the base.
- **Case-sensitive slugs:** member files must be lowercase; careful on macOS renames.
- **Fresh checkout:** run `migrate` then `runserver` (middleware syncs content; `db.sqlite3` is derived).
