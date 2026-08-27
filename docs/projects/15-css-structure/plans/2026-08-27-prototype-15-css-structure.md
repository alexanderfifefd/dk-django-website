# Plan: prototype 15 — CSS structure

**Status:** done — implemented 2026-08-27. All six phases landed in a single pass (the fork made incremental gates unnecessary); greps clean, all routes 200, home verified visually.

## Goal

Reorganise CSS into a minimal layer split with a real token system, retire NT naming for generic design-system names (button / card / panel), build a storybook-style component catalog, delete lab experiments and dead code — **same look as prototype 14** except the deliberate diffs listed in the checklist.

## Decisions (all locked)

| Topic | Decision | Doc |
|---|---|---|
| File split | tokens → base → layout → components → pages (+ catalog.css) | [file-layout.md](../discussions/file-layout.md) |
| Tokens | Palette + semantic layers; lanes merged into peach/clay tints; `--surface-panel` replaces nt-tip; `--border-section` replaces border-peach; spacing + type scales added; hero-inv minimal group | [tokens-and-palette.md](../discussions/tokens-and-palette.md) |
| Token migration | **One pass**, no aliases | same |
| Naming | BEM; **de-NT**: `btn` / `card` / `panel`; `hero--inverted`; `catalog-*`; `clickable-card` dropped (cards are links by default) | [class-naming.md](../discussions/class-naming.md) |
| Legacy `.btn` | Deleted; all buttons are the bevel `btn` (deletion + rename same phase — name collision otherwise) | same |
| Catalog | Storybook-style component catalog; foundations + full variant matrix; URL stays `/design-lab/` | [catalog-scope.md](../discussions/catalog-scope.md) |
| Lab experiments | Hero stripe lab deleted from 15 (lives on in 14) | same |
| QA | Expanded checklist with phase gates + greps; baseline screenshots in `assets/` | [visual-checklist.md](../discussions/visual-checklist.md) |

---

## Phase 1 — Tokens (one pass)

- Create `tokens.css`: palette, semantic, layout/spacing/type scales, hero-inv, stripe constants
- Rename every `var(--old)` in `site.css` / `btn-nt.css` to new semantic tokens; delete old `:root` block
- Replace the two hero hexes and the nt-tip `color-mix` with tokens

**Gate:** checklist A + B + one join form; token greps zero.

## Phase 2 — Split `site.css`

- Move rules to `base.css`, `layout.css`, `pages.css` (hero, home, articles, join, about)
- `.design-lab-*` rules parked in `pages.css` temporarily (move to `catalog.css` in Phase 5)
- Update `base.html` links with order comment; delete `site.css`

**Gate:** checklist A–C; file listing correct.

## Phase 3 — Components + de-NT

- Create `components.css` from `btn-nt.css` with generic names: `btn`, `card`, `panel`, shared caret
- **Same commit:** delete legacy `.btn` rules; migrate about + join templates to `btn btn--primary`
- Rename template partials: `card.html`, `card_join.html`, `panel.html`, `caret.html`; replace inline caret SVGs with the include
- Update all templates to new class names; delete `btn-nt.css`

**Gate:** checklist A–C; rename greps zero; every button bevels.

## Phase 4 — Hero rename + lab deletion

- `hero--night` → `hero--inverted`, `hero-night__*` → `hero-inv__*` (CSS + `home.html`)
- Delete `hero-stripe-lab.css` + `hero_lab_*.html` partials

**Gate:** checklist B hero items; hero greps zero.

## Phase 5 — Component catalog (build-out)

Per [catalog-scope.md](../discussions/catalog-scope.md):

- Rebuild `design_lab.html` → catalog sections: foundations (swatches, scales), buttons, cards, panel, forms, navigation & chrome, content patterns
- Create `catalog.css` (`catalog-*` classes; `page-catalog` body class); move parked `design-lab-*` rules in, renamed
- Settle join lane classes (`card--path` + lane modifiers) while touching join CSS

**Gate:** checklist D; catalog.css loads only on catalog route.

## Phase 6 — README + doc sync

- `static/css/README.md` (load order, where-do-I-put-X)
- Update prototype `README.md` "what changed" section
- Update [current-state.md](../discussions/current-state.md) to after-state; mark plan phases done
- Full checklist pass A–F

---

## Done

- Fork 14 → 15; baseline screenshots in `assets/`
- Discussion docs: tokens (reworked), file layout, class naming (de-NT), catalog spec (storybook), checklist (expanded)
- All blocking decisions resolved
- **Phases 1–6 implemented** (2026-08-27): six-file split live, tokens migrated one-pass, de-NT renames done, lab deleted, catalog rebuilt, READMEs written

## Deviations from plan (all deliberate, from final review feedback)

- `--action-transport` shipped as **`--action-tertiary`** (preferred name)
- **Articles redesign**: home + `/articles/` lists are now `card`s (title in espresso, muted summary, `card__meta` date line) — orange reserved for prose links; join and articles pages share the card language
- **Forms went NT**: sunken-bevel fields on new `--surface-field`, sage focus ring; `join-form` → generic `form-stack`, `join-notice` → `notice` (sunken parchment strip)
- **Footer**: gradient bar replaced by the real three-band stripe closing the page bottom (mirrors the header), brand block over a section rule
- **First-letter nav mark moved to HTML** (`nav-mark` span) — `::first-letter` is unreliable
- **No `card--path` / lane modifiers** — join path cards are uniform; lane tokens kept for future accents
- Stripe band colour tokens (`--stripe-band-1..3`) dropped — bands reference palette directly in `layout.css`

## Verify

```bash
cd prototypes/15-css-structure
uv run python manage.py runserver
```

Phase gates in [visual-checklist.md](../discussions/visual-checklist.md).

## Non-goals

- Dark mode (light-first; hero inversion only)
- New visual design beyond the deliberate button upgrade
- Promotion to prototype 11/14 (still prototyping)
