---
title: Parsing on every request
date: 2026-08-01
tags: [django, performance]
summary: This blog re-reads every file from disk each time you load the index. On purpose.
---

Every load of the blog index walks `content/blog/`, opens each file, parses its YAML frontmatter, and
converts its markdown to HTML. Nothing is cached anywhere.

That sounds wasteful, and at some size it will be. But it buys the two properties this prototype cares
about most:

1. **Instant authoring feedback.** Save the file, reload the browser. No sync step to forget.
2. **No state to invalidate.** The filesystem is always right, because it's the only copy.

The open question — tracked in the project docs — is where the ceiling is. A future prototype can add an
index (in memory, or in the sqlite database that's already sitting there unused) *if* this one proves we
need it.
