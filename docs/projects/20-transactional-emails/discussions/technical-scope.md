# Technical scope

**Project:** `transactional-emails`
**Date:** 2026-09-11

Implementation choices for the manual-onboarding design in [pivot-to-manual-onboarding.md](./pivot-to-manual-onboarding.md) and [join-flows.md](./join-flows.md).

## Mail flow

```
POST form → Form.is_valid() → render .txt template → send_mail(to=hei@)
          → thank-you page (no outbound mail to submitter)
```

- **To:** `hei@datakollektivet.no` (setting: `ONBOARDING_INBOX`).
- **From:** verified TEM domain (e.g. `noreply@datakollektivet.no` or `hei@` if configured).
- **Subject:** prefixed by flow — e.g. `[Følg oss]`, `[Bli medlem]`, `[Bygg med oss]` — plus submitter email for scanability.

## Email template shape

One `.txt` template per flow under `public/templates/public/emails/join/`:

```
{# folg_oss.txt — structure, not final copy #}

Ny henvendelse: Følg oss

--- Innsendt ---
E-post: {{ email }}
Hold meg oppdatert: {{ newsletter|yesno:"Ja,Nei" }}

--- Forslag til svar ---
Hei!

Takk for at du vil følge med på Datakollektivet.
...
```

Welcomer replies manually; the site never sends the "Forslag til svar" block to the visitor automatically.

## Validation

**Django Forms** — `FollowForm`, `MemberForm`, `BuildForm` (one per path). Templates render fields with `{{ form.email }}` etc.; layout stays in HTML, widgets carry placeholders and `autocomplete`.

## Abuse (inbox protection)

Third-party email bombing is **out of scope** — we do not mail submitter addresses.

Remaining risks: flooding `hei@`, garbage submissions.

| Mitigation | Purpose |
|---|---|
| CSRF | Baseline POST protection |
| Hashed email + flow cooldown (`EmailSendLog`) | Same person cannot trigger 100 notifications for one address in an hour |
| Per-IP limit (optional v1) | Script flood protection |
| Field length limits (Form fields) | Readable notifications |

On rate-limit hit: skip send, still show thank-you (do not leak block reason to bots).

## Storage

**Mailbox is the system of record** — no ORM models. No `EmailSendLog` (decided 2026-09-11).

## Scaleway TEM

| Path | Notes |
|---|---|
| **SMTP** (leaning) | `smtp.tem.scaleway.com:587`, Project ID + API secret |
| **REST API** | Fallback if SMTP awkward |

Dev: `MAILERS` default → `console.EmailBackend`. Prod: SMTP when env vars set.

Setup checklist: verified domain, SPF/DKIM, IAM key — unchanged from earlier discussion.

## Sync send

Send synchronously in the view. Low volume; failure → error page, no log row, no thank-you.

No Celery in v1.

## Fork base

**Prototype 15** — form CSS, layout, join section structure. Replace join pages with the three Norwegian flows; strip articles if not needed for smoke test.

Add `CsrfViewMiddleware` (missing in 15 today despite `{% csrf_token %}`).

## Suggested prototype layout

```
prototypes/20-transactional-emails/
  config/settings.py
  public/
    forms.py                  # FollowForm, MemberForm, BuildForm
    mail.py                   # notify_onboarding_inbox(flow, data)
    views.py
    templates/
      public/join/              # hub + three flow pages
      public/emails/join/       # follow.txt, member.txt, build.txt
```

## Open (technical)

- Exact `From` address on TEM domain.
- Member payment details: thank-you page only, or also embedded in internal template for welcomer's reference?
- SMTP vs API — try SMTP first unless blocked during setup.

## Non-goals

- Outbound mail to submitter (including "we received your request").
- SSO, Keycloak, payment verification, Forgejo/Loomio API integration.
- Listmonk / newsletter automation.
- HTML email, attachments, admin UI for submissions.
- Celery, CAPTCHA (defer).
