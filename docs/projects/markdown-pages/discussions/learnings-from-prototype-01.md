# Learnings from prototype 01

Written 2026-08-06, after building and browser-testing `prototypes/01-markdown-pages/`. This records what
the first prototype taught us and what looks worth exploring next. It does not supersede
`filesystem-as-content-source.md`; it answers part of that discussion's question.

## What held up

- **The core idea works and is small.** A markdown-backed blog inside a normal Django site took one app,
  one ~70-line module, and two libraries. There is no framework to build here — the interesting questions
  are all about conventions and scale, not plumbing.
- **The authoring loop is the selling point.** Save a file, reload the browser. No sync command, no cache
  to bust, no admin form. This is the property future prototypes should refuse to give up.
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
- **Trust is assumed.** Post bodies are rendered with `|safe`, so markdown can embed raw HTML. Correct for
  content that lives in our own git repo; a hard boundary to remember if content ever comes from anyone
  else.
- **Listings parse more than they need.** The index converts every post's full body to HTML just to show
  titles and summaries. Harmless now, and the obvious first cut if volume ever hurts — before any cache.
- **Silent fallbacks can mislead.** A date written as a quoted string (`date: "2026-08-06"`) isn't parsed
  as a date by YAML, so the post silently sorts by file mtime instead. Convenience and surprise are the
  same feature here.
- **The ceiling is unmeasured.** We never generated hundreds of files to time the index page. The
  per-request approach is unproven beyond toy scale, so the cache/index question from the original
  discussion stays open.

## Candidate directions for the next prototypes

Roughly ordered by how much they'd tell us:

1. **Volume and the index question.** Generate 500–5000 posts, measure the index page, then try the
   cheapest mitigations in order: parse frontmatter only for listings, an in-memory index invalidated by
   mtime, a sqlite index built by a management command. This directly resolves the open decision in
   `filesystem-as-content-source.md`.
2. **Markdown beyond the blog.** Let arbitrary site pages come from a content tree (nested folders mapping
   to nested URLs), instead of only a flat `blog/` folder. This is where URL-from-path gets genuinely
   tested.
3. **Content relationships.** Tag pages, post-to-post links, ordered collections — the things a database
   join would normally do. Likely the first place the pure-filesystem approach really strains.
4. **Authoring safety.** A `manage.py` command that lints frontmatter (unknown keys, unparseable dates),
   plus a draft-preview mode so drafts are viewable at their URL with an explicit flag but never listed.
5. **Richer rendering.** Syntax highlighting, footnotes, a table of contents — all available as extensions
   to the `markdown` library. Also: images and other assets living next to the `.md` files that reference
   them.
6. **HTMX where it earns its place.** Tag filtering or infinite scroll on a large index would be the first
   honest use case; don't add it before one of those exists.

## Practical notes for whoever builds next

- Copy `pages/posts.py` into the new prototype rather than importing it; that's the repo convention.
- The slug URL converter plus a resolved-path containment check is all the traversal defence needed when
  slugs are flat. Nested content paths (direction 2) will need real path handling.
- `uv run python manage.py runserver` from inside the prototype directory just works; uv finds the root
  `pyproject.toml` on its own.
