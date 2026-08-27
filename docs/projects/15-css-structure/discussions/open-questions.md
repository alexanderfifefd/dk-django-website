# Open questions — resolution log

**Date:** 2026-08-27 (final review pass done; refactor implemented same day)

All blocking questions are resolved. Kept as a log of what was decided and where.

## Decided

| Question | Decision | Doc |
|---|---|---|
| File split | Layer split: tokens / base / layout / components / pages + catalog | [file-layout.md](./file-layout.md) |
| Load order contract | `base.html` comment + `static/css/README.md` | [file-layout.md](./file-layout.md) |
| Page-specific CSS | Catalog only via `extra_css`; everything else selector-scoped in `pages.css` | [file-layout.md](./file-layout.md) |
| Token naming | Palette (`--color-*`) + semantic (`--surface-*`, `--action-*`, `--border-*`) | [tokens-and-palette.md](./tokens-and-palette.md) |
| Token migration | One pass, no aliases | same |
| Join lanes | Merged — peach/clay + named tints; semantic `--lane-*` aliases | same |
| `--bg-nt-tip` | → `--color-parchment` / `--surface-panel` (NT naming retired) | same |
| `--border-peach` | → `--border-section` (name the job, not the colour) | same |
| Spacing / type scale | Added, minimal; adopt as rules get touched | same |
| Hero dark colours | Minimal `--hero-inv-*` group; light-mode-first, inverted hero only | same |
| Class naming | BEM; **generic names**: `btn`, `card`, `panel` — NT fully retired from names | [class-naming.md](./class-naming.md) |
| `clickable-card` | Dropped — cards are whole-surface links by default | same |
| Legacy `.btn` | Deleted; all buttons are the bevel button (same phase as `btn-nt → btn` rename) | same |
| Templates | Plain Django includes per component; shared `caret.html` replaces inline SVG copies | same |
| Catalog | Storybook-style component catalog (foundations + variant matrix); name stays **catalog**; URL stays `/design-lab/` | [catalog-scope.md](./catalog-scope.md) |
| Hero stripe lab | Deleted from 15; remains in prototype 14 | same |
| QA | Expanded checklist, phase gates, greps; baseline screenshots in `assets/`; no screenshot tooling | [visual-checklist.md](./visual-checklist.md) |
| Promotion | Still prototyping — no merge to 11/14 yet | [overview.md](../overview.md) |
| Transport button token | `--action-tertiary` (user preferred "tertiary" over "transport") | [tokens-and-palette.md](./tokens-and-palette.md) |
| Join lane classes | Not needed — path cards uniform; lane tokens reserved | [class-naming.md](./class-naming.md) |
| Nav first-letter mark | HTML `<span class="nav-mark">`, not `::first-letter` (breaks under display changes) | [class-naming.md](./class-naming.md) |
| Articles design | Redesigned as cards (espresso titles; orange for prose links only); join and articles share the card language | [visual-checklist.md](./visual-checklist.md) |
| Forms | NT sunken-bevel fields (`form-stack`, `--surface-field`); `notice` strip | [class-naming.md](./class-naming.md) |
| Bottom stripe | Three-band stripe also closes the page (footer) | [visual-checklist.md](./visual-checklist.md) |

## Deferred (non-blocking)

1. **URL `/design-lab/` → `/catalog/`** — optional cleanup, not scheduled
2. **Hero direction** — waiting per project 14 ([hero-directions.md](../../14-design-elements/discussions/hero-directions.md)); catalog gets a hero section once final
3. **Route-by-route visual pass** — home verified after refactor; full checklist A–D eyeball pass still open

## Related

- [css-structure.md](./css-structure.md) · [current-state.md](./current-state.md) · [plan](../plans/2026-08-27-prototype-15-css-structure.md)
