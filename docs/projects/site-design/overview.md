# Site design

**Question:** How should the first public site look and feel — starting with the brand color palette?

**Status:** first design pass on prototype 11 (2026-08-21) — see iteration summary.

**Prototype:** `prototypes/11-site-design/` — fork of prototype 10; CSS tokens only.

**Builds on:** [first-version](../first-version/overview.md) (page set and slim chrome),
[site-ui](../site-ui/overview.md) (hand-written CSS conventions from prototypes 06/07).

## Scope

Prototype 10 keeps prototype 07's generic blue tokens while the v1 **structure** stabilises.
**Prototype 11** is the design sandbox: same routes and templates, warm brand palette in CSS.

| In scope (for now) | Out of scope (for now) |
|---|---|
| CSS custom properties (tokens) | JavaScript, HTMX, or a CSS preprocessor |
| Background, text, link, button, accent surfaces | Logo redraw or new static assets (unless palette forces it) |
| Join path card colors (member / volunteer lanes) | Systems, initiatives, or other collections not in v1 |
| Spacing, type, or chrome tweaks driven by the palette | Deployment, dark mode, or a full design system |

Implementation lives in `prototypes/11-site-design/static/css/site.css`.

## Palette

Five colors from the Aug 2026 brand mockup (wordmark + swatches):

| Token | Role | Hex |
|---|---|---|
| `--bg` | Page background — warm cream | `#F5F1E5` |
| `--text` | Body and headings — espresso brown | `#3D2E2A` |
| `--accent` | Primary accent — sage / mint (logo heart) | `#8DC7A5` |
| `--accent-2` | Secondary — dusty peach | `#E9A57D` |
| `--accent-3` | Tertiary — burnt orange / clay | `#D77E57` |

Muted text, rules, and code blocks are derived — see the plan for values.

## Docs

1. **[2026-08-21-design-iteration-summary.md](./discussions/2026-08-21-design-iteration-summary.md)** — **what we changed** (start here after the plan)
2. **[brand-palette.md](./discussions/brand-palette.md)** — palette source and rationale
3. **[token-mapping.md](./discussions/token-mapping.md)** — surface mapping options (reference)
4. **[header-stripe.md](./discussions/header-stripe.md)** — technical approach (HTML partial)
5. **[stripe-variants.md](./discussions/stripe-variants.md)** — stripe exploration and decisions
6. **[2026-08-21-prototype-11-site-design.md](./plans/2026-08-21-prototype-11-site-design.md)** — original build plan

## Related

- `prototypes/10-first-version/` — scope baseline (unchanged palette)
- `prototypes/11-site-design/static/css/site.css` — branded stylesheet
- `prototypes/11-site-design/static/img/` — wordmark assets (shared from fork)
