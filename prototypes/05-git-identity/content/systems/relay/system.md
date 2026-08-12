---
title: Relay
summary: Event routing between our systems and the outside world.
teamlead: bob
admins: [carol, alex]
---

Relay moves data between services without every team inventing their own queue-and-retry story. Webhooks in,
webhooks out, with signing and replay built in.

## Why it exists

Point-to-point integrations don't scale when you have a dozen systems and twice as many members touching
them. Relay is the shared pipe.
