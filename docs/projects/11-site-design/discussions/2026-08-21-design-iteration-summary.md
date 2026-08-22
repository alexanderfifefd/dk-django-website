# Design iteration summary — prototype 11

**Project:** `site-design`
**Date:** 2026-08-21
**Prototype:** `prototypes/11-site-design/`
**Status:** first design pass complete; prototype 10 unchanged

## What this document is

A record of the first visual-design session on prototype 11: what we tried, what we kept, and where
the important files live. Prototype 10 remains the scope baseline (generic blue CSS). All design work
happens in prototype 11.

## Starting point

Prototype 10 shipped home, articles, about, and join with prototype 07's **cool blue tokens**
(`--accent: #1a5fb4`, white/grey chrome). The Aug 2026 brand mockup defines a **warm palette**
(cream, espresso brown, sage heart, peach, clay) that prototype 11 applies.

## Decisions kept

### Brand palette (site-wide)

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#F5F1E5` | Page background |
| `--text` | `#3D2E2A` | Body and headings |
| `--accent` | `#8DC7A5` | Sage — buttons, form focus |
| `--accent-2` | `#E9A57D` | Peach |
| `--accent-3` | `#D77E57` | Clay — links |
| `--rule-peach` | mixed from peach + `--rule` | Home section dividers |
| `--bg-code` | `#EDE8D8` | Blocks, join CTA fill |

Links use clay (`--accent-3`); primary buttons use sage with dark text (not white-on-green).

### Header chrome

- **Sticky** `.site-top` — header + stripe stay pinned on scroll
- **Compact header** — reduced padding, smaller logo (`1.25rem`), nav at `0.95rem`
- **Join button** — green pill restored, smaller than default `.btn`
- **Warm triad stripe** — full-bleed bar under nav: clay → peach → cream (`partials/stripe.html`)
- Header, main, and footer share one column width (`--content-width: 44rem`)

See [stripe-variants.md](./stripe-variants.md) for alternatives we explored and rejected.

### Home page

- **Centered hero** — H1 + lead line; divider below is a single peach rule (not tri-colour)
- **Hero spacing** (2026-08-21, also on prototype 12) — `.page-hero` / `.hero`:
  `padding-top: 1.25rem`, `margin-bottom: 3rem`, divider `margin-top: 2.25rem`; `.hero-lead`
  gap `1.15rem`
- **Section rules** — peach-tinted lines between “What we do”, “Who we are”, and “Latest articles”
- **No rule** below the last article or around the join CTA (removed double lines)
- **Join CTA box** — grey `--bg-code` background with a **warm triad cap** (3px gradient top edge);
  no border, no shadow, no peach fill (tried and rejected)

### Join hub (`/join/`)

- **Three columns** on viewports ≥ 900px; single column on mobile
- Join page main widens to `54rem` on desktop so cards breathe
- Path cards keep peach (member) and clay (volunteer) lane tints from the palette

## What we tried and dropped

| Experiment | Outcome |
|---|---|
| Palette on prototype 10 | Moved to prototype 11 fork instead |
| Seven stripe variants (`?stripe=`) | Warm triad chosen for header; switcher removed |
| Full tri-colour rules on home body | Too busy — single peach rule instead |
| Peach / embossed / shadow CTA backgrounds | Looked off — back to flat grey + triad cap |
| Join as text link in nav | Reverted — compact green button preferred |
| Wider header/footer column (`76rem`) | Aligned everything to `44rem` |

## Files that changed

| Path | What |
|---|---|
| `static/css/site.css` | Tokens, layout, header, home, join, footer |
| `public/templates/public/layouts/base.html` | Sticky top, stripe include, `body_class` block |
| `public/templates/public/partials/stripe.html` | Warm triad bands |
| `public/templates/public/partials/header.html` | Compact nav + Join button |
| `public/templates/public/home.html` | Hero lead, `page-home` body class |
| `public/templates/public/join/index.html` | `page-join` body class |

## Prototype mapping

Same routes as prototype 10. Run from `prototypes/11-site-design/`:

```bash
uv run python manage.py runserver
```

Compare with `prototypes/10-first-version/` side by side.

## Open follow-ups

- Hero and home copy may still need editorial polish
- Exact `--text` hex could be sampled from logo artwork
- Typography (font choice) not explored — still system sans-serif
- Apply header/home patterns to about and article pages if they feel disjoint
- Promote stable decisions back into prototype 10 when v1 design is frozen

## Related docs

- [brand-palette.md](./brand-palette.md) — palette source
- [stripe-variants.md](./stripe-variants.md) — stripe exploration and final split (triad header / peach rules)
- [header-stripe.md](./header-stripe.md) — why HTML partial vs gradient vs SVG
- [2026-08-21-prototype-11-site-design.md](../plans/2026-08-21-prototype-11-site-design.md) — original build plan
