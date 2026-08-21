# Minimal v1 scope

**Project:** `first-version`
**Date:** 2026-08-21

## Question

Prototype 07 validates systems, initiatives, members, groups, recruiting, and join sub-paths together.
That is the right sandbox for exploring the full noun model — but it is too much for a first public
version. What do we ship first?

## Decision

**Prototype 10** (`prototypes/10-first-version/`) covers four surfaces:

1. **Home** — H1, what we do, who we are (links to about), latest articles, join CTA. No systems or
   initiatives sections.
2. **Articles** — markdown in git, synced to a single `Article` model. The only dynamic content.
3. **About** — static page; collective story without linking to members or systems indexes.
4. **Join** — chooser hub plus account, member, and volunteer sub-pages (static templates; forms not wired up).

Everything else from prototype 07 stays out until there is a concrete need.

## What we deliberately drop

| Feature | Why deferred |
|---|---|
| Systems & initiatives | Core to the long-term site, but not required to publish articles and explain who we are |
| Members & groups | Article authors are plain names for now; profiles and org structure add sync complexity |
| Recruiting cards on volunteer page | Needs systems/initiatives models |
| Forge / identity | Observed activity and SSO linking are separate projects, already answered elsewhere |
| Recruiting badges | Depends on systems and initiatives |

## Architecture choices

- **Single app: `public`** — all visitor-facing Django code in one app with internal folders (`loaders/`,
  `templates/`, etc.). A future logged-in area is a separate app (`portal`), not more apps inside
  the public surface.
- **Keep the ORM + dev sync pattern** from prototype 06/07 — articles need querying on home and index.
- **One model, one loader module** — `Article` and `public/loaders/articles.py` only. No shared
  orchestrator syncing five collections.
- **Plain-string author** — frontmatter `author: "Alex"` instead of FK to `Member`. Restores member
  linking when profiles return.
- **Slim CSS** — same tokens and layout feel as prototype 07 (~500 lines, not ~1500). Add rules when
  a page needs them, not preemptively.
- **Templates in three layers** — `layouts/` (extend), `partials/` (include), section folders for pages
  (`articles/`, `join/`). Top-level templates for one-off routes (`home.html`, `about.html`).
- **No copy-paste from 07** — write only the files this scope needs; use 07 as reference for copy and
  design, not as a template tree to duplicate.

## Non-goals (unchanged from repo overview)

Deployment, auth, API, JS tooling, cross-prototype abstractions.
