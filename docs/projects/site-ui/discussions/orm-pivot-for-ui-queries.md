# Discussion: ORM pivot for UI queries

**Follow-up to:** [ui-without-ingest.md](./ui-without-ingest.md)
**Date:** 2026-08-12

## What changed

The prototype shipped with per-request parsing (`pages/content.py`, dataclasses, no ORM). That worked for
bootstrapping pages and real content, but UI features accumulated quickly — system leads on the members
index, org groups, org roles — and each one added manual query helpers that reimplemented what Django
already provides (`related_name`, `prefetch_related`).

We moved back to the **integration-layer pattern**: derived ORM tables, ingest under `pages/sources/`,
save–reload preserved via **dev middleware** that runs `sync_content` on every request.

`pages/content.py` was deleted. Views now query models directly.

## Decision

**ORM + auto-sync in dev.** Markdown in git remains the source of truth; the database is derived and
disposable. Authors still edit files and reload — no manual `sync_content` step during normal UI work.

Manual sync remains available: `uv run python manage.py sync_content` (or `--flush`).

Sync errors in dev render as a plain HTML error page (middleware), not a silent 500.

## Content extensions since launch

Beyond the original four nouns:

- **Org groups** — `content/members/groups.yaml` defines group slugs and titles (`board`, `maintainers`).
  Membership assigned on each member file: `groups: [board, maintainers]`.
- **Org role** — optional `role:` on member frontmatter (e.g. `Styreleder`, `Technical Coordinator`).
  Separate from per-system `teamlead` / `admins`.
- **Member slugs** — lowercase nick, filename = slug (`alexanrf.md` → slug `alexanrf`). Display `name`
  in frontmatter.

Real collective data is in place: 9 members, 5 systems (Keycloak, Matrix, Loomio, Forgejo, Website), 1
article. Placeholder content from early prototyping was removed.

## What we learned

- Skipping the ORM saved bootstrap time but **did not save UI time** once relationships mattered.
  The manual loader grew to ~320 lines and a new helper per query pattern.
- Total ingest code is comparable to prototype 03 (~430 lines in `sources/`), but views and templates
  stay thinner with the ORM.
- The hybrid (ORM + per-request sync in dev) is the workable compromise: no sync ceremony, normal
  Django queries for UI work.

## Considerations for continuing UI work

**In scope for this prototype**

- Typography, layout, information hierarchy on system/member/article pages
- More real content (bios, updates, articles)
- Group/role presentation — badges, ordering, prominence
- Home page composition (what to surface above the fold)

**Still deferred**

- Forge issues/PRs and identity linking (`git-identity`, `forge-issues`)
- Member `identities` map in frontmatter
- Admin, auth, pagination, search, deployment
- Production sync policy (deploy-time ingest vs webhook) — dev middleware is not for prod

**Schema may still move**

- Groups are a model + M2M today; fine to keep or collapse to JSONField if group pages never materialise
- Updates still JSONField on `System` — promote to a table only if cross-system update queries become real

**Authoring gotchas**

- Member slugs must be lowercase; macOS case-insensitive filesystem can bite renames — use a two-step
  rename (via temp name) if changing case
- Unknown group slugs or member references fail sync loudly — fix the file, reload
- Sync order: groups → members → systems → articles

## Related prototype files

```
prototypes/06-site-ui/
  content/
    members/<slug>.md, groups.yaml
    systems/<slug>/system.md, updates.json
    articles/<slug>.md
  pages/
    models.py
    sources/          # groups, members, systems, updates, articles, sync
    middleware.py     # ContentSyncMiddleware (DEBUG)
    views.py          # ORM queries
```

First-time setup: `uv sync`, `cd prototypes/06-site-ui`, `migrate`, `runserver`.
