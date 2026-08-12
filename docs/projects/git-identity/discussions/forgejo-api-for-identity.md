# Forgejo API for Identity Linking

**Question:** What does the Forgejo API expose for users and authorship, and does it support the git-backed identity approach for prototype 05?

Explored against [forge.hornwitser.no](https://forge.hornwitser.no) (Forgejo 16.0.2), using `alexanrf` and the `alexanrf/public-api-test-repo` test repo.

## User profile — `GET /api/v1/users/{login}`

Relevant fields:

| Field | Notes |
|---|---|
| `id` | Stable numeric Forgejo user ID. Best key if handles change. |
| `login` / `username` | Human-readable handle. What prototype 04 stores as `author`. |
| `html_url` | Link back to the forge profile — useful for external contributors. |
| `source_id` / `login_name` | SSO hook points; empty on local accounts, may populate for OIDC users. Not portable across services. |
| `email` | Noreply address on this instance; not useful for cross-system linking. |

Forgejo also exposes profile fields (`description`, `location`, `website`, `pronouns`) on the user object. We deliberately ignore these — site profile lives in git.

## Issues and PRs — already ingested in prototype 04

Each issue/PR embeds a full `user` object (`id`, `login`, `username`, `html_url`). Prototype 04 stores only `user.username` as a string `author` field.

Also present but unused: `original_author` / `original_author_id` (for imported content). PR vs issue is distinguished by the presence of a `pull_request` key.

**Implication:** linking needs no new API calls. During `sync_issues`, match `user.login` (or `user.id`) against `identities.forgejo` in member frontmatter and set a nullable `Member` FK.

## Activity feed — `GET /api/v1/users/{login}/activities/feeds`

Rich event stream (commits, PRs, merges, comments, releases). Wrong abstraction for member profiles:

- Mixes authored activity with activity on watched/participated repos.
- Forge-native event types (`commit_repo`, `create_pull_request`, …), not site nouns.

Useful for a future "forge activity" widget; not for "show me this member's PRs."

## No global author search

- `/api/v1/issues/search?q=author:…` → 404 on this instance.
- No cross-repo "all PRs by this user" endpoint.

Options for finding a member's work:

1. **Sync from known repo(s), filter locally** — prototype 04 approach. Correct for a monorepo with `system/<slug>` labels.
2. Activity feed — noisy, wrong semantics.
3. Iterate every repo — expensive, fragile.

Member profile pages query the already-synced `Issue` table, not the forge per-user.

## Frontmatter key: login or id?

Start with the login string — matches what prototype 04/05 already store. The site slug (filename) is
separate; see [member slug and references](./member-slug-and-references.md).

```yaml
identities:
  forgejo: alexanrf
```

Add `forgejo_id: 10` later if handle renames orphan historical records (see [organizational implications](./organizational-implications.md)).

## External contributors

Every issue has a `user` object with `html_url`. When no `Member` matches, link the author name to their forge profile instead of an internal member page.
