---
title: SSO is live — what we shipped
date: 2025-11-20
author: gingermusketeer
initiative: build-sso
system: keycloak
summary: A short retrospective on getting single sign-on working across collective services.
---

When the Build SSO initiative started, members logged into Forgejo, Matrix,
and everything else with separate credentials. That was fine at small scale; it doesn't scale with
turnover, onboarding, or the number of services we operate.

## What shipped

Keycloak now sits in front of the services that support it. Members authenticate once; the identity
layer handles the rest. The Keycloak system page is where ongoing operational notices live — downtime,
upgrades, federation changes.

This article is about the *initiative* — the push to get SSO in place — not the day-to-day running of
the service. That split is deliberate: goals and recruitment on initiative pages; operational truth on
system pages.

## What we learned

- **Label your forge work.** SSO touched many repos; issues labeled `system/keycloak` still surface on
  the site as observed activity.
- **Authored updates matter.** The forge shows merges; it doesn't tell affected users about a
  maintenance window. We wrote those as system updates.
- **Initiatives can close.** The initiative is marked completed; Keycloak stays in production. Ongoing
  maintenance belongs on the system, not on a goal page forever.

## For future cross-cutting work

Build SSO spanned one primary system but was still a goal someone drove. Articles can link to both the
initiative (context and history) and the system (where the software lives). Use both when the story
needs it; use one when it doesn't.
