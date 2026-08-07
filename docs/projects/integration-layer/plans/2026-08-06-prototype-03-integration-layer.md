# Plan: prototype 03 — the collective's homepage

**Project**: `integration-layer`
**Discussion**: `docs/projects/integration-layer/discussions/collections-relationships-and-freshness.md`
**Ingest layout**: `docs/projects/integration-layer/discussions/ingest-structure-and-pydantic.md`
**Context**: `docs/organizational-context.md`
**Prototype directory**: `prototypes/03-integration-layer/`
**Status**: built — see Outcome below

## Goal

The software collective's homepage, built as an integration layer: members cached from a Keycloak-shaped
source, systems and articles from git, updates as JSON deliberately kept out of the ORM. Stress the ingest
pattern with relationships and cross-source references.

## Content model

```
content/
  systems/<slug>/
    system.md          # System: title, summary, teamlead, admins; body = marketing page
    updates.json       # list of {date, kind, message} -> System.updates JSONField
  blog/*.md            # Article: title, date, author, optional system, summary, draft
external/
  members.json         # Keycloak-shaped user list (externally owned, synced — not authored content)
```

Models: `Member` (username, name — cached, nothing in git creates one), `System` (slug, title, summary,
body_html, `teamlead` FK, `admins` M2M, `updates` JSONField), `Article` (slug, title, date, `author` FK,
`system` FK nullable, summary, body_html). Owned tables (auth) coexist and survive re-ingest.

## Scope

In:

- `manage.py sync_members` — reads a Keycloak-shaped JSON list from a settings-configured file path
  (``external/members.json`` by default). Separate command on purpose: freshness is per-source.
- `manage.py sync_systems` — syncs ``content/systems/``. Members must already be synced; a ``system.md``
  naming an unknown member aborts with file and reference named. Malformed ``updates.json`` aborts the
  same way. Strict validation, sync of removals. ``--flush``.
- `manage.py sync_articles` — syncs ``content/blog/``. Members (and any named systems) must already be
  synced; dangling references abort the same way. ``--flush``.
- Pages: home (the collective, latest articles, recent updates merged across systems in Python), systems
  index, system detail (marketing body, team, updates, related articles), blog index/detail, member
  detail (leads / administers / wrote). Read-only admin as inspection window. Prototype 02's CSS style.

Out:

- Real Keycloak; webhooks; scheduled sync (documented story only). Authorization from roles. Editing via
  admin. Pagination, search, scale.
- A generic loader/collection framework — write the collections concretely, note the repetition in the
  outcome.

## How we know it worked

- Fresh checkout: `uv sync`, `migrate`, `sync_members`, `sync_systems`, `sync_articles`, `runserver` —
  everything renders.
- A system's detail page shows its team (from the member cache), its updates (from JSON), and articles
  that reference it; a member page shows what they lead, administer, and wrote.
- An article with an unknown `author` or `system`, or a `system.md` naming a member absent from the
  cache, aborts sync naming the file and the bad reference.
- `--flush` on each sync command reproduces identical content; the admin superuser survives.
- Outcome must answer honestly: did updates-as-JSONField hurt anywhere (the ORM-or-not probe), and how
  much sync code do the collections share (the framework itch)?

## Outcome

Built 2026-08-07. All criteria met except the dev middleware items — deliberately out of scope for this
build; save–ingest–reload remains manual here.

- **Multiple collections work.** One `sync_*` command per collection (per-source freshness). Systems,
  articles, and member references validate before any write; dangling refs abort with file and name
  named.
- **Updates-as-JSONField held up.** Home merges recent updates across systems in Python; system detail
  renders the list from the field. No pain yet — the cross-system query is trivial enough not to miss an ORM
  table.
- **Framework itch is visible but not urgent.** Per-collection modules under `pages/sources/`
  (including a separate `updates.py` for JSON that deliberately stays out of the ORM) share a
  validate-then-sync shape, but a generic loader framework is still not justified.
- **Added beyond plan**: no dev middleware (per decision during build).
- **Refactored 2026-08-07**: three `sync_*` commands, one module per collection under
  `pages/sources/` (members, systems, updates, articles — schema, loader, syncer where
  applicable, and `run_sync_*` on the synced collections), Pydantic at the file boundary,
  management commands as thin CLI wrappers. `fixtures/` renamed to `external/`. See the
  ingest-layout discussion.
