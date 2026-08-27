# Component catalog — scope and spec

**Date:** 2026-08-27 (rewritten after review)  
**Status:** built — live at `/design-lab/` per this spec (footer block demo skipped; forms section gained the `notice` strip)

## What this page is

A **storybook-style component catalog**: one page that shows every pattern in the design system, with variants side by side, the class names to use, and the tokens behind them. Server-rendered Django only — no JS, no interactivity beyond hover states.

It is the place where the design system becomes **visible and larger than the current pages**. The live site only exercises a subset of each component (e.g. only primary buttons with carets in the header); the catalog shows the full variant matrix so new pages can pick from it.

Naming: it stays **"catalog"** — body class `page-catalog`, CSS prefix `catalog-*`, stylesheet `catalog.css`. The URL stays `/design-lab/` for now (route rename to `/catalog/` is optional cleanup later; not worth churn yet).

What it is **not**: an experiment surface. Hero stripe variants and other explorations live in **prototype 14's** design lab. If something is in the catalog here, it is a supported pattern.

## Page anatomy

Every section follows the same shape (this is the storybook convention, minus JS):

```
## Section title            ← component family
Short usage note            ← when to use, one or two sentences
[ demo row — variants side by side, real markup ]
Class reference line        ← `btn`, `btn--secondary`, `btn__caret`
```

Demos use **real markup**: the same Django include the site uses where a partial exists (`card`, `panel`), inline markup where it doesn't (buttons, form fields). If a demo and the site ever look different, that's a bug.

## Sections (v1)

### 1. Foundations

- **Palette swatches** — grid of colour chips: cream, cream-deep, parchment, espresso, stone, rule, sage, sage-hover, peach, clay, peach-tint, clay-tint. Chip shows the colour, token name, and hex.
- **Semantic tokens** — short table: `--surface-*`, `--text-*`, `--action-*`, `--border-*` and which palette colour each points at.
- **Type scale** — one line of text per step (`--font-size-s` → `--font-size-2xl`) at its actual size.
- **Spacing scale** — horizontal bars at each `--space-*` step.

Foundations render from hardcoded chips in the template (values change rarely; a mismatch would be caught by eye here — that's part of the point of the page).

### 2. Buttons

- Variant row: **primary / secondary / tertiary**
- With caret (transport pattern)
- Disabled state
- Usage note: *primary = main action; secondary = warm emphasis; tertiary = section transport; prose links stay links.*

### 3. Cards

- **Action card** (whole-surface link, was tip card): with icon tile, and without
- **Join path card** — the bordered variant used on the join hub (see [join-hub screenshot](../assets/join-hub.png)) with underlined action + caret
- Usage note: entire card is one link; one card = one destination.

### 4. Panel

- Framed panel with title bar + sunken body + action row (was window card)
- Usage note: static chrome; put a button inside for the action.

### 5. Forms

- Field group: label + text input
- Select, textarea (used by join member/volunteer forms)
- Submit row with primary button
- Shown as one small form block, not a full page.

### 6. Navigation & chrome

- Header pattern (logo + nav links with first-letter mark + Join button) — static demo, not the real sticky header
- Stripe (three bands)
- Footer block

### 7. Content patterns

- Section heading with transport button right (home "Latest articles" pattern)
- Article list item (title link + date + summary)
- Prose link vs transport button — side by side with a one-line rule for choosing

## Sections (later, as system grows)

- Hero (inverted) mini-demo — once hero direction is final (waiting per project 14)
- Callout / CTA banner — if prototype 13 shortcode components get promoted
- Tables, blockquotes, code blocks — article typography deep-dive

## CSS

`catalog.css`, loaded only on this route via `extra_css`:

- `catalog-section`, `catalog-note`, `catalog-row` (+ `--stack`), `catalog-demo`
- `catalog-swatch`, `catalog-swatch__chip`, `catalog-swatch__name` — foundations grid
- `catalog-ref` — class reference line under each demo
- **No component internals** — components style themselves from `components.css`; if a demo needs component CSS tweaks, the component is wrong, not the catalog.

## Template

`design_lab.html` (file name stayed) — rebuilt to the section list above. Demos include the real partials:

```django
{% include "public/partials/card.html" with card_url="#" heading="…" %}
{% include "public/partials/card_join.html" %}
{% include "public/partials/panel.html" %}
```

## Removed from prototype 15 (stays in 14)

- Hero stripe lab (all four variants) + `hero-stripe-lab.css` + `hero_lab_*.html` partials
- Variant-caption compare grid — the catalog shows supported patterns, not competing directions

## Baseline screenshots

Reference for what components look like at fork time: [home](../assets/home.png) · [join hub](../assets/join-hub.png) · [about](../assets/about.png)

## Related

- [class-naming.md](./class-naming.md) — generic component names the catalog documents
- [tokens-and-palette.md](./tokens-and-palette.md) — foundations section source of truth
- [file-layout.md](./file-layout.md) — where `catalog.css` sits
