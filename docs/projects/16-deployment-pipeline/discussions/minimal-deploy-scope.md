# Minimal deploy scope

**Project:** `deployment-pipeline`
**Date:** 2026-08-30

## Question

Before wiring CI/CD or hosting, we need a site small enough that deploy failures map cleanly to infrastructure — not content sync, migrations, or CSS regressions. What do we keep?

## Options considered

1. **Fork prototype 15** — full CSS structure, articles, join paths. Rejected: too much surface area; a broken deploy could be content, DB, or static.
2. **Fork prototype 10** — slimmer, but still articles, ORM, loaders, middleware. Rejected for the same reason.
3. **Bare minimum** — one view, base layout with header/footer, one CSS file, `collectstatic` target. **Chosen.**

## Decision

Prototype 16 is a deployment smoke test:

- Single route and template
- Header and footer as includes (proves partial + extend pattern)
- One hand-written CSS file (proves `STATICFILES_DIRS` and template `{% static %}`)
- `STATIC_ROOT` set for production-style collection
- No models, no `content/`, no management commands beyond Django defaults

When the pipeline works here, promote patterns into richer prototypes — not the other way around.

## Non-goals

- Real copy, branding, or navigation
- Production settings, secrets, or security hardening (repo-wide non-goal until a dedicated project claims it)
- JavaScript or HTMX
