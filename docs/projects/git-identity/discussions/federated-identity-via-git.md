# Federated Identity via Git

**Question:** If SSO is too brittle for linking a user's cross-system activity (like Forgejo PRs) to their site profile, how do we establish identity?

## The Approach: Git-Backed Identity Assertion

Instead of relying on complex API verification or OAuth flows, we use markdown frontmatter to manually assert identity. The source of truth for "who owns what" lives in git.

A member's profile file (`content/members/alexander.md`) would look like this:

```yaml
---
name: Alexander
role: Core Maintainer
identities:
  forgejo: alexander
  matrix: "@alexander:matrix.org"
---
This is my profile description...
```

## Why this fits the architecture

1. **Explicit and unbreakable:** Django doesn't have to guess who owns what. When Django ingests this file, it knows exactly which Forgejo PRs belong to the member because the mapping is hardcoded in the data.
2. **Social Trust over Cryptographic Trust:** To prevent someone from putting `forgejo: torvalds` in their frontmatter to steal credit, we rely on the collective's existing social layer: the forge's PR review process. A human maintainer reviews the profile change in git and rejects it if it's fraudulent.
3. **Eliminates the need for a CMS:** We discussed allowing users to log into Django to edit their markdown profiles. However, providing an edit UI turns Django into a CMS, violating the principle that git is the source of truth. By keeping edits in git, Django remains a pure, read-only integration layer.
4. **Delays the need for Django Auth:** If users edit their profiles via git, and we link their activity via frontmatter, Django doesn't actually need an authentication system right now to fulfill the site's goals.

## Decision

We will proceed with Git-Backed Identity for Prototype 05. The prototype will focus on ingesting member profiles with identity mappings and linking them to the Forgejo activity synced in Prototype 04.
