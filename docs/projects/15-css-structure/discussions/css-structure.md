# CSS structure — the organising question

**Date:** 2026-08-27  
**Status:** decided — layer split; see [file-layout.md](./file-layout.md)

## Question

Prototype 14 landed the right *look* through iterative CSS — but `site.css` is ~800 lines with section comments, two sibling stylesheets, and page-specific rules mixed with globals. How do we reorganise (and simplify) without losing the brand work?

## Decision

**Option A — split by layer.** Five global stylesheets in fixed order, plus `catalog.css` for the component catalog route only.

```
tokens → base → layout → components → pages   (+ catalog on /design-lab/)
```

Rationale: matches mental model, caps file size, makes “where do I put this?” obvious. Five `<link>` tags is acceptable at our scale; documented in `base.html` and `static/css/README.md`.

Options B–D are set aside — see history in git if needed.

## Constraints (unchanged)

- Hand-written CSS only
- Less code, fewer footguns
- Inherit prototype 14 look; delete lab duplication from 15

## Target outcome

| Before (14/15 fork) | After (15) |
|---|---|
| `site.css` ~793 lines | Split across base/layout/pages |
| `btn-nt.css` separate | Merged into `components.css` |
| `hero-stripe-lab.css` + lab partials | **Deleted** — stays in prototype 14 |
| `.design-lab-*` in global CSS | `catalog.css` only |
| Magic hex in hero | `--hero-inv-*` in `tokens.css` |
| Mixed token names | Palette + semantic layers |

## Related

- [file-layout.md](./file-layout.md) — file tree, load order, rules
- [tokens-and-palette.md](./tokens-and-palette.md)
- [catalog-scope.md](./catalog-scope.md)
- [open-questions.md](./open-questions.md)
