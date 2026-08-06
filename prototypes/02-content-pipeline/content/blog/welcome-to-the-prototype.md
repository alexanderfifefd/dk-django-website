---
title: Welcome to the prototype
date: 2026-08-06
tags: [meta]
summary: What this site is, and why this post is a file that became a database row.
---

This post is a markdown file. It lives at `content/blog/welcome-to-the-prototype.md`, and the URL you're
reading it at comes from that filename. But the server never opened that file to show you this page —
`manage.py ingest` parsed it, rendered it to HTML, and stored it as a database row. The page you're reading
is a query.

## Why bother?

Because content-as-files is a genuinely nice authoring model, and the database is a genuinely nice serving
model:

- Posts live in git, so they diff, branch, and revert like code.
- Writing happens in your editor, not a browser form.
- Listings, lookups, and ordering are querysets, not directory walks.

## What this prototype should tell us

Whether putting an ingest step between the files and the pages is worth what it costs: the save-and-reload
loop now has a `manage.py ingest` in the middle of it.
