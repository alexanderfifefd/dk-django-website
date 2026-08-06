---
title: Frontmatter is the contract
date: 2026-08-04
tags: [markdown, design]
summary: The YAML block at the top of each file is the only schema this blog has.
---

With no database there is no schema, so the frontmatter block quietly becomes the contract between authors
and the site. This prototype expects:

| Key       | Required | Meaning                              |
|-----------|----------|--------------------------------------|
| `title`   | no       | Falls back to a titleised filename   |
| `date`    | no       | Falls back to the file's mtime       |
| `tags`    | no       | A list of strings                    |
| `summary` | no       | Shown on index pages                 |
| `draft`   | no       | `true` hides the post entirely       |

Everything optional is a deliberate choice: a half-written file should degrade into an ugly post, not a
500 error. Whether that's the right trade-off is exactly the kind of thing a prototype is for.

```yaml
---
title: Frontmatter is the contract
date: 2026-08-04
tags: [markdown, design]
---
```
