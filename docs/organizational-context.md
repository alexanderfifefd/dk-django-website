# Organizational context

What the site actually is, so the data model has something real to mirror.

## The collective

A software collective maintains a set of **systems** — services and software — for its **members**. The
site is the collective's homepage: it presents the collective, markets each system, surfaces operational
updates, and carries a blog. Members market, give updates about, and communicate about the systems.

## The nouns

- **Member**: a person in the collective. Identity is owned by Keycloak (prototypes: a Keycloak-shaped
  fixture); Django caches a lightweight profile. Nothing in git creates a member.
- **System**: software the collective maintains. Has a marketing/description page, one **teamlead**
  (single accountable person), several **admins**, operational updates, and related articles.
- **Update**: a short operational notice scoped to one system ("downtime expected"). Record-like data,
  not prose.
- **Article**: a blog post by a member — about one system, or collective-wide when it names none.

## How collaboration works

Through git pushes, not CMS accounts. Anyone in the collective edits content in the repo; review happens
in the forge. Roles carried in the data (teamlead, admins) are presentation today and the seed of
authorization later — e.g. CODEOWNERS on a system's content folder, or Django-side permission checks once
Keycloak is wired up for real. Out of scope for the prototypes.
