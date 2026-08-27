# File layout — layer split

**Date:** 2026-08-27 (updated after review)  
**Status:** implemented — tree, load order, and deletions all landed as specified

## Decision

Five global layers plus one catalog-only file. Load order is fixed and documented in a comment in `base.html` and in `static/css/README.md`.

## Target tree

```
static/css/
  README.md         ← load order + “where do I put X?” (one screenful)
  tokens.css        ← :root variables only — see tokens-and-palette.md
  base.css          ← reset, body, typography, links, headings
  layout.css        ← site-top, header, stripe, nav, footer, main column
  components.css    ← btn, card, panel, caret (bevel components)
  pages.css         ← home hero (inverted), home sections, articles, join, about
  catalog.css       ← /design-lab/ (component catalog) only — via {% block extra_css %}
```

### Deleted at refactor

| File | Reason |
|---|---|
| `site.css` | Split into layers above |
| `btn-nt.css` | Merged into `components.css` under generic names ([class-naming.md](./class-naming.md)) |
| `hero-stripe-lab.css` | Hero experiments stay in prototype 14 |
| `hero_lab_demo.html`, `hero_lab_svg_horizon.html`, `hero_lab_svg_wings.html` | With the above |

### Renamed partials (de-NT pass)

`join_panel_nt.html` → `card_join.html` · `clickable_card.html` → `card.html` · `window_card_nt.html` → `panel.html` · `panel_nt_caret.html` → `caret.html` (also replaces the inline caret SVG copies in header/home).

## Load order

```html
<!-- base.html — order matters: tokens → base → layout → components → pages -->
<link rel="stylesheet" href="{% static 'css/tokens.css' %}">
<link rel="stylesheet" href="{% static 'css/base.css' %}">
<link rel="stylesheet" href="{% static 'css/layout.css' %}">
<link rel="stylesheet" href="{% static 'css/components.css' %}">
<link rel="stylesheet" href="{% static 'css/pages.css' %}">
{% block extra_css %}{% endblock %}
```

Catalog template:

```html
{% block extra_css %}
  <link rel="stylesheet" href="{% static 'css/catalog.css' %}">
{% endblock %}
```

No other page-specific stylesheets expected. The home hero lives in `pages.css` scoped by `.hero--inverted` / `.page-home` — selector scoping, not per-route files.

## What goes where

| If you are styling… | File |
|---|---|
| A colour, scale step, semantic alias | `tokens.css` |
| `body`, `a`, headings, `.lead` | `base.css` |
| Header, stripe, sticky chrome, footer shell | `layout.css` |
| Reusable UI: `btn`, `card`, `panel`, caret | `components.css` |
| One page or route group: hero, join lanes, article list | `pages.css` |
| Catalog page scaffolding (`catalog-*`) | `catalog.css` |

**Footgun rules:**

- No hex outside `tokens.css` — only `var(...)`
- No selectors in `tokens.css` — variables only
- No page-specific rules in `components.css`; no component internals in `catalog.css`
- `catalog.css` never loaded globally

## `static/css/README.md` (stub)

1. Load order (list above)
2. "Where do I put X?" table (above)
3. "New component" → `components.css`, BEM block, semantic tokens only
4. Pointer to `docs/projects/15-css-structure/` for reasoning

## Actual sizes after refactor

| File | Lines (estimate) |
|---|---:|
| `tokens.css` | 72 (est. 80–100) |
| `base.css` | 43 (est. 40–50) |
| `layout.css` | 165 (est. 120–150) |
| `components.css` | 311 (est. 220–250 — forms + notice moved in as components) |
| `pages.css` | 324 (est. 320–380) |
| `catalog.css` | 122 (est. 60–90 — foundations swatch/scale demos) |
| **Total** | **1,037** (was ~1,177 in 3 files) — lab experiments and legacy `.btn` deleted |

## Related

- [tokens-and-palette.md](./tokens-and-palette.md)
- [class-naming.md](./class-naming.md)
- [catalog-scope.md](./catalog-scope.md)
