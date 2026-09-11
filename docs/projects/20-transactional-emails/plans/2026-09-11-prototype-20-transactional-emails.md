# Plan: prototype 20 transactional emails

**Date:** 2026-09-11
**Status:** built

## Goal

Three join forms notify `hei@datakollektivet.no` with submitted fields and a suggested reply template. No automated email to visitors. Manual welcomer onboarding.

## Decisions (final)

| Topic | Choice |
|---|---|
| Flows | Follow us, Become a member, Build with us |
| URLs | `/join/follow/`, `/join/member/`, `/join/build/` (English) |
| Recipient | `ONBOARDING_INBOX` (default `hei@datakollektivet.no`) |
| Visitor email | None |
| Member payment | Thank-you page + internal notification |
| Validation | Django Forms + per-field template rendering |
| Storage | None — mailbox is the record; no `EmailSendLog` |
| TEM | SMTP via `EMAIL_MAILER=scaleway`; console in dev |
| Send | Synchronous in view |
| Base | Prototype 15 CSS/forms; no articles or loaders |

## Built

- `prototypes/20-transactional-emails/`
- Three POST forms, three `.txt` notification templates
- `README.md` with env var guide

## Verify

```bash
cd prototypes/20-transactional-emails
uv run python manage.py runserver
```

1. Open `/join/` — three cards
2. Submit each form — email prints to console
3. Member thank-you shows payment details
4. Invalid email re-renders with error

With TEM configured, set `EMAIL_MAILER=scaleway` and confirm delivery to `hei@`.

## Outcome

**Answer:** Django + Scaleway TEM + `.txt` templates is straightforward for org-inbox notifications. Manual onboarding avoids third-party email-bombing. Standard Django Forms with per-field rendering fits the prototype 15 form CSS.
