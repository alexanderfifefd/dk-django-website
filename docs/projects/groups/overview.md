# Groups

**Question:** How should we present the collective's **org groups** — Board, Maintainers, Moderators —
on the site, using the existing `Group` model and `groups.yaml` vocabulary?

**Status:** Built (2026-08-14).

**Builds on:** [site-ui](../site-ui/overview.md), [initiatives](../initiatives/overview.md)

## Prototype mapping

| | |
|---|---|
| **Work in** | `prototypes/07-initiatives/` |
| **Separate prototype?** | **No.** There is no `08-groups/` directory. |
| **Relationship to 07** | A **pass on the initiatives prototype** — same Django project, same `content/`, same `pages/` app. |

When orienting or running commands for this project, use **prototype 07 only**:

```bash
cd prototypes/07-initiatives
uv run python manage.py runserver
```

Code and content touched by this project include `content/members/groups.yaml`, `pages/sources/groups.py`,
`pages/models.py` (`Group`), members/about templates, and migration `0007_group_summary_matrix`.

The [initiatives](../initiatives/overview.md) project owns the 07 fork; **groups** adds org-group
presentation on top of that baseline without forking again.

## Summary

Three org groups: **Board**, **Maintainers**, **Moderators**. Group definitions include **summary** and
**matrix** for nicer section headers and join paths. **Members index** is the primary surface — one
section per group with anchors. **About** points to Members instead of listing the board inline.
Membership on profiles is **explicit only**. Interest-based persona groups remain deferred.

## How to read this project

1. [org-groups-on-the-site.md](./discussions/org-groups-on-the-site.md) — decisions and content shape
2. [2026-08-14-three-org-groups.md](./plans/2026-08-14-three-org-groups.md) — build plan and outcome

## Related docs

- `docs/organizational-context.md`
- `docs/projects/site-ui/discussions/orm-pivot-for-ui-queries.md` — original groups ingest (prototype 06)
