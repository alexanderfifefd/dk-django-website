# Inheritance from prototype 14

**Date:** 2026-08-27 (updated)

Prototype 15 **forks prototype 14** for HTML/templates initially; this project changes CSS **structure and tokens**, not the settled visual direction.

## Carry forward unchanged (intent)

| Area | Doc |
|---|---|
| Brand tensions | [datakollektivet-brand.md](../../14-design-elements/discussions/datakollektivet-brand.md) |
| Header nav | [header-nav.md](../../14-design-elements/discussions/header-nav.md) |
| Transport / NT | [transport-buttons.md](../../14-design-elements/discussions/transport-buttons.md) |
| Clickable card | [clickable-card.md](../../14-design-elements/discussions/clickable-card.md) |
| Home hero look | [hero-directions.md](../../14-design-elements/discussions/hero-directions.md) — inverted field + band handoff |

## Palette — go deeper in prototype 15

Visual colours stay the same; **names and structure** change. Full proposal:

**[tokens-and-palette.md](./tokens-and-palette.md)** — read this for:

- **Palette layer** — `--color-cream`, `--color-sage`, `--color-peach`, `--color-clay`, …
- **Semantic layer** — `--surface-page`, `--text-link`, `--action-primary`, …
- **Hero inverted** — minimal `--hero-inv-*` group (not sitewide dark mode)
- **Stripe constants** — band heights and band → palette mapping
- **Bevel pattern** — local `--bevel-face` + `color-mix` hi/lo (preserve from `btn-nt.css`)

Note: the **NT look stays, the NT names go** — components rename to generic `btn` / `card` / `panel` ([class-naming.md](./class-naming.md)). Project 14 docs keep their NT vocabulary as historical record.

Prototype 11 [brand-palette.md](../../11-site-design/discussions/brand-palette.md) remains the historical source for hex values.

## What prototype 15 drops (still in 14)

- Hero stripe lab variants (horizon, wings, flat compare grid)
- Full design lab as experiment surface

See [catalog-scope.md](./catalog-scope.md).

## Explicitly out of scope

Re-opening hero direction, card chrome, or nav patterns — update project 14 docs if those change visually.
