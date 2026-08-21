# Plan: prototype 11 — site design

**Project:** `site-design`
**Discussion:** `docs/projects/site-design/discussions/brand-palette.md`
**Prototype:** `prototypes/11-site-design/`
**Status:** first design pass complete (2026-08-21)

## Goal

Explore the brand color palette on the first-version page set without mutating prototype 10.

## Approach

Fork `prototypes/10-first-version/` → `prototypes/11-site-design/`. Apply token swap in
`static/css/site.css` only.

## Token mapping (best-effort)

Hybrid of discussion options A and B:

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#F5F1E5` | Page background |
| `--text` | `#3D2E2A` | Body, headings, button label on green |
| `--muted` | `#73665E` | Secondary copy |
| `--accent` | `#8DC7A5` | Primary buttons, form focus |
| `--accent-hover` | `#6FA888` | Button hover |
| `--accent-2` | `#E9A57D` | Member join lane |
| `--accent-3` | `#D77E57` | Links, volunteer lane, card hovers |
| `--rule` | `#D9D0C0` | Borders |
| `--bg-code` | `#EDE8D8` | Code blocks, CTA panel, notices |

Join path cards: account neutral cream; member peach tint; volunteer clay tint.

## Verify

From `prototypes/11-site-design/`:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Home, join hub, and article pages should show cream background and warm accents. Prototype 10 unchanged.

## Header stripe (2026-08-21)

**Warm triad** — clay, peach, cream bands in `partials/stripe.html`. Home body uses peach rules only.
Full iteration log: [2026-08-21-design-iteration-summary.md](../discussions/2026-08-21-design-iteration-summary.md).

## Open follow-ups

- Sample exact `--text` from logo artwork
- Typography or spacing tweaks if palette exposes weak hierarchy
- Promote decisions back into discussions if we revise the mapping
