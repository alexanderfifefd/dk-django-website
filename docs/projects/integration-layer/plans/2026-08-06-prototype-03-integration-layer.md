# Plan: prototype 03 — the collective's homepage

**Project**: `integration-layer`
**Discussion**: `docs/projects/integration-layer/discussions/collections-relationships-and-freshness.md`
**Context**: `docs/organizational-context.md`
**Prototype directory**: `prototypes/03-integration-layer/`
**Status**: not started

## Goal

The software collective's homepage, built as an integration layer: members cached from a Keycloak-shaped
source, systems and articles from git, updates as JSON deliberately kept out of the ORM. Stress the ingest
pattern with relationships, cross-source references, and a dev loop without manual ingest.

## Content model

```
content/
  systems/<slug>/
    system.md          # System: title, summary, teamlead, admins; body = marketing page
    updates.json       # list of {date, kind, message} -> System.updates JSONField
  blog/*.md            # Article: title, date, author, optional system, summary, draft
fixtures/
  members.json         # Keycloak-shaped user list
```

Models: `Member` (username, name — cached, nothing in git creates one), `System` (slug, title, summary,
body_html, `teamlead` FK, `admins` M2M, `updates` JSONField), `Article` (slug, title, date, `author` FK,
`system` FK nullable, summary, body_html). Owned tables (auth) coexist and survive re-ingest.

## Scope

In:

- `manage.py sync_members` — reads a Keycloak-shaped JSON list from a settings-configured file path or
  URL (fixture by default). Separate command on purpose: freshness is per-source.
- `manage.py ingest` — the file collections. Members must already be synced; a file naming an unknown
  member or system slug aborts with file and reference named. Malformed `updates.json` aborts the same
  way. Strict as prototype 02, plus sync of removals. `--flush`.
- Dev middleware (DEBUG only): re-run the file ingest per request, skipped when no content mtime changed;
  ingest failures render as a readable error page, not a 500.
- Pages: home (the collective, latest articles, recent updates merged across systems in Python), systems
  index, system detail (marketing body, team, updates, related articles), blog index/detail, member
  detail (leads / administers / wrote). Read-only admin as inspection window. Prototype 02's CSS style.

Out:

- Real Keycloak; webhooks; scheduled sync (documented story only). Authorization from roles. Editing via
  admin. Pagination, search, scale.
- A generic loader/collection framework — write the collections concretely, note the repetition in the
  outcome.

## How we know it worked

- Fresh checkout: `uv sync`, `migrate`, `sync_members`, `ingest`, `runserver` — everything renders.
- A system's detail page shows its team (from the member cache), its updates (from JSON), and articles
  that reference it; a member page shows what they lead, administer, and wrote.
- An article with an unknown `author` or `system`, or a `system.md` naming a member absent from the
  cache, aborts ingest naming the file and the bad reference.
- With the server running: edit `system.md` or `updates.json`, reload the browser, see the change — no
  command. Break frontmatter or JSON, reload: readable error page; fix, reload, site is back.
- `--flush` + `sync_members` + `ingest` reproduces identical content; the admin superuser survives.
- Outcome must answer honestly: did updates-as-JSONField hurt anywhere (the ORM-or-not probe), and how
  much sync code do the collections share (the framework itch)?
