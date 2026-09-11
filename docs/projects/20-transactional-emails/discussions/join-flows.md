# Join flows — three paths (manual onboarding)

**Project:** `transactional-emails`
**Date:** 2026-09-11
**Status:** built in prototype 20 (English slugs and copy; Norwegian product names kept here for intent)

Replaces the prototype 07 / 15 split of **account / member / volunteer**. The old "create account → SSO button" path is dropped from this project; onboarding starts with human contact.

Each flow: visitor fills a form → site emails **`hei@datakollektivet.no`** → welcomer handles manually → welcomer replies with links, access, and context using the suggested template in the notification mail.

**No automated email to the visitor** in v1.

---

## 1. Følg oss

**Intent:** Low-commitment — stay informed, ask questions, find the community without joining the org.

**Visitor sees:**

- Fyll ut e-post, så tar vi kontakt med mer informasjon.
- Checkbox: *Ja takk, hold meg oppdatert på Datakollektivet.*
- Alternative contact: Matrix (link or handle on the page — not a form field).

**Form fields (minimum):**

| Field | Required |
|---|---|
| E-post | yes |
| Hold meg oppdatert (checkbox) | no (but expected default-on UX TBD) |

**Internal email includes:**

- Submitted e-post and newsletter opt-in.
- **Forslag til svar:** welcome tone, current-state blurb (where the collective is right now), Matrix entry points, invitation to ask questions.

**Welcomer does:**

- Reply manually from `hei@` (or agreed channel).
- Optionally add to a newsletter list later (Listmonk — out of scope here).

---

## 2. Bli medlem

**Intent:** Org membership — Loomio voting, fee, obligations. Heavier than "følg oss."

**Visitor sees:**

- Fyll ut e-post.
- Explanation: you will get Loomio access; transfer membership fee to our account **with your email in the payment reference field**.
- Checkbox: *Ja takk, hold meg oppdatert.*
- Thank-you copy may **repeat payment details on the page** after submit (so the visitor has them while waiting for human follow-up) — TBD in plan.

**Form fields:**

| Field | Required |
|---|---|
| E-post | yes |
| Hold meg oppdatert (checkbox) | no |

**Internal email includes:**

- Submitted e-post and newsletter opt-in.
- **Forslag til svar:** membership welcome, Loomio invite steps, payment amount + bank details + "use your email as reference", what happens next, link to governance docs if useful.

**Welcomer does:**

- Verify payment when it arrives (manual, outside this project).
- Invite to Loomio.
- Reply via `hei@`.

**Note:** Payment details appear in the **suggested reply template** and possibly the **post-submit page** — not emailed automatically to the submitter.

---

## 3. Bygg med oss

**Intent:** Contribution path — Forgejo, Matrix areas, maintenance, initiatives. Replaces "volunteer application" framing with builder/contributor tone.

**Visitor sees:**

- Fyll ut e-post.
- Free text: where you could imagine contributing (moderation, systems, initiatives, skills).
- Explanation: you will hear back about Forgejo access and/or Matrix spaces to join.

**Form fields:**

| Field | Required |
|---|---|
| E-post | yes |
| Hvor du kunne tenke deg å bidra (textarea) | yes |

**Internal email includes:**

- E-post and contribution text.
- **Forslag til svar:** thank-you, relevant Matrix rooms, Forgejo onboarding pointer, who to ping, realistic expectations about volunteer agreement if applicable.

**Welcomer does:**

- Tailor reply to what they wrote.
- Forgejo account / group invites manually.

---

## Hub page

`/join/` (or successor URL) becomes a **chooser for these three paths**, not four. Copy and card labels shift from English account/member/volunteer to the Norwegian framing above.

Prototype URLs: `/join/follow/`, `/join/member/`, `/join/build/`. Old `/join/account/` path removed.

## Relationship to organizational context

[`docs/organizational-context.md`](../../../organizational-context.md) still defines account / member / volunteer as **participation types**. This project changes **how the site converts** — human-first contact rather than self-serve SSO or auto-email. Update organizational context or member-journeys when the prototype lands, not before.

## Success UX (all flows)

After valid submit:

- Thank-you message: we have received your request; **velkomstansvarlig** will contact you at the email you provided (or via Matrix if you reached out there).
- No promise of instant access.
- Member flow may additionally show payment instructions on the page.
