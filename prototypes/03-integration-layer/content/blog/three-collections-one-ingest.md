---
title: Three collections, three sync commands
date: 2026-08-05
author: bob
system: relay
summary: Members from an external source, systems and articles from git — with real foreign keys between them.
---

Prototype 02 had one flat collection. This one has members cached from a Keycloak-shaped JSON file,
systems with team references, and articles naming both an author and an optional system.

Each collection has its own sync command. A `system.md` naming an unknown member aborts the run. So does
an article with a bad `author` or `system` slug. Sync order matters: `sync_members`, then
`sync_systems`, then `sync_articles`.
