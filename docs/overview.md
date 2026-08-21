# Project Overview: Markdown-driven Django (prototypes)

## Purpose

This repo explores how to build a pleasant Django website whose written content — blog posts, articles,
long-form pages — is **authored as markdown files** rather than typed into an admin or CMS.

An author writes a `.md` file with frontmatter, drops it in a content folder, and Django serves it as a
page. The one fixed commitment: **markdown files in git are the source of truth an author edits**.

How those files become pages is open — parsed per request, ingested into the ORM by a management command,
or handled by a package. Build/sync steps and content in the database are both fine, as long as the files
stay what the author edits and the database can be rebuilt from them. The longer arc goes beyond markdown
(structured data as JSON, cached external APIs): see `docs/high-level-goals.md`.

The repo is a **collection of prototypes**, not one product. Each prototype exists to answer a specific
question and is expected to be thrown away once it has. See `docs/projects/index.md` for what is being
explored and why.

## Prototype stage

Treat all state as disposable:

- sqlite files, migrations, and content folders can be deleted and regenerated at will.
- Migration history and continuity do not matter.
- We optimise for how fast an assumption can be tested, not for correctness or durability.

## Tech stack

- **Backend**: Django (latest stable)
- **Templating**: Django templates, no template extensions or component libraries
- **Interactivity**: server-rendered pages by default. HTMX is the only sanctioned enhancement, and only
  when a page genuinely needs it — don't reach for it preemptively.
- **Styling**: hand-written CSS, no framework, no preprocessor
- **Markdown**: chosen per prototype — a parsing library plus frontmatter, or a package that owns the
  markdown-to-page path
- **Database**: sqlite; whether content lives in it is per-prototype
- **Python env**: `uv`, with one shared environment at the repo root
- **Frontend tooling**: none. No Node, no bundler, no npm. Python-side build or sync steps are fine.

## Repo layout

```
pyproject.toml              # one shared uv environment for every prototype
prototypes/
  01-<name>/                # a standalone Django project
  02-<name>/                # another standalone Django project
docs/
  overview.md               # this file
  projects/                 # the thinking behind each prototype
```

Each prototype under `prototypes/` is a **fully standalone Django project** with its own `manage.py`,
settings, templates, and content. Prototypes never import from each other. Copying code between them is
fine and expected; sharing it is not. They all draw on the single uv environment at the repo root.

How a prototype is organised internally — app layout, where markdown lives, whether it uses a database — is
that prototype's own business. Its project docs under `docs/projects/` describe the structure it chose.

## Documentation map

- **`docs/overview.md`** (this file): orientation. Stack, layout, conventions, non-goals.
- **`docs/high-level-goals.md`**: where this is heading — Django as an integration layer over git-owned
  data. The prototypes test pieces of it.
- **`docs/organizational-context.md`**: what the site is for — a software collective's homepage — the
  nouns the data model mirrors, paths to participate, recruitment signals.
- **`docs/systems-and-initiatives.md`**: the two core work nouns — what we operate vs what we are trying
  to accomplish, lifecycle, and how they relate.
- **`docs/projects/`**: the reasoning behind each prototype, grouped by project.
  - **Start here**: `docs/projects/index.md` lists active and completed projects.
  - **`<project>/overview.md`**: when present, a project index with summaries and reading order.
  - **`<project>/discussions/`**: what question we're answering, what options exist, what we chose.
  - **`<project>/plans/`**: date-prefixed implementation plans (`YYYY-MM-DD-<slug>.md`).
  - Don't read a project's docs unless the current task concerns it — start with that project's
    `overview.md` when one exists.

A project in `docs/projects/` usually maps to one prototype directory under `prototypes/`. The project docs
hold the intent; the prototype holds the code.

### Documentation authority

`docs/projects/<project>/` is authoritative for that prototype's intent and decisions. When code changes
what a prototype does or concludes, update its project docs in the same change. If a decision turns out to
apply to the whole repo rather than one prototype, **promote it into `docs/organizational-context.md`**
(for what the site *is*) or this overview (for repo-wide conventions). The member-journeys project
documents Join UX implementation; the three participation paths and recruitment signals are defined in
organizational context.

## Local workflows

The uv environment is shared, so `uv run` works from inside any prototype directory — uv resolves the
`pyproject.toml` at the repo root.

```bash
uv sync                                  # from the repo root, once

cd prototypes/01-<name>
uv run python manage.py runserver
uv run python manage.py migrate          # only if a prototype uses the ORM at all
```

## Explicit non-goals

- No deployment, hosting, or production settings
- No secrets management or security hardening
- No wired-up identity provider or login flows (caching external identity data, e.g. Keycloak-shaped
  fixtures, is fine)
- No API, no JSON endpoints, no SPA routing
- No JavaScript build pipeline
- No shared framework or abstraction layer extracted across prototypes
