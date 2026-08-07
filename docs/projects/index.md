# Projects

A **project** is one line of enquiry: a question about the markdown-driven approach, the options considered,
the decision taken, and the prototype built to test it. Projects are procedural logs — they record what we
thought at the time and are not rewritten when we later change our minds. A later project supersedes an
earlier one instead.

Each project lives in `docs/projects/<name>/`:

- `discussions/<slug>.md` — the question, the options, the reasoning, the decision.
- `plans/YYYY-MM-DD-<slug>.md` — what will be built, in what order, and how we'll know it worked.

Most projects map to one prototype directory under `prototypes/`.

## Starting a new project

Discussion first, then an entry under Active here, then a plan once a decision is reached, then the
prototype (`prototypes/NN-<project-name>/`, numbered in build order). When the question is answered, note
the outcome in the plan and move the project to Completed.

## Active

(none)

## Completed

### `integration-layer` — do collections, relationships, and mixed sources break the ingest pattern?

**Answer: yes, with separate sync commands.** Three derived collections (members from `external/`,
systems and articles from git) with real FKs and strict cross-source validation. Updates stay in a
JSONField without pain at this scale. Dev middleware deferred — manual sync remains.

- **Discussion**: `docs/projects/integration-layer/discussions/collections-relationships-and-freshness.md`
- **Plan**: `docs/projects/integration-layer/plans/2026-08-06-prototype-03-integration-layer.md`
- **Prototype**: `prototypes/03-integration-layer/` — built and validated (2026-08-07)

### `markdown-pages` — can markdown files on disk be the content layer?

**Answer: yes.** Markdown files with frontmatter work as the authoring format; per-request parsing worked
at toy scale but gave up querying, validation, and relationships. Superseded by `content-pipeline`.

- **Discussion**: `docs/projects/markdown-pages/discussions/filesystem-as-content-source.md`
- **Learnings**: `docs/projects/markdown-pages/discussions/learnings-from-prototype-01.md`
- **Plan**: `docs/projects/markdown-pages/plans/2026-08-06-prototype-01-markdown-pages.md`
- **Prototype**: `prototypes/01-markdown-pages/` — built and working (2026-08-06)

### `content-pipeline` — who owns the path from markdown file to page?

**Answer: we do.** No credible package exists; a ~100-line ingest command with strict validation syncs
files into a derived `Post` table. Main cost found: the save–ingest–reload authoring loop, picked up by
`integration-layer`.

- **Discussion**: `docs/projects/content-pipeline/discussions/who-owns-the-markdown-layer.md`
- **Learnings**: `docs/projects/content-pipeline/discussions/learnings-from-prototype-02.md`
- **Plan**: `docs/projects/content-pipeline/plans/2026-08-06-prototype-02-content-pipeline.md`
- **Prototype**: `prototypes/02-content-pipeline/` — built and validated (2026-08-06)

## Open questions not yet claimed by a project

These are known unknowns. Each will likely become its own project.

- **Draft preview**: drafts are simply not ingested; viewing one at its URL behind an explicit flag is
  unexplored.
- **Media and assets**: images living next to the `.md` files that reference them.
- **Scale**: parked. Never measured, not currently a priority.