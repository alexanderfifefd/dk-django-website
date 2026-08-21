# Plan: recruiting surfaces on prototype 07

**Project**: `member-journeys`
**Discussion**: `docs/projects/07-member-journeys/discussions/entry-points-and-conversion.md`
**Prototype**: `prototypes/07-initiatives/` — pass on 07
**Status**: built (2026-08-14)

## Goal

Make `recruiting: open` visible on the site so initiative and system recruitment entry points exist
alongside the existing collective Join funnel. CSS stubs already live in `static/css/site.css`; wire
templates and views.

## Scope (revised during build)

Initial scope included home strips and index "Looking for help" bands. Those were removed — recruiting
is surfaced via badges, shared **`recruiting-card`** grids, and detail pitch panels instead. See
[three-paths-to-participate.md](../discussions/three-paths-to-participate.md).

### Shipped

| Surface | Behaviour |
|---|---|
| List items | "Looking for help" badge when `recruiting: open` |
| **Ideas** / **Proposed** index sections | `recruiting-card` grid with pitch CTAs |
| **`/join/volunteer/`** | Recruiting cards for open roles |
| Detail pages | Badge; pitch panel for `idea` / `proposed`; get-involved aside for other recruiting |

### Out of scope

- Join form backend, new URL routes, forge integration, article embeds, copy overhaul on Join page.

## Seed content exercising the UI

| Slug | Type | `recruiting: open` |
|---|---|---|
| `terms-of-service` | initiative | yes (no takers, no coord links — tests fallback) |
| `listmonk` | system | yes |

## Done when

- `recruiting: open` visible on list items, index pitch sections, volunteer page, and detail pages
- Collective Join CTAs unchanged (later rebuilt as three-path hub — see three-join-paths plan)
- Project docs updated

## Outcome

**2026-08-14:** Recruiting surfaces shipped on prototype 07.

- List items: "Looking for help" badge
- **Ideas** and **Proposed** index sections: shared `recruiting-card` grid (pitch labels + lane-coloured CTAs)
- **`/join/volunteer/`**: recruiting cards for open initiatives/systems
- Detail pages: badge; expanded pitch card for `idea` systems and `proposed` initiatives; get-involved aside for production recruiting

Home/index recruiting strips from the first sketch were **removed** after feedback. Join flow later
split into three paths (account / member / volunteer) — see [2026-08-14-three-join-paths.md](./2026-08-14-three-join-paths.md).
