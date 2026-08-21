# Initiatives

**Question:** How should we represent initiatives — goal-oriented efforts someone drives forward, not
necessarily tied to a single system — in the site's information architecture and content model?

**Status:** In progress — prototype 07 forked from 06 (2026-08-13); lifecycle/recruiting split
(2026-08-14). See [lifecycle-and-recruiting.md](./discussions/lifecycle-and-recruiting.md).

**Prototype:** `prototypes/07-initiatives/`

**Also on this prototype:** [groups](../groups/overview.md) — org-group presentation (no separate fork).

**Builds on:** [site-ui](../site-ui/overview.md) (prototype 06)

## Summary

Core definitions: **`docs/systems-and-initiatives.md`**. This project implements them in prototype 07.

Systems are *what we operate*; initiatives are *what we're trying to accomplish*. An initiative has
taker(s), lifecycle **status**, optional **recruiting**, optional related systems, authored updates, and
optional Loomio/Matrix links. Articles can link to an initiative and/or a system. Index pages group by
lifecycle (initiatives: active → proposed → completed/paused; systems: production → development →
ideas). The shared `recruiting: open` field syncs from git; **recruiting UI** is implemented by the
[member-journeys](../member-journeys/overview.md) project (2026-08-14). Forge activity stays
system-scoped.

## How to read this project

1. [initiatives-as-a-noun.md](./discussions/initiatives-as-a-noun.md) — definitions and decisions
2. [lifecycle-and-recruiting.md](./discussions/lifecycle-and-recruiting.md) — lifecycle vs recruiting split
3. [2026-08-13-prototype-07-initiatives.md](./plans/2026-08-13-prototype-07-initiatives.md) — **plan and
   build checklist**

## File index

### Discussions

| File | Summary |
|---|---|
| [initiatives-as-a-noun.md](./discussions/initiatives-as-a-noun.md) | Initiative vs system, updates, status model, nav, decisions |
| [lifecycle-and-recruiting.md](./discussions/lifecycle-and-recruiting.md) | Split lifecycle from recruiting; shared `recruiting: open` field |

### Plans

| File | Summary |
|---|---|
| [2026-08-13-prototype-07-initiatives.md](./plans/2026-08-13-prototype-07-initiatives.md) | Prototype 07 scope, content model, success criteria |

## Related docs

- **`docs/systems-and-initiatives.md`** — core model (authoritative)
- `docs/organizational-context.md`
- `docs/projects/site-ui/` — prototype 06 baseline (unchanged)
