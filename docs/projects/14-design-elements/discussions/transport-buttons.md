# Transport buttons

**Question:** How should a control signal “go to another page” — without inventing a third button language?

## Distinction

- **Action** — submit, pay, continue (commits)
- **Transport** — navigate onward (About, All articles, Join hub)

## On the site today (prototype 14 home)

| Location | Pattern | Classes | Tier / read |
|---|---|---|---|
| Header **Join** | NT button + pixel caret | `.btn-nt.btn-nt--primary.btn-nt--with-caret` | Sage — main hub entry |
| **Latest articles** heading | NT + pixel caret | `.btn-nt.btn-nt--tertiary.btn-nt--with-caret` | Cream — section index, right of `h2` |
| **Want to participate?** | Clickable card | `.panel-nt` link | Liked — see [clickable-card.md](./clickable-card.md) |
| **Who we are** footer | NT + caret | `.btn-nt.btn-nt--tertiary.btn-nt--with-caret` | Warm transport, right-aligned |
| Prose | Terracotta link | `a` | In-copy only |

Copy: **All articles** (was “View all”), **About us**, **Join the collective**.

Earlier experiments (underlined transport + hand-drawn arrow, script fonts, bottom-right orphan links,
three-tier test row under What we do) were removed or rejected.

## NT button prototype (`btn-nt.css`)

Loaded site-wide from `base.html`. Windows-style **inset bevel** (light top/left, dark bottom/right;
inverts on `:hover` for pressed read), square corners, face colour parameterized:

| Variant | Class | Face | Read |
|---|---|---|---|
| Primary | `.btn-nt--primary` | `--accent` (sage) | Main affirmative action |
| Secondary | `.btn-nt--secondary` | `--accent-3` (terracotta) | Warm transport — not corporate blue |
| Tertiary | `.btn-nt--tertiary` | `--bg-nt-tip` | Warm surface — section transport, matches header/card |

Shared `--nt-face`, `--nt-hi`, `--nt-lo` drive bevel from each face colour.

**Pixel caret** — `.btn-nt--with-caret` appends an 8×10 block-arrow SVG (mirrored for right-pointing read). Used on header Join, Latest articles, About us, and inside the tip card's `.panel-nt__go`.

## NT panel (`.panel-nt`)

Evolved into the **clickable card** pattern — see [clickable-card.md](./clickable-card.md).

## Still open

- Secondary NT vs prose-link semantics (terracotta overlap)
- Final hero direction (night sky vs stripe-lab variants)
- Promote NT / panel / hero patterns to prototype 11, or keep sandbox-only

## Brand context

- [datakollektivet-brand.md](./datakollektivet-brand.md) — NT vs logo/stripe tensions
- [header-nav.md](./header-nav.md) — nav text + first-letter underline (liked)
