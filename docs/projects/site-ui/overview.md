# Site UI

**Question:** How should we present systems, members, articles, and updates on the collective homepage?

**Status:** Paused — UI baseline validated; resume for content polish or forge surfaces (2026-08-12).

**Prototype:** `prototypes/06-site-ui/`

## Current approach

Markdown in git is still the authoring layer. Content syncs into derived ORM tables via
`pages/sources/`; **dev middleware** re-syncs on every request so edits show on reload without a
manual sync step.

Started without the ORM for speed; [pivoted back](./discussions/orm-pivot-for-ui-queries.md) once UI
features needed real relationships (system leads on members index, org groups, org roles).

**Out of scope:** forge issues/PRs, identity linking, auth, deployment.

## Content in place

| Collection | Location | Notes |
|---|---|---|
| Members | `content/members/<nick>.md` | Lowercase slug = nick; `name`, optional `role`, `groups: [...]` |
| Groups | `content/members/groups.yaml` | Vocabulary (`board`, `maintainers`); membership on member files |
| Systems | `content/systems/<slug>/` | `system.md` + `updates.json`; `stage`, optional `url`, teamlead, admins |
| Articles | `content/articles/<slug>.md` | author, optional system, summary, draft flag |

Real data: **9 members**, **6 systems** (5 live + Listmonk suggestion), **2 groups**, **1 article**.
Board group populated on the About page (4 members at time of writing).

## Pages shipped

| Page | URL | Notes |
|---|---|---|
| Home | `/` | Hero, systems list, latest articles, join CTA |
| Systems | `/systems/`, `/systems/<slug>/` | Index: stage badge + external URL; detail: header metadata + full-width body/updates/articles |
| Members | `/members/`, `/members/<nick>/` | Not in main nav; linked from About and footer |
| Articles | `/articles/`, `/articles/<slug>/` | Index and detail layouts refined; system badge where linked |
| About | `/about/` | Static template; board listing from `groups: [board]` |
| Join | `/join/` | Lead form (not wired up) |

## Site chrome

- **Header/footer** — `pages/templates/pages/includes/header.html` and `footer.html`, included from
  `base.html`. Wider layout width (`--layout-width`) than main content (`--content-width`).
- **Logo** — `static/img/logo-light-theme.png` (datakollektivet wordmark), centered in header; footer
  centre column.
- **CSS** — `static/css/site.css`; evolved from prototype 03 baseline. Stage badges, article bylines,
  two-tier page width.

## Static vs markdown pages

- **Markdown-authored** — member/system/article detail bodies (synced to `body_html`).
- **Template HTML** — home intro, about, join, header, footer (not in `content/`).

## System frontmatter

### `stage`

Lifecycle, not runtime state: `suggestion`, `development`, or `production`. Shown as a badge on the
systems index and in system detail metadata. Migration `0002_system_stage`.

### `url`

Optional public URL for the running service. Authors write a hostname or full URL in `system.md`; ingest
adds `https://` when omitted (`pages/sources/systems.py`). Shown on the systems index and in detail
metadata as an external link. Migration `0003_system_url`.

Current URLs in content:

| System | URL |
|---|---|
| Keycloak | sso.datakollektivet.no |
| Loomio | loomio.datakollektivet.no |
| Forgejo | forge.hornwitser.no |
| Website | datakollektivet.no |
| Matrix | — |
| Listmonk | — |

## How to read this project

1. [ui-without-ingest.md](./discussions/ui-without-ingest.md) — original decision (per-request parsing)
2. [orm-pivot-for-ui-queries.md](./discussions/orm-pivot-for-ui-queries.md) — **current architecture**, extensions, considerations
3. [2026-08-12-prototype-06-site-ui.md](./plans/2026-08-12-prototype-06-site-ui.md) — plan and outcome

## File index

### Discussions

| File | Summary |
|---|---|
| [ui-without-ingest.md](./discussions/ui-without-ingest.md) | Original decision: defer ingest/ORM; parse per request. Superseded for architecture by ORM pivot. |
| [orm-pivot-for-ui-queries.md](./discussions/orm-pivot-for-ui-queries.md) | **Current.** ORM + dev auto-sync; groups/roles; learnings and open considerations. |

### Plans

| File | Summary |
|---|---|
| [2026-08-12-prototype-06-site-ui.md](./plans/2026-08-12-prototype-06-site-ui.md) | Plan, outcome, and status. |

## Related docs

- **`docs/systems-and-initiatives.md`** — systems (core model)
- `docs/organizational-context.md` — the nouns this prototype presents
- `docs/projects/integration-layer/` — ingest pattern this prototype now follows
- `docs/projects/index.md` — repo-wide project list and open questions (media, template tags in markdown, …)

## Resume here

- Member bios, system copy, real updates, more articles
- Forge/identity surfaces layered onto these templates (`git-identity`, `forge-issues`)
- Media in markdown and template components — see open questions in `docs/projects/index.md`
