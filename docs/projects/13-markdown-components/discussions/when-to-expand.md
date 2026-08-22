# When to expand markdown components

**Project:** `markdown-components`
**Date:** 2026-08-22

## Question

Article bodies today are markdown → HTML at sync time, stored in `Article.body_html`, rendered with
`|safe`. No second template pass. If we add reusable blocks (callouts, CTAs, highlighted code), **when**
should markdown syntax become HTML?

## Options considered

| Approach | When | Good for | Weak for |
|---|---|---|---|
| **A. Ingest-only** | `load_articles` | Static markup, validated specs, no per-request cost | CSRF forms, live ORM data |
| **B. Render pass** | Request time (filter / template tag) | CSRF, user context, live badges | Extra complexity; git content + Django templates is risky if open-ended |
| **C. Browser JS** | Page load | Interactive charts, tab switching | JS on article pages; CDN deps |
| **D. Sidecar files** | Ingest joins `.md` + sibling asset | Large specs, co-located images | Path resolution, media serving |
| **E. Partial / HTMX** | Separate HTTP request | Heavy or cacheable fragments | More routes; overkill for static blocks |
| **F. Raw HTML in markdown** | Author pastes | One-off embeds | No validation, styling drift |
| **G. Template / frontmatter** | Layout, not body | Same CTA on every article | Inline placement in prose |

We also mapped a wider catalogue (quote, timeline, figure, API example, live forge badges, etc.) against
these columns. Most **typography and static layout blocks** fit **A**. **Forms and live data** need **B**
or **G**. **Interactive charts** need **C** (often with an ingest shell).

## Decision (v1)

**Ingest-only (A)** for the first slice:

- **Callout** — static HTML + CSS class per type
- **CTA banner** — four author fields (header, subheader, button text, url); link is fixed at sync time
- **Syntax-highlighted code** — Pygments (or equivalent) at sync; stored highlighted HTML in `body_html`

No render pass, no JavaScript, no new routes. The article template stays:

```django
{{ article.body_html|safe }}
```

### Why not render time (v1)?

We discussed newsletter forms and similar CTAs that need CSRF tokens. That pushes toward a render pass.
For v1 the CTA is a **link button** (GET to `/join/` or similar), not a POST form — so ingest is enough.
Forms and live data are explicitly deferred.

### Update (2026-08-22): hybrid for cross-entity shortcodes

We prototyped **article callout at ingest** with a catalog pass in `load_articles`. It worked, but scaling
to more collections (systems, members, initiatives) would bloat the loader and denormalize cross-refs into
`body_html`.

**Revised rule:**

| Shortcode kind | When | Examples |
|---|---|---|
| Self-contained | **Ingest** | callout, CTA, timeline, figure (static) |
| References another synced row | **Render** (placeholder at ingest) | article callout, system badge, member card |

Article callout ingest code was **removed**. See [article-callout.md](./article-callout.md).

### Why not browser JS?

Charts and tabbed API examples were examples of client-side expansion. v1 components are purely presentational.
JS remains available later without changing the ingest pipeline shape.

### Why not Django template tags in markdown?

Authors would write `{% include … %}` inside `.md` files. That requires either trusting git content with
the template engine (bad) or a sandboxed tag library (heavy). **Shortcodes** — a small author-facing syntax
expanded by Python at ingest — give reuse without exposing Django templates to content.

## Implementation shape (ingest shortcodes)

See [shortcode-registry.md](./shortcode-registry.md) for package layout. Pipeline:
1. **Pre-process** — `expand_shortcodes()` before Python-Markdown; validate; emit HTML (or placeholders for live blocks).
2. **Markdown** — fenced code, tables, smarty, codehilite on the result.
3. **CSS** — `static/css/site.css` for component classes.

Ingest errors (unknown type, missing field) fail `load_articles` like bad frontmatter.

## Deferred to later projects

| Component | Likely approach |
|---|---|
| Article callout | Render (placeholder at ingest) — see [article-callout.md](./article-callout.md) |
| Figure + caption | Ingest + sidecar (media project) |
| Timeline | Ingest |
| API example (tabs) | Ingest shell + optional JS |
| Newsletter / POST form | Render pass or template slot |
| Live system badge, forge issues | Render pass or HTMX |

## Non-goals (unchanged)

Cross-prototype shared library, npm/JS build pipeline, deployment.
