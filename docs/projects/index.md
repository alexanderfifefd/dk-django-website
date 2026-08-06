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

### `markdown-pages` — can markdown files on disk be the content layer?

A minimal site (home, about, blog) where blog posts are markdown files with frontmatter, parsed per request
— the naive baseline.

- **Discussion**: `docs/projects/markdown-pages/discussions/filesystem-as-content-source.md`
- **Learnings**: `docs/projects/markdown-pages/discussions/learnings-from-prototype-01.md`
- **Plan**: `docs/projects/markdown-pages/plans/2026-08-06-prototype-01-markdown-pages.md`
- **Prototype**: `prototypes/01-markdown-pages/` — **built and working** (2026-08-06)
- **Status**: prototype 01 done. Markdown as the authoring format is settled; per-request parsing is not.
  The `content-pipeline` project picks up from here.

### `content-pipeline` — who owns the path from markdown file to page?

Explores replacing per-request parsing: content built into the ORM by an ingest command, or handed to a
package. Files stay the source of truth; the database is derived and rebuildable.

- **Discussion**: `docs/projects/content-pipeline/discussions/who-owns-the-markdown-layer.md`
- **Plan**: `docs/projects/content-pipeline/plans/2026-08-06-prototype-02-content-pipeline.md`
- **Prototype**: `prototypes/02-content-pipeline/` — not started.
- **Status**: planned. Package survey found nothing credible; building our own ingest command.

## Completed

_None yet._

## Open questions not yet claimed by a project

These are known unknowns. Each will likely become its own project.

- **Content beyond a flat blog**: nested content folders mapping to nested URLs — where URL-from-path gets
  properly tested.
- **The content model**: if content is ingested into the ORM, what the models look like — one `Page` table
  or a model per content type, and how tags and collections are represented.
- **Authoring safety**: frontmatter is an unenforced contract (typos publish drafts); linting and draft
  preview are unexplored. An ingest step is a natural place to validate.
- **Scale**: parked. Never measured, not currently a priority.