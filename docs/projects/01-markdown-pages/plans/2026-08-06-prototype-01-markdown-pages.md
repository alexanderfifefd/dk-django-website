# Plan: prototype 01 — a minimal site with a markdown blog

**Project**: `markdown-pages`
**Discussion**: `docs/projects/01-markdown-pages/discussions/filesystem-as-content-source.md`
**Prototype directory**: `prototypes/01-markdown-pages/`
**Status**: built — see Outcome below

## Goal

A minimal test site — homepage, about page, and a blog — where the blog posts are markdown files on disk.
The point is to get the scaffolding up, prove the pure-markdown path end to end, and learn enough to improve
the repo docs. Nothing clever: per-request parsing, no caching, no HTMX.

## Scope

In:

- Three sections: home (`/`), about (`/about/`), blog (`/blog/`, `/blog/<slug>/`).
- Blog posts as markdown files with frontmatter (title, date, tags, draft) in a content folder.
- Blog index sorted by date descending, hiding drafts; detail pages rendering markdown to HTML.
- Standard `startproject` settings. The default sqlite database stays wired up but holds no content —
  content is pure markdown.
- Hand-written CSS, enough to read comfortably.

Out:

- HTMX or any JavaScript — nothing on these pages needs it.
- Models, admin, or ORM use for content.
- Caching, indexing, search, pagination, tag pages.
- Volume testing (deferred; worth doing before trusting per-request parsing at scale).

## Layout chosen

```
prototypes/01-markdown-pages/
  manage.py
  config/                   # settings, root urls (standard startproject output)
  pages/                    # the single app
    posts.py                # markdown discovery, frontmatter parsing, HTML rendering
    views.py                # home, about, blog index, blog detail
    urls.py
    templates/pages/        # base, home, about, blog_index, blog_detail
  content/blog/*.md         # the blog posts
  static/css/site.css
```

## Dependencies

In the root `pyproject.toml`, shared by all prototypes: `django`, `markdown` (markdown → HTML),
`python-frontmatter` (frontmatter parsing).

## How we know it worked

- All three sections render from a fresh `uv sync` + `runserver`.
- Every non-draft `.md` file in `content/blog/` appears on the index and is reachable at `/blog/<slug>/`.
- A draft post is hidden from the index and 404s at its URL.
- An unknown slug 404s; a slug containing path separators cannot escape the content folder.
- Editing a post and reloading shows the change without restarting the server.

## Outcome

Built 2026-08-06, verified in the browser the same day. All success criteria met: three sections render,
non-draft posts appear on the index and resolve at their slugs, the draft post is hidden and 404s, unknown
slugs 404, and edits to markdown files show up on reload with no restart.

Notes against the plan:

- **The scaffolding needed nothing special.** Standard `startproject` output plus one app. We had
  considered stripping the database, auth, and admin out of settings; in practice leaving the defaults
  alone was simpler, and the unused sqlite file costs nothing. "Pure markdown" turned out to mean *content
  never touches the ORM*, not *there is no database*.
- **The entire markdown layer is one small module** (`pages/posts.py`, ~70 lines): parse a file, list the
  folder, look up a slug. Two dependencies (`markdown`, `python-frontmatter`) did all the real work.
- **HTMX was never needed.** Three pages of server-rendered HTML with links between them; there was no
  interaction to enhance.
- **Volume is still untested.** Four posts parse imperceptibly fast per request; the ceiling question from
  the discussion remains open and is the most useful thing a follow-up could measure.

Fuller reflections and candidate next prototypes:
`docs/projects/01-markdown-pages/discussions/learnings-from-prototype-01.md`.
