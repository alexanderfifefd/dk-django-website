# Organizational and UX Implications of Git Identity

**Question:** By moving identity and ownership assertions into git (markdown frontmatter) rather than a database or SSO system, what secondary effects does this have on the collective's UX, organization, and maintainability?

## 1. The Control Plane vs. Data Plane Split

**Observation:** If maintainers edit their profiles in git, they do not need a Django login. If we later add SSO to Django, it would be purely for end-users (e.g., consumers managing newsletter preferences), not for collective members doing maintenance.

**Implication:** This creates a clean architectural boundary.
- **Control Plane (Git/Forgejo):** Where the collective works. Requires strong authentication, 2FA, and audit logs.
- **Data Plane (Django):** The public face. Stateless, disposable, and requires no special privileges for members.

## 2. Locality of System Ownership

**Observation:** System ownership (e.g., `teamlead: alex`) should live in the system's markdown file
(`content/systems/atlas/system.md`), not the member's profile.

**Implication:**
- **Locality:** To find out who owns Atlas, you look at the Atlas file.
- **Security via PRs:** If ownership is defined in the system file, changing the owner requires a PR against that file. You can use forge branch protection to ensure only the current owner (or an admin) can approve a handover. If ownership was in the member profile, anyone could theoretically open a PR to their own profile claiming ownership of a system they don't maintain.

## 3. The "External Contributor" Fallback (UX)

**Observation:** If we link Forgejo PRs to `Member` profiles, PRs from random open-source contributors will fail the foreign key lookup because they don't have a `content/members/*.md` file.

**Implication:** The UI must handle this gracefully. If a PR has no linked `Member`, it should still render on the system's timeline, but the author's name should link directly to their Forgejo profile instead of an internal Django member page. This ensures the site accurately reflects *all* activity, not just the inner circle's.

## 4. Offboarding and "Alumni" (Organizational)

**Observation:** If a member leaves the collective and we delete their `content/members/*.md` file, the next Django sync will drop their `Member` record, breaking author attribution on all their historical PRs and articles.

**Implication:** We should not delete members. Instead, we need an `active: false` flag in the
frontmatter. Alumni profiles are hidden from the members index, but their historical URLs
(`/members/alice/`) must remain active so old content doesn't break.

## 5. Identity Rotation / Handle Changes (Maintainability)

**Observation:** If a member changes their Forgejo handle (e.g., from `alexanrf` to `alex-dk`), updating
their frontmatter to `forgejo: alex-dk` will link their new PRs, but might orphan old PRs if the forge
API still reports them under the old handle.

**Implication:** The `identities` frontmatter may eventually need to support arrays (e.g.,
`forgejo: [alex-dk, alexanrf]`). The site slug (filename) stays stable; only external mappings change.
See [member slug and references](./member-slug-and-references.md).
