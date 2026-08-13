# Plan: prototype 07 — initiatives

**Project**: `initiatives`
**Discussion**: `docs/projects/initiatives/discussions/initiatives-as-a-noun.md`
**Context**: `docs/organizational-context.md`, `docs/projects/site-ui/` (prototype 06 baseline)
**Prototype directory**: `prototypes/07-initiatives/`
**Status**: in progress

## Goal

Fork prototype 06 and add **initiatives** as a first-class authored noun — goal-oriented efforts
someone drives forward, distinct from systems. Validate content shape, ORM/sync, and UI surfaces without
touching prototype 06.

## Content model

```
content/
  members/ …                          # unchanged from 06
  systems/<slug>/ …                   # unchanged from 06
  initiatives/<slug>/
    initiative.md                     # title, summary, status, start_date, end_date, takers, …; body = pitch
    updates.json                      # [{date, kind, message}, …] — same shape as system updates
  articles/<slug>.md                  # optional initiative FK added (alongside optional system)
```

All slugs and site copy in **English**.

### Initiative frontmatter

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Display title |
| `summary` | no | One-line deck |
| `status` | yes | `proposal`, `seeking-contributors`, `active`, `paused`, `completed` |
| `start_date` | yes | When the initiative started |
| `end_date` | no | When it ended; omit while ongoing. Must be on or after `start_date` |
| `takers` | no | Member slugs; validated against members |
| `systems` | no | System slugs; validated against systems |
| `loomio` | no | Discussion URL |
| `matrix` | no | Room address |

### Seed content (three initiatives)

| Slug | Title | Status | Systems |
|---|---|---|---|
| `governance-documents` | Governance documents | `active` | — |
| `build-sso` | Build SSO | `completed` | keycloak |
| `build-website` | Build website | `active` | website |

## Architecture

- **Fork:** full copy of `prototypes/06-site-ui/` → `prototypes/07-initiatives/`; prototype 06 untouched.
- **Models:** `Initiative` with `updates` JSONField (same shape as `System.updates`); `Article.initiative`
  optional FK.
- **Ingest:** `pages/sources/initiatives.py`; sync order groups → members → systems → **initiatives** →
  articles. Reuse `updates.load_updates()` with a collection label for error paths.
- **Dev freshness:** unchanged — `ContentSyncMiddleware` on every request.
- **Navigation:** left nav — **Systems** and **Initiatives** (Articles / About / Join unchanged on the
  right).

## Scope

**In**

- Initiative index and detail pages (`/initiatives/`, `/initiatives/<slug>/`)
- Updates section on initiative detail (same markup as system updates)
- Status badges on index and detail
- Home: initiatives section (active + seeking-contributors)
- Member detail: initiatives led
- Article optional `initiative` frontmatter + badge in article lists/detail
- CSS for status badges

**Out**

- Initiative creation form — authoring is git-only
- Open areas yaml / "want to start something?" surface
- Forge issues/PRs on initiative pages
- Loomio/Matrix activity ingest
- Auth, deployment, production sync policy

## How we know it worked

```bash
uv sync
cd prototypes/07-initiatives
uv run python manage.py migrate
uv run python manage.py sync_content
uv run python manage.py runserver
```

- Three initiatives sync from `content/initiatives/`
- `/initiatives/` lists all with status badges
- Initiative detail: takers, related systems, updates, related articles, Loomio/Matrix when set
- Header left nav: Systems + Initiatives
- Home shows initiatives section
- Member pages show initiatives led where applicable
- Edit an initiative markdown file, reload — change appears (middleware sync)
- Sync errors (unknown taker/system slug) show readable HTML error in dev

## Outcome

**2026-08-13:** Prototype 07 forked from 06. Initiative model, ingest, three seed initiatives, index and
detail pages, updates on initiative pages, home and member surfaces, Systems + Initiatives left nav.
Article optional `initiative` frontmatter. Prototype 06 untouched.
