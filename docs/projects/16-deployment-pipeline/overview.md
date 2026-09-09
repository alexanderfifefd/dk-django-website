# Deployment pipeline

**Question:** What is the smallest Django site we can deploy to validate a pipeline — static files, WSGI, templates — without carrying content or design?

**Status:** Built (2026-08-30).

**Prototype:** `prototypes/16-deployment-pipeline/` — see **`README.md`** there.

**Builds on:** [first-version](../10-first-version/overview.md) — same `config/` + `public/` layout, stripped to one route and no ORM.

## Scope

Prototype 16 exists to exercise deployment mechanics, not product features.

| In | Out |
|---|---|
| Home (`/`) | Articles, about, join, any other routes |
| Header + footer partials | Navigation, logos, org copy |
| `static/css/site.css` via `{% static %}` | Design system, tokens, component CSS |
| `STATIC_ROOT` for `collectstatic` | Database models, migrations, loaders |
| WSGI/ASGI entrypoints | Middleware, markdown, content folders |

Copy is placeholder text only (`Header`, `Home`, `Footer`).

## Prototype structure

```
prototypes/16-deployment-pipeline/
  README.md
  config/
  public/
    views.py          # home only
    templates/public/
      layouts/base.html
      partials/header.html
      partials/footer.html
      home.html
  static/css/site.css
```

## Request flow

`/` → `public.views.home` → `public/home.html` extends `layouts/base.html` → includes header/footer → loads `static/css/site.css`.

## Docs

1. **`prototypes/16-deployment-pipeline/README.md`** — run and collectstatic
2. **[minimal-deploy-scope.md](./discussions/minimal-deploy-scope.md)** — what we cut and why
3. **[2026-08-30-prototype-16-deployment-pipeline.md](./plans/2026-08-30-prototype-16-deployment-pipeline.md)** — build plan and outcome
