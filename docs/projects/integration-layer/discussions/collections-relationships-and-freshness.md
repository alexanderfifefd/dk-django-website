# Discussion: collections, relationships, and freshness

## The question

Prototype 02 proved the ingest pattern for one flat collection. The real target
(`docs/high-level-goals.md`, `docs/organizational-context.md`) has multiple collections with
relationships, structured data as JSON, and externally-owned data cached locally. Does the ingest pattern
survive that — and how much shared machinery does it force into existence?

## The data model

The collective's homepage (see `docs/organizational-context.md`):

- **Member** — owned by Keycloak, cached by sync. The externally-owned collection.
- **System** — markdown in git (`system.md` per system), with frontmatter naming its people
  (`teamlead: alice`, `admins: [bob, carol]`). Git-owned content referencing externally-owned rows.
- **Update** — record-like JSON scoped to a system (`updates.json` next to `system.md`).
- **Article** — markdown blog post with an `author` member reference and an optional `system` slug.

## What this stresses that prototype 02 didn't

1. **Cross-source references.** `system.md` names members that only exist if the Keycloak sync ran.
   Sync order becomes a dependency chain (members before files), and a file naming an unknown member is an
   ingest error — the file-based equivalent of a broken FK constraint. Correct, but it means content
   ingest can fail because of an external system's state.
2. **Which collections earn a table at all.** Astro creates no real FKs — references are validated slugs,
   joins happen at render. The honest test for the ORM is cross-cutting queries. Members, systems and
   articles pass it ("what does alice maintain", "articles about X") and become models with real FKs.
   Updates don't: they render on their own system's page. So updates deliberately stay out of the ORM —
   ingested into a `JSONField` on `System`, no table, no identity convention. If cross-system update
   queries ever become real, promoting the field to a model is the finding, and its cost is the answer.
3. **The authoring loop.** Prototype 02's headline cost was save–ingest–reload. Fix: dev-only middleware
   re-running the file ingest per request, mtime-gated, rendering ingest errors as a readable error page.
   Only file sources — the member cache syncs explicitly in every environment, which is fine, because
   nobody authors Keycloak users in their editor. Freshness is a per-source policy.

## Constraints carried forward

- Files/git and external systems own the truth; derived tables rebuild, never get edited. Strict
  fail-loud validation. Owned tables (auth, future app state) coexist and survive re-ingest.
- The framework trap: no generic loader/collection framework up front. Write the four collections
  concretely; note where they repeat.

## Decisions

- Team structure: `teamlead` is a single required FK; `admins` an M2M. Concrete beats a role-through-table
  at two roles.
- Articles carry an `author` member reference — a second cross-source reference, and organizationally real.
- Updates: `JSONField` on `System`, per point 2 above.

Plan: `plans/2026-08-06-prototype-03-integration-layer.md`.
