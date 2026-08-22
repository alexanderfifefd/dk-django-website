# Dark mode

**Question:** How should the first public site look on a dark background — using the brand accent triad?

**Status:** first pass on prototype 12 (2026-08-21).

**Prototype:** `prototypes/12-dark-mode/` — fork of prototype 11; CSS tokens only.

**Builds on:** [site-design](../11-site-design/overview.md) (light palette and chrome decisions on prototype 11).

## Scope

Prototype 11 applies the warm **light** brand mockup (cream background, espresso text). **Prototype 12**
is the dark counterpart: same routes, templates, and content — charcoal background, cream text, same
accent split as prototype 11.

| In scope (for now) | Out of scope (for now) |
|---|---|
| CSS custom properties (tokens) | `prefers-color-scheme` toggle or runtime theme switch |
| Derived muted, rules, code blocks, join lanes | Light-theme logo PNGs (unused; dark assets referenced) |
| Header stripe and footer bar remapped for dark | Systems, initiatives, or collections not in v1 |
| Join path card tints on dark surfaces | Deployment or a full design system |

Implementation lives in `prototypes/12-dark-mode/static/css/site.css`.

## Palette

Five colors from the Aug 2026 **dark** brand mockup (cream wordmark on charcoal + three swatches):

| Token | Role | Hex |
|---|---|---|
| `--bg` | Page background — warm charcoal | `#373430` |
| `--text` | Body and headings — cream | `#EEE6D4` |
| `--accent` | Primary accent — sage / mint (logo heart) | `#79C39D` |
| `--accent-2` | Secondary — lighter orange | `#EE9B69` |
| `--accent-3` | Tertiary — higher-contrast orange (links) | `#E77843` |

Muted text, rules, code blocks, and join lane fills are derived — see the plan.

## Accent split (same as prototype 11)

- **Links** → `--accent-3` (terracotta); hover → `--text`
- **Primary buttons** → `--accent` (mint) with `--text` label; hover → `--accent-hover`
- **Join path cards** → account neutral; member peach tint; volunteer terracotta tint

## Chrome on dark

- **Header stripe** — terracotta → peach → lifted charcoal (`--bg-code`)
- **Header nav** — full cream text; hover lighter orange
- **Footer bar** — terracotta → peach → mint (mockup swatch order)
- **Join CTA panel** — `--bg-code` (slightly lifted charcoal), no cream fill
- **Hero spacing** — extra padding above title and before divider (shared with prototype 11)

## Docs

1. **[dark-palette.md](./discussions/dark-palette.md)** — palette source, rationale, and decisions
2. **[2026-08-21-prototype-12-dark-mode.md](./plans/2026-08-21-prototype-12-dark-mode.md)** — build plan

## Related

- `prototypes/11-site-design/` — light palette baseline (unchanged)
- `prototypes/12-dark-mode/static/css/site.css` — dark stylesheet
