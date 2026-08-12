# Plan: Prototype 05 (Git Identity)

**Goal:** Prove that we can link cross-system activity (Forgejo PRs and issues) to a user's site profile using git-backed identity assertions, without relying on SSO or Django authentication.

This builds directly on the ingest patterns established in `04-forge-issues`.

## Steps

1. **Member Content Structure**
   - Create a `content/members/` directory.
   - Add markdown files for members with an `identities` dictionary in the frontmatter (e.g., `forgejo: username`).

2. **Member Ingestion**
   - Create a `Member` model in Django.
   - Write a `sync_members` command to ingest the markdown files, storing the parsed identities.

3. **Link Forgejo Activity**
   - Update the Forgejo sync logic (from Prototype 04).
   - When ingesting an `Issue` or `PullRequest`, attempt to link it to a `Member` by matching the Forgejo author username against the `Member.identities.forgejo` field.

4. **Profile Pages**
   - Build a member profile view.
   - Render the member's markdown bio.
   - Display a live feed of their recent Forgejo PRs and issues, queried via the new foreign key relationship.

## Success Criteria
- A member's page successfully displays both their authored markdown content and their automated forge activity.
- The linking is robust and driven entirely by the frontmatter configuration.

## Outcome (2026-08-08)

**Answer: yes.** Member profiles live in `content/members/*.md` with an `identities` map in frontmatter. `sync_issues` resolves `author` against `identities.forgejo` and sets a nullable `Issue.member` FK. Member pages show markdown bio plus linked PRs and open issues. No SSO or Django auth required.
