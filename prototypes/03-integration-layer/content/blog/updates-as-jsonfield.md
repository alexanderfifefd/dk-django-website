---
title: Why updates live in JSON, not the ORM
date: 2026-08-06
author: alice
system: atlas
summary: Operational notices don't need their own table — until they do.
---

We scoped updates as record-like data that only ever renders on a system's page. No cross-system queries, no
foreign keys to chase — so they land in a `JSONField` on `System` instead of a dedicated model.

That keeps the ingest path simple: read `updates.json` beside `system.md`, validate the shape, store the
list. If we later need "all maintenance windows across systems this week", promoting the field to a model
is the experiment — and its cost is part of what this prototype is meant to surface.
