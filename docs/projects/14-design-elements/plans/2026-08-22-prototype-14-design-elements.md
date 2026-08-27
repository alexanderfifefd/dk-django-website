# Plan: prototype 14 — design elements

**Status:** paused 2026-08-27

## Goal

Sandbox on the first-version page set for components and brand/style — not a frozen design system.

## Done

- Fork from prototype 11
- Project docs under `docs/projects/14-design-elements/`
- **Design lab** page at `/design-lab/` — `public/design_lab.html`
- **Header nav** — `--text` links, first-letter underline on Articles/About, NT Join + pixel caret; (lab) in footer
- **Header stripe** — reordered cream → peach → clay (was clay-first)
- **Home transport** — All articles (heading), About us (tertiary + caret, right), clickable card join panel
- **Clickable card** — tip card (`.panel-nt`) on home + join paths; window card (`.win-nt`) in design lab — both liked; see [clickable-card.md](../discussions/clickable-card.md)
- **Home hero** — night sky (`.hero--night`): charcoal field, soft brand-colour stars, five-band stripe handoff into cream body
- **Hero stripe lab** — four variants on design lab (`hero-stripe-lab.css`, SVG horizon/wings partials); home keeps night sky until one lands

## Open

- Final hero direction — night sky vs stripe convergence (flat / horizon / wings) from design lab
- Typography, secondary NT vs prose-link semantics
- Promote anything to prototype 11 only when deliberately chosen

## Verify

From `prototypes/14-design-elements/`: `uv run python manage.py runserver`
