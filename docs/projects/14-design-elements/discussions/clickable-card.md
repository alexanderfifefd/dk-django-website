# Clickable card

**Status:** liked on prototype 14 (updated 2026-08-27)

**What it is:** A whole-surface link dressed as a card. Two NT chrome variants share copy/layout
patterns (`panel-nt__*` inside).

**Feeling:** Half Windows NT tip box, half modern UI card — retro chrome without costume. The bevel
and icon say “this is a control”; the warm paper face and typography say “human site, not enterprise
software.” One clickable surface instead of a card plus a button — informational and actionable
together. Invitation, not funnel.

The NT parts are functional (depth, affordance); the rest is contemporary layout and brand colour.

**Not:** A marketing hero block, a form panel, or pure nostalgia.

**Ripple:** `--bg-nt-tip` also used for header and tertiary buttons — the card established a shared
warm surface.

## Variants

| Variant | Classes | Chrome | Status |
|---|---|---|---|
| **Tip card** | `.clickable-card.panel-nt` | Single inset face; optional icon tile | On home join CTA (`join_panel_nt.html`) |
| **Window card** | `.win-nt` | Raised frame, sage title bar, sunken client; button inside | Liked — design lab; not hero |

Both use `--bg-nt-tip` client face. Tip card is a whole-surface link; window card is static chrome
with an NT button for the action.

## Implementation

- `public/templates/public/partials/clickable_card.html` — tip-style card (no icon), join paths
- `public/templates/public/partials/join_panel_nt.html` — tip card with icon (home)
- `public/templates/public/partials/window_card_nt.html` — window card (design lab)
- `public/templates/public/join/index.html` — three tip-style path cards
- `static/css/btn-nt.css` — `.panel-nt`, `.win-nt`, shared `.panel-nt__*`
- Design lab: Panel CTA + Window card sections

## Related

- [hero-directions.md](./hero-directions.md) — window chrome tried as hero, set aside
- [transport-buttons.md](./transport-buttons.md) — NT button tiers
- [datakollektivet-brand.md](./datakollektivet-brand.md) — NT vs warm brand tensions
- [header-nav.md](./header-nav.md) — header uses same `--bg-nt-tip` surface
