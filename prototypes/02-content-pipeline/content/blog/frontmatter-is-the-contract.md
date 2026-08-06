---
title: Frontmatter is the contract
date: 2026-08-04
tags: [markdown, design]
summary: The YAML block at the top of each file is a schema — and this time it's enforced.
---

The frontmatter block is the contract between authors and the site, and unlike prototype 01, this one is
enforced. Ingest validates every file and refuses to write anything if any file is wrong:

| Key       | Required | Meaning                              |
|-----------|----------|--------------------------------------|
| `title`   | yes      | A string                             |
| `date`    | yes      | An unquoted YAML date (`2026-08-04`) |
| `tags`    | no       | A list of strings                    |
| `summary` | no       | Shown on index pages                 |
| `draft`   | no       | `true` keeps the post out entirely   |

An unknown key — say the `drafts: true` typo that silently published a draft in prototype 01 — is now an
error that aborts the whole ingest. A half-written file no longer degrades into an ugly post; it fails
loudly before it can reach the database at all.

```yaml
---
title: Frontmatter is the contract
date: 2026-08-04
tags: [markdown, design]
---
```
