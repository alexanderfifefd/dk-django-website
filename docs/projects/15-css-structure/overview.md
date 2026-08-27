# CSS structure

**Question:** How should we organise hand-written CSS so it stays minimal, readable, and safe to change at our scale?

**Status:** implemented — refactor landed 2026-08-27; all six phases done in one pass, greps clean, routes verified.

**Prototype:** `prototypes/15-css-structure/` — fork of prototype 14; CSS refactor only.

**Builds on:** [design-elements](../14-design-elements/overview.md), [site-design](../11-site-design/overview.md)

## Goals

1. **Layer split** — tokens, base, layout, components, pages (+ catalog)
2. **Token system** — palette + semantic names; spacing/type scales; minimal hero-inverted group
3. **Generic component names** — `btn` / `card` / `panel`; NT naming retired (bevel look stays)
4. **Component catalog** — storybook-style page showing the full variant matrix
5. **Less code** — delete lab duplication, legacy `.btn`, dead rules
6. **Human-readable** — README in `static/css/`, BEM for components

## Reading order

**Decisions (review before code):**

1. **[file-layout.md](./discussions/file-layout.md)** — decided file tree + load order
2. **[tokens-and-palette.md](./discussions/tokens-and-palette.md)** — palette, semantic, scales, hero-inv tokens
3. **[class-naming.md](./discussions/class-naming.md)** — BEM + de-NT renames (`btn`, `card`, `panel`)
4. **[catalog-scope.md](./discussions/catalog-scope.md)** — storybook-style component catalog spec

**Context:**

5. **[css-structure.md](./discussions/css-structure.md)** — why layer split
6. **[current-state.md](./discussions/current-state.md)** — fork baseline audit
7. **[inheritance-from-14.md](./discussions/inheritance-from-14.md)** — what we keep visually
8. **[open-questions.md](./discussions/open-questions.md)** — decided vs still open
9. **[visual-checklist.md](./discussions/visual-checklist.md)** — manual QA routes

## Plan

- [2026-08-27-prototype-15-css-structure.md](./plans/2026-08-27-prototype-15-css-structure.md)

## Related

Prototype 14 design exploration: `docs/projects/14-design-elements/` (paused, not superseded).
