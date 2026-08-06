# Discussion: who owns the path from markdown file to page?

## The question

Prototype 01 parses markdown per request with nothing in between — no queries, no validation, no
relationships. Should something own that path instead: a build/ingest step that puts content into the ORM,
or a package that manages markdown-to-Django for us?

The constraint carried over from prototype 01: markdown files in git stay the source of truth. Anything
derived from them (database rows, caches) must be rebuildable and flushable from the files. We are not
turning Django into a CMS — no authoring through the admin.

Scale is explicitly not the driver here. We judge options on ergonomics, code size, and what the authoring
loop feels like.

## Options

**1. Our own ingest step.** A management command walks the content tree, parses frontmatter and body, and
writes rows (a `Post` model, maybe a generic `Page`). Re-run to reparse; `--flush` to rebuild from scratch.

- Gets back the ORM: querying, ordering, tags as relations, pagination.
- An ingest step is a natural place to validate frontmatter and fail loudly.
- Costs the instant save-and-reload loop unless something re-ingests on change (dev-only file watcher,
  or re-run the command — how much that hurts is a thing to find out).

**2. A package that owns the markdown layer.** Surveyed 2026-08-06; ruled out.

- Coltrane (the only live candidate) doesn't use a database at all — it's per-request parsing with
  filesystem routing, i.e. a packaged prototype 01. 120 stars, one maintainer, dormant since May 2025,
  ~15 transitive dependencies, untested on Django 6. Its URL-from-path conventions are worth stealing;
  the dependency is not.
- No established package does the ingest-to-ORM route. What exists is tiny or experimental
  (Django-Spellbook, 26 stars, generates code not rows; django-markdown-database, a v0.1 read-only
  sqlite virtual table). The standard answer in the wild is a short DIY management command.

**3. Per-request parsing (prototype 01).** Already built. The baseline to beat.

## Decision

Write it ourselves (option 1). The package route died in the survey: nothing credible does
markdown-into-the-ORM, and the one healthy-ish package solves the problem we already solved. Prototype 02
is a single prototype — the same small site as 01, content ingested into the ORM by a management command.

## Resolved (2026-08-06, see the plan)

- Store rendered HTML only — the database is derived, always rebuilt from files, never the other way.
- Manual ingest command for the prototype; deployment story is ingest-on-deploy.
- Strict validation: bad frontmatter fails the ingest loudly, nothing half-written.

Still open: the content model beyond a flat blog (one table vs. per-type, tags as relations) — deferred.
