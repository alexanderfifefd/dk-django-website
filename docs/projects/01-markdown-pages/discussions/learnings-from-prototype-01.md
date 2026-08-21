# Learnings from prototype 01

Written 2026-08-06, after building and browser-testing `prototypes/01-markdown-pages/`. This records what
the first prototype taught us and what looks worth exploring next. It does not supersede
`filesystem-as-content-source.md`; it answers part of that discussion's question.

## What held up

- **The core idea works and is small.** A markdown-backed blog inside a normal Django site took one app,
  one ~70-line module, and two libraries. There is no framework to build here — the interesting questions
  are all about conventions and scale, not plumbing.
- **The authoring loop is the selling point.** Save a file, reload the browser. No sync command, no cache
  to bust, no admin form. Whatever replaces per-request parsing should stay close to this.
- **"No database for content" coexists fine with a database.** We kept stock Django settings; sqlite sits
  there for whatever a later feature needs, while content stays on disk. The earlier instinct to strip
  Django down was solving a problem we didn't have.
- **Degrading instead of crashing feels right for files.** Title falls back to the filename, date falls
  back to file mtime, missing tags are just empty. A half-written file becomes an ugly post, not a 500.
- **Plain templates and plain CSS were enough.** No HTMX, no JS. For read-only pages the "only if
  necessary" rule cost us nothing.

## What feels fragile or unresolved

- **Frontmatter is an unenforced contract.** A typo like `drafts: true` is silently ignored and the post
  publishes. There is no validation anywhere. Fine at four files; worrying at forty.
- **Listings parse more than they need.** The index converts every post's full body to HTML just to show
  titles and summaries. Harmless now, and the obvious first cut if volume ever hurts — before any cache.
- **Silent fallbacks can mislead.** A date written as a quoted string (`date: "2026-08-06"`) isn't parsed
  as a date by YAML, so the post silently sorts by file mtime instead. Convenience and surprise are the
  same feature here.
- **The ceiling is unmeasured.** We never generated hundreds of files to time the index page. The
  per-request approach is unproven beyond toy scale, so the cache/index question from the original
  discussion stays open.

## Practical notes for whoever builds next

- Copy `pages/posts.py` into the new prototype rather than importing it; that's the repo convention.
- The slug URL converter plus a resolved-path containment check is all the traversal defence needed when
  slugs are flat. Nested content paths (direction 2) will need real path handling.
- `uv run python manage.py runserver` from inside the prototype directory just works; uv finds the root
  `pyproject.toml` on its own.
