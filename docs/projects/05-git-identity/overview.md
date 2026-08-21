# Git Identity

**Question:** How do we link a member's site profile to their cross-system activity (Forgejo PRs, issues,
and eventually other services)?

**Answer:** Git-backed identity assertions. Member profiles live in `content/members/<slug>.md` with an
`identities` map in frontmatter. The filename is the canonical slug for in-repo references; external
handles (e.g. `forgejo: alexanrf`) bridge to cached forge activity at sync time. No SSO or Django auth
required for this to work.

**Prototype:** `prototypes/05-git-identity/` — built and validated (2026-08-12).

**Supersedes:** the Keycloak-shaped JSON member fixture from `integration-layer` / prototype 03. Member
profiles are now git-owned like systems and articles.

## How to read this project

Start with [federated identity via git](./discussions/federated-identity-via-git.md) for the core decision.
Read [member slug and references](./discussions/member-slug-and-references.md) for how members are
referenced across content. The other discussions cover rejected alternatives and implementation detail.

## File index

### Discussions

| File | Summary |
|---|---|
| [sso-and-account-linking.md](./discussions/sso-and-account-linking.md) | Why shared SSO (e.g. Keycloak) on Django and Forgejo is good for login but brittle for linking activity across systems. Evaluates Forgejo-as-IdP and Django-as-IdP; rejects both for this architecture. |
| [federated-identity-via-git.md](./discussions/federated-identity-via-git.md) | **Core decision.** Use markdown frontmatter to assert external identities (`identities.forgejo`, etc.). Profiles edited in git, not via a CMS. Social trust (PR review) prevents fraudulent identity claims. |
| [member-slug-and-references.md](./discussions/member-slug-and-references.md) | **Canonical ID convention.** Filename = site slug (same rule as system directories). Three layers: slug for references, `name` for display, `identities` for external systems. Covers renames, alumni, and anti-patterns. |
| [organizational-implications.md](./discussions/organizational-implications.md) | UX and org fallout: control plane vs data plane split, system ownership on the system file, external contributor fallback, alumni offboarding, forge handle rotation. |
| [forgejo-api-for-identity.md](./discussions/forgejo-api-for-identity.md) | What the Forgejo API actually exposes for users and authorship. Confirms linking happens at ingest from repo-scoped issue data; no global author search; activity feed is wrong for member profiles. |

### Plans

| File | Summary |
|---|---|
| [2026-08-08-prototype-05-git-identity.md](./plans/2026-08-08-prototype-05-git-identity.md) | Implementation plan and outcome: `sync_members`, `Issue.member` FK via `identities.forgejo`, member profile pages, members index. |

## Reading order

1. [federated-identity-via-git.md](./discussions/federated-identity-via-git.md) — the approach
2. [member-slug-and-references.md](./discussions/member-slug-and-references.md) — how to reference members in content
3. [forgejo-api-for-identity.md](./discussions/forgejo-api-for-identity.md) — what the forge API supports
4. [organizational-implications.md](./discussions/organizational-implications.md) — edge cases and org policy
5. [sso-and-account-linking.md](./discussions/sso-and-account-linking.md) — what we rejected and why (optional; useful if SSO comes back on the agenda)

## Related docs

- `docs/organizational-context.md` — Member noun updated to reflect git-backed profiles
- `docs/projects/index.md` — repo-wide project list
- `docs/projects/04-forge-issues/` — predecessor; forge issue/PR ingest pattern this project extends
