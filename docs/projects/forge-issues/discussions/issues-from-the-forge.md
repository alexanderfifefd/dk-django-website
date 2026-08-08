# Discussion: issues from the forge

## The question

Every source so far lives on disk: markdown and JSON in git, a Keycloak-shaped file standing in for an
external system. The high-level goals name a third kind of source — an HTTP API that Django caches on a
schedule — and no prototype has touched one. Forgejo is the collective's forge, and its issues are real
operational data nobody would ever author as files.

Does the ingest pattern extend to an externally-owned HTTP API? Concretely: can Forgejo issues, labeled
by system, become a derived collection alongside the git-owned systems — fetched live, validated at the
boundary, synced idempotently?

**Issues are a new noun, not a replacement.** Updates (`updates.json`, authored in git, JSONField on
`System`) stay exactly as they are. An issue is forge-owned work-tracking data; an update is an authored
operational notice. A system page will show both.

*Amended 2026-08-08*: pull requests joined the scope — same labels, same endpoint, rendered as
aggregate activity rather than items. See `forge-primitives-as-site-content.md` (decisions and "How
states render"); the plan is updated. Where this document says issues are fetched with `type=issues`,
that filter is gone.

## What Forgejo gives back

`GET /api/v1/repos/{owner}/{repo}/issues` with `state=all&type=issues` (the endpoint returns pull
requests too unless filtered). Paginated via `page`/`limit`; auth is `Authorization: token <t>`. Each
issue carries far more than we need — the fields that matter:

| Field | Notes |
|---|---|
| `number` | Issue index within the repo — the natural key, since we use one repo |
| `title` | |
| `state` | `open` or `closed` |
| `labels` | Objects with `name`, `color`, `description` |
| `html_url` | Link back to the forge |
| `user` | The Forgejo poster — a forge identity, not a Keycloak one |
| `created_at`, `updated_at`, `closed_at` | ISO 8601; `closed_at` null while open |
| `body` | Markdown |

## Decisions

### One repo, labels carry the structure

A single monorepo on the live Forgejo server holds all issues. Labels do the categorising:

- **`system/<slug>`** — assigns the issue to a system. The prefix keeps system labels unmistakable next
  to ordinary tags (a bare `atlas` label could be anything). Exact label taxonomy gets defined in the
  repo together as part of the test.
- **Everything else** (`incident`, `maintenance`, whatever emerges) — plain tags, stored and rendered
  as-is (name + color), no semantics attached. Deliberately simple; semantics can be a later finding.

Reference rules, matching the strictness of the file sources where it is genuinely an error and relaxing
it where it is not:

- `system/<slug>` naming a slug with no `System` row → **abort loudly**. Same as a dangling frontmatter
  reference: the forge and git disagree, and someone should know.
- **No** system label → **ingest anyway, present nowhere**. An unlabeled issue isn't an error, it's just
  not site content yet; a row with a null system FK costs nothing and keeps the sync total honest.
- **Multiple** system labels → take the first (sorted by name). Theoretically possible, not worth
  machinery.

### Issues get their own table

Updates stayed a JSONField because they render only on their own system's page and ride in on that
system's directory. Issues fail both halves of that argument: they arrive as one repo-wide list that has
to be split across systems, they have external identity (`number`) and links, and the ingest-anyway rule
means rows that belong to *no* system — which a JSONField on `System` cannot hold. So: a derived `Issue`
model.

```
Issue
  number      unique integer — natural key
  title       char
  state       char: open | closed
  url         html_url, for linking out
  system      FK → System, nullable (null = no system label), SET_NULL on system removal
  labels      JSONField: [{name, color}] — the non-system labels, presentation only
  author      char — the Forgejo username, deliberately NOT a Member FK
  created_at / updated_at / closed_at (nullable) datetimes
```

Two deliberate exclusions:

- **`author` is a string.** Mapping forge identities onto the Keycloak member cache is a real question
  (a fourth cross-source reference) and a whole project's worth of edge cases. Not this one.
- **No `body`.** Issues render as title + tags + link out to the forge. The forge is the reading and
  discussion surface; the site surfaces, it doesn't mirror.

`SET_NULL` rather than `PROTECT` on the FK because "unassigned" is already a legal state here — a system
vanishing from git demotes its issues to unpresented rather than blocking `sync_systems`.

### Pydantic at the boundary — but `extra="ignore"`

The file sources use `extra="forbid"` as a typo gate for authors. That logic inverts for an API we don't
own: Forgejo adding a response field is routine, not an authoring error. So the issue schema validates
the fields we consume and ignores the rest. Same boundary, different failure contract — worth having
written down as a finding about API sources generally.

### Live API, separate command, same layout

- `pages/sources/issues.py` — schema → fetcher (httpx, page loop) → syncer → `run_sync_issues()`,
  reading top to bottom like the other source modules. `httpx` joins the shared environment.
- `manage.py sync_issues` — thin wrapper, like the others. Freshness stays per-source: file sources sync
  manually as before, the API source syncs manually too for now (the goals doc says scheduled +
  short-circuit eventually; a manual command is the honest prototype of that).
- Sync order: `sync_members` → `sync_systems` → `sync_issues` (label resolution needs System rows).
- Settings: `FORGEJO_BASE_URL`, `FORGEJO_REPO` (`owner/name`). The test repo is public and anonymous
  read access works (verified against the live server), so no token is required; an optional
  `FORGEJO_TOKEN` env var is sent as `Authorization: token <t>` if set — never committed, no secrets
  hardening beyond that (non-goal).
- Fetch `state=all`: closed issues stay rows (so a re-sync reflects closure), presentation decides what
  to show. Delete rows whose number no longer comes back.

### Verified against the live server (2026-08-07)

The monorepo is `alexanrf/public-api-test-repo` on `https://forge.hornwitser.no`. Anonymous curl
against `/api/v1/repos/.../issues?state=all&type=issues` confirmed the assumed shape end to end: the
`system/atlas` label arrives as `{"name": "system/atlas", "color": "70c24a", ...}` inside `labels`,
`user.username` carries the poster, timestamps are ISO 8601, `x-total-count` reports the total for the
page loop, and unlabeled issues simply have `labels: []`.

### Scope of the prototype around it

`prototypes/04-forge-issues/`, copied from prototype 03 and stripped: members, systems, and updates stay
(updates are kept precisely because issues are *not* their replacement); articles and the blog go.
Pages: home (collective, recent updates, recent open issues), systems index, system detail (body, team,
updates, open issues), member detail. Unassigned issues appear nowhere on the site — admin is the
inspection window for them.

## What stays open

- Whether closed issues deserve a "recently resolved" strip on system pages, or stay invisible.
- Label semantics beyond presentation (e.g. `incident` styling) — only if the rendered page begs for it.

Plan: `plans/2026-08-07-prototype-04-forge-issues.md`.
