# CSS structure

Hand-written CSS, no build step. Load order matters and is fixed in `base.html`:

```
tokens.css      → variables only (palette, semantic, scales, hero-inv, stripe)
base.css        → reset, body, typography, links
layout.css      → sticky header, stripe, nav, footer, content sections
components.css  → btn, card, panel, form-card, caret, form fields, notice
pages.css       → heroes, articles, join
catalog.css     → /design-lab/ only, via {% block extra_css %}
```

## Where do I put X?

| Styling… | File |
|---|---|
| A colour, scale step, semantic alias | `tokens.css` |
| `body`, `a`, headings | `base.css` |
| Header, stripe, footer shell, prose `.content-section` | `layout.css` |
| Reusable UI (BEM block) | `components.css` |
| One page or route group | `pages.css` |
| Catalog page scaffolding | `catalog.css` |

## Rules

- **No hex outside `tokens.css`** — always `var(...)`; derive shades with `color-mix`.
- **No selectors in `tokens.css`** — variables only.
- **Components use semantic tokens** (`--surface-*`, `--action-*`, `--text-*`), never palette directly where a semantic role exists.
- **New component**: BEM block in `components.css` (`block`, `block__element`, `block--modifier`), then add it to the catalog page.
- **Bevel pattern**: set `--bevel-face`, derive `--bevel-hi`/`--bevel-lo` with `color-mix`; raised = light top/left, sunken = dark top/left; hover inverts.

Reasoning and decisions: `docs/projects/15-css-structure/`.
