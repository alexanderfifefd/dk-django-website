# Prototype 20 — transactional emails

Join forms notify `hei@datakollektivet.no` via Scaleway TEM (or console in dev). A welcomer replies manually using the suggested template in each notification.

## Run locally

```bash
cd prototypes/20-transactional-emails
uv run python manage.py runserver
```

Open `/join/` — three paths: follow, member, build. Submitting a form prints the notification email to the terminal (console backend).

[Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/) is enabled when `DEBUG=True` — panel appears on local requests from `127.0.0.1`.

## Scaleway TEM

```bash
export EMAIL_MAILER=scaleway
export SCW_TEM_PROJECT_ID=your-project-id
export SCW_TEM_SECRET_KEY=your-secret-key
export DEFAULT_FROM_EMAIL=noreply@your-verified-domain.no
export ONBOARDING_INBOX=hei@datakollektivet.no
uv run python manage.py runserver
```

## Settings

| Variable | Default |
|---|---|
| `ONBOARDING_INBOX` | `hei@datakollektivet.no` |
| `DEFAULT_FROM_EMAIL` | `noreply@datakollektivet.no` |
| `EMAIL_MAILER` | `default` (console) or `scaleway` |
| `MATRIX_CONTACT_URL` | Matrix room link for suggested replies |

Member payment details live in `config/settings.py` → `MEMBER_PAYMENT`.

## Project docs

`docs/projects/20-transactional-emails/`
