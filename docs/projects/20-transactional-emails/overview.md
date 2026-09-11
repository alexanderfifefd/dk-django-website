# Transactional emails

**Question:** How do we wire join-style forms to Scaleway TEM so onboarding requests reach the collective — without auto-emailing visitors?

**Status:** built 2026-09-11

**Prototype:** `prototypes/20-transactional-emails/`

## Summary

Three join paths (**Follow us**, **Become a member**, **Build with us**) send a structured notification to **`hei@datakollektivet.no`**. A welcomer handles onboarding manually. Each notification includes submitted fields plus a **suggested reply template**. No automated email to the visitor; member payment details appear on the thank-you page.

## Reading order

1. **[pivot-to-manual-onboarding.md](./discussions/pivot-to-manual-onboarding.md)** — why manual
2. **[join-flows.md](./discussions/join-flows.md)** — three paths (product intent; English slugs in prototype)
3. **[forms-and-css.md](./discussions/forms-and-css.md)** — Django Forms, `as_div`, cascade styling
4. **[technical-scope.md](./discussions/technical-scope.md)** — mail, TEM, prototype layout
5. **[2026-09-11-prototype-20-transactional-emails.md](./plans/2026-09-11-prototype-20-transactional-emails.md)** — plan and verification
6. **[scope-and-options.md](./discussions/scope-and-options.md)** — superseded auto-email exploration
