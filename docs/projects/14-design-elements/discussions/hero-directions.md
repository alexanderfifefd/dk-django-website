# Hero directions

**Date:** 2026-08-23 (updated 2026-08-27)  
**Status:** paused — wait before picking a final hero; dark background liked; stripe-lab directions on hold

## Question

What should the home hero feel like — without fighting logo, stripe, NT chrome, and the warm palette?

## Brand constraints

- **Anchors:** Pacifico wordmark, tri-band stripe, cream paper, anti–big-tech contract
- **Emerging chrome:** NT buttons, clickable card, `--bg-nt-tip` surfaces
- **Deprioritized:** Generic SaaS hero (purple CTAs, stock cosmos, growth funnel)
- **Merge goal:** Honest tools on a human desk — not costume, not scale cosplay

## Directions considered

### 1. Space-esque (Y42-style)

Black field, stars, luminous headline — infrastructure as cosmos.

| Pros | Cons |
|---|---|
| Reads “systems at scale” | Default B2B SaaS pattern — cold next to warm brand |
| Could bridge to dark mode (proto 12) | Pacifico + heart vs enterprise gravitas |
| Dramatic | Black hero → cream body needs careful handoff |

**Refined:** *Observatory* — charcoal not `#000`, cream stars, no purple CTAs, copy stays collective not “data must flow.” Stripe as transition band. Member-scale static stars, not WebGL.

### 2. Grid vaporwave

Perspective grid, navy/cyan, rainbow horizon, CRT optional — 80s cyberspace aesthetic.

| Pros | Cons |
|---|---|
| Retro thread (different era from NT) | Vaporwave is ironic/neon; brand is nice/warm |
| Distinct from big-tech minimal | Full vaporwave fights logo + stripe |
| Depth without SaaS polish | Three eras at once if combined with NT + Pacifico |

**Refined:** *Grid on cream* — tried on home; readable only at high contrast, still fought copy and brand. Set aside.

**Also refined:** *NT desktop wallpaper* — hero as monitor backdrop; header = title bar, stripe = accent. Unifies with `.panel-nt`.

### 3. Other directions

| Direction | Read |
|---|---|
| **Letterhead / notice board** | Extend current hero — lowest risk, most coherent |
| **Git / terminal** | “Documented in git” — honest, risk of too hacker |
| **Polaroid frame** | Photography metaphor explicit — ties stripe + cards |
| **Proto-12 bridge** | Dark hero, light body — night ops without SaaS layout |

## Ranking (prototype 14)

1. **Night sky hero** — dark invert + soft stars, band handoff into cream ← *active on home*
2. **Simple hero** — centered H1 + lead only
3. **Warm observatory** — enterprise-leaning; set aside

## Leaning (2026-08-27)

- **Dark hero background** — liked. Charcoal field reads warm-inverted, not SaaS cold; worth keeping in whatever lands.
- **Direction 1 (horizon)** — the old **60s coloured-stripes** approach: brand bands bent into converging geometry, Polaroid/retro print energy rather than NT or vaporwave.
- **Wait a tad** — don't promote a stripe-lab variant to home yet. Night sky stays live; let the dark + stripes ideas sit before merging or replacing.

## Active sketch: night sky (cutesy dark)

- **Where:** `home.html` — `.hero--night` in `site.css`
- **Palette:** proto-12 charcoal `#373430`, cream text, sage + peach stars (small, soft — not Y42)
- **Read:** inverted brand warmth, member-scale night — not enterprise cosmos
- **Handoff:** five horizontal bands at the hero foot (sage → sage-light → cream → peach → clay) bridge into the cream page body; full-bleed band, no margin under `.site-top` on home

## Hero stripe lab (design lab)

Parallel exploration on `/design-lab/` — `hero-stripe-lab.css` + partials `hero_lab_demo.html`, `hero_lab_svg_horizon.html`, `hero_lab_svg_wings.html`. Same charcoal field as home; tests how header stripe logic scales into the hero.

| Label | Variant | Idea |
|---|---|---|
| Baseline | `fade` | Soft gradient fade into cream — reference only; home now uses bands |
| Direction 0 | `flat` | Five brand bands horizontal, full bleed — header stripe logic enlarged |
| Direction 1 | `horizon` | **60s coloured stripes** — same palette, parallel bands converging at 45° from corners toward centre; retro print read |
| Direction 3 | `wings` | Upper/lower fan wings from both sides; dark centre open |

None promoted to home yet. Night sky remains the live hero. Direction 1 (60s stripes) and the dark field are the current lean — but **wait before committing**; no rush to merge lab variants into home.

## Implementation

**Home (night sky)**

- `public/templates/public/home.html` — `.hero--night` markup
- `static/css/site.css` — `.hero--night`, `.hero-night__stars`, `.hero-night__bands`

**Design lab (stripe variants)**

- `public/templates/public/design_lab.html` — Hero stripe lab section
- `public/templates/public/partials/hero_lab_demo.html` — reusable demo frame
- `public/templates/public/partials/hero_lab_svg_horizon.html` — Direction 1 SVG
- `public/templates/public/partials/hero_lab_svg_wings.html` — Direction 3 SVG
- `static/css/hero-stripe-lab.css` — lab-only styles (loaded via `extra_css` on design lab)

## Window card (not hero)

NT window chrome (**`.win-nt`**) liked as a **card variant** — see [clickable-card.md](./clickable-card.md).
Design lab only.

## Tried and set aside

- **Grid on cream** — lines crossed copy; cyberspace vs desk
- **Letterhead** — too constrained
- **NT window as hero** — good chrome, wrong slot
- **Y42 / enterprise space** — cold scale cosplay (see ranking in brainstorm below)

## Related

- [datakollektivet-brand.md](./datakollektivet-brand.md)
- [clickable-card.md](./clickable-card.md)
- [brand-palette](../../11-site-design/discussions/brand-palette.md)
