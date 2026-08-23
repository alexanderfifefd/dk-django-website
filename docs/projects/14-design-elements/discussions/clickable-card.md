# Clickable card

**Status:** liked on prototype 14 (2026-08-23)

**What it is:** A whole-surface link dressed as a card — first use: home “Want to participate?”
(`join_panel_nt.html`, `.panel-nt`). Warm `--bg-nt-tip` face, NT inset bevel (inverts on hover),
pixel icon on sage tile, heading + copy, underlined label + caret bottom-right.

**Feeling:** Half Windows NT tip box, half modern UI card — retro chrome without costume. The bevel
and icon say “this is a control”; the warm paper face and typography say “human site, not enterprise
software.” One clickable surface instead of a card plus a button — informational and actionable
together. Invitation, not funnel.

The NT parts are functional (depth, affordance); the rest is contemporary layout and brand colour.

**Not:** A marketing hero block, a form panel, or pure nostalgia.

**Ripple:** `--bg-nt-tip` also used for header and tertiary buttons — the card established a shared
warm surface.

## Implementation

- `public/templates/public/partials/clickable_card.html` — reusable card (no icon)
- `public/templates/public/partials/join_panel_nt.html` — home variant with icon
- `public/templates/public/join/index.html` — three path cards
- `static/css/btn-nt.css` — `.panel-nt`, `.panel-nt__*`
- Design lab: Panel CTA section

## Related

- [transport-buttons.md](./transport-buttons.md) — NT button tiers
- [datakollektivet-brand.md](./datakollektivet-brand.md) — NT vs warm brand tensions
- [header-nav.md](./header-nav.md) — header uses same `--bg-nt-tip` surface
