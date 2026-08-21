# Plan: prototype 10 — first version

**Project:** `first-version`
**Discussion:** `docs/projects/first-version/discussions/minimal-v1-scope.md`
**Prototype:** `prototypes/10-first-version/`
**Status:** in progress (2026-08-21)

## Goal

A bootable, focused Django prototype: home, markdown articles, about, join. Same design language as
prototype 07, minimal code and CSS.

## Phase 1 — scaffold (this change)

- [x] Project docs and index entry
- [x] Django project: `config/`, `public/` app, sqlite, dev sync middleware
- [x] `Article` model + `sync_content` for `content/articles/*.md`
- [x] Routes: `/`, `/articles/`, `/articles/<slug>/`, `/about/`, `/join/` + join sub-paths
- [x] Templates and slim `site.css`
- [x] Two sample articles with simplified frontmatter
- [x] Logo static assets (full wordmark in header, small logo in footer)
- [x] Rename `sources/` → `loaders/`; rename app `pages/` → `public/` (see overview — `site` rejected)

**Verify:** from `prototypes/10-first-version/`:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Home shows articles; article detail renders markdown; about and join load; editing a `.md` file and
reloading updates the page in DEBUG.

## Phase 2 — content and copy

- [ ] Rewrite home hero and about copy for v1 (no systems/members references)
- [ ] Port 2–4 real articles from prototype 07 with simplified frontmatter (`author` string only)
- [ ] Join hub: wire path cards to external registration URLs when ready (account page already links to SSO)

## Phase 3 — join polish (optional)

- [ ] Recruiting cards on volunteer page **only if** systems/initiatives return

## Phase 4 — grow when needed

Add back one collection at a time from prototype 07, each as its own decision:

1. Members (profiles + about board listing)
2. Systems (home section, article badges)
3. Initiatives
4. Groups and recruiting surfaces

Do not pre-build models or CSS for collections that are not shipped.

## Article frontmatter (v1)

```yaml
---
title: Example post
date: 2026-08-21
author: Alex
summary: Optional deck line.
draft: false
---
```

`draft: true` skips ingest. No `system`, `initiative`, `author_group`, or member slug references.

## Files that matter

| Path | Role |
|---|---|
| `public/models.py` | `Article` only |
| `public/loaders/articles.py` | Load, validate, sync |
| `public/middleware.py` | Dev auto-sync |
| `public/views.py` | Route handlers |
| `static/css/site.css` | Stylesheet (CSS class prefix `site-` is visual chrome, not the app name) |
| `content/articles/*.md` | Authoring layer |

## Success criteria

- A new contributor can run the server and edit an article markdown file without reading prototype 07.
- Total Python outside migrations fits on one screen skim.
- CSS is smaller than prototype 07 by an order of magnitude.
- No dead routes, models, or templates for systems/initiatives/members.
