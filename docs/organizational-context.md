# Organizational context

What the site actually is, so the data model has something real to mirror.

## The collective

A software collective maintains a set of **systems** — services and software — for its **members**. The
site is the collective's homepage: it presents the collective, markets each system, surfaces operational
updates, and carries a blog. Members market, give updates about, and communicate about the systems.

## What the site is trying to do

Make the collective's work legible from outside — and let that visibility do quiet process work inside.
The stories the site is designed around:

- **Trust a system.** A potential user judges a system by its page: what it is, who is accountable,
  what is known-broken, and whether things get fixed.
- **Stay informed.** Someone affected by downtime or a release finds an authored notice in a
  predictable place, in the collective's voice — not by reading an issue tracker.
- **See that it's alive.** A visitor wondering "is this maintained?" sees recent merged work at a
  glance, without knowing their way around a forge.
- **Scratch an itch.** A developer with a one-off bug or fix lands, via the site, directly in the right
  forge thread — the site is a funnel into contribution, not a destination.
- **Find a place.** A prospective maintainer sees where help is wanted and which systems are looking
  for people. Stewardship gaps are advertised, not hidden.
- **Converge on a workflow.** Members are disparate and async, and there is no formal process yet. The
  site rewards forge hygiene — label it right and it appears on the site — nudging everyone toward the
  same light workflow without writing a rulebook.

The collective runs on **participation**, not passive sign-ups. The site separates *having an identity*,
*belonging to the org*, and *taking on work* — see [Paths to participate](#paths-to-participate) below.

**Systems** and **initiatives** are how work is organized on the site — what we operate vs what we are
trying to accomplish. See [`docs/systems-and-initiatives.md`](systems-and-initiatives.md).

## Paths to participate

Three distinct ways someone enters. They share an SSO **account** as the technical front door, but they
are not the same commitment:

| Path | Who | What they get |
|---|---|---|
| **Account** | Everyone | One identity (Keycloak / SSO). Access to Forgejo, Loomio, Matrix, and other free-tier collective services. No fee; not org membership. |
| **Member** | People joining the org | Voting rights, full Loomio participation, member obligations. Carries a fee. Assumes an account already exists. |
| **Volunteer** | People taking on work | Moderation, technical maintenance, driving initiatives — real responsibility, usually with a light agreement. Assumes an account; distinct from paying for membership. |

On the site, **Join** is the chooser for these paths — account creation, membership (and payment), and
volunteer application are separate flows. Implementation details and prototype status live in
`docs/projects/07-member-journeys/`.

A maintainer and a member both need an account first. Volunteering to steward a system is not the same
as becoming a member, and neither is implied by registering.

## Recruitment signals

"Help wanted" is not one thing. The site distinguishes:

| Signal | Source | Meaning |
|---|---|---|
| **`recruiting: open`** | Authored (system or initiative frontmatter) | Collective statement: we need a **driver, maintainer, or taker** |
| **`help wanted` (forge label)** | Observed (forge issue) | A **specific task** is open — natural thread to join |
| **Loomio link** | Authored (often on initiatives) | **Input wanted** on a decision — not necessarily "own this" |

**Input wanted ≠ maintainer wanted.** A Loomio poll and a stewardship gap should not share one badge.

- **Stewardship gap** — needs a person → `recruiting: open`, teamlead/taker, volunteer path.
- **Task gap** — needs work done → forge issue with `help wanted`; lower-commitment entry.

System and initiative pages answer *what can I do here?* locally (teamlead, taker, future help-wanted
issues). Open stewardship roles also appear on the volunteer path. See
[`docs/systems-and-initiatives.md`](systems-and-initiatives.md) and
`docs/projects/07-member-journeys/discussions/help-wanted-and-recruiting.md`.

## Two voices

Site content divides by who is speaking, and the split is deliberate:

- **Authored** — updates and articles. Written for readers on purpose; the collective *speaking*. A
  downtime window or a release announcement is an authored update even when the underlying event lives
  in the forge.
- **Observed** — issues and pull requests. Work exhaust cached from the forge; the collective *seen
  working*. The site filters and frames it, never edits it.

The delineation cuts both ways: things users must know get written as updates (nobody should have to
read a tracker to learn about Saturday's downtime), and work-in-progress stays in the forge (nobody
hand-copies it into content files).

HUMAN NOTE: This goes for more systems as well. E.g. work on Loomio. We're discussing the forge here, but there could be other systems where work is done or activity is done. Or even just "10 people in this Matrix maintainer chatroom"

## The nouns

- **Account**: an identity in the collective's SSO (Keycloak). Everyone who uses Forgejo, Loomio,
  Matrix, or other collective tools has one. An account is **not** org membership — it is the shared
  technical front door. See [Paths to participate](#paths-to-participate).
- **Member**: a person with **org membership** in the collective — voting rights, member obligations,
  usually a fee. Profile authored in git as
  `content/members/<slug>.md` — the filename is the canonical slug for cross-references (`teamlead`,
  `author`, etc.). Frontmatter carries a display `name` and an `identities` map linking to external
  accounts (forge, Matrix, …). Django ingests and caches the profile; forge activity links via
  `identities.forgejo`, not via SSO. See `docs/projects/05-git-identity/`.
- **System**: software the collective maintains — teamlead, admins, updates, lifecycle stage. See
  [`docs/systems-and-initiatives.md`](systems-and-initiatives.md#system).
- **Initiative**: a goal members drive forward — taker(s), status, optional related systems, coordination
  links. See [`docs/systems-and-initiatives.md`](systems-and-initiatives.md#initiative).
- **Update**: a short operational notice scoped to one system ("downtime expected Saturday", "2.0 is
  out"). Authored deliberately for the system's users — the collective choosing to say something.
  Record-like data, not prose.
- **Issue**: a unit of work or discussion in the forge — bug, request, task — scoped to a system by
  label. Forge-owned; the site caches and surfaces it for honesty about what's broken and where help
  is wanted.
- **Pull request**: a proposed change in the forge, labeled like issues. Surfaced as aggregate
  activity — the alive-ness signal — not as items to read.
- **Article**: a blog post by a member — about one system, or collective-wide when it names none.

## How collaboration works

Through git pushes, not CMS accounts. Anyone in the collective edits content in the repo; review happens
in the forge. Roles carried in the data (teamlead, admins) are presentation today and the seed of
authorization later — e.g. CODEOWNERS on a system's content folder, or Django-side permission checks once
Keycloak is wired up for real. Out of scope for the prototypes.
