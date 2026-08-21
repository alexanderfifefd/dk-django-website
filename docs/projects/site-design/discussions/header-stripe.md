# Discussion: header stripe (Polaroid-style lines)

**Project:** `site-design`
**Date:** 2026-08-21
**Prototype:** `prototypes/11-site-design/`
**Status:** approach 3 chosen and implemented (best-effort)

## The question

Can a short band of horizontal colour lines below the site header give the warm, retro feel of
vintage Polaroid chrome — without clashing with the cream palette or adding JS/asset pipeline?

Reference: three equal warm stripes (burnt orange → peach → cream), mapped to existing tokens
(`--accent-3`, `--accent-2`, `--bg-code`).

## Approach 1 — CSS gradient on one element

Add a single empty `<div class="site-stripe">` and paint all bands with one
`linear-gradient(to bottom, …)` using palette variables.

**Pros:** Minimal HTML; one node; no partial file if inlined in `base.html`.

**Cons:** Gradient stop math is fiddly (equal thirds, sub-pixel gaps on some zoom levels); harder to
tune one band’s height independently; documenting which stop maps to which token is less obvious in
the template layer.

## Approach 2 — Static SVG (or PNG) asset

Export the three stripes as `static/img/header-stripe.svg` and `<img>` or CSS `background-image`
below the header. Colours baked into the file or set via SVG `fill` if inlined.

**Pros:** Pixel-match to a design export; designers can hand off the asset; zero layout logic in CSS.

**Cons:** Palette tweaks require re-exporting the asset; fights the token-driven CSS direction of
prototype 11; extra file to keep in sync with `--accent-*` changes.

## Approach 3 — HTML partial, one element per band

New `partials/stripe.html`: a decorative wrapper with three `<span>` children, each class-named to
a token colour. Full-bleed via `100vw` + centering trick so stripes span the viewport while header
content stays in the layout column. `aria-hidden="true"` — pure ornament.

**Pros:** Each stripe maps explicitly to a CSS variable; band height per child; no image file; easy
to reorder or add a fourth band later; readable in DevTools.

**Cons:** Three extra DOM nodes (negligible); slightly more markup than approach 1.

## Recommendation

**Approach 3** — token-linked partial with three bands. Prototype 11 is exploring palette application
in CSS; baking stripes into an asset (approach 2) would fork whenever colours move. A gradient
(approach 1) works but is harder to iterate when we want uneven band weights (Polaroid rainbows are
not always equal; our warm triad may want a thicker cream band later).

Implementation: include `stripe.html` from `base.html` immediately after the header; remove the header
`s border-bottom so the stripe is the chrome divider.

## Band mapping (implemented)

Default variant **warm-triad** — see [stripe-variants.md](../discussions/stripe-variants.md) for
design rationale and six other directions switchable via `?stripe=`.
