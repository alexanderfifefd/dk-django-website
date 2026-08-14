# Plan: three org groups — Board, Maintainers, Moderators

**Project**: `groups`
**Discussion**: `docs/projects/groups/discussions/org-groups-on-the-site.md`
**Context**: `docs/organizational-context.md`, [initiatives](../initiatives/overview.md) (prototype 07 baseline)
**Prototype**: `prototypes/07-initiatives/` — **not a separate prototype directory**; groups work is a pass on 07
**Status**: built (2026-08-14)

## Goal

Add **Moderators**, enrich group definitions with **summary** and **matrix**, and present all three groups
on the **Members** page in **sections per group**. About keeps narrative prose and **points to Members**
for group listings — no duplicate board block.

## Display decision

**Option B — Members-centric, sections per group** (2026-08-14).

| Page | Behaviour |
|---|---|
| **`/members/`** | Intro + three sections: Board, Maintainers, Moderators. Each section: title, summary, Matrix room, member list. Anchors: `#board`, `#maintainers`, `#moderators`. |
| **`/about/`** | Remove current Board member list. Add pointer(s) to `/members/#board` (and optionally other anchors). |
| **Member detail** | Unchanged pattern: group titles inline on profile. |

Options A, C, and D in earlier drafts are **not** chosen.

## Content model

### `groups.yaml`

```yaml
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

### Group fields

| Field | Required | Notes |
|---|---|---|
| `title` | yes | Display name |
| `summary` | no | Shown in each group section on Members index |
| `matrix` | no | Shown as join path; placeholder addresses until rooms exist |

### Member `groups:` — explicit assignment only

Do **not** default every active member to `maintainers`. Add groups only where accurate in git.

**Current / planned assignments (prototype seed):**

| Member | Groups | Notes |
|---|---|---|
| alexanrf | board, maintainers | unchanged |
| gingermusketeer | board, maintainers | unchanged |
| daniel | board | explicit; add maintainers only when accurate |
| hornwitser | board | explicit; add maintainers only when accurate |
| hallvord | moderators | seed — no other group roles |
| papiris | moderators | seed — no other group roles |
| tormod | moderators | seed — no other group roles |
| erik, luisa | *(none)* | explicit empty until assigned |

## Architecture

- **Models:** extend `Group` with `summary` (TextField, blank) and `matrix_room` (CharField, blank) —
  mirror initiative/system matrix handling.
- **Ingest:** extend `pages/sources/groups.py` to load `summary` and `matrix`; strict validation via
  Pydantic (same pattern as other sources).
- **Views:** `members_index` loads groups in fixed order (board → maintainers → moderators) with prefetched
  members per group; members may appear in multiple sections if they hold multiple groups.
- **Templates:** `members_index.html` — sectioned layout; `about.html` — pointer instead of board list.
- **Migration:** one migration on prototype 07 for new Group fields.

## Scope

**In**

- Rich `groups.yaml` (three groups with summary + matrix)
- Group model + ingest for summary/matrix
- Members index: sections per group with Matrix link
- About: pointer to `/members/#board` (and cross-links as needed)
- Explicit member `groups:` updates per table above
- CSS for group sections on Members index

**Out**

- Interest-group / persona pages
- Group detail URLs (`/groups/<slug>/`)
- Matrix membership ingest, recruiting UI, auth
- Defaulting `maintainers` onto all members

## How we know it worked

```bash
cd prototypes/07-initiatives
uv run python manage.py migrate
uv run python manage.py sync_content
uv run python manage.py runserver
```

- `/members/` shows three sections with summaries and Matrix addresses
- Board, Maintainers, and Moderators each list the correct members
- `/members/#moderators` shows hallvord, papiris, tormod
- About no longer duplicates the board list; links to Members
- Sync errors on unknown group slugs still fail loudly in dev

## Outcome

**2026-08-14:** Group model extended with `summary` and `matrix_room`; ingest via Pydantic. Three groups in
`groups.yaml`. Members index: sections per group with anchors. About: pointers to `/members/#board` (and
maintainers/moderators). Moderators seeded: hallvord, papiris, tormod.
