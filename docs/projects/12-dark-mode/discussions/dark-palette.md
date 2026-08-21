# Discussion: dark mode palette

**Project:** `dark-mode`
**Date:** 2026-08-21
**Prototype:** `prototypes/12-dark-mode/`
**Builds on:** [site-design](../../11-site-design/overview.md) — prototype 11 unchanged
**Status:** palette captured; first pass applied in CSS

## The question

Prototype 11 validates the warm **light** brand mockup on the first-version page set. The same brand
also has a **dark** mockup: cream wordmark on charcoal, with mint, peach, and terracotta swatches below.

How should the v1 site look when the background is dark?

## Source

Aug 2026 dark brand mockup: **datakollektivet** wordmark in cream on warm charcoal, heart in mint green,
three accent swatches (mint widest, then peach, then terracotta).

## Palette (as read from the mockup)

| Swatch | Role | Hex (approx.) | Notes |
|---|---|---|---|
| Warm charcoal | Page background | `#373430` | Authoritative brand value |
| Cream | Primary text | `#EEE6D4` | Logo lettering |
| Sage / mint | Primary accent | `#79C39D` | Heart; buttons |
| Peach | Secondary accent | `#EE9B69` | Lighter orange; middle stripe |
| Terracotta | Tertiary accent | `#E77843` | Higher contrast orange; links |

Overall feel: same warm, organic identity as the light mockup — inverted luminance, accents slightly
brighter than their light-mode counterparts for contrast on charcoal.

## Decisions

### Same accent split as prototype 11

- Links and inline emphasis → `--accent-3` (terracotta)
- Primary buttons and form focus → `--accent` (mint)
- Join member / volunteer lanes → peach and terracotta tints on dark surfaces

### Logo assets

Dark-theme PNGs in `static/img/` (`logo-dark-theme.png`, `logo-dark-theme-small.png`); header and
footer reference those paths.

### Header stripe and footer bar

Light mode ends the tri-band with a **cream** band (`--bg-code`). On dark, the third band is a
**lifted charcoal** (`--bg-code`) — neutral, not mint.

### Derived tokens

| Token | Approach |
|---|---|
| `--muted` | `color-mix(in srgb, var(--text) 76%, var(--bg))` |
| `--rule` | `color-mix(in srgb, var(--text) 12%, var(--bg))` |
| `--bg-code` | `color-mix(in srgb, var(--text) 8%, var(--bg))` — lifted charcoal for panels and third stripe |
| `--accent-hover` | `color-mix(in srgb, var(--accent) 82%, var(--bg))` |
| `--lane-member-bg` | `color-mix(in srgb, var(--accent-2) 14%, var(--bg))` |
| `--lane-volunteer-bg` | `color-mix(in srgb, var(--accent-3) 14%, var(--bg))` |

## What we are not changing (yet)

- **Page structure** — same as prototype 11 / 10
- **Typography stack** — system sans-serif
- **Theme switching** — one fixed dark palette; no `prefers-color-scheme` branch
- Dark-theme logo PNGs in `static/img/`; light-theme copies remain but are unused

## Open questions

1. **Contrast audit** — terracotta links and mint buttons on `#2B2826`; adjust if any pair fails WCAG targets we care about.
2. **Side-by-side with light** — compare prototype 11 and 12 on the same pages before promoting either.
