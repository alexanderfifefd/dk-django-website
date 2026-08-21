# Discussion: ingest structure and Pydantic at the boundary

## The question

Prototype 03's first pass put all ingest logic in one management command (~300 lines): schemas,
loaders, reference checks, and ORM sync in a single file. Does a cleaner layout exist — and is
Pydantic worth adding for validation?

## What was wrong

Management commands are CLI entry points, not a home for business logic. The monolithic
`ingest.py` mixed four concerns:

1. **Authoring schemas** — allowed frontmatter/JSON keys and types
2. **Loaders** — read files, parse, render markdown
3. **Reference resolution** — usernames and slugs against the member cache and parsed systems
4. **Sync** — transactional upsert/delete into derived tables

Hard to navigate, hard to test without the management command harness, and not something you'd
happily point a stranger to in an open-source repo.

## Decisions

### Layered layout under `pages/sources/`

One direction, obvious layers:

```
files on disk  →  validated records  →  ORM rows  →  views
```

One module per collection keeps things local — systems in `sources/systems.py`,
updates in `sources/updates.py`, each reading top to bottom as schema → loader →
syncer (updates have no syncer; they ride on the System row):

```
pages/sources/
  common.py           # shared helpers: markdown, error formatting, abort_if, SyncResult
  members.py          # schema + loader + syncer + run_sync_members()
  systems.py          # schema + loader + syncer + run_sync_systems()
  updates.py          # schema + loader for updates.json (stored on System, not a table)
  articles.py         # schema + loader + syncer + run_sync_articles()
```

A first cut used per-collection subpackages (`systems/schema.py`, `systems/load.py`,
`systems/sync.py`) plus an `IngestReport` class. At ~100 lines per collection that was nine
files where three would do, so it was flattened: one module per collection, and loaders append
to a plain `list[str]` of errors that `abort_if()` checks once.

To avoid a third field list per collection (schema, record, model), the intermediate record
wraps the frontmatter model instead of copying its fields — `SystemRecord(slug, meta:
SystemFrontmatter, body_html, updates)`. Each collection's fields are declared exactly twice:
once in the authoring schema, once on the Django model, with the loader as the explicit
transform between them.

Management commands are thin wrappers around each module's ``run_sync_*`` function.

### Pydantic at the file boundary only

Pydantic models describe **what authors write** (frontmatter keys, JSON shapes). Django models
describe **what the site queries** (FKs, rendered HTML, slugs from filenames). These are
different layers with an explicit one-way transform in each module's loader and syncer — not two
sources of truth in the DRF-serializer sense.

Use Pydantic for:

- `extra="forbid"` as the unknown-key gate
- Self-documenting authoring contracts at the top of each source module (or in
  ``updates.py`` for the update record shape)
- JSON sources (`members.json`, `updates.json`)

Keep outside Pydantic:

- Cross-source FK checks (member cache, system slugs) — plain functions with explicit context
- Markdown → HTML rendering
- Slug from filename or directory name
- ORM sync

Added `pydantic` to the shared repo environment; only prototype 03 uses it today.

### No generic collection framework

Same constraint as the original project discussion: write each collection concretely. Shared
pieces are limited to `common.py` (markdown rendering, validation-error formatting, a
`SyncResult` dataclass) — not a `CollectionLoader[T]` base class.

### `fixtures/` renamed to `external/`

"Fixtures" is Django vocabulary for `loaddata` files and reads as throwaway dev data. The
member list is neither — it stands in for an externally owned system that Django caches. It
also doesn't belong in `content/`, which means git-authored collective content. So the
ownership split is explicit on disk: `content/` is authored, `external/` is synced.

## What we did not do

- Dev middleware (still deferred)
- Mirror Pydantic schemas onto Django models
- A separate Django app for ingest
