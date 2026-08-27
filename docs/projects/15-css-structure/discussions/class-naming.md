# Class naming

**Date:** 2026-08-27 (reworked after review)  
**Status:** implemented — all renames landed; grep list verified zero

## Decision: NT is a style, not a name

The Windows-NT bevel is **how our components look**, not what they are. Class names use the **common design-system vocabulary** — button, card, panel — so a contributor recognises them instantly. `btn-nt`, `panel-nt`, `win-nt`, `--bg-nt-tip` all go. The bevel chrome itself is unchanged.

## Rules

1. **Block** — standalone component: `btn`, `card`, `panel`, `site-header`
2. **Element** — part of a block: `btn__caret`, `card__title`, `panel__titlebar`
3. **Modifier** — variant or state: `btn--primary`, `card--path`, `hero--inverted`
4. **Page scope** — on `<body>`: `page-home`, `page-join`, `page-catalog`
5. **BEM separators** — hyphenated block names, `__` element, `--` modifier

## Component renames (the de-NT pass)

### Button — `btn`

The old rounded `.btn` is deleted (all buttons are the bevel button now), which frees the name:

| Old | New |
|---|---|
| `btn-nt` | `btn` |
| `btn-nt--primary` / `--secondary` / `--tertiary` | `btn--primary` / `--secondary` / `--tertiary` |
| `btn-nt--with-caret` | `btn--with-caret` |
| `btn-nt__caret` | `btn__caret` |
| `.btn`, `.btn-primary`, `.btn--transport`, `.btn__icon` (legacy rounded) | **deleted** — templates move to new `btn btn--primary` |

**Order matters:** legacy `.btn` deletion and `btn-nt → btn` rename happen in the **same phase** — otherwise the names collide.

### Card — `card` (was tip card / clickable card)

Whole-surface link card. `clickable-card` class dropped — clickability is the card's default behaviour, not a modifier.

| Old | New |
|---|---|
| `clickable-card panel-nt` | `card` |
| `panel-nt__icon` | `card__icon` |
| `panel-nt__content` | `card__body` |
| `panel-nt__heading` | `card__title` |
| `panel-nt__copy` | `card__text` |
| `panel-nt__go` | `card__action` |
| join path cards (join hub) | plain `card` — the three paths are visually uniform, so no `card--path` / lane modifiers were needed; lane semantic tokens stay in `tokens.css` for when a lane accent is actually designed |

**Added at implementation:** `card__meta` — muted meta line (date · author) for article cards; article lists on home and `/articles/` now use `card` too (the articles redesign).

### Panel — `panel` (was window card)

Static framed chrome: title bar + sunken body + button inside.

| Old | New |
|---|---|
| `win-nt` | `panel` |
| `win-nt__titlebar` | `panel__titlebar` |
| `win-nt__body` | `panel__body` |
| `win-nt__actions` | `panel__actions` |
| `.win-nt__body .panel-nt__heading` etc. | `panel__title`, `panel__text` — own elements, no cross-block reach-ins |

### Hero

| Old | New |
|---|---|
| `hero--night` | `hero--inverted` |
| `hero-night__stars` / `__bands` / `__band--sage` / `__content` | `hero-inv__stars` / `__bands` / `__band--sage` / `__content` |

Generic `.hero` / `.page-hero` stay for inner-page titles.

### Catalog page

| Old | New |
|---|---|
| `page-design-lab` | `page-catalog` |
| `design-lab-section` / `-note` / `-row` / `-demo` | `catalog-section` / `catalog-note` / `catalog-row` / `catalog-demo` |
| `design-lab-caption` | removed (no compare grids) |
| `design-lab-footer-note` | `catalog-footer` |

URL stays `/design-lab/` for now.

### Layout & navigation (keep — mostly)

`site-top`, `site-header`, `site-logo`, `site-nav`, `site-stripe`, `site-stripe-band(-*)`, `site-footer`, `footer-lab`, `nav-join`, `section-heading`, `home-section` — no churn.

**One change:** `nav-link--mark` (CSS `::first-letter`) became `nav-link` + a `nav-mark` `<span>` wrapping the first letter **in the template**. `::first-letter` only works on block containers and silently breaks under display changes — the mark is content, so it lives in HTML.

### Forms (new component names)

| Old | New |
|---|---|
| `join-form` | `form-stack` (generic — sunken bevel fields, sage focus ring) |
| `join-form-checkbox` | `form-checkbox` |
| `join-notice` | `notice` (sunken parchment strip) |
| `field-hint` | unchanged |

## Template partials (rename with classes)

Simplest thing that works with Django: **one include per component**, named after the component:

| Old partial | New partial |
|---|---|
| `join_panel_nt.html` | `card_join.html` (the home join CTA instance) |
| `clickable_card.html` | `card.html` |
| `window_card_nt.html` | `panel.html` |
| `panel_nt_caret.html` | `caret.html` (shared pixel caret — also stops the inline SVG copy-paste in header/home) |
| `hero_lab_*.html` | deleted (stay in prototype 14) |

The pixel-caret SVG is currently pasted inline in three templates; `{% include "public/partials/caret.html" %}` replaces all copies.

## What we are not doing

- Utility classes (`mt-4`, `text-muted`) — tokens + component rules instead
- SMACSS prefixes (`l-`, `c-`) — the file split carries layer info
- Template component libraries / custom tags — plain includes are enough at this scale

## Grep list for the rename (verification)

After the pass, these must return **zero** hits in `prototypes/15-css-structure/` (CSS + templates):

```
btn-nt   panel-nt   win-nt   clickable-card   nt-tip   hero-night   hero--night   design-lab-   btn-primary
```

## Related

- [tokens-and-palette.md](./tokens-and-palette.md) — `--surface-panel` replaces `--bg-nt-tip`
- [catalog-scope.md](./catalog-scope.md) — catalog documents these names
- [visual-checklist.md](./visual-checklist.md) — post-rename QA
