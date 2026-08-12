# Member Slug and Cross-References

**Question:** What is the canonical ID for a member when other content references them — and how does that
relate to display names and external identities (forge, Matrix, etc.)?

## Decision: the filename is the slug

Members follow the same rule as systems: **the path is the natural key**. No duplicate `slug:` or `id:`
field in frontmatter.

```
content/members/alice.md   →  slug: alice
content/members/alex.md    →  slug: alex
```

Systems work the same way — `content/systems/atlas/system.md` → slug `atlas`, referenced as
`teamlead: alice` in frontmatter, not as a separate declared ID.

## Three layers — keep them separate

| Layer | Example | Purpose |
|---|---|---|
| **Site slug** | `alex` | In-repo references, URLs (`/members/alex/`), Django natural key. Collective-owned; pick once, rename deliberately. |
| **Display name** | `Alexander` | Human-readable; free to change in frontmatter without breaking references. |
| **External identity** | `forgejo: alexanrf` | Links forge/Matrix/etc. activity to the member. Never used for in-git cross-references. |

Example member file:

```yaml
---
name: Alexander
identities:
  forgejo: alexanrf
---
Profile markdown…
```

Other content references the **slug**, not the forge handle:

```yaml
# content/systems/atlas/system.md
teamlead: alex
admins: [bob]
```

```yaml
# content/blog/some-post.md
author: alice
```

## What not to do

- **Don't put `slug:` in frontmatter** unless you also validate it matches the filename — otherwise two
  sources of truth.
- **Don't use forge handles as the site slug** (`content/members/alexanrf.md`, `teamlead: alexanrf`) —
  ties collective identity to a third-party username; breaks on forge renames.
- **Don't use display names as references** — `teamlead: Alexander` would break when someone edits their
  `name` field.

## Renames and alumni

- **Renaming a member** means renaming the file *and* updating every reference (`teamlead`, `author`,
  etc.) in one PR — same as renaming a system directory.
- **Alumni** keep their slug with `active: false` in frontmatter. References in old articles and forge
  history keep working; the members index hides them.

## Optional future refinements

- **Directory layout** — `content/members/alex/member.md` if per-member assets are needed later. Slug
  still comes from the directory name.
- **Model rename** — `Member.username` → `Member.slug` for symmetry with `System.slug`. Behaviour
  unchanged.
- **Identity arrays** — `forgejo: [alexanrf, alex-old]` for handle renames without losing historical
  forge links (see [organizational implications](./organizational-implications.md)).
