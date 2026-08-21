# Discussion: mapping palette tokens to surfaces

**Project:** `site-design`
**Date:** 2026-08-21
**Depends on:** [brand-palette.md](./brand-palette.md)
**Status:** options listed — no decision yet

## The question

Given the five brand colors (cream background, brown text, green / peach / clay accents), **which CSS
custom properties and UI surfaces get which color?** Prototype 10 already has named surfaces; we need
a mapping before touching `site.css`.

## Surfaces in prototype 10 today

| Surface | CSS today | Template / context |
|---|---|---|
| Page background | implicit white | `body` |
| Body text | `--text` | everywhere |
| Muted copy | `--muted` | leads, bylines, form hints |
| Links | `--accent` (blue) | inline `<a>`, section links |
| Primary button | `--accent` background | Join CTA, `.btn-primary` |
| Nav links | `--muted`, hover `--accent` | header |
| Rules / borders | `--rule` | header/footer border, lists, forms |
| Code / notice blocks | `--bg-code` | `pre`, `.join-cta`, `.join-notice` |
| Join CTA section | `--bg-code` fill | home bottom block |
| Member path card | `--lane-member-bg`, blue border | `/join/` |
| Volunteer path card | `--lane-volunteer-bg`, purple border | `/join/` |
| Form focus ring | `--accent` outline | join forms |

## Option A — green-led (minimal change)

Keep the same **roles**, swap hex values only:

- `--bg: #F5F1E5` on `body`
- `--text` → espresso brown; `--muted` → brown at ~60% opacity or a mixed gray-brown
- `--accent` → `#8DC7A5`; darker green for button hover
- `--rule` → warm gray derived from cream + brown
- `--bg-code` → slightly darker cream (`#EDE8D8` or similar)
- Join lanes → peach and clay backgrounds with matching borders (`--accent-2`, `--accent-3`)

**Pros:** Smallest diff; every template keeps working. **Cons:** Green links on cream can feel soft;
low contrast if green is used for body links at full saturation.

## Option B — brown links, green actions

Separate **navigation / reading** from **conversion**:

- Links and nav hover → `--text` or a brown underline; not green
- Buttons and Join nav pill → `--accent` (green) with dark green hover
- Section accents (CTA background, optional left border) → `--accent-2` (peach) or `--accent-3` (clay)
- Join path cards → neutral cream/white cards; color only on the path title or arrow

**Pros:** Clear hierarchy; green reads as "do something". **Cons:** More token names (`--link`,
`--action`); slightly more CSS churn.

## Option C — accent triad on join only

Use green globally for primary actions; reserve peach and clay **only** for the three join paths
(account = neutral, member = peach, volunteer = clay) instead of blue/purple lanes.

**Pros:** Join hub feels branded without coloring the whole site. **Cons:** Account path stays plain;
need a third neutral or repeat green.

## Derived tokens (all options)

These are not in the mockup; propose deriving them consistently:

| Token | Purpose | Suggested approach |
|---|---|---|
| `--muted` | secondary text | `color-mix(in srgb, var(--text) 55%, var(--bg))` or fixed warm gray |
| `--rule` | borders | `color-mix(in srgb, var(--text) 12%, var(--bg))` |
| `--bg-code` | blocks, `pre` | darken `--bg` ~5–8% |
| `--accent-hover` | buttons | darken `--accent` ~12% |

Document chosen formulas in the implementation plan so hover/focus states stay consistent.

## Non-goals for v1 mapping

- Dark mode or `prefers-color-scheme`
- Semantic colors beyond brand (success/error on forms stay generic or unstyled)
- Per-page one-off colors outside tokens

## Decision needed before implementation

Until revised, prototype 11 uses the mapping in
[2026-08-21-prototype-11-site-design.md](../plans/2026-08-21-prototype-11-site-design.md). Prototype 10
keeps prototype 07 blues.
