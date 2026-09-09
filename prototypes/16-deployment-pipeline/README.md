# Deployment pipeline — minimal site

Smallest bootable Django site for testing deploy, static files, and `collectstatic`. One route,
header/footer chrome, layered CSS (see `static/css/README.md`). No database models, no markdown.

## Quick start

```bash
uv sync                                    # once, from the repo root
cd prototypes/16-deployment-pipeline
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Static files

```bash
uv run python manage.py collectstatic --noinput
```

Output goes to `staticfiles/` (gitignored).

## Layout

```
config/           # Django project settings and root URLs
public/           # home view and templates
static/css/       # tokens → base → layout → components → pages
static/img/       # logos
```
