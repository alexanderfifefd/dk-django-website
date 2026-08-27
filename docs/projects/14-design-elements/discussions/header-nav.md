# Header nav

**Date:** 2026-08-22 (updated 2026-08-27)  
**Status:** liked — keep exploring on prototype 14

## Question

How should wayfinding sit next to the Pacifico wordmark without competing with it or reading as generic SaaS nav?

## On the site today (prototype 14)

| Item | Treatment | Notes |
|---|---|---|
| **Articles** | Plain text link, `--text` | First letter underlined (`.nav-link--mark`) |
| **About** | Plain text link, `--text` | Same first-letter mark |
| **Join** | `.btn-nt.btn-nt--primary.btn-nt--with-caret` | Sage primary + pixel caret — main hub entry |
| **(lab)** | Footer only (`.footer-lab`) | Small, muted, below org nr — not in nav |

Nav links use **`--text`** (espresso), same ink as NT button labels — not `--muted` or terracotta prose-link colour.

## First-letter underline

**Articles** and **About** get a subtle underline on the **first character only** via `::first-letter` on
`.nav-link--mark`. Reads as a quiet wayfinding cue — interesting without a full link underline row next to
the script wordmark.

Hover on marked links does **not** extend the underline to the whole word; **(lab)** in the footer still
underlines on hover.

## Rejected

- **Tertiary NT** for Articles/About — cream face on cream header disappears; nav stays text, not buttons.
- **Muted nav colour** — too weak next to the wordmark; `--text` aligns nav with control labels.
- **(lab) in header** — prototype sandbox link belongs out of the main wayfinding row.

## Implementation

- `public/templates/public/partials/header.html`
- `public/templates/public/partials/footer.html` — `.footer-lab`
- `static/css/site.css` — `.site-nav`, `.nav-link--mark`, `.footer-lab`
- Join uses same pixel caret as tertiary transport buttons — see [transport-buttons.md](./transport-buttons.md)

## Related

- [transport-buttons.md](./transport-buttons.md) — NT Join button
- [datakollektivet-brand.md](./datakollektivet-brand.md) — logo + stripe precedence
