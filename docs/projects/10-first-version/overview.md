# First version

**Question:** What is the smallest useful site that still feels like the collective homepage?

**Status:** In progress — foundation built; first home copy landed (2026-08-21).

**Prototype:** `prototypes/10-first-version/` — see **`README.md`** there for developer onboarding.

**Builds on:** [site-ui](../06-site-ui/overview.md), [member-journeys](../07-member-journeys/overview.md) — design and copy
from prototype 07, deliberately stripped back.

## Scope

Prototype 10 is a **step change**: same visual language as prototype 07, but only what belongs in a first
public version:

| In | Out (for now) |
|---|---|
| Home | Systems index and detail |
| Articles (markdown in git) | Initiatives |
| About | Members index and detail |
| Join hub + sub-paths | Forge issues/PRs, identity linking |
| Site chrome (header, footer, CSS) | Recruiting surfaces, org groups |

Articles are the **only** git-owned collection. Author is a plain string in frontmatter — no member
profiles, no cross-references to systems or initiatives.

Static pages (home intro, about, join) are template HTML, not markdown files.

## Prototype structure

One Django app — **`public`** — holds all visitor-facing code. Internal layout:

```
prototypes/10-first-version/
  README.md         # developer onboarding (standalone-repo ready)
  config/           # project settings, root URLs
  public/           # the public app (not split into many apps)
    loaders/        # git → ORM (load on request in dev, or via load_articles)
    management/commands/load_articles.py
    templates/public/
      layouts/          # pages extend base.html
      partials/         # header, footer — included by base
      home.html
      about.html
      articles/
      join/
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
| Command: **`load_articles`** | Renamed from `sync_content` — matches loader vocabulary. |
| Templates by **section** | `articles/`, `join/`, plus top-level pages; `layouts/` for extend, `partials/` for include. |

**Template conventions** (three layers):

| Layer | Folder | Mechanism | Holds |
|---|---|---|---|
| Layout | `layouts/` | `{% extends %}` | `base.html` — document shell, blocks |
| Partials | `partials/` | `{% include %}` | Header, footer — shared chrome |
| Pages | top-level, `articles/`, `join/` | extends layout | One template per route |

Pages never include header/footer directly — only `layouts/base.html` does.

**UI differences from prototype 07** (same design language, slimmer chrome):

- **Header** — full wordmark top-left; Articles, About, Join top-right
- **Footer** — small logo centered, org. nr. `936667864` below; no newsletter signup, no page links column
- **Join** — hub plus account / member / volunteer sub-pages; no recruiting cards (needs systems/initiatives)

## Prototype mapping

| URL | Template | Notes |
|---|---|---|
| `/` | `public/home.html` | H1, what we do, who we are → about, latest articles, join CTA |
| `/articles/` | `public/articles/index.html` | Synced from `content/articles/*.md` |
| `/articles/<slug>/` | `public/articles/detail.html` | Markdown body from ORM |
| `/about/` | `public/about.html` | Static template |
| `/join/` | `public/join/index.html` | Chooser — three path cards |
| `/join/account/` | `public/join/account.html` | SSO registration link |
| `/join/member/` | `public/join/member.html` | Payment stub form |
| `/join/volunteer/` | `public/join/volunteer.html` | Application form |

All page templates extend `public/layouts/base.html`.

## Docs

1. **`prototypes/10-first-version/README.md`** — developer onboarding (run, layout, articles, language rule)
2. **[minimal-v1-scope.md](./discussions/minimal-v1-scope.md)** — what we cut and why
3. **[2026-08-21-prototype-10-first-version.md](./plans/2026-08-21-prototype-10-first-version.md)** — build plan and outcome

## Related

- [site-design](../11-site-design/overview.md) — brand palette in prototype 11 (`prototypes/11-site-design/`)
- `docs/organizational-context.md` — full noun model (prototype 10 presents a subset)
- `prototypes/07-initiatives/` — feature-rich reference; do not copy wholesale
