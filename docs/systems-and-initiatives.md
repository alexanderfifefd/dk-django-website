# Systems and initiatives

How the collective organizes work on the site — the two nouns that drive most of what visitors see
and what members commit to.

See also `docs/organizational-context.md` for participation paths, recruitment signals, and the wider
noun list.

## Two questions

| | **System** | **Initiative** |
|---|---|---|
| **Answers** | *What do we operate?* | *What are we trying to accomplish?* |
| **What it is** | Software or a service the collective runs | A goal someone drives forward — not always technical |
| **Shape** | Long-lived; teamlead + admins | Goal-oriented; one or more **takers** |
| **Examples** | Keycloak, Matrix, Forgejo, Website | Governance documents, terms of service, build SSO |
| **Outcome** | A running service | A decision made, a doc written, a system shipped, a habit established |

Systems are the **inventory of what we maintain**. Initiatives are how we **lift up work in progress**
so others can see it, weigh in, or volunteer — before and while it becomes (or without becoming) a
system.

## System

A **system** is software the collective maintains for its members and users. On the site it has a
description page, accountable **teamlead**, **admins**, operational **updates**, and related
**articles**.

**Lifecycle** (`stage`) describes software maturity — not recruitment:

| Stage | Meaning |
|---|---|
| `idea` | We think this should exist; not building yet |
| `development` | Actively being built |
| `production` | Operating |

**Recruitment** is separate: optional `recruiting: open` in frontmatter when the collective needs
maintainers — an authored statement, not implied by stage alone.

Forge **issues** and **pull requests** scoped to a system (via labels) show what's broken and that
work is happening — observed activity, not authored copy.

## Initiative

An **initiative** is something members want to *make happen* — governance, onboarding, shipping a
new service, cross-cutting process. It may be non-technical and may never become a system.

On the site it has a pitch page, **taker(s)**, optional links to related **systems**, authored
**updates**, and optional **Loomio** / **Matrix** coordination links.

**Lifecycle** (`status`) describes goal progress:

| Status | Meaning |
|---|---|
| `proposed` | Pitched; may still need clarification or approval |
| `active` | Work underway |
| `paused` | Stalled or deprioritised |
| `completed` | Goal met or explicitly closed |

Like systems, **`recruiting: open`** is an optional separate field when we need a driver or
contributors — not bundled into status.

Initiatives exist to:

1. **Clarify** — surface a proposal before work starts.
2. **Recruit** — show that help is welcome and who to talk to.
3. **Coordinate** — point to where discussion happens.

## How they relate

```
Initiative
  ├─ may land in → System     (outcome is a running service)
  ├─ may span → System(s)     (cross-cutting work)
  └─ may have no system       (content, process, governance)

System
  └─ may be referenced by → Initiative(s)
```

An initiative to "build SSO" and the Keycloak **system** are related but not the same thing: the
initiative carries the goal and recruitment; the system carries operational truth once it runs.

**Articles** can link to either or both. **Updates** belong to systems (operational notices). Initiative
progress uses initiative-scoped updates.

## Participation and recruitment

Both nouns can carry `recruiting: open` when the collective needs people. That is a **stewardship**
signal — we need a maintainer or taker — distinct from forge **`help wanted`** on a specific task.
See [Recruitment signals](organizational-context.md#recruitment-signals) in organizational context.

- **System page** — local next steps: teamlead, future help-wanted issues, link to account / volunteer paths.
- **Initiative page** — taker, Loomio/Matrix, same participation paths.
- **Volunteer path** — open stewardship roles (`recruiting: open`) aggregated for discovery.

## Site presentation

Systems and initiatives each have index pages grouped by lifecycle, detail pages, and a place on the
home page. They are first-class navigation — the primary way outsiders see what the collective operates
and what it is pushing forward.

Implementation: `docs/projects/initiatives/` (prototype 07). Systems began in
`docs/projects/site-ui/`; initiatives extended the model on the same prototype.
