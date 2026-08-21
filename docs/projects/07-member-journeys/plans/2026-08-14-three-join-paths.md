# Plan: three Join paths

**Project**: `member-journeys`
**Discussion**: `docs/projects/07-member-journeys/discussions/three-paths-to-participate.md`
**Prototype**: `prototypes/07-initiatives/`
**Status**: built (2026-08-14)

## Goal

Split Join into a chooser plus three dedicated pages: account, member, volunteer. Move recruiting
cards to the volunteer page.

## Routes

| Route | Template |
|---|---|
| `/join/` | `join.html` — path cards |
| `/join/account/` | `join_account.html` |
| `/join/member/` | `join_member.html` |
| `/join/volunteer/` | `join_volunteer.html` |

## Outcome

- Hub is chooser only; no forms on `/join/`
- Account page explains free services → registration link
- Member page: benefits, fee, payment stub form
- Volunteer page: responsibilities, recruiting cards, application + agreement checkbox
- Detail pages link to `join_account` / `join_volunteer`

## Supersedes

[2026-08-14-join-hub.md](./2026-08-14-join-hub.md) — single-page hub with stacked sections.
