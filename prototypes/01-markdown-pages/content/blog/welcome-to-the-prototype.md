---
title: Welcome to the prototype
date: 2026-08-06
tags: [meta]
summary: What this site is, and why this post is a file instead of a database row.
---

This post is a markdown file. It lives at `content/blog/welcome-to-the-prototype.md`, and the URL you're
reading it at comes from that filename. Nobody inserted it into a database; the server found it on disk,
parsed its frontmatter, converted the body to HTML, and handed it to a template.

## Why bother?

Because content-as-files is a genuinely nice authoring model:

- Posts live in git, so they diff, branch, and revert like code.
- Writing happens in your editor, not a browser form.
- There is no build step — save the file, reload the page.

## What this prototype should tell us

Whether the naive version of this — read and parse on every request, no cache, no index — holds up, and
where it starts to hurt. Everything else in this repo builds on that answer.
