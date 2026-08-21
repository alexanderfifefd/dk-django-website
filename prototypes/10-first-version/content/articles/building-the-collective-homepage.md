---
title: Building the collective homepage
date: 2026-08-12
author: Alexander
summary: Why we're prototyping the site as markdown in git, and what we're learning along the way.
---

We're building the collective's public face as a Django site whose content lives in git. Not a CMS:
you edit a markdown file, reload the browser, and see the change.

## What the site is for

Outsiders should be able to trust what we maintain, stay informed about downtime, see that work is
happening, and find a path into contribution.

## How we're prototyping

This first version keeps the surface area small: home, articles, about, and join. Articles sync from
`content/` into the ORM on each request in dev, so the authoring loop stays save–reload while views
use normal Django queries.

## What's next

Flesh out join flows, add member profiles and system pages when the authored content feels right.
The markdown stays the source of truth; the database is derived.
