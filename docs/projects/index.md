# Projects

A **project** is one line of enquiry: a question about the markdown-driven approach, the options considered,
the decision taken, and the prototype built to test it. Projects are procedural logs — they record what we
thought at the time and are not rewritten when we later change our minds. A later project supersedes an
earlier one instead.

Each project lives in `docs/projects/<name>/`:

- `discussions/<slug>.md` — the question, the options, the reasoning, the decision.
- `plans/YYYY-MM-DD-<slug>.md` — what will be built, in what order, and how we'll know it worked.

Most projects map to one prototype directory under `prototypes/`.

## Active

### `markdown-pages` — can markdown files on disk be the content layer?

A minimal site (home, about, blog) where blog posts are markdown files with frontmatter, parsed per
request. No content in the database, no build step.

- **Discussion**: `docs/projects/markdown-pages/discussions/filesystem-as-content-source.md`
- **Learnings**: `docs/projects/markdown-pages/discussions/learnings-from-prototype-01.md`
- **Plan**: `docs/projects/markdown-pages/plans/2026-08-06-prototype-01-markdown-pages.md`
- **Prototype**: `prototypes/01-markdown-pages/` — **built and working** (2026-08-06)
- **Status**: prototype 01 done. The approach works at toy scale; the volume/caching question is still
  open. The learnings doc lists candidate next prototypes, with volume testing as the highest-value one.

## Completed

_None yet — `markdown-pages` stays active until the volume question is answered._

## Open questions not yet claimed by a project

These are known unknowns. Each will likely become its own project.

- **Caching / indexing**: prototype 01 proved per-request parsing works at toy scale but never measured a
  large content tree. Still the biggest unknown; first candidate for prototype 02.
- **Content beyond a flat blog**: nested content folders mapping to nested URLs — where URL-from-path gets
  properly tested.
- **Content relationships**: tags, collections, and cross-references between files without a database to
  join on.
- **Authoring safety**: frontmatter is an unenforced contract (typos publish drafts); linting and draft
  preview are unexplored.
- **Navigation**: how much page-to-page navigation HTMX could handle with partial swaps, once a page
  actually needs it. Prototype 01 needed none.
