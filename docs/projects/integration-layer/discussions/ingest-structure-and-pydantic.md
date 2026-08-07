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

Per-collection subpackages keep things local — everything about systems lives under
`sources/systems/`:

```
pages/sources/
  errors.py           # collect errors; abort if any
  markdown.py         # render markdown body
  pipeline.py         # ordering, transaction, orchestration
  members/            # schema, load, sync
  systems/            # schema, load, sync
  articles/           # schema, load, sync
```

Management commands stay thin wrappers that call `pipeline.run_sync_members()` and
`pipeline.run_ingest()`.

### Pydantic at the file boundary only

Pydantic models describe **what authors write** (frontmatter keys, JSON shapes). Django models
describe **what the site queries** (FKs, rendered HTML, slugs from filenames). These are
different layers with an explicit one-way transform in `load.py` / `sync.py` — not two sources
of truth in the DRF-serializer sense.

Use Pydantic for:

- `extra="forbid"` as the unknown-key gate
- Self-documenting authoring contracts in `schema.py`
- JSON sources (`members.json`, `updates.json`)

Keep outside Pydantic:

- Cross-source FK checks (member cache, system slugs) — plain functions with explicit context
- Markdown → HTML rendering
- Slug from filename or directory name
- ORM sync

Added `pydantic` to the shared repo environment; only prototype 03 uses it today.

### No generic collection framework

Same constraint as the original project discussion: write each collection concretely. Shared
pieces are limited to `errors.py`, `markdown.py`, and validation-error formatting — not a
`CollectionLoader[T]` base class.

## What we did not do

- Dev middleware (still deferred)
- Mirror Pydantic schemas onto Django models
- A separate Django app for ingest
