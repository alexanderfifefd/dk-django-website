# Technical scope

**Project:** `transactional-emails`
**Date:** 2026-09-11 (updated)

Implementation choices for the manual-onboarding design in [pivot-to-manual-onboarding.md](./pivot-to-manual-onboarding.md) and [join-flows.md](./join-flows.md).

**Forms and CSS:** [forms-and-css.md](./forms-and-css.md) — Django Forms, `as_div`, cascade styling (authoritative for form decisions).

## Mail flow

```
POST form → Form.is_valid() → render .txt template → send_mail(to=hei@)
          → thank-you page (no outbound mail to submitter)
```

- **To:** `hei@datakollektivet.no` (setting: `ONBOARDING_INBOX`).
- **From:** verified TEM domain (e.g. `noreply@datakollektivet.no` or `hei@` if configured).
- **Subject:** prefixed by flow — e.g. `[Follow us]`, `[Become a member]`, `[Build with us]` — plus submitter email for scanability.

## Email template shape

One `.txt` template per flow under `public/templates/public/emails/join/`:

- `follow.txt`, `member.txt`, `build.txt`
- **Submitted** — field summary from `form.cleaned_data`
- **Suggested reply** — copy/edit block for welcomer; never sent to visitor automatically

## Validation

See [forms-and-css.md](./forms-and-css.md). **Django Forms only** — `FollowForm`, `MemberForm`, `BuildForm`.

## Abuse (inbox protection)

Third-party email bombing is **out of scope** — we do not mail submitter addresses.

Remaining risks: flooding `hei@`, garbage submissions. Mitigations in v1: CSRF, field length limits on forms. No `EmailSendLog`, no per-IP limit (decided 2026-09-11).

## Storage

**Mailbox is the system of record** — no ORM models.

## Scaleway TEM

| Path | Notes |
|---|---|
| **SMTP** (leaning) | `smtp.tem.scaleway.com:587`, Project ID + API secret |
| **REST API** | Fallback if SMTP awkward |

Dev: `MAILERS` default → `console.EmailBackend`. Prod: SMTP when `EMAIL_MAILER=scaleway`.

## Sync send

Send synchronously in the view. Low volume; on send failure show error and keep form — do not show thank-you.

No Celery in v1.

## Dev tooling

- **Django Debug Toolbar** when `DEBUG=True` (`debug_toolbar` in settings + `__debug__/` URLs).
- Shared dependency in root `pyproject.toml`.

## Fork base

**Prototype 15** — form-card chrome, layout, tokens. Prototype 20 strips articles/loaders; join-only.

## Prototype layout

```
prototypes/20-transactional-emails/
  config/settings.py
  public/
    forms.py                  # FollowForm, MemberForm, BuildForm
    mail.py
    views.py                  # join_follow, join_member, join_build (explicit, no helper)
    templates/
      public/join/            # hub + three pages (form inlined, {{ form.as_div }})
      public/emails/join/     # notification .txt templates
  static/css/components.css   # .form-card__body form { … } cascade
```

## Non-goals

- Outbound mail to submitter.
- Pydantic for POST / HTML forms.
- SSO, payment verification, Forgejo/Loomino API integration.
- ORM submission storage, Celery, CAPTCHA.
