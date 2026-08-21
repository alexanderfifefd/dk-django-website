# Plan: prototype 10 — first version

**Project:** `first-version`
**Discussion:** `docs/projects/first-version/discussions/minimal-v1-scope.md`
**Prototype:** `prototypes/10-first-version/`
**Status:** foundation built (2026-08-21) — ready to copy; about copy and real articles open

## Goal

A bootable, focused Django prototype: home, markdown articles, about, join. Same design language as
prototype 07, minimal code and CSS. Structured so new work copies this tree rather than prototype 07.

## Outcome (2026-08-21)

Prototype 10 is a working, documented foundation:

- Single `public` app with `loaders/`, section templates, `layouts/` + `partials/`
- `load_articles` command and dev middleware (loader vocabulary throughout)
- Slim header/footer chrome; join hub + three sub-paths
- Home page content blocks: what we do, who we are, articles, CTA
- `README.md` in the prototype for early developers (English UI copy convention documented)

Intentionally **not** shipped: systems, initiatives, members, forge, recruiting, newsletter footer.

## Phase 1 — foundation (done)

- [x] Project docs and index entry
- [x] Django project: `config/`, `public/` app, sqlite, dev load middleware
- [x] `Article` model + `load_articles` for `content/articles/*.md`
- [x] Routes: `/`, `/articles/`, `/articles/<slug>/`, `/about/`, `/join/` + join sub-paths
- [x] Slim `site.css`; header/footer chrome distinct from prototype 07
- [x] Two sample articles with simplified frontmatter
- [x] Logo assets: full wordmark (header), small logo + org nr (footer)
- [x] Rename `sources/` → `loaders/` (see overview)
- [x] Rename app `pages/` → `public/`; rejected `site` (Python stdlib conflict)
- [x] Templates by URL section: `articles/`, `join/`
- [x] Template layers: `layouts/base.html`, `partials/header|footer.html`
- [x] Prototype `README.md`

**Verify:** from `prototypes/10-first-version/`:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Home shows content sections and articles; article detail renders markdown; about and join load;
editing a `.md` file and reloading updates the page in DEBUG.

## Phase 2 — content and copy

- [x] Home page v1 copy — H1, what we do, who we are (links to about), articles, CTA
- [ ] About page copy polish (still has generic collective voice)
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
| `README.md` | Developer onboarding; language convention |
| `config/settings.py` | `public` app, `CONTENT_DIR`, dev load middleware |
| `public/models.py` | `Article` only |
| `public/loaders/articles.py` | Load, validate, upsert markdown → ORM |
| `public/loaders/common.py` | Markdown render, validation helpers |
| `public/management/commands/load_articles.py` | Manual load from disk |
| `public/middleware.py` | Re-load on every request in DEBUG |
| `public/views.py` | Route handlers |
| `public/urls.py` | URL patterns |
| `public/templates/public/layouts/base.html` | Document shell; includes partials |
| `public/templates/public/partials/` | Header, footer |
| `public/templates/public/articles/` | Index and detail |
| `public/templates/public/join/` | Hub and sub-paths |
| `public/templates/public/home.html` | Home — section blocks (template HTML) |
| `public/templates/public/about.html` | About page |
| `static/css/site.css` | Stylesheet (`site-` CSS classes ≠ Django app name) |
| `content/articles/*.md` | Authoring layer |

## Success criteria

- A new contributor can run the server and edit an article markdown file without reading prototype 07.
- Total Python outside migrations fits on one screen skim.
- CSS is smaller than prototype 07 by an order of magnitude.
- No dead routes, models, or templates for systems/initiatives/members.
- Template tree documents extend vs include — copyable as a convention for new sections.

## Open questions

- **Home content blocks** — currently inline template sections. Revisit if blocks need authoring outside
  templates (markdown partials, shortcodes, or similar) once copy stabilises.
