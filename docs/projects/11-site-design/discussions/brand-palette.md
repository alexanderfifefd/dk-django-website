# Discussion: brand color palette

**Project:** `site-design`
**Date:** 2026-08-21
**Prototype:** `prototypes/11-site-design/`
**Builds on:** [first-version](../../10-first-version/overview.md) — prototype 10 unchanged
**Status:** palette captured; exact text color and derivations open

## The question

Prototype 10 reuses prototype 07's **layout vocabulary** (header wordmark, slim footer, section blocks,
join path cards) but was built for **scope**, not visual identity. The CSS still uses a cool,
product-default palette — blue links and buttons, gray muted text, white background, blue/purple join
lanes.

What colors should the first public site actually use?

## Source

Aug 2026 brand mockup: **datakollektivet** wordmark on cream (**Pacifico**), with three accent swatches below the
logo. The heart above the **i** is sage green; the wordmark text is a warm near-black brown.

## Palette (as read from the mockup)

| Swatch | Role | Hex (approx.) | Notes |
|---|---|---|---|
| Cream | Page background | `#F5F1E5` | Warm off-white; not pure `#fff` |
| Espresso brown | Primary text | TBD | Logo lettering; warmer than `#1f2430` |
| Sage / mint | Primary accent | `#8DC7A5` | Logo heart; largest accent swatch |
| Dusty peach | Secondary accent | `#E9A57D` | Middle swatch |
| Burnt orange / clay | Tertiary accent | `#D77E57` | Right swatch |

Overall feel: **warm, organic, approachable** — earth tones and soft green, not corporate blue.

## Current state

**Prototype 10** (`prototypes/10-first-version/static/css/site.css`) still uses generic blue tokens.

**Prototype 11** applies the brand palette — see
[plan](../plans/2026-08-21-prototype-11-site-design.md).

Prototype 10 CSS defines:

```css
:root {
  --text: #1f2430;
  --muted: #6b7280;
  --accent: #1a5fb4;
  --rule: #e5e7eb;
  --bg-code: #f3f4f6;
  /* … */
  --lane-member: #1e40af;
  --lane-member-bg: #eff6ff;
  --lane-volunteer: #7c3aed;
  --lane-volunteer-bg: #f5f3ff;
}
```

`body` has no explicit background — effectively white. Nothing references the brand cream or accent
triad. Join path cards use blue and purple lanes carried over from prototype 07.

## What we are not changing (yet)

- **Logo PNGs** in `static/img/` — already the wordmark on light background; likely fine on cream once
  `--bg` is set. Re-export only if contrast fails.
- **Page structure** — home sections, join hub, article layouts stay as in [first-version](../../10-first-version/overview.md).
- **Typography stack** — system sans-serif until a separate type decision says otherwise.

## Open questions

1. **Exact `--text` hex** — sample from logo artwork or pick a named brown (e.g. `#3D2E2A`) and
   validate contrast on `#F5F1E5`.
2. **Muted and rules** — derive from `--text` (opacity or mix) vs fixed grays that harmonise with cream.
3. **Link vs button accent** — single `--accent` (green) for both, or links in brown with green buttons?
4. **Join lane colors** — remap member/volunteer cards to peach/clay, or neutral cards with green
   CTAs only?
5. **Accent usage density** — green as rare highlight (heart, primary button) vs repeated section
   backgrounds (CTA block, cards).
6. **Code blocks** — slightly darker cream vs green-tinted gray for `pre` backgrounds on a cream page.

## Next step (when revising)

Update [token-mapping.md](./token-mapping.md) and the plan before further CSS changes in prototype 11.
