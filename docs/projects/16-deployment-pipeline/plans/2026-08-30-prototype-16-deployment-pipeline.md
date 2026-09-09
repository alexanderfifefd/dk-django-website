# Plan: prototype 16 — deployment pipeline

**Project:** `deployment-pipeline`
**Discussion:** `docs/projects/16-deployment-pipeline/discussions/minimal-deploy-scope.md`
**Prototype:** `prototypes/16-deployment-pipeline/`
**Status:** built (2026-08-30)

## Goal

A bootable Django prototype with the smallest possible page graph to validate deploy, WSGI, templates, and static file serving.

## Outcome

- Django project: `config/`, `public/` app, sqlite config present but unused
- One route: `/` → home template
- Layout: `base.html` + header/footer partials
- Static: `static/css/site.css`, `STATIC_ROOT` for `collectstatic`
- Placeholder copy only

Intentionally **not** shipped: ORM models, markdown, loaders, middleware, images, nav links, design tokens.

## Verify

From `prototypes/16-deployment-pipeline/`:

```bash
uv run python manage.py runserver
uv run python manage.py collectstatic --noinput
```

Home shows header, "Home" heading, footer; CSS borders visible on header/footer.

## Next (outside this prototype)

- Wire CI/CD against this tree
- Add production settings when a project explicitly claims deployment
- Promote to richer prototypes once pipeline is green
