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

- **Member**: a person in the collective. Identity is owned by Keycloak (prototypes: a Keycloak-shaped
  fixture); Django caches a lightweight profile. Nothing in git creates a member.
- **System**: software the collective maintains. Has a marketing/description page, one **teamlead**
  (single accountable person), several **admins**, operational updates, and related articles.
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
