# Plan: prototype 12 — dark mode

**Project:** `dark-mode`
**Discussion:** `docs/projects/12-dark-mode/discussions/dark-palette.md`
**Prototype:** `prototypes/12-dark-mode/`
**Status:** first pass (2026-08-21)

## Goal

Explore the dark brand palette on the first-version page set without mutating prototype 11.

## Approach

Fork `prototypes/11-site-design/` → `prototypes/12-dark-mode/`. Apply token swap in
`static/css/site.css`. Point header/footer at `logo-dark-theme.png` and
`logo-dark-theme-small.png`.

## Token mapping

Same surface roles as prototype 11; inverted base, accents from the dark mockup:

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#373430` | Page background |
| `--text` | `#EEE6D4` | Body, headings, button label on mint |
| `--muted` | `color-mix(in srgb, var(--text) 76%, var(--bg))` | Secondary copy |
| `--accent` | `#79C39D` | Primary buttons, form focus |
| `--accent-hover` | `color-mix(in srgb, var(--accent) 82%, var(--bg))` | Button hover |
| `--accent-2` | `#EE9B69` | Member join lane, stripe band |
| `--accent-3` | `#E77843` | Links, volunteer lane, card hovers |
| `--rule` | `color-mix(in srgb, var(--text) 12%, var(--bg))` | Borders |
| `--bg-code` | `color-mix(in srgb, var(--text) 8%, var(--bg))` | Code blocks, CTA panel, third stripe band |
| `--lane-member-bg` | `color-mix(in srgb, var(--accent-2) 14%, var(--bg))` | Member path card |
| `--lane-volunteer-bg` | `color-mix(in srgb, var(--accent-3) 14%, var(--bg))` | Volunteer path card |

Links → `--accent-3`; primary buttons → `--accent` with `--text` label (same split as prototype 11).

## Chrome adjustments

- **Header stripe** (`.site-stripe-band-muted`) → `--bg-code` (lifted charcoal)
- **Footer bar** gradient third stop → `var(--accent)` (mint, matching mockup swatch order)
- **Join path card hover shadow** → `rgba(0, 0, 0, 0.25)` instead of light-mode brown tint

## Verify

From `prototypes/12-dark-mode/`:

```bash
uv run python manage.py migrate
uv run python manage.py runserver
```

Home, join hub, and article pages should show charcoal background and warm accents. Prototype 11
unchanged. Compare side by side with prototype 11 on the same routes.

## Open follow-ups

- Contrast pass on links and muted text
- Optional iteration summary after visual review (mirror prototype 11's summary doc)
