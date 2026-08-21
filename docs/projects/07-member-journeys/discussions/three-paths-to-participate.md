# Discussion: three paths to participate

**Date:** 2026-08-14
**Status:** prototype 07 implementation of core model — see **`docs/organizational-context.md`**
**Prototype:** `prototypes/07-initiatives/`

The **three paths** (account, member, volunteer) and how they relate are defined in
[`docs/organizational-context.md`](../../../organizational-context.md#paths-to-participate). This doc
covers how prototype 07 implements them on the site.

This doc supersedes the single-page hub layout in [join-as-entry-hub.md](./join-as-entry-hub.md).
Earlier member-journeys docs remain as procedural history.

## Site routes (prototype 07)

| Path | URL | Prototype behaviour |
|---|---|---|
| **Account** | `/join/account/` | Explains free services → SSO registration link (stub) |
| **Member** | `/join/member/` | Voting, fee, payment stub |
| **Volunteer** | `/join/volunteer/` | Application + agreement checkbox + recruiting cards |

**`/join/`** is a chooser — three cards, no forms on the hub.

## Page responsibilities

### `/join/` — chooser

Three path cards. Framing: collective runs on participation; pick the path that fits.

### `/join/account/` — create account

Dedicated page (not a bare SSO link on the hub). Explains free-tier access, then **Continue to
account creation** → identity provider registration URL.

### `/join/member/` — become a member

Voting rights, fee, payment step. Assumes account exists. Stub: confirm handle + email → continue
to payment.

### `/join/volunteer/` — become a volunteer

- What volunteering involves (moderation, maintenance, initiative driving).
- **Recruiting cards** (`recruiting: open` initiatives/systems) — open roles to reference in the
  application.
- Application form + checkbox acknowledging volunteer agreement / contract.

## Detail pages and other CTAs

System/initiative pages stay **local** (teamlead, taker, future forge help-wanted). They link out to:

- **Account** → `/join/account/` when tools require identity
- **Volunteer** → `/join/volunteer/` when recruiting a driver/maintainer

Recruitment **signals** (authored `recruiting: open` vs forge `help wanted` vs Loomio input) are
defined in organizational context. Contributor-flow detail:
[help-wanted-and-recruiting.md](./help-wanted-and-recruiting.md).

## What earlier docs got wrong (and we keep)

| Earlier idea | Verdict |
|---|---|
| Single Join page with account + recruiting + membership stacked | **Superseded** — split into paths |
| Recruiting strips on home/index | **Removed** — still correct |
| Badges on list items, detail asides | **Kept** |
| Forge `help wanted` on system pages | **Still planned** — not on Join hub |
| "Membership form" as the whole Join page | **Superseded** — member path + payment |

## Open (implementation)

- Real Keycloak registration URL and payment provider integration
- Volunteer contract as downloadable/signable document
- Pre-fill volunteer application from `?role=listmonk` or initiative slug
- Forge help-wanted section on system detail (separate from volunteer application)

## Related

- **`docs/organizational-context.md`** — authoritative participation model
- [help-wanted-and-recruiting.md](./help-wanted-and-recruiting.md) — detail-page contributor flow
- [2026-08-14-three-join-paths.md](../plans/2026-08-14-three-join-paths.md) — build plan
