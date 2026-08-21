# First version

**Question:** What is the smallest useful site that still feels like the collective homepage?

**Status:** In progress — prototype 10 scaffolded (2026-08-21).

**Prototype:** `prototypes/10-first-version/`

**Builds on:** [site-ui](../site-ui/overview.md), [member-journeys](../member-journeys/overview.md) — design and copy
from prototype 07, deliberately stripped back.

## Scope

Prototype 10 is a **step change**: same visual language as prototype 07, but only what belongs in a first
public version:

| In | Out (for now) |
|---|---|
| Home | Systems index and detail |
| Articles (markdown in git) | Initiatives |
| About | Members index and detail |
| Join hub | Forge issues/PRs, identity linking |
| Site chrome (header, footer, CSS) | Recruiting surfaces, org groups |

Articles are the **only** git-owned collection. Author is a plain string in frontmatter — no member
profiles, no cross-references to systems or initiatives.

Static pages (home intro, about, join) are template HTML, not markdown files.

## Prototype structure

One Django app — **`public`** — holds all visitor-facing code. Internal layout:

```
prototypes/10-first-version/
  config/           # project settings, root URLs
  public/           # the public app (not split into many apps)
    loaders/        # git → ORM sync (was `sources/` in earlier prototypes)
    templates/public/
    views.py
    models.py
    middleware.py
  content/articles/
  static/
```

**Naming decisions:**

| Choice | Reason |
|---|---|
| App: **`public`** | One app for the unauthenticated site. Pairs with a future **`portal`** app for logged-in users. |
| Not **`site`** | Python stdlib already has a `site` module — imports break. |
| Not **`pages`** | Scaffold name only; too generic for a deliberate app boundary. |
| Folder: **`loaders/`** | Renamed from `sources/` — these modules load markdown from disk into the ORM. |

**UI differences from prototype 07** (same design language, slimmer chrome):

- **Header** — full wordmark top-left; Articles, About, Join top-right
- **Footer** — small logo centered, org. nr. `936667864` below; no newsletter signup, no page links column
- **Join** — hub plus account / member / volunteer sub-pages; no recruiting cards (needs systems/initiatives)

## Prototype mapping

| URL | Notes |
|---|---|
| `/` | Hero, latest articles, join CTA |
| `/articles/`, `/articles/<slug>/` | Synced from `content/articles/*.md` |
| `/about/` | Static template |
| `/join/` | Chooser — three path cards |
| `/join/account/` | Create account (SSO link) |
| `/join/member/` | Membership + payment stub form |
| `/join/volunteer/` | Volunteer application form |

## Docs

1. **[minimal-v1-scope.md](./discussions/minimal-v1-scope.md)** — what we cut and why
2. **[2026-08-21-prototype-10-first-version.md](./plans/2026-08-21-prototype-10-first-version.md)** — build plan

## Related

- `docs/organizational-context.md` — full noun model (prototype 10 presents a subset)
- `prototypes/07-initiatives/` — feature-rich reference; do not copy wholesale
