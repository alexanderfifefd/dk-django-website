# Discussion: org groups on the site

**Date:** 2026-08-14
**Builds on:** `docs/projects/site-ui/`, `docs/organizational-context.md`, [initiatives](../initiatives/overview.md)
**Prototype:** `prototypes/07-initiatives/` only — **no separate groups prototype** (pass on 07)
**Status:** decisions recorded — see [plan](../plans/2026-08-14-three-org-groups.md)

## The question

The site already has a stub **Group** model: `content/members/groups.yaml` defines slugs and titles;
member profiles assign `groups: [...]`. Today only **Board** and **Maintainers** exist; Board is listed
on the About page; both appear as inline text on the members index and member detail pages.

How far should we take group **presentation** — and which three groups define membership in the
collective for now?

## What we considered and deferred

A longer-term idea: **interest groups** (frontend, devops, administrators, …) as first-class pages with
Matrix rooms — an easier recruitment funnel than system-specific maintainer channels alone. Matrix stays
central to the member journey; some rooms may be open before full membership.

**Decision (2026-08-14): do not prototype that now.** The collective is still starting up; the website
is a tool for clarifying how we think, but publishing many affinity groups risks **over-departmentalizing**
too early. Personas we want to recruit can be **called out in prose** (articles, Join, initiative pitches)
and people can land in **shared Matrix rooms** for now — without a separate group noun or index on the site.

That exploration may return as a later project if the org stabilises and dedicated rooms deserve pages.

## Decision: three org groups

One vocabulary — the existing `Group` model — for **organizational belonging**, not skill silos:

| Slug | Title | Meaning |
|---|---|---|
| `board` | Board | Governance and collective-level decisions |
| `maintainers` | Maintainers | Everyone involved in building and running the collective |
| `moderators` | Moderators | People who moderate collective spaces (e.g. Matrix rooms) |

**Maintainers** is the broad group: if you're actively involved, you're a maintainer. **Moderators** is
narrower and specific. **Board** is governance; overlap with maintainers is expected (board members are
maintainers too).

Membership stays **authored on member profiles** (`groups: [board, maintainers, …]`). Assign **explicitly**
only — no default of `maintainers` for every active member. No group creation form. No Matrix membership
sync in scope.

## Content shape

Group definitions carry enough context to render a useful section on the Members page — not just a title:

```yaml
# content/members/groups.yaml
board:
  title: Board
  summary: Governance and collective-level decisions for the collective.
  matrix: "#board:datakollektivet.no"

maintainers:
  title: Maintainers
  summary: Members actively building and running the collective — systems, initiatives, and infrastructure.
  matrix: "#maintainers:datakollektivet.no"

moderators:
  title: Moderators
  summary: Moderation across Matrix rooms and other collective spaces.
  matrix: "#moderators:datakollektivet.no"
```

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Display name |
| `summary` | no | One-line description for the group section header |
| `matrix` | no | Room address for the group's main Matrix space |

Matrix room addresses are placeholders until real rooms exist; they are the primary join path for each
group on the site. Same pattern as initiative/system frontmatter — authored link, not synced membership.

## Site surfaces (decided)

**Option B — Members-centric, sections per group.**

- **`/members/`** — intro explaining the three groups; **one section per group** (Board, Maintainers,
  Moderators) with summary, Matrix link, and member list. Anchor ids for deep links (`#board`,
  `#maintainers`, `#moderators`).
- **`/about/`** — remove the inline Board member list; replace with a short pointer to `/members/#board`
  (and optionally Maintainers / Moderators). About stays governance narrative; Members is the directory.

Member detail pages keep inline group labels; no group detail URLs in this pass.

## Relationship to other nouns

```
Member
  └─ groups → Board | Maintainers | Moderators  (org belonging)

Group (groups.yaml)
  └─ summary, matrix  (presentation + join path)

System / Initiative
  └─ matrix in frontmatter  (service- or goal-specific rooms)

Deferred interest personas
  └─ prose + shared Matrix rooms  (not group pages yet)
```

Systems and initiatives keep their own coordination links. Org groups answer *what kind of member are
you in the collective structure* — not *what stack do you work on*.

## Seed membership (explicit assignments)

Documented in the plan. Moderators start empty in production terms — plan seeds **three members** with
no board or system roles for prototype content: `hallvord`, `papiris`, `tormod`.
