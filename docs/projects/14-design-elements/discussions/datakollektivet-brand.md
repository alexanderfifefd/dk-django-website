# Datakollektivet brand — tensions and fit

**Project:** `design-elements`  
**Date:** 2026-08-22 (updated 2026-08-27)  
**Status:** paused — logo and stripe are anchors; NT chrome and night-sky hero settling in sandbox

## What is established

**Logo (wordmark PNG).** Lowercase *datakollektivet* set in **[Pacifico](https://fonts.google.com/specimen/Pacifico)**
(handwritten script; sage **heart** over the *i* in the artwork). Shipped as PNG in `static/img/` — not
loaded as a web font on page chrome. Tone: **cutesy, nice, not mean** — approachable, human,
anti-corporate coldness. This is the emotional center of the brand; changing it is not on the table for
prototype 14.

**Stripe under the header.** Warm triad bands (cream → peach → clay on prototype 14; was clay-first) — documented in
[site-design](../../11-site-design/discussions/stripe-variants.md) and
[header-stripe.md](../../11-site-design/discussions/header-stripe.md). Reads **retro, almost
Polaroid-like**: a major design element, full-bleed, sticky with the header. **Really strong** — one
of the clearest “this isn’t a SaaS template” signals on the page.

**Palette.** Cream paper, espresso text, sage + peach + clay accents — warm and slightly **retro** in
evocation (analog warmth, not skeuomorphic UI for its own sake). See
[brand-palette](../../11-site-design/discussions/brand-palette.md).

Everything else — buttons, transport, hero treatment beyond the band handoff, typography beyond system sans — is **exploration**, with several patterns now **liked in the sandbox** (not yet promoted).

## Windows NT thread

The **NT-style button** prototype ([`btn-nt.css`](../../../prototypes/14-design-elements/static/css/btn-nt.css))
is deliberately **functionality over form** in a 2000s PC sense:

- Square corners, inset bevel (light top/left, dark bottom/right)
- Solid fills, no rounded “app store” softness
- Honest about being a **control**, not decoration

That sits in **tension** with the logo’s softness and the stripe’s handmade warmth.

| NT / utilitarian | Logo / warm |
|---|---|
| Hard edges, bevel chrome | Pacifico wordmark, heart |
| “Click the button” clarity | “We’re people, not a funnel” |
| Desktop metaphor | Cooperative, git-owned, small |

**Compatible when:** NT bevel reads as **honest chrome** — nav Join (primary), section transport
(tertiary **All articles**, secondary **About us**), join panel CTA — not megacorp dashboard or
marketing fluff replacing Pacifico. Nav **text links** stay plain `--text` with a quiet first-letter
underline; see [header-nav.md](./header-nav.md).

**In tension when:** NT chrome gets loud enough to feel like **Big Tech enterprise software** (gray
boxes, dominance, extraction) rather than **tools members actually run**.

## What takes precedence

1. **The contract** — what we refuse to be (see below). No dark patterns, no growth-at-all-costs
   chrome, no “platform” voice.
2. **Logo + stripe** — identity and wayfinding; they set warmth and retro honesty.
3. **Readable controls** — NT-inspired buttons can serve (2) if they stay **member-scale**, not
   megacorp dashboard.
4. **Generic SaaS polish** — explicitly deprioritized (rounded everything, purple gradients, hero
   stock vibes).

## The real opposition (what we do not want to be)

Datakollektivet exists in opposition to **big tech** as default infrastructure for daily life:

- Surveillance and lock-in dressed as convenience
- Extraction (attention, data, rent) over stewardship
- Opaque “trust us” instead of git-owned, documented systems
- Scale cosplay — looking enterprise while serving nobody in particular

**The brand promise in contrast:** collectively owned, documented in git, democratically governed —
**nicer services to people** because members build and operate for users, not shareholders.

Design should feel **human and retro-warm** (logo, stripe, cream) while **controls stay legible**
(NT buttons, clear transport). The merge is not “cute site with brutal buttons” — it is **honest
tools on a human desk**: Polaroid stripe on the wall, NT button on the form.

## Open design questions

- **Hero** — night sky on home; stripe convergence variants in design lab — see [hero-directions.md](./hero-directions.md)
- Does terracotta **secondary** NT pair with link semantics or confuse it with prose links?
- Dark mode (prototype 12): does NT chrome invert cleanly or read as Windows 95 cosplay?
- Promote header nav + NT + clickable card + hero to prototype 11, or keep sandbox-only

## Related

- [header-nav.md](./header-nav.md) — nav text colour, first-letter underline, lab in footer
- [transport-buttons.md](./transport-buttons.md) — NT tiers, home transport map, panel CTA
- [clickable-card.md](./clickable-card.md) — tip + window card variants
- [hero-directions.md](./hero-directions.md) — night sky hero, stripe lab
- [brand-style-framework.md](./brand-style-framework.md) — doc index
- [site-design iteration summary](../../11-site-design/discussions/2026-08-21-design-iteration-summary.md) — stripe + sticky chrome on prototype 11
