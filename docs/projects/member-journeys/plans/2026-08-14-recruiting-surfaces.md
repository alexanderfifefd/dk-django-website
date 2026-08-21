# Plan: recruiting surfaces on prototype 07

**Project**: `member-journeys`
**Discussion**: `docs/projects/member-journeys/discussions/entry-points-and-conversion.md`
**Prototype**: `prototypes/07-initiatives/` — pass on 07
**Status**: built (2026-08-14)

## Goal

Make `recruiting: open` visible on the site so initiative and system recruitment entry points exist
alongside the existing collective Join funnel. CSS stubs already live in `static/css/site.css`; wire
templates and views.

## Scope

### Views

- Filter querysets: `Initiative` and `System` where `recruiting=Recruiting.OPEN`.
- Pass to `home`, `systems_index`, `initiatives_index`.

### Templates

| File | Change |
|---|---|
| `includes/recruiting-badge.html` | New — reusable Open badge |
| `includes/initiative-list-item.html` | Badge when recruiting |
| `includes/system-list-item.html` | Badge when recruiting |
| `initiatives_index.html` | "Looking for help" section |
| `systems_index.html` | "Looking for help" section |
| `home.html` | Recruiting links strip above join-cta |
| `initiative_detail.html` | Badge; get-involved aside when recruiting (with Join fallback) |
| `system_detail.html` | Badge; get-involved aside when recruiting |

### Out of scope

- Join form backend, new URL routes, forge integration, article embeds, copy overhaul on Join page.

## Seed content exercising the UI

| Slug | Type | `recruiting: open` |
|---|---|---|
| `terms-of-service` | initiative | yes (no takers, no coord links — tests fallback) |
| `listmonk` | system | yes |

## Done when

- Home, both index pages, and both detail page types show recruiting where content sets `recruiting: open`
- Collective Join CTAs unchanged
- Project docs and `docs/projects/index.md` updated

## Outcome

**2026-08-14:** Recruiting surfaces shipped on prototype 07.

- Home: "Looking for help" link strip above collective join-cta
- `/initiatives/` and `/systems/`: shared "Looking for help" band (initiatives + systems with `recruiting: open`)
- List items: "Looking for help" badge
- Initiative detail: badge + get-involved aside when recruiting (Join fallback when no taker/coord links)
- System detail: badge + get-involved aside with teamlead + Join when recruiting

Collective Join CTAs unchanged. See `pages/views.py`, recruiting includes, and detail templates.
