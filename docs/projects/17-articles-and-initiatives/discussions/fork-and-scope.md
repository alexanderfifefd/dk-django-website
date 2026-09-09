# Discussion: fork base and scope

**Project:** `articles-and-initiatives`
**Date:** 2026-09-03
**Status:** open — no decision yet

## The question

Prototype 17 should be **based on 15** and take **inspiration from 07** for initiatives and articles.
What exactly do we copy, what do we simplify, and what is the smallest useful site that still tests
the two-noun relationship?

## Why fork 15, not 07

| | Fork 15 | Fork 07 |
|---|---|---|
| CSS | Layer split done; component catalog; current visual language | Pre-15 CSS; would need css-structure work merged in |
| App layout | `public/` app, `loaders/`, section templates | `pages/` app, `sources/`, older naming |
| Starting weight | Articles + static pages + design lab | Systems, members, groups, initiatives, forge sync |
| Intent | Forward-looking baseline | Historical full-model sandbox |

Prototype 17 is a **forward fork**: keep 15's stack and add initiative abstractions from 07, not a
retrofit of 07.
https://nettside.datakollektiv.no/
## What prototype 15 gives us for free

Keep unchanged unless the new noun forces a change:

- Six-file CSS layer split + `/design-lab/` catalog
- Routes: home, articles, about, join (+ sub-paths)
- `Article` model + `load_articles` + dev sync middleware
- Plain-string `author` on articles (no member profiles)
- Template layers: `layouts/`, `partials/`, section folders

## What we port from 07 (initiative + article abstractions)

The **relationship** is the point — articles explain *why*; initiatives carry the goal.

```
Article                          Initiative
  optional initiative FK    →    has many related articles (reverse)
  markdown body                    initiative.md pitch + frontmatter
  content/articles/*.md            content/initiatives/<slug>/initiative.md
```

From 07 we want the **content shape and ORM fields** that make this work, not the full social graph:

| From 07 | Port to 17? | Notes |
|---|---|---|
| `Initiative` model | **Yes** | Core noun |
| `content/initiatives/<slug>/initiative.md` | **Yes** | Same authoring path |
| `Article.initiative` FK | **Yes** | Frontmatter `initiative: <slug>` |
| Initiative index + detail routes | **Yes** | `/initiatives/`, `/initiatives/<slug>/` |
| Status badges | **Yes** | Reuse 15 card/badge CSS where possible |
| Related articles on initiative detail | **Yes** | Query `Article.objects.filter(initiative=…)` |
| Initiative badge on article list/detail | **Yes** | Shows cross-ref works both ways |
| Home section for active initiatives | **Likely** | Small teaser block — mirrors 07 home |
| `updates.json` on initiatives | **TBD** | See [content-model.md](./content-model.md) |
| `takers` → Member M2M | **No** (initially) | 15 uses plain-string author; keep takers as slug list or strings |
| `systems` M2M | **No** | Systems stay in 07 |
| Members, groups, forge | **No** | Out of scope |
| Loomio / Matrix frontmatter | **TBD** | Fields are cheap; UI can defer |
| `recruiting: open` | **TBD** | Valid field; recruiting UI deferred like prototype 10 |
| Left nav "Systems + Initiatives" | **No** | No systems; add Initiatives link only |

## Proposed scope (draft)

**In**

1. Fork `prototypes/15-css-structure/` → `prototypes/17-articles-and-initiatives/`
2. `Initiative` model + `loaders/initiatives.py` (or extend sync orchestration)
3. Extend `Article` frontmatter with optional `initiative` slug; validate against synced initiatives
4. Routes and templates: initiatives index, initiative detail
5. Nav: Initiatives alongside Articles
6. Home: short initiatives section (active/proposed) + existing articles section
7. Port 2–3 seed initiatives and 2–4 articles from 07 (trimmed frontmatter — no member FKs)
8. CSS in `pages.css` / `components.css` only as needed (status badges, initiative cards)

**Out**

- Systems, members, groups, forge, identity
- Recruiting cards and volunteer-page integration
- Initiative creation form (git authoring only — same as 07)
- Open areas yaml
- Deployment, auth, production settings

## Architecture choices to decide

### 1. Loader orchestration

Prototype 15 syncs articles only (`load_articles` + middleware).

Options:

| Option | Pros | Cons |
|---|---|---|
| **A. `load_content` command** — sync initiatives then articles | Matches 07 order; one entry point | New command name; slightly more than 15 |
| **B. Extend middleware** — call initiative loader then article loader | Same dev UX as 15 | Two modules to maintain |
| **C. Separate commands** — `load_initiatives`, `load_articles` | Explicit | Easy to forget order; article sync fails if initiative missing |

**Lean:** A or B — initiatives must sync **before** articles so FK validation works.

### 2. Takers without members

07 validates `takers: [daniel]` against `Member` rows. Without members:

| Option | Example | Trade-off |
|---|---|---|
| Plain strings | `takers: [Daniel]` | Simple; no profile links |
| Slug strings, display as-is | `takers: [daniel]` | Consistent with 07 files; links deferred |
| Omit takers field | — | Loses an important initiative affordance |

**Lean:** slug strings stored on Initiative (JSONField or comma-separated), displayed as text — no FK until members return.

### 3. Status vocabulary

Use current org doc vocabulary (`docs/systems-and-initiatives.md`):

`proposed` | `active` | `paused` | `completed`

Not the older 07 values (`proposal`, `seeking-contributors`). Seed content migrated on port.

## Non-goals (unchanged from repo overview)

Deployment, auth, API, JS tooling, cross-prototype shared packages.

## Open until decided

See [open-questions.md](./open-questions.md). Once closed, write the plan and build prototype 17.
