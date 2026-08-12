# Site UI

**Question:** How should we present systems, members, articles, and updates on the collective homepage?

**Status:** Active — prototype built; UI and content work in progress (2026-08-12).

**Prototype:** `prototypes/06-site-ui/`

## Current approach

Markdown in git is still the authoring layer. Content syncs into derived ORM tables via
`pages/sources/`; **dev middleware** re-syncs on every request so edits show on reload without a
manual sync step.

Started without the ORM for speed; [pivoted back](./discussions/orm-pivot-for-ui-queries.md) once UI
features needed real relationships (system leads on members index, org groups, org roles).

**Out of scope:** forge issues/PRs, identity linking, auth, deployment.

## Content in place

| Collection | Location | Notes |
|---|---|---|
| Members | `content/members/<nick>.md` | Lowercase slug = nick; `name`, optional `role`, `groups: [...]` |
| Groups | `content/members/groups.yaml` | Vocabulary (`board`, `maintainers`); membership on member files |
| Systems | `content/systems/<slug>/` | `system.md` + `updates.json`; teamlead + admins |
| Articles | `content/articles/<slug>.md` | author, optional system, draft flag |

Real data: 9 members, 5 systems, 2 groups, 1 article. No placeholder alice/bob/atlas content remains.

## Pages shipped

Home, systems index/detail, members index/detail, articles index/detail. CSS is prototype 03 baseline —
expected to change substantially.

## How to read this project

1. [ui-without-ingest.md](./discussions/ui-without-ingest.md) — original decision (per-request parsing)
2. [orm-pivot-for-ui-queries.md](./discussions/orm-pivot-for-ui-queries.md) — **current architecture**, extensions, considerations
3. [2026-08-12-prototype-06-site-ui.md](./plans/2026-08-12-prototype-06-site-ui.md) — plan and outcome

## File index

### Discussions

| File | Summary |
|---|---|
| [ui-without-ingest.md](./discussions/ui-without-ingest.md) | Original decision: defer ingest/ORM; parse per request. Superseded for architecture by ORM pivot. |
| [orm-pivot-for-ui-queries.md](./discussions/orm-pivot-for-ui-queries.md) | **Current.** ORM + dev auto-sync; groups/roles; learnings and open considerations. |

### Plans

| File | Summary |
|---|---|
| [2026-08-12-prototype-06-site-ui.md](./plans/2026-08-12-prototype-06-site-ui.md) | Plan, outcome, and status for continuing UI work. |

## Related docs

- `docs/organizational-context.md` — the nouns this prototype presents
- `docs/projects/integration-layer/` — ingest pattern this prototype now follows
- `docs/projects/index.md` — repo-wide project list
