# Article callout shortcode

**Project:** `markdown-components`
**Date:** 2026-08-22

## Question

Can authors embed a **prominent link card** to another article inline — with title and summary from the
target, not duplicated in markdown?

## Author syntax (proposed)

```markdown
:::article
slug: building-the-collective-homepage
:::
```

Optional later: `label: See also` to override the default “Related article” line.

Authors write **slug only**. Title and summary come from the target article's frontmatter / ORM row.

## What it is (and isn't)

| Thing | Role |
|---|---|
| Inline `[text](/articles/slug/)` | Link inside a sentence |
| **Article callout** | Editorial “read this next” card in the prose flow |
| CTA banner | Action (join, download) — fixed copy in the shortcode |
| Related posts footer | Template chrome, same on every page |

## Options considered

### A. Full expansion at ingest

At `load_articles`, look up the target slug in a **catalog** built from all `content/articles/*.md`
frontmatter, emit final HTML into `body_html`.

| Pros | Cons |
|---|---|
| No render pass | Catalog pass in loader for every cross-ref type (articles, then systems, members…) |
| Sync-time validation of slugs | Title/summary **denormalized** — linking articles must re-sync when target edits |
| | `articles.py` becomes site-wide orchestrator |

We built this. It worked for articles-only. Reverted (2026-08-22).

### B. Placeholder at ingest, resolve at render (chosen)

**Ingest** validates slug syntax and emits:

```html
<aside class="article-callout" data-article-slug="building-the-collective-homepage"></aside>
```

**Render** (view or template filter) looks up `Article` by slug and fills the card:

```html
<aside class="article-callout">
  <p class="article-callout-label">Related article</p>
  <h3 class="article-callout-title"><a href="/articles/…/">…</a></h3>
  <p class="article-callout-summary">…</p>
</aside>
```

| Pros | Cons |
|---|---|
| Loader stays thin | Small render pass (bounded — not open Django templates in markdown) |
| Card always fresh from ORM | Broken slug at **view** time unless optional validate command |
| Scales to systems/members same pattern | |

### C. Template / frontmatter only

`related: [slug-a, slug-b]` in frontmatter; template renders cards after body.

Rejected for inline placement — author cannot choose where in the prose the card appears.

## Decision

**B — hybrid.** Fits the rule in [when-to-expand.md](./when-to-expand.md): self-contained blocks at ingest;
references to other synced rows at render (placeholder in stored HTML).

Ingest prototype (A) was removed from prototype 13. Implementation not started.

## Open choices (when building)

- **Unknown slug at render:** omit card, show empty box, or 500?
- **Self-link:** reject at ingest when validating placeholder?
- **Optional `validate_articles` command:** sync-time slug check without full catalog expansion

## Related

- [when-to-expand.md](./when-to-expand.md) — general ingest vs render matrix
- [shortcode-registry.md](./shortcode-registry.md) — ingest registry stays separate from live resolution
- [v1-component-syntax.md](./v1-component-syntax.md) — author syntax reference (when implemented)
