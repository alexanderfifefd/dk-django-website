# Discussion: UI prototyping without the ingest layer

## The question

Prototypes 03–05 validated the data model and ingest patterns — collections, cross-references, forge
caching, git-backed member identity. The UI stayed deliberately minimal: single-column layout, plain
linked lists, no design exploration.

Can we prototype the collective homepage's *presentation* — system pages, member profiles, articles,
updates — without carrying the ingest pipeline, ORM, or external data sync?

## What we need

From `docs/organizational-context.md`, four **authored** nouns:

- **System** — marketing page plus team, updates, and related articles
- **Member** — profile page plus systems and articles they are linked to
- **Article** — blog post by a member, optionally scoped to a system
- **Update** — short operational notice scoped to one system (record-like, not prose)

We do not need forge issues, pull requests, identity linking, or externally cached members for this.
Those are solved problems in other prototypes; this one assumes the content shapes they established.

## Options considered

### Per-request file parsing (no database)

Read markdown and JSON from `content/` on every request. Dataclasses in memory; views pass them to
templates. Edit a file, reload the browser — no `migrate`, no `sync_*`.

Prototype 01 proved this for a flat blog collection. The content shapes from 03–05 (nested system
directories, member slugs as cross-references, updates as JSON beside `system.md`) fit the same pattern
with a slightly richer loader module.

**Pros:** Zero ceremony while authoring content and iterating on UI. Matches "I don't care if we use
models." Fastest path to real production markdown on disk.

**Cons:** No query layer — cross-cutting lookups ("all updates across systems", "articles by member")
happen in Python at load time. Fine at prototype scale; that is not what we are testing here.

### ORM + sync commands (copy prototype 03)

Keep the derived-table pattern: `sync_members`, `sync_systems`, `sync_articles`, sqlite, Pydantic
validation at the boundary.

**Pros:** Identical data path to the integration-layer prototype; relationships are real FKs.

**Cons:** Every content edit needs a sync step before the UI updates. Friction that buys nothing when
the question is presentation, not ingest.

### Hybrid (ORM with dev middleware re-ingest)

The freshness policy from `integration-layer`: auto re-sync file sources per request in dev.

**Pros:** Save–reload without manual sync; keeps the ORM for later.

**Cons:** Still carries migrations, models, and sync machinery we explicitly want to defer. More code
than the question requires.

## Decision

**Per-request file parsing, no database usage beyond Django's minimum.** One `content.py` module loads
all collections from disk, resolves cross-references in memory, and returns dataclasses views can pass
to templates.

This is a deliberate step sideways from the integration-layer arc: we are not testing ingest, freshness,
or external sources. We are testing layout, typography, information hierarchy, and how the four authored
nouns read together on real content.

When presentation stabilises, a later prototype can wire the same templates back to the ingest pattern
from 03/05. The content directory layout stays compatible.

## Content layout

```
content/
  members/<slug>.md
  systems/<slug>/
    system.md
    updates.json
  articles/<slug>.md
```

Conventions inherited from prior prototypes:

- Member filename = canonical slug for cross-references (`teamlead: alice` → `members/alice.md`)
- System directory name = slug; `system.md` carries frontmatter and marketing body
- Updates stay JSON beside the system — record-like `{date, kind, message}` entries
- Articles name `author` (required) and `system` (optional) as member/system slugs

## What this defers

- Forge issues and pull requests (observed content) — out of scope entirely
- Ingest commands, Pydantic validation, sync error pages
- Member `identities` map and external account linking
- Authorization, admin, pagination, search, deployment

## What this claims

The open question about **forge content presentation** in `docs/projects/index.md` partially overlaps —
how to surface activity on system pages — but this project starts with authored content only. Forge
presentation can be layered onto these templates in a follow-up once the authored-noun UI is settled.

## Follow-up (2026-08-12)

Per-request parsing shipped in `prototypes/06-site-ui/` but was replaced the same day with ORM + dev
auto-sync once UI features needed relationship queries. See
[orm-pivot-for-ui-queries.md](./orm-pivot-for-ui-queries.md). The original decision above is unchanged;
the pivot is documented separately.
