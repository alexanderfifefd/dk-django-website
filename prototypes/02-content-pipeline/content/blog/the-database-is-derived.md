---
title: The database is derived
date: 2026-08-01
tags: [django, design]
summary: Content lives in the database here — but the database is a build artifact, not a source.
---

Every post on this site is a row in a `Post` table, which sounds like the CMS pattern this repo set out to
avoid. The difference is direction: nothing ever writes to that table except `manage.py ingest`, and ingest
only ever reads from `content/blog/`. The files are the source of truth; the database is a build artifact.

That one rule buys some pleasant properties:

- The sqlite file is never precious. Delete it, `migrate`, `ingest` — identical site.
- `ingest --flush` rebuilds the world from scratch whenever the sync logic feels suspicious.
- Deploys are boring: check out the repo, migrate, ingest, serve.
- The admin, fixtures, and backups have nothing to protect. Git already has everything.

The cost is equally concrete: an edit does not exist until ingest runs. Prototype 01's save-and-reload loop
is gone, replaced by save-ingest-reload. Whether that middle step is an annoyance or a rounding error is
most of what this prototype exists to find out.
