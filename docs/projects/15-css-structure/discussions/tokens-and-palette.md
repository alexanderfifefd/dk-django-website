# Tokens and palette

**Date:** 2026-08-27  
**Status:** implemented — this is now the live `tokens.css` (deviations from the original proposal noted inline)

## Question

How do we name and layer colour tokens so a non-expert can edit the palette safely, components derive consistently (bevels, surfaces), and no magic hex hides in page CSS?

## Principle: two layers

| Layer | Question it answers | Example | Who edits it |
|---|---|---|---|
| **Palette** | What are our brand inks? | `--color-sage: #8dc7a5` | Brand / design pass |
| **Semantic** | What role does this colour play? | `--surface-page: var(--color-cream)` | Day-to-day CSS work |

**Rule:** components and layout reference **semantic** tokens. Semantic tokens reference **palette** tokens. No raw hex outside `tokens.css`.

The bevel pattern is a **third, local layer** — computed per component from a face colour (pattern preserved from the old `btn-nt.css`, naming already generic):

```css
.btn {
  --bevel-face: var(--action-primary);
  --bevel-hi: color-mix(in srgb, var(--bevel-face) 40%, white);
  --bevel-lo: color-mix(in srgb, var(--bevel-face) 45%, var(--text-primary));
}
```

`color-mix` stays on the component. Tokens supply the face; components derive hi/lo.

---

## Palette tokens (brand inks)

```css
:root {
  /* Neutrals */
  --color-cream: #f5f1e5;        /* page */
  --color-cream-deep: #ede8d8;   /* code blocks, stripe band */
  --color-parchment: #ede8d6;    /* warm raised surface (was --bg-nt-tip mix) */
  --color-espresso: #3d2e2a;     /* primary text */
  --color-stone: #73665e;        /* muted text */
  --color-rule: #d9d0c0;         /* dividers */

  /* Accent triad (logo / stripe) */
  --color-sage: #8dc7a5;
  --color-sage-hover: #6fa888;
  --color-peach: #e9a57d;
  --color-clay: #d77e57;

  /* Accent tints (join lane backgrounds — tints of peach/clay, not new colours) */
  --color-peach-tint: #f9ebdf;
  --color-clay-tint: #f5ddd0;
}
```

**Join lanes merged:** the old `--lane-member` / `--lane-volunteer` hex values were duplicates of peach and clay; their backgrounds are tints of the same inks. They are no longer independent colours — lanes become semantic aliases below. One brand edit moves everything.

**`--color-parchment`:** replaces the anonymous `color-mix(in srgb, var(--bg-code) 85%, #f0e8c8 15%)` — the computed value, promoted to a named ink. Used by tertiary buttons, cards, and panel bodies.

### Migration map (one pass, on go)

| Old (14) | New |
|---|---|
| `--bg` | `--color-cream` (via `--surface-page`) |
| `--text` | `--color-espresso` (via `--text-primary`) |
| `--muted` | `--color-stone` (via `--text-muted`) |
| `--accent` | `--color-sage` |
| `--accent-hover` | `--color-sage-hover` |
| `--accent-2` | `--color-peach` |
| `--accent-3` | `--color-clay` |
| `--rule` | `--color-rule` |
| `--rule-peach` | `--border-section` (semantic) |
| `--bg-code` | `--color-cream-deep` (via `--surface-code`) |
| `--bg-nt-tip` | `--color-parchment` (via `--surface-panel`) |
| `--lane-member` / `--lane-member-bg` | `--lane-member` → peach / peach-tint (semantic) |
| `--lane-volunteer` / `--lane-volunteer-bg` | `--lane-volunteer` → clay / clay-tint (semantic) |

No aliases, no shim period — full rename in one pass since this is a fork.

---

## Semantic tokens (roles)

```css
:root {
  /* Surfaces */
  --surface-page: var(--color-cream);
  --surface-code: var(--color-cream-deep);
  --surface-panel: var(--color-parchment);   /* cards, panels, tertiary buttons, header ties */
  --surface-field: color-mix(in srgb, var(--color-cream) 45%, white);
                                             /* form inputs — near-white sunken face */

  /* Text */
  --text-primary: var(--color-espresso);
  --text-muted: var(--color-stone);
  --text-link: var(--color-clay);            /* prose links */

  /* Actions (buttons reference intent, not colour) */
  --action-primary: var(--color-sage);
  --action-primary-hover: var(--color-sage-hover);
  --action-secondary: var(--color-clay);
  --action-tertiary: var(--surface-panel);   /* tertiary / transport buttons */

  /* Borders */
  --border-default: var(--color-rule);
  --border-section: color-mix(in srgb, var(--color-peach) 38%, var(--color-rule));
                                             /* home section dividers — named for the job, not the colour */

  /* Join lanes (join pages only) */
  --lane-member: var(--color-peach);
  --lane-member-surface: var(--color-peach-tint);
  --lane-volunteer: var(--color-clay);
  --lane-volunteer-surface: var(--color-clay-tint);
}
```

**Naming rule for semantics:** name the **job** (`--border-section`), never the colour (`--border-peach`). If the brand shifts peach to something else, the token name still tells the truth.

---

## Layout, spacing, type scale

Minimal scales — new and edited rules use them; no mass rewrite of every existing `rem` on day one. Adopt as files get touched.

```css
:root {
  /* Layout */
  --layout-content-width: 44rem;
  --layout-gutter: 1.25rem;

  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-s: 0.5rem;
  --space-m: 1rem;
  --space-l: 1.5rem;
  --space-xl: 2.5rem;
  --space-2xl: 4rem;

  /* Type scale */
  --font-size-s: 0.9rem;     /* captions, footer, catalog notes */
  --font-size-m: 1.05rem;    /* body */
  --font-size-l: 1.15rem;    /* lead */
  --font-size-xl: 1.65rem;   /* section headings */
  --font-size-2xl: 2.5rem;   /* page titles */
}
```

Both scales are shown visually on the [component catalog](./catalog-scope.md) foundations section.

---

## Hero inverted tokens (minimal — not dark mode)

The site is **light-mode first**. The home hero uses a small inverted group — charcoal field, cream text — without implying a sitewide theme:

```css
:root {
  /* Hero inverted — home hero only; not a theme switch */
  --hero-inv-bg: #373430;
  --hero-inv-text: #eee6d4;
  --hero-inv-text-muted: color-mix(in srgb, var(--hero-inv-text) 72%, var(--hero-inv-bg));
  --hero-inv-band-height: 10px;
}
```

Band colours in the hero handoff reuse palette tokens (sage, peach, clay, cream-deep). Stars use palette colours at low opacity in `pages.css` — no extra tokens.

Class rename to match: `hero--night` → `hero--inverted` (see [class-naming.md](./class-naming.md)).

---

## Stripe tokens

```css
:root {
  --stripe-band-height: 3px;
}
```

Band colours reference the palette directly in `layout.css` (cream-deep / peach / clay) — three extra indirection tokens bought nothing. Hero-foot sage-light stays a local `color-mix` in hero CSS.

---

## File placement

Everything above lives in **`tokens.css`** only, in this order:

1. Palette
2. Semantic aliases
3. Layout / spacing / type scales
4. Hero inverted group
5. Stripe constants

Variables only — no selectors with rules.

## Editing guide (for humans)

- **Change the brand sage?** Edit `--color-sage` once; `--action-primary` follows.
- **New component surface?** Add one semantic token pointing at a palette colour. Never hex in component files.
- **New spacing?** Pick the nearest `--space-*` step; only add a step if two components genuinely need it.

## Related

- [file-layout.md](./file-layout.md) — load order
- [class-naming.md](./class-naming.md) — component names using these tokens
- [catalog-scope.md](./catalog-scope.md) — foundations rendered visually
