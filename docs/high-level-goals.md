# High-level goals: Django as an integration layer

Where this repo is ultimately heading. The prototypes test pieces of this; none of them is this.

## The idea

Build a Django site that is **not the source of truth for most of its data**. Data is authored and owned
elsewhere — above all in git — and Django imports, indexes, queries, renders, and authorizes. Collaboration
on content happens through git pushes, not by handing out CMS admin accounts. The feel to aim for is
Astro's content collections, but server-rendered with a real ORM behind it.

## Sources of truth

| Domain | Owner |
|---|---|
| Content (markdown + frontmatter) | Git |
| Structured data (JSON/YAML files) | Git |
| External data (e.g. Keycloak users) | The external system; Django caches it |
| Application state | Django's database |
| Identity, billing (later, out of prototype scope) | Keycloak, payment provider |

## The database has two kinds of tables

- **Derived**: rebuilt from sources at any time by an ingest step. Never edited by hand, never precious,
  never data-migrated — schema changes are code + `migrate` + re-ingest.
- **Owned**: real application state (users, sessions, whatever features need). Normal Django rules apply,
  including real migrations. These coexist with derived tables in the same database; they are never mixed
  in one table.

## The shape of the ingest layer

Three concepts, however concretely or generically they end up written:

- **Source**: where raw records come from — a markdown directory, a JSON file, an HTTP API. Each record
  has a natural key (path/slug or external id).
- **Schema**: strict validation at the boundary. Django models are the schema; bad input fails the ingest
  loudly and writes nothing. References between collections are declared data: containment via directory
  structure, cross-references via frontmatter slugs. Dangling references are errors.
- **Syncer**: idempotent upsert-and-delete in a transaction, two passes when relationships exist
  (entities first, then wiring).

## Freshness is a per-source policy, not a global one

- File sources, dev: re-derive per request (mtime-gated), so authoring is save–reload. Ingest errors
  render as a readable error page — a compiler screen, not a 500.
- File sources, prod: ingest at deploy; later a job keyed on the content repo's commit SHA, or webhooks.
- API sources: on a schedule with a cheap short-circuit (etag / updated-since), never per request, in any
  environment. Staleness-by-minutes is correct here, not a compromise.

## What this is not

Not a CMS (no authoring through the admin — read-only inspection is fine), not a static site generator
(Django serves at request time), and not a framework until repetition forces one: collections get written
concretely first, and shared machinery is extracted only when a third collection makes it obvious.
