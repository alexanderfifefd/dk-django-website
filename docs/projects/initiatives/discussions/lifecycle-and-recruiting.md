# Discussion: lifecycle and recruiting

**Date:** 2026-08-14
**Builds on:** [initiatives-as-a-noun.md](./initiatives-as-a-noun.md), `docs/organizational-context.md`
**Status:** decisions recorded — content model in prototype 07; recruiting UI deferred (2026-08-14)

## The question

Prototype 07 mixes **lifecycle** (where is this thing in its existence?) with **recruitment** (do we
want people to join?) in single enums — `stage` on systems, `status` on initiatives. That breaks down
when a production system needs maintainers, or when an active initiative could still welcome help.

Should recruitment be a separate dimension, shared across both nouns?

## Problem with the current model

| Thing | Lifecycle field | Recruitment today | Gap |
|---|---|---|---|
| Terms of service (no taker) | `seeking-contributors` | bundled into status | conflates goal progress with hiring |
| Listmonk (system idea) | `stage: suggestion` | bundled into stage | "suggestion" also implies recruitment |
| Matrix in production, understaffed | `stage: production` | nowhere to express it | org context wants stewardship gaps visible |

`seeking-contributors` on initiatives and `suggestion` on systems are doing double duty. Recruitment
should not be initiative-only.

## Decision: two independent dimensions

### 1. Lifecycle

**Systems** — software maturity (rename `suggestion` → `idea`):

| Stage | Meaning |
|---|---|
| `idea` | We think this software should exist; not building yet |
| `development` | Actively being built |
| `production` | Operating |

**Initiatives** — goal progress (drop `seeking-contributors` from status):

| Status | Meaning |
|---|---|
| `proposed` | Pitched; may still need clarification or approval |
| `active` | Work underway |
| `paused` | Stalled or deprioritised |
| `completed` | Goal met or explicitly closed |

(`proposal` may be renamed to `proposed` for parity with system `idea`.)

### 2. Recruiting — shared field on both nouns

Optional frontmatter on systems and initiatives:

```yaml
recruiting: open
```

| Value | Meaning |
|---|---|
| *(omitted)* | Not actively looking for people (default) |
| `open` | Actively looking for taker(s) — advertise on index pages |

Start with this single active value. Finer roles (`lead`, `contributors`, `maintainers`) can be added
later if copy on the site needs to distinguish them.

Forge labels like `seeking-maintainer` stay **observed** signals from the forge. `recruiting` is an
**authored** collective statement on the site. They may agree; they are not the same field.

## Site surfaces

Index pages group by lifecycle:

- **Initiatives** — active, then proposed, then completed and paused.
- **Systems** — production, then development, then ideas.

### Recruiting UI — deferred

The `recruiting: open` field is in the content model and syncs to the ORM. **Surfacing it on the site
is not implemented yet.** A plausible future layout (to explore later):

1. **Main list** — lifecycle groups as above.
2. **Looking for takers** — a lower band on index pages (and possibly home) filtering
   `recruiting: open`, presented more lightly than underway work.

Detail-page badges are likewise deferred. Seed content may still set `recruiting: open` so the shape is
ready when presentation is picked up.

## Examples

**Terms of service** (initiative):

```yaml
status: active
takers: []
recruiting: open
```

**Listmonk** (system idea):

```yaml
stage: idea
recruiting: open
```

**Matrix** (live, wants maintainers):

```yaml
stage: production
recruiting: open
```

## Supersedes

- **Open areas yaml** — deferred in [initiatives-as-a-noun.md](./initiatives-as-a-noun.md); concrete
  pitches with `recruiting: open` cover the same intent without a third abstraction.
- **`seeking-contributors` initiative status** — replaced by `recruiting: open` plus lifecycle status.
- **System `suggestion` stage** — rename to `idea`; recruitment no longer implied by stage alone.

## Open after this decision

- Recruiting presentation on home, index pages, and detail pages (see **Recruiting UI — deferred**
  above).
- Whether `proposed` + `recruiting: open` should warn at sync time.
