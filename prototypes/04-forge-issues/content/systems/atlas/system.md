---
title: Atlas
summary: Internal deployment and observability platform for the collective's services.
teamlead: alice
admins: [bob]
---

Atlas is the backbone we run everything else on. It handles deployments, health checks, and the dashboards
we stare at when something breaks at 2am.

## What it does

- Deploys services from git tags
- Aggregates logs and metrics in one place
- Pages the on-call rotation when thresholds trip

If you maintain a system in this collective, you probably interact with Atlas daily — even if you never
think about it by name.
