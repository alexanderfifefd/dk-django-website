# Discussion: stripe variants (design directions)

**Project:** `site-design`
**Date:** 2026-08-21
**Prototype:** `prototypes/11-site-design/`
**Status:** **warm triad chosen** (2026-08-21). Variant switcher removed from prototype 11; other
directions kept here as procedural record.

## The question

The warm triad (clay → peach → cream) is a **monochromatic** stripe — one hue family, like a sepia
Polaroid body. It reads retro but does not use the **sage green** from the wordmark heart. What other
directions fit a collective homepage that should feel warmer and more handmade than big-tech chrome?

Big-tech header dividers: 1px neutral gray, or a single flat brand-color bar. Fine for SaaS; cold for
a cooperative that already chose cream, script lettering, and a heart dot.

## What we have in the palette

| Token | Colour | Brand role |
|---|---|---|
| `--accent` | Sage / mint | Logo heart — identity anchor |
| `--accent-2` | Peach | Warm secondary |
| `--accent-3` | Clay / burnt orange | Warm tertiary, good for links |
| `--bg` / `--bg-code` | Cream | Page and block fills |

A stripe is a **small canvas** — 6–16px tall. Every band choice signals what the site leads with:
warmth only, green as signature, or full triad.

## Direction 1 — Warm triad (current default)

**Bands:** clay → peach → cream (equal weight)

Monochromatic sunset. Polaroid-adjacent without the rainbow. Safe, cohesive; the heart green stays
only in the logo and Join button unless you look elsewhere.

**Risk:** Orange-on-orange can blur together at 4px band height — reads as one salmon bar (see
reference screenshot).

## Direction 2 — Heart-led

**Bands:** clay → peach → sage (green at the bottom)

Warm accents first, **heart green anchors** the stripe where it meets the page — opposite of
full-palette. Not monochromatic; the green lands as a footer to the bar rather than a headline.

**Risk:** Green band at the bottom can read as a second divider; keep bands thin.

## Direction 3 — Single accent

**Bands:** one colour only (clay or sage), 6–8px

Maximum restraint. Closer to a **bookmark** or **underline** than camera chrome. Big-tech minimalism
but in warm pigment instead of `#e5e7eb`.

Try both **single-clay** (warm, matches links) and **single-sage** (heart echo, quieter page).

## Direction 4 — Sage pinstripe

**Bands:** cream → thin sage → cream

Green as a **needle** in warm paper — tailoring, not stadium stripe. Subtle identity without a colour
block. Works if the full heart-led bar feels loud.

## Direction 5 — Full palette

**Bands:** sage → peach → clay → cream (four equal bands, green at the top)

Every brand accent once, descending into page colour. Closest to “iconic lines” energy while staying
on-palette (no Polaroid magenta/cyan). Contrast with **heart-led**, which ends on green instead of
starting with it.

## Direction 6 — Weighted cream

**Bands:** thin clay, thin peach, **thick cream**

Mimics a Polaroid **body** proportion: colour cap, mostly material. Warm triad logic but the bar
mostly disappears into the page — ornament, not stripe.

## Direction 7 — Inverted emphasis (future)

Thick coloured block with thin cream gap — or stripe **above** header only on home. Not implemented
yet; note if we want page-specific chrome later.

## Recommendation for iteration order

1. **single-clay** — baseline; matches “one salmon line” reference
2. **heart-led** — green anchors at bottom (vs full-palette green on top)
3. **warm-triad** — current default; compare at equal vs weighted height
4. **sage-pin** — if heart-led is too much
5. **full-palette** — if you want maximum playfulness
6. **weighted-cream** — if bars feel loud
7. **single-sage** — quietest identity nod

Pick one, then tune band height in CSS — not new variants.

## Decision (2026-08-21)

**Header:** warm triad stripe — clay → peach → cream (`--accent-3`, `--accent-2`, `--bg-code`).

**Home dividers:** single peach rule (`--rule-peach`) — not tri-colour.

## Try in the browser (historical)

~~Append `?stripe=<key>`~~ — removed after decision. Keys below are reference only.

| Key | Direction |
|---|---|
| `warm-triad` | Default — clay, peach, cream (equal) |
| `single-clay` | One clay band |
| `single-sage` | One sage band |
| `heart-led` | Clay, peach, sage (green bottom) |
| `sage-pin` | Cream, sage, cream (thin centre) |
| `full-palette` | Sage, peach, clay, cream (green top) |
| `weighted-cream` | Thin clay, thin peach, thick cream |

Examples:

```
http://127.0.0.1:8000/?stripe=heart-led
http://127.0.0.1:8000/join/?stripe=single-sage
```

Invalid or missing param → `warm-triad`.

## Related

- [header-stripe.md](./header-stripe.md) — technical implementation (HTML partial vs gradient vs SVG)
