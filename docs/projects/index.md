# Projects

A **project** is one line of enquiry: a question about the markdown-driven approach, the options considered,
the decision taken, and the prototype built to test it. Projects are procedural logs — they record what we
thought at the time and are not rewritten when we later change our minds. A later project supersedes an
earlier one instead.

Each project lives in `docs/projects/NN-<slug>/`:

- `overview.md` — when present, project summary, file index, and suggested reading order.
- `discussions/<slug>.md` — the question, the options, the reasoning, the decision.
- `plans/YYYY-MM-DD-<slug>.md` — what will be built, in what order, and how we'll know it worked.

**Naming:** `NN` is the prototype number the project works in — the same prefix as
`prototypes/NN-<slug>/`. Most projects map 1:1 to one prototype directory. When several lines of enquiry
share a prototype (e.g. `07-initiatives`, `07-member-journeys`, and `07-groups` all on
`prototypes/07-initiatives/`), each enquiry still gets its own doc folder with the shared `NN` prefix.

## Starting a new project

Discussion first, then an entry under Active here, then a plan once a decision is reached, then the
prototype (`prototypes/NN-<slug>/`, numbered in build order) and matching docs folder
(`docs/projects/NN-<slug>/`). When the question is answered, note the outcome in the plan and move the
project to Completed.

## Active

### `transactional-emails` — join forms → org inbox via Scaleway TEM?

**Status: built 2026-09-11** — three paths (`/join/follow/`, `/join/member/`, `/join/build/`) notify `hei@datakollektivet.no` with suggested reply templates. No auto-email to visitors. Django Forms, console/SMTP mailers, no DB storage.

- **Overview**: `docs/projects/20-transactional-emails/overview.md` — **start here**
- **Plan**: `docs/projects/20-transactional-emails/plans/2026-09-11-prototype-20-transactional-emails.md`
- **Discussion**: `docs/projects/20-transactional-emails/discussions/pivot-to-manual-onboarding.md`
- **Prototype**: `prototypes/20-transactional-emails/`
- **Builds on**: [`css-structure`](15-css-structure/overview.md)

### `articles-and-initiatives` — initiatives + articles on the prototype 15 stack?

**Status: discussion (2026-09-03)** — docs only. Fork prototype 15; port initiative abstractions from
prototype 07 (content shape, article cross-refs, index/detail routes). No systems, members, or forge.

- **Overview**: `docs/projects/17-articles-and-initiatives/overview.md` — **start here**
- **Discussion**: `docs/projects/17-articles-and-initiatives/discussions/fork-and-scope.md` — fork base, in/out
- **Discussion**: `docs/projects/17-articles-and-initiatives/discussions/content-model.md` — initiative + article shape
- **Discussion**: `docs/projects/17-articles-and-initiatives/discussions/open-questions.md` — decisions before plan
- **Prototype (planned)**: `prototypes/17-articles-and-initiatives/`
- **Builds on**: [`css-structure`](15-css-structure/overview.md), [`initiatives`](07-initiatives/overview.md)

### `deployment-pipeline` — what is the smallest site we can deploy to test the pipeline?

**Status: built 2026-08-30** — one route, header/footer chrome, one CSS file, `STATIC_ROOT` for
`collectstatic`. No ORM, markdown, or content loaders.

- **Overview**: `docs/projects/16-deployment-pipeline/overview.md` — **start here**
- **Discussion**: `docs/projects/16-deployment-pipeline/discussions/minimal-deploy-scope.md`
- **Plan**: `docs/projects/16-deployment-pipeline/plans/2026-08-30-prototype-16-deployment-pipeline.md`
- **Prototype**: `prototypes/16-deployment-pipeline/`
- **Inherits layout from**: [`first-version`](10-first-version/overview.md)

### `css-structure` — how should hand-written CSS be organised at our scale?

**Status: built 2026-08-27** — six-file layer split (tokens → base → layout → components → pages → catalog) live on prototype 15; two-layer token system, de-NT naming (`btn`/`card`/`panel`), storybook-style catalog at `/design-lab/`, and `static/css/README.md` for contributors. Also shipped from the same review: article-list card redesign, NT sunken-bevel forms, bottom stripe, HTML nav marks.

- **Overview**: `docs/projects/15-css-structure/overview.md` — **start here**
- **Discussion**: `docs/projects/15-css-structure/discussions/file-layout.md` — layer split (decided)
- **Discussion**: `docs/projects/15-css-structure/discussions/tokens-and-palette.md` — token system + scales
- **Discussion**: `docs/projects/15-css-structure/discussions/class-naming.md` — BEM + de-NT renames
- **Discussion**: `docs/projects/15-css-structure/discussions/catalog-scope.md` — storybook-style component catalog
- **Plan**: `docs/projects/15-css-structure/plans/2026-08-27-prototype-15-css-structure.md`
- **Prototype**: `prototypes/15-css-structure/`
- **Inherits look from**: [`design-elements`](14-design-elements/overview.md) (paused)

### `design-elements` — how should reusable visual components look on the site?

**Status: paused 2026-08-27** — NT chrome, clickable card, and night-sky hero liked on prototype 14; hero stripe lab open; nothing promoted to prototype 11.

- **Overview**: `docs/projects/14-design-elements/overview.md`
- **Brand**: `docs/projects/14-design-elements/discussions/datakollektivet-brand.md` — **start here**
- **Hero**: `docs/projects/14-design-elements/discussions/hero-directions.md` — night sky on home; stripe lab on `/design-lab/`
- **Clickable card**: `docs/projects/14-design-elements/discussions/clickable-card.md` — tip + window variants; liked
- **Transport / NT buttons**: `docs/projects/14-design-elements/discussions/transport-buttons.md`
- **Prototype**: `prototypes/14-design-elements/`

### `markdown-components` — can articles carry reusable components in markdown?

**Status: in progress** — prototype 13 built (2026-08-22).

Ingest-time shortcodes: callout, CTA banner, syntax-highlighted code. Shortcode package + registry.
Article callout planned at **render-time** (ingest approach tried and reverted). Showcase article in
`content/articles/markdown-features.md`. Fork of prototype 11.

- **Overview**: `docs/projects/13-markdown-components/overview.md` — **start here**
- **Discussion**: `docs/projects/13-markdown-components/discussions/when-to-expand.md`
- **Discussion**: `docs/projects/13-markdown-components/discussions/shortcode-registry.md`
- **Discussion**: `docs/projects/13-markdown-components/discussions/v1-component-syntax.md`
- **Discussion**: `docs/projects/13-markdown-components/discussions/article-callout.md`
- **Plan**: `docs/projects/13-markdown-components/plans/2026-08-22-prototype-13-markdown-components.md`
- **Plan**: `docs/projects/13-markdown-components/plans/2026-08-22-shortcode-package-split.md`
- **Plan**: `docs/projects/13-markdown-components/plans/2026-08-22-article-callout.md` (planned)
- **Prototype**: `prototypes/13-markdown-components/`

### `dark-mode` — how should the site look on a dark background?

**Status: in progress** — first pass on prototype 12 (2026-08-21).

Charcoal + cream palette from the dark brand mockup. Fork of prototype 11; CSS tokens only.
Prototype 11 stays on the light palette.

- **Overview**: `docs/projects/12-dark-mode/overview.md` — **start here**
- **Discussion**: `docs/projects/12-dark-mode/discussions/dark-palette.md`
- **Plan**: `docs/projects/12-dark-mode/plans/2026-08-21-prototype-12-dark-mode.md`
- **Prototype**: `prototypes/12-dark-mode/`

### `site-design` — how should the first public site look?

**Status: in progress** — first design pass on prototype 11 (2026-08-21); see iteration summary.

Warm cream + sage / peach / clay palette. Fork of prototype 10; CSS tokens only in
`prototypes/11-site-design/`. Prototype 10 stays on generic blue tokens.

- **Overview**: `docs/projects/11-site-design/overview.md` — **start here**
- **Discussion**: `docs/projects/11-site-design/discussions/brand-palette.md`
- **Discussion**: `docs/projects/11-site-design/discussions/stripe-variants.md`
- **Summary**: `docs/projects/11-site-design/discussions/2026-08-21-design-iteration-summary.md`
- **Plan**: `docs/projects/11-site-design/plans/2026-08-21-prototype-11-site-design.md`
- **Prototype**: `prototypes/11-site-design/`

### `first-version` — what is the smallest useful public site?

**Status: in progress** — foundation built; home copy v1 (2026-08-21).

Focused fork of the prototype 07 design: home, markdown articles, about, join hub + sub-paths. No
systems, initiatives, members, or forge surfaces. Single Django app `public`; `loaders/` +
`load_articles`; templates in `layouts/`, `partials/`, and section folders. Onboarding:
`prototypes/10-first-version/README.md`.

- **Overview**: `docs/projects/10-first-version/overview.md` — **start here**
- **Discussion**: `docs/projects/10-first-version/discussions/minimal-v1-scope.md`
- **Plan**: `docs/projects/10-first-version/plans/2026-08-21-prototype-10-first-version.md`
- **Prototype**: `prototypes/10-first-version/`

### `member-journeys` — how should the site convert visitors into participants?

**Status: in progress** — three Join paths on prototype 07 (2026-08-14).

`/join/` chooser → **account**, **member**, **volunteer**. Core model in
**[`docs/organizational-context.md`](../../organizational-context.md)**; implementation in
[member-journeys](docs/projects/07-member-journeys/overview.md).

- **Overview**: `docs/projects/07-member-journeys/overview.md` — **start here**
- **Discussion**: `docs/projects/07-member-journeys/discussions/three-paths-to-participate.md`
- **Discussion**: `docs/projects/07-member-journeys/discussions/help-wanted-and-recruiting.md`
- **Plan**: `docs/projects/07-member-journeys/plans/2026-08-14-three-join-paths.md`
- **Prototype**: `prototypes/07-initiatives/`

### `initiatives` — how should we represent goal-oriented efforts on the site?

**Status: in progress** — prototype 07 forked from 06 (2026-08-13); lifecycle/recruiting in content
model (2026-08-14).

Initiatives are distinct from systems: goal-oriented efforts with taker(s), lifecycle status, optional
`recruiting: open`, and authored updates. Fork of prototype 06; English slugs and copy; Systems +
Initiatives in left nav; index pages grouped by lifecycle. Git authoring only — no creation form.

- **Overview**: `docs/projects/07-initiatives/overview.md` — **start here**
- **Discussion**: `docs/projects/07-initiatives/discussions/initiatives-as-a-noun.md`
- **Discussion**: `docs/projects/07-initiatives/discussions/lifecycle-and-recruiting.md`
- **Plan**: `docs/projects/07-initiatives/plans/2026-08-13-prototype-07-initiatives.md`
- **Prototype**: `prototypes/07-initiatives/`

### `groups` — how should we present Board, Maintainers, and Moderators?

**Status: built** (2026-08-14).

Org groups on the existing `Group` model in **prototype 07** — enriched `groups.yaml`, Members index
sections per group, About pointers. **No separate prototype** (`08-groups/` does not exist); this project
is a pass on `prototypes/07-initiatives/` alongside `initiatives`.

- **Overview**: `docs/projects/07-groups/overview.md` — **start here** (includes prototype mapping)
- **Discussion**: `docs/projects/07-groups/discussions/org-groups-on-the-site.md`
- **Plan**: `docs/projects/07-groups/plans/2026-08-14-three-org-groups.md`
- **Prototype**: `prototypes/07-initiatives/` (shared with `initiatives`; not a standalone fork)

### `site-ui` — how should we present systems, members, articles, and updates?

**Status: paused** — UI baseline validated (2026-08-12). Resume for content polish or forge surfaces.

Authored content only (no forge). Markdown in git syncs to ORM via `pages/sources/`; dev middleware
re-syncs on each request. Real collective data: 9 members, 6 systems, 2 groups, 1 article. Site chrome,
about/join pages, system `stage` and `url`, article layouts in place.

- **Overview**: `docs/projects/06-site-ui/overview.md` — **start here for current state**
- **Discussion**: `docs/projects/06-site-ui/discussions/ui-without-ingest.md` (original decision)
- **Discussion**: `docs/projects/06-site-ui/discussions/orm-pivot-for-ui-queries.md` (current architecture)
- **Plan**: `docs/projects/06-site-ui/plans/2026-08-12-prototype-06-site-ui.md`
- **Prototype**: `prototypes/06-site-ui/`

## Completed

### `git-identity` — how do we link cross-system activity to users?

**Answer: yes, via git-backed identity assertions.** Member profiles in `content/members/<slug>.md` carry
an `identities` map in frontmatter (e.g. `forgejo: alexanrf`). The filename is the canonical slug for
cross-references. `sync_issues` matches forge author logins against that map and sets a nullable
`Issue.member` FK. Member pages show markdown bio plus linked PRs and open issues; a members index
lists active members. No SSO or Django auth required.

- **Overview**: `docs/projects/05-git-identity/overview.md`
- **Discussion**: `docs/projects/05-git-identity/discussions/sso-and-account-linking.md`
- **Discussion**: `docs/projects/05-git-identity/discussions/federated-identity-via-git.md`
- **Discussion**: `docs/projects/05-git-identity/discussions/member-slug-and-references.md`
- **Discussion**: `docs/projects/05-git-identity/discussions/organizational-implications.md`
- **Discussion**: `docs/projects/05-git-identity/discussions/forgejo-api-for-identity.md`
- **Plan**: `docs/projects/05-git-identity/plans/2026-08-08-prototype-05-git-identity.md`
- **Prototype**: `prototypes/05-git-identity/` — built and validated (2026-08-12)

### `forge-issues` — does the ingest pattern extend to a forge's HTTP API?

**Answer: yes.** Forgejo issues and pull requests, labeled `system/<slug>` in one monorepo, cached as a
derived table alongside git-owned systems. First API source; Pydantic with `extra="ignore"` at the
boundary; separate `sync_issues` command. Issues and PRs render as linked lists (open/closed badges on
PRs); updates stay as authored JSON beside each system.

- **Discussion**: `docs/projects/04-forge-issues/discussions/issues-from-the-forge.md`
- **Primitives brainstorm**: `docs/projects/04-forge-issues/discussions/forge-primitives-as-site-content.md`
- **Plan**: `docs/projects/04-forge-issues/plans/2026-08-07-prototype-04-forge-issues.md`
- **Prototype**: `prototypes/04-forge-issues/` — built and validated (2026-08-08)

### `integration-layer` — do collections, relationships, and mixed sources break the ingest pattern?

**Answer: yes, with separate sync commands.** Three derived collections (members from `external/`,
systems and articles from git) with real FKs and strict cross-source validation. Updates stay in a
JSONField without pain at this scale. Dev middleware deferred — manual sync remains.

- **Discussion**: `docs/projects/03-integration-layer/discussions/collections-relationships-and-freshness.md`
- **Plan**: `docs/projects/03-integration-layer/plans/2026-08-06-prototype-03-integration-layer.md`
- **Prototype**: `prototypes/03-integration-layer/` — built and validated (2026-08-07)

### `markdown-pages` — can markdown files on disk be the content layer?

**Answer: yes.** Markdown files with frontmatter work as the authoring format; per-request parsing worked
at toy scale but gave up querying, validation, and relationships. Superseded by `content-pipeline`.

- **Discussion**: `docs/projects/01-markdown-pages/discussions/filesystem-as-content-source.md`
- **Learnings**: `docs/projects/01-markdown-pages/discussions/learnings-from-prototype-01.md`
- **Plan**: `docs/projects/01-markdown-pages/plans/2026-08-06-prototype-01-markdown-pages.md`
- **Prototype**: `prototypes/01-markdown-pages/` — built and working (2026-08-06)

### `content-pipeline` — who owns the path from markdown file to page?

**Answer: we do.** No credible package exists; a ~100-line ingest command with strict validation syncs
files into a derived `Post` table. Main cost found: the save–ingest–reload authoring loop, picked up by
`integration-layer`.

- **Discussion**: `docs/projects/02-content-pipeline/discussions/who-owns-the-markdown-layer.md`
- **Learnings**: `docs/projects/02-content-pipeline/discussions/learnings-from-prototype-02.md`
- **Plan**: `docs/projects/02-content-pipeline/plans/2026-08-06-prototype-02-content-pipeline.md`
- **Prototype**: `prototypes/02-content-pipeline/` — built and validated (2026-08-06)

## Open questions not yet claimed by a project

These are known unknowns. Each will likely become its own project.

- **Draft preview**: drafts are simply not ingested; viewing one at its URL behind an explicit flag is
  unexplored.
- **Media and assets**: images and other files living next to the `.md` files that reference them.
  Site chrome (logo, CSS) stays in `static/`; author content stays in `content/`. Today
  `render_markdown()` emits bare relative `<img src="…">` paths with no bridge to HTTP — they 404.
  Likely a dedicated prototype (`07-media-assets` or similar). Open design choices:
  - **Co-location** — e.g. `content/articles/<slug>/article.md` + `diagram.png`; markdown uses relative
    paths.
  - **Serve from git** — URL maps into `CONTENT_DIR`; ingest rewrites paths in `body_html` (no copy;
    custom view + path safety).
  - **Copy at sync** — `sync_content` mirrors assets into `static/content/…`; ingest rewrites to
    static URLs (simpler serving, derived like the ORM).
  - **Scope** — inline markdown images first; frontmatter assets (member avatar, system hero) can reuse
    the same resolver.
  - **Touched by** — `pages/sources/common.py` (`render_markdown` needs a source path), plus either a
    content-media view or a sync copy step.
- **Template tags and HTML components in markdown** — **partially claimed** by
  [`markdown-components`](13-markdown-components/overview.md) (callout, CTA, code highlight at ingest;
  shortcode package; article callout planned at render-time). Still open: other live ORM embeds, figures,
  timeline, API tabs, forms with CSRF. Ingest shortcodes expand at sync; cross-ref cards will resolve at
  render.
- **Scale**: parked. Never measured, not currently a priority.
- **Forge content presentation**: prototype 04 syncs issues and PRs and renders plain linked lists.
  How to present them on the site is unresolved — e.g. promoting certain forge labels prominently
  (`seeking-maintainer`, `help wanted`), dedicated surfaces (get-involved page, system timeline),
  or giving labels semantics beyond small tags (status badges). Partially related to `site-ui`
  (authored-noun presentation comes first); forge surfaces can layer onto those templates later.