# Pivot: manual onboarding via org inbox

**Project:** `transactional-emails`
**Date:** 2026-09-11
**Status:** decided — supersedes the auto-email-to-submitter approach in the 2026-09-10 discussion

## What we rejected

The first pass assumed **public forms email instructions directly to the address the visitor typed** — SSO link, payment details, Matrix room links. That pattern:

- Is an **email-bombing surface** (attacker POSTs someone else's address; our domain sends them mail).
- Felt wrong architecturally — the join ladder already assumes account-before-member; auto-mailing unverified addresses sidesteps that.
- Was not worth building "just to learn TEM" on a design we would not ship.

See [scope-and-options.md](./scope-and-options.md) (2026-09-10 version) in git history for the full exploration of that approach (auto-email to submitter, hashed-email rate limits, etc.). The **recipient and workflow** changed; form and CSS decisions are in [forms-and-css.md](./forms-and-css.md).

## Decision

**Manual onboarding.** A form submission sends one transactional email to an **org-owned inbox** (`hei@datakollektivet.no`). A welcomer (*velkomstansvarlig*) reads it, replies manually, and handles access (Matrix, Loomio, Forgejo, payment confirmation).

- **No automated email to the submitter** in v1. The thank-you page sets expectations ("vi tar kontakt").
- **No "create account" path** as a separate join flow. SSO self-registration is not the entry point we optimize for here; see [join-flows.md](./join-flows.md) for the three paths that replace the old account/member/volunteer split.

## Why this is better

| Concern | Auto-email to submitter | Email to `hei@` only |
|---|---|---|
| Third-party email bombing | Real risk | None — we only mail ourselves |
| Liability / reputation | Our domain spams strangers | Bounded — we spam our own inbox |
| Onboarding quality | One-size template | Human can adapt, answer questions |
| Audit trail | Ephemeral or rate-limit hash | Mailbox is the record |
| Fits collective scale | Over-automated | Appropriate for low volume |

Abuse is not gone — someone can still flood `hei@` — but that is **inbox spam**, not **weaponized outbound mail**. Rate limits and CSRF are still worth having; CAPTCHA remains optional.

## The template insight

Internal notification emails should include **two sections**:

1. **Innsendt** — structured summary of form fields (what the visitor asked for).
2. **Forslag til svar** — a copy-ready reply template the welcomer can paste into their mail client, edit, and send from `hei@` (or personal, depending on practice).

That gives consistency without pretending the reply is automatic. TEM + Django `.txt` templates still earn their keep — they structure the *internal* mail, not a user-facing drip campaign.

## What carries forward from the earlier discussion

- Fork **prototype 15** for form UX and CSS.
- **Django Forms** + `as_div` + cascade CSS — see [forms-and-css.md](./forms-and-css.md).
- **Django `.txt` templates** for email bodies.
- **Scaleway TEM** via SMTP (leaning).
- **Sync send** in the view; console backend in dev.
- **`EmailSendLog`** with hashed email for duplicate-submission cooldown (now protects the inbox, not third parties).
- **CSRF middleware** on the fork.

## What changed

- Recipient is always `hei@datakollektivet.no` (configurable), never the submitter's address.
- Three flows renamed and reframed — [join-flows.md](./join-flows.md).
- Success UX is "thanks, we'll be in touch" — not "check your inbox."
- Learning TEM happens **through the design we would ship**, not a throwaway pattern.

## Open (product)

- Confirm no auto-confirmation to submitter in v1 (leaning: none).
- Who is *velkomstansvarlig* — role rotation, shared mailbox, Matrix as parallel channel?
- When SSO self-serve registration returns to the site, it is a separate concern — link from welcomer's reply, not a fourth join form.
