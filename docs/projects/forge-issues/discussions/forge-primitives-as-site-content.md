# Discussion: forge primitives as site content

Brainstorm, 2026-08-07; decisions taken 2026-08-08 — see the end. Recorded so the reasoning survives
past the first collection.

## The lens

The site serves two audiences: non-technical users (is it working, what changed, what's coming) and
prospective maintainers (is this alive, where could I fit). And it has a shaping role: **the site is the
reward for forge hygiene**. If release notes render on the homepage, people write release notes; if
milestones render as a roadmap, work gets grouped into milestones. We're too early for formal process,
so the selection criterion is: primitives where the hygiene cost is low and the display payoff is
visible. Displaying a primitive *is* choosing a workflow.

## The primitives

| Primitive | Answers | For whom | Hygiene cost |
|---|---|---|---|
| Issues (operational) | is it working / what's known-broken | users | labels only |
| Issues (`help wanted`) | where could I fit | future maintainers | labels only |
| Pull requests | is work actually happening | future maintainers | none — activity is the signal |
| Releases | what changed | both | writing notes (which *is* the content) |
| Milestones | what's coming | both | real planning must exist first |
| Projects (kanban) | who's doing what today | nobody outside the team | constant gardening |

- **Issues** are the big one — the first API source, already in flight.
- **Pull requests** are the raw alive-ness signal. They carry labels, so `system/<slug>` scopes them
  like issues, and they arrive through the same API endpoint (`type=pulls`) — mechanically almost free.
  Low value to non-technical users as items, but strong as a pulse: "3 PRs merged on Atlas this week".
  Display aggregate activity, not PR titles.
- **Releases** are the natural collection #2: the only primitive that is already outward-facing, a list
  endpoint with `tag_name` as natural key, and the process they encourage (write a paragraph when you
  ship) is one we want anyway. A release note can *be* the announcement — no separate blog post.
- **Milestones** wait until planning is real. A milestone with three issues and no due date renders as
  an embarrassing roadmap. When used: at most one "roadmap card" per system (title, due date, progress
  bar) — the cap forces the healthy curation decision of which milestone is *the* current one.
- **Projects/kanban** never render on the site. Internal coordination, high gardening cost, and a stale
  public board is worse than none.

## The monorepo fault line

The primitives split by what scopes them, and the monorepo only supports one side:

- **Label-scoped: issues and pull requests.** `system/<slug>` assigns them to a system. These survive
  the monorepo cleanly.
- **Repo-scoped: milestones and releases.** A milestone or release belongs to the repository, so in a
  monorepo it cannot belong to a system. Tag conventions (`atlas-v1.2`) could fake it for releases, but
  that's hygiene cost of exactly the kind we're trying to avoid.

So the monorepo may simply not be granular enough for what we want to lift up. If releases or
milestones earn a place on the site, that is probably the moment the monorepo becomes repo-per-system —
where both scope naturally, and where CODEOWNERS-style team boundaries (see the organizational context)
land better anyway. Unresolved; the issues prototype doesn't force it. We'll see.

## Surfaces these point at

- **System timeline**: updates, releases, and closed incident issues merged into one reverse-
  chronological "what's been happening" feed per system.
- **Get involved**: `help wanted` issues across all systems — the deliberate funnel from reader to
  forge thread to first contribution. Likely the highest-leverage page for maintainer recruitment.
- **Pulse**: aggregate PR/issue activity as an alive-ness strip on home and system pages.
- **Status badge** (toy, deferred): an open `incident`-labeled issue flips the system's badge amber.
  Gives labels semantics — only if the rendered page begs for it.

## Open after prototype 04

Presentation is unresolved. The sync and minimal list rendering are proven; the site UX is not. Particular
threads:

- **Prominent forge labels** — tags like `seeking-maintainer` or `help wanted` lifted out of the tag row
  and surfaced prominently (system page header, get-involved strip, home callout).
- **Which labels earn semantics** — convention to define in the monorepo vs presentation logic in Django;
  prototype 04 treats all non-system labels as inert tags.
- **Layout and surfaces** — get-involved page, system timeline, pulse vs lists — see Surfaces above.
  Prototype 04 kept single-column lists on purpose; design is a later prototype.

## Decisions (2026-08-08)

- **Issues and pull requests both go into prototype 04.** Same labels, same endpoint, one sync. Issues
  attract engagement; PRs communicate alive-ness. The plan is amended accordingly.
- **PR presentation (amended during build):** item lists with open/closed badges, not aggregate pulse.
  The pulse idea from the brainstorm was simpler to skip for now.
- **Releases deferred.** PR lists say "things ship" well enough for now, and a release *announcement*
  is an authored update in any case (see "Two voices" in the organizational context) — which also
  sidesteps releases being repo-scoped in the monorepo.
- **Milestones and projects: out at this stage**, as argued above.

## How states render

The state machine is small — issues are open/closed, PRs are open/merged/declined — but each state
lands differently depending on the audience:

| State | Renders as | Serves |
|---|---|---|
| Issue, open | "known issues" on its system page; `help wanted` also on the get-involved surface | honesty (users), entry points (maintainers) |
| Issue, closed | leaves the lists; feeds a resolved count ("12 resolved this month") | responsiveness (users) |
| PR, open | a list item with an "open" badge | work in flight (maintainers) |
| PR, merged | a list item with a "closed" badge | alive-ness (both) |
| PR, closed unmerged | nothing | — |

Declined PRs deliberately render nowhere. Item-level rejection display would publicly shame one-off
contributors — exactly the people the funnel exists to attract — and a "declined" aggregate helps no
audience. They still become rows (ingest-anyway, like unlabeled issues); the admin can see them.

The audience split in one line: **users read states as a reliability narrative** (honest open issues,
resolved counts, authored updates in the collective's voice); **prospective maintainers read them as an
activity narrative** (PR lists, help-wanted entry points). Same rows, two framings — which is the
argument for keeping presentation logic in views and templates, not in the sync.
