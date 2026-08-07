# Learnings from prototype 02

Written 2026-08-06, after building `prototypes/02-content-pipeline/`.

## What held up

- **The ingest pattern is small and boring, in a good way.** One model, one command, plain views. The
  ecosystem was right that this doesn't need a package.
- **Strict validation is the correct trade.** Prototype 01's `drafts: true` typo is now a loud error
  instead of a silent publish. The ingest step is the natural gate the filesystem approach lacked.
- **Derived vs. owned tables coexist cleanly.** The `Post` table is rebuilt at will; the auth tables
  (superuser for the admin) persist untouched beside it. This distinction matters more as the site grows —
  future models will not all be derived, so "delete the sqlite" stops being free at some point.
- **A read-only admin is a good inspection window.** Register the model, forbid add/change/delete: you can
  look at what ingest produced without pretending the admin is an editor.

## What feels fragile or unresolved

- **The authoring loop regression is the headline cost.** Save–ingest–reload is annoying immediately, at
  four files, with no scale excuse. The promising fix: dev-only middleware that re-runs the same sync per
  request (mtime-gated), rendering ingest errors as a readable error page. Deferred to the next project.
- **Sync-by-slug is untested against renames and relationships.** With one flat collection, deletes and
  renames are trivial. FKs between collections will stress it.
- **Deployment story is still on paper** (migrate → ingest → serve). Fine for this repo's non-goals.

## Practical notes for whoever builds next

- Copy, don't import: `pages/management/commands/ingest.py` holds the parse/validate/sync logic.
- `update_or_create` keyed on slug plus an `exclude(slug__in=...)` delete is all the sync needed here.
- Superuser for the admin: `admin` (created manually; survives re-ingest by design).
