---
title: Building the collective homepage
date: 2026-08-12
author: alexanrf
system: website
summary: Why we're prototyping the site as markdown in git, and what we're learning along the way.
---

We're building the collective's public face — systems, members, articles, operational updates — as a
Django site whose content lives in git. Not a CMS: you edit a markdown file, reload the browser, and
see the change.

## What the site is for

Outsiders should be able to trust a system, stay informed about downtime, see that work is happening,
and find a path into contribution. Members should not have to hand-copy forge activity into content
files — authored notices and observed activity stay separate.

## How we're prototyping

This prototype started UI-first: real member and system data, no forge sync, no identity plumbing.
Content syncs from `content/` into the ORM on each request in dev, so the authoring loop stays
save–reload while views use normal Django queries.

Groups (`Board`, `Maintainers`) and org roles (`Styreleder`, `Technical Coordinator`) live beside
member profiles. System teamleads and admins stay on each system's page — different kind of
accountability.

## What's next

Flesh out system pages, write real updates when something changes, and figure out how forge activity
should appear once the authored content feels right. The markdown stays the source of truth; the
database is derived.
