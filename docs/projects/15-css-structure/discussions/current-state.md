# Current CSS state (fork baseline — prototype 14)

**Date:** 2026-08-27  
**Source:** `prototypes/15-css-structure/static/css/` — copied unchanged from prototype 14 at fork time.

## Files

| File | Lines (approx) | Loaded | Role |
|---|---:|---|---|
| `site.css` | ~793 | Every page via `base.html` | Tokens, base, header, stripe, nav, hero, home sections, articles, join, footer, design-lab section styles |
| `btn-nt.css` | ~218 | Every page via `base.html` | NT buttons, `.panel-nt` tip card, `.win-nt` window card, pixel caret |
| `hero-stripe-lab.css` | ~166 | Design lab only (`extra_css`) | Hero stripe lab variants on `/design-lab/` |

**Total:** ~1,177 lines across 3 files.

## Load order (`base.html`)

```html
<link rel="stylesheet" href="{% static 'css/site.css' %}">
<link rel="stylesheet" href="{% static 'css/btn-nt.css' %}">
{% block extra_css %}{% endblock %}
```

Design lab adds `hero-stripe-lab.css` in `extra_css`. Home hero (night sky) lives in `site.css` even though hero *experiments* are lab-only — a coupling worth revisiting.

## `site.css` sections (comment markers)

1. `:root` tokens + universal box-sizing
2. Body, links, headings, `.lead`
3. Header — sticky `.site-top`, stripe bands, nav, first-letter underline, footer lab link
4. Buttons (non-NT legacy?)
5. Page titles / generic `.hero`
6. Hero — night sky (`.hero--night`, stars, bands) — **home only in practice**
7. Home sections, transport footer
8. Article lists + detail
9. Join pages
10. Footer
11. Design lab page layout (`.design-lab-*`) — **only used on `/design-lab/` but in global file**

## Token usage

`:root` holds brand palette and layout vars (`--content-width`, `--gutter`, join lane colours). Some hero/lab colours are **hard-coded** (`#373430`, `#eee6d4`) — same values as prototype 12 dark palette but not shared via token.

NT chrome derives bevel colours from `--nt-face` / `--tip-face` via `color-mix` in `btn-nt.css` — good pattern to preserve.

## Footguns spotted

- **Global file carries page-specific weight** — hero-night and design-lab rules ship to every page
- **Two hero systems** — night sky in `site.css`, stripe lab in separate file with overlapping palette vars
- **No documented section index** — navigable by comments only
- **Class naming** — mix of BEM-ish (`.panel-nt__heading`), utility-ish (`.home-section--transport-footer`), and element classes (`.site-nav`)
- **Cascade surprises** — sticky header + full-bleed stripe/hero use `100vw` + negative margin pattern repeated

## What not to break on first refactor

Visual output should match prototype 14 until we explicitly change design:

- Header nav, stripe order (cream → peach → clay)
- NT buttons + clickable card on home
- Night sky hero + band handoff
- Design lab showcase (all sections)

Compare side-by-side with prototype 14 after structural moves.

---

## Final state (refactor landed 2026-08-27 — see [file-layout.md](./file-layout.md))

| File | Lines | Role |
|---|---:|---|
| `tokens.css` | 72 | Palette + semantic + scales + hero-inv + stripe constant (variables only; only file with hex) |
| `base.css` | 43 | Reset, body, type, links |
| `layout.css` | 165 | Sticky header, stripe (top + bottom), nav, footer |
| `components.css` | 311 | `btn`, `card`, `panel`, caret, form fields, `notice` — all bevel via `--bevel-face` pattern |
| `pages.css` | 324 | Heroes (incl. `hero--inverted`), home sections, articles, join |
| `catalog.css` | 122 | `/design-lab/` only, via `extra_css` |

**Total:** 1,037 lines across 6 files (was ~1,177 across 3), plus `static/css/README.md` with load order and placement rules.

**Removed:** `site.css`, `btn-nt.css`, `hero-stripe-lab.css`, hero lab partials, legacy rounded `.btn`, the `::first-letter` nav hack (mark is an HTML `<span>` now).
