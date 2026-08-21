# Discussion: initiatives as a site noun

**Date:** 2026-08-13
**Builds on:** `docs/systems-and-initiatives.md`, `docs/organizational-context.md`
**Status:** decisions recorded (2026-08-13) — status/stage vocabulary superseded for prototype 07 by
[lifecycle-and-recruiting.md](./lifecycle-and-recruiting.md) (2026-08-14). See also
[plan](../plans/2026-08-13-prototype-07-initiatives.md) and `prototypes/07-initiatives/`

## The question

How should we represent **initiatives** — non-technical or cross-cutting efforts someone drives forward
("We should do this!") — in the site's information architecture and content model, alongside the existing
nouns (systems, members, articles, updates)?

All site copy, slugs, and content files use **English**.

## Why this isn't a system

Prototype 06 presents **systems** as software the collective maintains: a running service with a
teamlead, admins, operational updates, and a lifecycle stage (`suggestion` → `development` →
`production`).

An **initiative** is a different kind of thing:

| | System | Initiative |
|---|---|---|
| **What it is** | Software/service the collective runs | Something someone wants to *make happen* |
| **Shape** | Long-lived, has teamlead/admins | Goal-oriented, has initiative taker(s) |
| **Examples** | Keycloak, Matrix, Website | Governance documents, Build SSO, Build website |
| **Technical?** | Always (by definition) | Not necessarily — can be content, process, cross-cutting |
| **Outcome** | A running service | A decision made, a doc written, a system shipped, a workflow established |

Systems answer *what do we operate?* Initiatives answer *what are we trying to accomplish, and who is
driving it?*

## What an initiative is for

An initiative exists to **lift work up** so people can see what is happening and get involved:

1. **Clarification** — surface a proposal so others can object or support it before work starts.
2. **Recruitment** — make it obvious that more people are welcome (and who to talk to).
3. **Communication** — establish where discussion and coordination happen (Loomio, Matrix, meetings).

## Relationship to existing nouns

```
Initiative (goal, driven by person)
  ├─ may land in → System (when the outcome is a running service)
  ├─ may span → System (M2M — cross-cutting work)
  ├─ may have no system (content, process, governance)
  ├─ has → Update (authored notices — same JSON shape as system updates)
  └─ discussed on → Loomio (primary); Matrix for day-to-day coordination

Article (authored prose)
  ├─ can link to → Initiative
  └─ can link to → System (existing optional FK)

Update (operational notice)
  ├─ scoped to → System (unchanged)
  └─ scoped to → Initiative (same `{date, kind, message}` records in updates.json)

Forge issue/PR (observed activity)
  └─ scoped to → System via `system/<slug>` label (unchanged)
```

### Articles

Articles have optional `system` and optional `initiative` FKs. An article about *why* we're building SSO
links to the initiative; an article about *how Keycloak federation works* links to the system. Both can
be set when the article spans initiative context and a specific system.

### Updates

Updates are **authored notices** — the collective choosing to say something. They already live beside
systems as `updates.json`. Initiatives use the same format at `content/initiatives/<slug>/updates.json`.

System updates remain for operational notices about a running service ("Keycloak downtime Saturday").
Initiative updates cover progress on the goal ("Governance draft ready for review", "Homepage prototype
shipped"). Same ingest shape, different scope.

### Initiative ↔ system overlap

Initiatives and systems can coexist for the same work (e.g. *Build website* + Website system). When they
diverge depends on context.

**Working assumption:** once a related system reaches **production**, the initiative that drove getting it
there is usually **completed**. Ongoing maintenance belongs on the system page. Before production, both
pages may be relevant: the initiative carries pitch and recruitment; the system carries technical
structure.

## Issues and PRs: not for initiatives

Forge issues and pull requests stay **system-scoped** via `system/<slug>` labels. The monorepo is the
systems workspace; initiatives have no forge home. Initiative progress is visible through status, updates,
articles, and external discussion links.

## Loomio and Matrix

**Loomio** for proposals and non-technical discussion. **Matrix** for day-to-day coordination. Optional
URLs in frontmatter; no ingest in prototype 07. Caching external activity deferred.

## Open areas ("help wanted" domains)

Broad invitations where the collective is open to someone *starting* work in a space — deferred. One
future approach: `content/initiatives/open-areas.yaml` rendered as a "Want to start something?" section.

## Content shape

```
content/initiatives/<slug>/
  initiative.md
  updates.json          # optional; same shape as system updates
```

### Frontmatter

```yaml
title: Governance documents
summary: Establish governance documents for the collective.
status: active
start_date: 2026-07-01   # required
end_date: 2026-12-01     # optional — omit while ongoing
takers: [daniel]
systems: []
loomio: https://loomio.datakollektivet.no/...
matrix: "#governance:datakollektivet.no"
```

### Status vocabulary

| Status | Meaning |
|---|---|
| `proposal` | Pitched, seeking clarification |
| `seeking-contributors` | Approved in principle; actively recruiting |
| `active` | Work underway with taker(s) driving it |
| `paused` | Stalled or deprioritised |
| `completed` | Goal met or explicitly closed |

## Site surfaces

| Page | URL | Notes |
|---|---|---|
| Initiatives index | `/initiatives/` | All initiatives with status badges |
| Initiative detail | `/initiatives/<slug>/` | Pitch, takers, status, systems, links, updates, articles |

**Navigation:** Systems and Initiatives on the **left** side of the header; Articles, About, Join on the
right.

**Home:** surface active and seeking-contributors initiatives alongside systems and articles.

**Member detail:** show initiatives led (`initiatives_led`).

**Authoring:** git only — no initiative creation form on the site.

## Seed content (prototype 07)

| Slug | Title | Status | Systems |
|---|---|---|---|
| `governance-documents` | Governance documents | `active` | — |
| `build-sso` | Build SSO | `completed` | keycloak |
| `build-website` | Build website | `active` | website |

## Out of scope for prototype 07

- Open areas yaml
- Forge issues/PRs on initiative pages
- Loomio/Matrix activity ingest
- Initiative creation form
- Auth, deployment

## Decisions (2026-08-13)

- **Initiatives are a first-class authored noun**, synced from `content/initiatives/<slug>/`.
- **Updates** use the same JSON shape on initiatives and systems.
- **Status values:** `proposal`, `seeking-contributors`, `active`, `paused`, `completed`.
- **Forge issues/PRs stay system-scoped.**
- **Articles** gain optional `initiative` FK.
- **Navigation:** Systems + Initiatives on the left.
- **English** for slugs and site copy.
- **No initiative creation form** — git authoring only.
- **Prototype:** `07-initiatives`, forked from `06-site-ui`; prototype 06 unchanged.

## Open after prototype 07

- Whether `proposal` initiatives need different index prominence.
- Validation: require non-empty `takers` for certain statuses?
- Open areas surface when recruitment domains are ready to be first-class.
