# Visual & structural checklist

**Date:** 2026-08-27 (expanded — core QA document)  
**Refactor QA result:** greps in section E all zero; every route + stylesheet returns 200; home verified visually (header marks, bevel Join, inverted hero, article cards, join CTA card, footer stripe). Remaining route-by-route eyeballing is a follow-up pass.  
**Use:** run the relevant gate after each refactor phase. Manual eyeballing plus greps — no screenshot tooling. Baseline screenshots from fork time live in [`assets/`](../assets/): [home](../assets/home.png) · [join hub](../assets/join-hub.png) · [about](../assets/about.png).

Server: `uv run python manage.py runserver` from `prototypes/15-css-structure/`.

---

## Route inventory (what to open)

| Route | Page |
|---|---|
| `/` | Home |
| `/articles/` | Articles index |
| `/articles/<slug>/` | Article detail (either seeded article) |
| `/about/` | About |
| `/join/` | Join hub |
| `/join/account/` · `/join/member/` · `/join/volunteer/` | Join paths (forms) |
| `/design-lab/` | Component catalog |

---

## A. Global chrome (every route)

- [ ] Sticky header: logo left; Articles/About text links with **first-letter underline**; Join button (sage bevel + pixel caret) right
- [ ] Stripe under header: three bands, **cream → peach → clay** top-to-bottom, full bleed
- [ ] Body: cream background, espresso text, terracotta prose links (hover → espresso)
- [ ] Footer: section rule, logo mark, org nr, small muted `(lab)` link, then the **three-band stripe closes the page** (redesign — mirrors header)
- [ ] **Hover:** any bevel button presses in (highlight/shadow invert)

## B. Home (`/`) — compare against [home.png](../assets/home.png)

- [ ] Hero: charcoal field flush under stripe (no cream gap), centered cream H1 + muted lead, soft scattered stars (cream/sage/peach)
- [ ] Hero foot: five bands (sage → sage-light → cream → peach → clay), then cream body
- [ ] "What we do": prose + terracotta inline article link
- [ ] "Who we are": About us **tertiary bevel + caret**, right-aligned below prose
- [ ] "Latest articles": heading row with **All articles** tertiary + caret on the right
- [ ] Article list: **cards** — espresso bold title, muted summary, date meta line; whole card is the link (redesign — see intentional diffs)
- [ ] Join card: parchment face, yellow pixel icon tile, "Want to participate?" title, copy, underlined **Join the collective** + caret bottom-right; **entire card is one link**; hover presses the bevel
- [ ] Section dividers: warm peach-tinted rules (`--border-section`)

## C. Inner pages

### About (`/about/`) — [about.png](../assets/about.png)

- [ ] Page hero title + rule; three prose sections
- [ ] "Want to participate?" row: **bevel** primary button (after Phase 3 the legacy rounded button is gone)

### Articles (`/articles/`, detail)

- [ ] Index list matches home list styling
- [ ] Detail: title, date, prose typography, code blocks on `--surface-code`

### Join hub (`/join/`) — [join-hub.png](../assets/join-hub.png)

- [ ] Three path cards side by side: title, copy, underlined action + caret bottom-right
- [ ] Whole card clickable; bevel press on hover

### Join forms (account / member / volunteer)

- [ ] Form fields: **sunken bevel** on near-white face (`--surface-field`), bold labels, muted hints, sage focus ring
- [ ] Submit buttons: **bevel primary** (not legacy rounded)
- [ ] Submitted state: `notice` strip (sunken parchment)
- Note: no lane accents shipped — path cards are uniform; lane tokens reserved

## D. Catalog (`/design-lab/`)

After Phase 5 build-out ([catalog-scope.md](./catalog-scope.md)):

- [ ] Foundations: palette swatches match `tokens.css` (spot-check 3 hexes in devtools); type + spacing scales render
- [ ] Buttons: primary / secondary / tertiary / caret / disabled all present
- [ ] Cards: action card (icon + no-icon), path card
- [ ] Panel: title bar + body + action button
- [ ] Forms, navigation & chrome, content patterns sections present
- [ ] `catalog.css` loads **only** here (devtools network on `/` shows no catalog.css)
- [ ] No hero stripe variants anywhere

---

## E. Structural greps (run after renames — all must be zero)

From `prototypes/15-css-structure/`:

```bash
# Old names fully gone (CSS + templates)
rg -l 'btn-nt|panel-nt|win-nt|clickable-card|nt-tip|hero-night|hero--night|design-lab-|btn-primary' public static

# No raw hex outside tokens.css
rg '#[0-9a-fA-F]{3,8}\b' static/css --glob '!tokens.css'
# (allowed exception: none — SVG fills in templates are fine, CSS is not)

# Old token names gone
rg -- '--bg[^-]|--accent|--muted|--rule[^-]|--lane-member-bg|--bg-code|--bg-nt-tip' static/css

# Deleted files really deleted
ls static/css   # → tokens, base, layout, components, pages, catalog, README only
```

## F. Phase gates

| After | Run |
|---|---|
| Phase 1 (tokens) | A + B + one join form; token greps in E |
| Phase 2 (split) | A–C fully; `ls` check in E |
| Phase 3 (components + de-NT) | A–C + rename greps in E; all buttons bevel |
| Phase 4 (hero rename + lab deletion) | B hero items; hero greps |
| Phase 5 (catalog) | D fully |
| Phase 6 (README) | Full pass A–F once, tick everything |

## Known intentional diffs vs prototype 14

- Catalog page: completely rebuilt (storybook layout) — do **not** compare to 14's design lab
- About/join buttons: rounded legacy → bevel (deliberate upgrade)
- **Articles redesign**: home + index lists are cards (espresso titles, not terracotta links) — orange stays for prose links only; articles and join pages share the card language
- **Forms**: NT sunken-bevel fields (was flat bordered inputs)
- **Footer**: three-band stripe at page bottom replaces the content-width gradient bar
- Nav first-letter mark is an HTML `<span class="nav-mark">` (was `::first-letter`)
- Everything else should match 14 visually; if it doesn't and it's not listed here, it's a regression
