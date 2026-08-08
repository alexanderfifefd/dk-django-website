# Plan: prototype 04 — issues from the forge

**Project**: `forge-issues`
**Discussion**: `docs/projects/forge-issues/discussions/issues-from-the-forge.md`
**Context**: `docs/organizational-context.md`, `docs/high-level-goals.md`
**Prototype directory**: `prototypes/04-forge-issues/`
**Status**: built — see Outcome below

## Goal

The first API-sourced collection: Forgejo issues **and pull requests**, labeled `system/<slug>` in one
monorepo, cached as a derived table next to the git-owned systems. Tests whether the ingest pattern
(source → schema → syncer, per-source command) extends to an HTTP API the site does not own. Issues
attract engagement (rendered as items); PRs communicate alive-ness (rendered as a list with open/closed
signifiers). Both are a new noun beside updates, not a replacement — `updates.json` stays, as the
authored voice (amendment 2026-08-08; see the primitives discussion and "Two voices" in the
organizational context).

## Sources

```
content/
  systems/<slug>/
    system.md          # System: unchanged from prototype 03
    updates.json       # unchanged from prototype 03
external/
  members.json         # unchanged from prototype 03
https://forge.hornwitser.no/alexanrf/public-api-test-repo
                       # issues + pull requests, labeled system/<slug> + plain tags — the new source
```

Settings: `FORGEJO_BASE_URL`, `FORGEJO_REPO`; optional `FORGEJO_TOKEN` env var (anonymous read verified
working — the token path exists but is not required).

Models: `Member`, `System` (with `updates` JSONField) unchanged; `Article` dropped. New `Issue`
(covering PRs too — mirroring the forge's own model, where a PR is an issue with pull metadata):
`number` (unique), `title`, `state` (open/closed), `url`, `system` FK nullable `SET_NULL`, `labels`
JSONField (`[{name, color}]`, non-system tags, presentation only), `author` (Forgejo username string,
deliberately not a `Member` FK), `is_pull` (bool), `merged_at` (nullable — non-null means merged;
closed with null `merged_at` on a PR means declined), `created_at`/`updated_at`/`closed_at` (nullable).

## Scope

In:

- Prototype 03 copied and stripped: `sync_members`, `sync_systems` (with updates), their source
  modules, models, and templates carry over; articles/blog and everything reachable from them go.
- `pages/sources/issues.py` — schema → fetcher → syncer → `run_sync_issues()`, reading top to bottom
  like the other source modules:
  - Pydantic schema for the fields we consume with `extra="ignore"` — the API-source inversion of the
    file sources' `extra="forbid"` typo gate.
  - Fetcher: httpx (added to the shared env), `GET /api/v1/repos/{repo}/issues?state=all` — no `type`
    filter, so issues and PRs arrive in one stream; the `pull_request` field distinguishes them and
    carries `merged_at`. Page loop via `page`/`limit` until `x-total-count` is exhausted.
  - Label resolution: `system/<slug>` → System row, unknown slug aborts naming the issue and slug;
    no system label → row with null FK; multiple system labels → first sorted by name; remaining
    labels stored as `[{name, color}]`.
  - Syncer: transactional upsert by `number`, delete rows whose number no longer comes back. `--flush`.
- `manage.py sync_issues` — thin wrapper. Sync order: members → systems → issues.
- Pages: home (the collective, recent updates, pull request list, recent open issues across systems),
  systems index, system detail (body, team, updates, open issues and pull requests as title + tags +
  link out to the forge, with open/closed badges on PRs), member detail (leads / administers).
  Declined PRs (closed, unmerged) and unassigned rows render nowhere; admin is their inspection window.
  State presentation lives in views/templates, not in the sync — see "How states render" in the
  primitives discussion. Page layout stays single-column — design is a later prototype.

Out:

- Comments, milestones, assignees, releases; issue bodies on the site (the forge is the reading
  surface, we link out).
- Mapping forge identities to the member cache.
- Webhooks, scheduled sync, etag/updated-since short-circuits (documented story only); any write back
  to the forge.
- A generic API-source framework — this is one collection, written concretely.

## How we know it worked

- Fresh checkout: `uv sync`, `migrate`, `sync_members`, `sync_systems`, `sync_issues`, `runserver` —
  everything renders with live data from the forge.
- The issue labeled `system/atlas` appears on the Atlas system page (title, tags, link to the forge)
  and in the home page's recent issues; the unlabeled issue is a row with a null FK, visible in the
  admin and nowhere on the site.
- A labeled PR appears in the pull request list with an open or closed badge; a closed unmerged PR
  renders nowhere while remaining a row in the admin.
- A `system/<slug>` label naming a system that isn't in git aborts `sync_issues` with the issue number
  and slug named; nothing is written.
- Closing, relabeling, or deleting an issue in Forgejo is reflected after the next `sync_issues`;
  `--flush` reproduces identical content; updates from `updates.json` render beside issues untouched.
- Outcome must answer honestly: did the sources layout absorb an HTTP fetcher without contortion, what
  differed at the validation boundary (`extra="ignore"`, network failure vs file-parse failure), and
  did anything about live-API-at-sync-time hurt (latency, availability, auth)?

## Outcome

Built 2026-08-08. All criteria met against the live test repo.

- **HTTP fetcher fit the sources layout.** `pages/sources/issues.py` reads schema → fetcher → syncer →
  `run_sync_issues()` top to bottom, same shape as the file sources. No contortion.
- **`extra="ignore"` at the API boundary worked.** Forgejo returns far more fields than we consume;
  forbidding extras would be the wrong failure mode for a source we don't own.
- **Live API at sync time was fine.** Anonymous read against the public test repo; sync completes in
  under a second. Network failure surfaces as a `CommandError` like a file-parse failure.
- **Issues and PRs coexist in one table.** `is_pull` + `merged_at` distinguish them; both render as
  linked lists with open/closed badges on PRs. Unlabeled rows ingest with a null FK and render nowhere;
  admin is the inspection window.
- **Added during build**: PR presentation changed from aggregate pulse to item lists (open/closed
  signifiers) — simpler and good enough for the prototype. Multi-column page layout was tried and
  reverted; layout is deferred to a later prototype.

## Deferred (not answered here)

How exactly to present forge-sourced content on the site is still open — prototype 04 proved the sync
and a minimal list rendering, not the final UX. Candidates for a later prototype:

- **Prominent label semantics** — forge labels like `help wanted` or a dedicated `seeking-maintainer`
  tag surfaced above the fold, not just as small tags beside titles.
- **Surfaces called out in the primitives brainstorm** — get-involved page, system timeline, status
  badges — none built here.
- **Page layout and information hierarchy** — single-column lists were deliberately kept simple;
  design is a later concern.
