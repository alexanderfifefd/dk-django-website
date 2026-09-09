# Articles and initiatives

**Question:** Can we add **initiatives** as a second git-owned collection on prototype 15's stack, with
**articles** linking to them — without importing the full prototype 07 surface area?

**Status:** Discussion (2026-09-03) — docs only; prototype not built yet.

**Prototype (planned):** `prototypes/17-articles-and-initiatives/` — fork of prototype 15.

**Builds on:** [css-structure](../15-css-structure/overview.md) (prototype 15), [initiatives](../07-initiatives/overview.md) (content model and relationships).

## Why this project exists

Prototype 15 validates CSS organisation and ships a pleasant public site with **articles only**.
Prototype 07 validates the full noun model — systems, members, initiatives, groups, forge — in one
large sandbox.

We need a middle step: **initiatives + articles together** on the modern 15 foundation (layered CSS,
`public` app, `loaders/` vocabulary) to test:

- a second authored collection beside articles
- cross-references (`article.initiative`)
- initiative index/detail UI using existing components (`card`, status badges, content sections)
- sync order and validation when two collections depend on each other

Without systems, members, forge, or recruiting surfaces — those stay in 07 until explicitly promoted.

## Reading order

**Start the discussion here:**

1. **[fork-and-scope.md](./discussions/fork-and-scope.md)** — what we fork, what we port from 07, what stays out
2. **[content-model.md](./discussions/content-model.md)** — initiative shape, article links, sync order
3. **[open-questions.md](./discussions/open-questions.md)** — unresolved decisions before a plan

**Authoritative context (do not duplicate):**

- `docs/systems-and-initiatives.md` — initiative vs system definitions
- `docs/projects/07-initiatives/discussions/initiatives-as-a-noun.md` — original initiative decisions
- `docs/projects/07-initiatives/discussions/lifecycle-and-recruiting.md` — status vs recruiting split

## Related

- Prototype 15: `prototypes/15-css-structure/`
- Prototype 07 reference: `prototypes/07-initiatives/`
- Prototype 10 precedent for "strip back 07": `docs/projects/10-first-version/discussions/minimal-v1-scope.md`
