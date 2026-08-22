# Markdown components

**Question:** Can git-authored article markdown carry a small, validated set of reusable components — and
when should they be expanded to HTML?

**Status:** in progress — prototype 13 built (2026-08-22).

**Prototype:** `prototypes/13-markdown-components/` — fork of prototype 11.

**Builds on:** [first-version](../10-first-version/overview.md), [site-design](../11-site-design/overview.md)

## Scope (v1)

Three **ingest-time** shortcodes plus a **showcase article** that documents everything an author can use in
`content/articles/` — base markdown and the new blocks together.

| In scope (v1) | Out of scope (v1) |
|---|---|
| Callout (note / warning / tip) | Render-time live shortcodes (planned) |
| Generic CTA banner | Browser JS hydration |
| Syntax-highlighted fenced code | Figures with caption (needs media project) |
| Shortcode package + registry | Timeline, API example tabs |
| Showcase article | Django template tags inside markdown |

**Article callout** — discussed and planned; ingest prototype reverted. See
[article-callout.md](./discussions/article-callout.md).

## Docs (reading order)

**Discussions first** — reasoning and decisions:

1. **[when-to-expand.md](./discussions/when-to-expand.md)** — ingest vs render vs JS; hybrid rule
2. **[shortcode-registry.md](./discussions/shortcode-registry.md)** — package layout and registry pattern
3. **[v1-component-syntax.md](./discussions/v1-component-syntax.md)** — author syntax (implemented + planned)
4. **[article-callout.md](./discussions/article-callout.md)** — link card; why render-time

**Plans** — what was or will be built:

5. **[2026-08-22-prototype-13-markdown-components.md](./plans/2026-08-22-prototype-13-markdown-components.md)** — initial prototype
6. **[2026-08-22-shortcode-package-split.md](./plans/2026-08-22-shortcode-package-split.md)** — registry refactor (complete)
7. **[2026-08-22-article-callout.md](./plans/2026-08-22-article-callout.md)** — link card (planned)

## Related

- `docs/projects/index.md` — repo project list
- [site-design](../11-site-design/overview.md) — fork source
- Media/assets — unclaimed; figures deferred
