# Discussion: help wanted, recruiting, and the contributor flow

**Date:** 2026-08-14
**Builds on:** `docs/organizational-context.md` ([Recruitment signals](../../../organizational-context.md#recruitment-signals)),
[three-paths-to-participate.md](./three-paths-to-participate.md),
[lifecycle-and-recruiting](../../initiatives/discussions/lifecycle-and-recruiting.md),
[forge-primitives-as-site-content](../../forge-issues/discussions/forge-primitives-as-site-content.md),
`docs/organizational-context.md`
**Prototype:** `prototypes/07-initiatives/` (forge issues not wired here yet)
**Status:** extends core model in **`docs/organizational-context.md`** — prototype 07 detail below

## The question

When a system or initiative says it needs help, what should a visitor see **on that page** — and how
does that relate to forge threads, SSO, Matrix, and the Join hub?

The first member-journeys pass surfaced `recruiting: open` but then **punted detail pages to "open
roles on Join"** — wrong. If we're promoting help on the Listmonk page, the next steps should be
**local and concrete**, not a link back to a card grid elsewhere.

## Does this flow make sense?

**Yes.** A plausible first-contribution path:

```
Visitor lands on system they care about
  → sees help is wanted (authored flag and/or forge issues)
  → reads what is needed
  → learns they need a collective account (SSO) first
  → creates account → can reach Matrix, Loomio, Forgejo
  → picks a channel:
       · join the issue discussion (forge)
       · join the Matrix room
       · message the teamlead / taker
```

SSO is the **turnstile** — same for members and contributors. Detail pages should say that locally
when pointing at tools that require identity. The Join hub explains it once; **detail pages repeat
it in context** ("to join this thread, you'll need an account → …").

## Not all "help wanted" is the same thing

We are mixing signals that serve different intents:

| Signal | Source | What it means | Typical next step |
|---|---|---|---|
| **`recruiting: open`** | Authored (git frontmatter) | Collective statement: we need a **driver / maintainer / taker** for this system or initiative | Talk to teamlead/taker; Matrix/Loomio if set; membership conversation if org-level |
| **`help wanted` (forge label)** | Observed (issue in forge) | A **specific task or problem** is open for contribution | Read issue → comment / pick up work in forge thread |
| **Loomio thread / poll** | Authored link or future sync | **Input wanted** on a decision — opinions, approval, scope | Discuss on Loomio — not necessarily "become the owner" |
| **Initiative with no taker** | Authored | **We want someone to drive this goal** | Strong overlap with `recruiting: open`; may later get a Loomio proposal |

**Input wanted ≠ maintainer wanted.** A Loomio poll ("should we adopt Listmonk?") is not the same as
"we need someone to run Listmonk." The site should not flatten these into one badge.

The lifecycle doc already split **authored `recruiting`** from **observed forge labels** — this
discussion carries that further into UX.

### Stewardship vs task

- **Stewardship gap** — "this system/initiative needs a person" → `recruiting: open`, teamlead/taker,
  maybe `seeking-maintainer` forge label as a secondary observed echo.
- **Task gap** — "this bug/feature needs doing" → forge issue with `help wanted`; natural discussion
  starter; lower commitment entry.

A new visitor who *knows the stack* may prefer jumping into a **task** before volunteering as
**maintainer**. Both should be visible on the system page when they exist.

## What belongs on a system detail page

When help is wanted, the page should answer **"what can I do here?"** without leaving:

1. **Prerequisite** — collective account (SSO) if the next steps need Forgejo/Matrix/Loomio.
2. **Open help-wanted issues** — when forge sync exists: linked list, prominent, not buried in a
   generic issue dump. Each item is a thread you can join.
3. **Stewardship** — if `recruiting: open`: teamlead (and admins); Matrix room when we add
   `matrix` to system frontmatter (today only on groups/initiatives).
4. **Coordination** — not "see open roles on Join."

The Join hub **aggregates** open stewardship pitches on **`/join/volunteer/`** (recruiting cards).
Detail pages **resolve** intent locally ("what do I do for *this* thing?").

Same split for initiatives: Loomio/Matrix/taker links stay local; SSO note when tools require it.

## Forge `help wanted` as first-class (future)

Prototype 04 proved syncing issues; 07 does not render them yet. The natural model:

- Issues labeled `help wanted` + `system/<slug>` appear in a **Help wanted** section on the system page.
- Optionally roll up on Join hub or a future `/get-involved/` — but **system page is the primary surface**
  for someone who already cares about that system.
- No separate authored flag required for task-level help — **existence of the issue is the signal**.
  Hygiene reward: label it right in the forge, it appears on the site.

Open design choices:

- Which labels earn semantics? Start with `help wanted`; maybe `good first issue` later.
- Link straight to forge issue URL (external) vs cached title/summary on site.
- Closed help-wanted issues drop off; aligns with "alive" narrative.

## Loomio's role

Initiatives already carry optional `loomio_url`. Reasonable uses:

| Loomio use | Site framing |
|---|---|
| Decision / proposal | "Have your say" — input wanted |
| Initiative coordination | "Discuss this effort" — may overlap with recruiting |
| Not a substitute for forge | Implementation work still lands in issues/PRs |

**Do not** treat every Loomio link as recruitment. Copy on the aside should match intent (discuss vs
volunteer to lead).

## Join hub vs detail pages (revised)

| Page | Job |
|---|---|
| **`/join/`** | Chooser: account, member, or volunteer |
| **`/join/account/`** | Free account creation → SSO registration |
| **`/join/member/`** | Membership, voting, payment |
| **`/join/volunteer/`** | Volunteer application + open role cards |
| **System detail** | Local: help-wanted issues (future) + teamlead + account/volunteer links |
| **Initiative detail** | Local: taker, Loomio/Matrix, account/volunteer links |

## What we are not building yet

- Full "job posting" objects for every recruitment need — start from forge issues + authored flags.
- Wiring forge sync into prototype 07 — likely a follow-on pass or layer from `forge-issues` /
  `git-identity` prototypes.
- Deciding Loomio API sync vs authored links only.
- Distinguishing every Loomio poll type in the UI.

## Open questions

1. **System `matrix` field** — add to system frontmatter (like groups/initiatives) for maintainer rooms?
2. **Label convention** — `help wanted` vs `seeking-maintainer` vs both on same issue?
3. **Initiative without taker** — is Loomio proposal the default coordination path before someone commits?
4. **SSO copy on detail pages** — one line + link to Join `#account`, or inline Keycloak link?
5. **When `recruiting: open` but no forge issues yet** (Listmonk today) — is teamlead + account note enough until someone opens a `help wanted` issue?
6. **Aggregate page** — still needed if system pages + Join hub cover discovery?

## Prototype fix (2026-08-14)

Removed "See open roles on Join" from system and initiative detail pages. Links now go to
`/join/account/` and `/join/volunteer/` as appropriate. See
[three-paths-to-participate.md](./three-paths-to-participate.md).

## Related

- [three-paths-to-participate.md](./three-paths-to-participate.md) — **current** Join design
- [entry-points-and-conversion.md](./entry-points-and-conversion.md) — intent inventory
- `docs/projects/forge-issues/` — sync proven; presentation next
