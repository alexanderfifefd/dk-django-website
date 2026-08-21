# Plan: prototype 02 — markdown ingested into the ORM

**Project**: `content-pipeline`
**Discussion**: `docs/projects/02-content-pipeline/discussions/who-owns-the-markdown-layer.md`
**Prototype directory**: `prototypes/02-content-pipeline/`
**Status**: built — see Outcome below

## Goal

The same small site as prototype 01 (home, about, blog), but content reaches the pages through the ORM: a
management command ingests markdown files into the database, and views query it. Find out what the ORM buys
(querying, validation, a real gate against bad frontmatter) and what the authoring loop loses.

## Scope

In:

- Copy prototype 01's site wholesale (app, templates, CSS, content folder), then swap the content layer.
- A `Post` model: slug, title, date, tags (JSONField), summary, body_html. **Rendered HTML only** — the
  database is a derived artifact, rebuilt from files, never edited and never rebuilt from.
- `manage.py ingest`: walks `content/blog/`, validates, renders, and syncs — new files inserted, changed
  files updated, deleted files' rows removed. `--flush` wipes the table first and rebuilds from nothing.
- **Strict validation**: unknown frontmatter keys, unparseable dates, or wrong types fail the whole ingest
  with a clear message and write nothing. This is the gate prototype 01 lacked — `drafts: true` becomes an
  error instead of a silent publish.
- Drafts (`draft: true`) are simply not ingested.
- Views use querysets for listing and lookup; no filesystem access at request time.

Out:

- File watcher or auto re-ingest — the manual command is the honest test of losing save-and-reload.
- Tag pages, pagination, search, scale testing, draft preview.

## Deployment note (not built, just the story)

Ingest runs at deploy time: migrate, then ingest, then serve. Any environment rebuilds its database from the
repo; the sqlite file is never precious.

## How we know it worked

- Fresh checkout: `uv sync`, `migrate`, `ingest`, `runserver` — all three sections render from the database.
- Editing a file changes nothing until `ingest` re-runs; after it, the page shows the edit.
- A file with an unknown key or bad date fails ingest loudly and the database is untouched.
- Deleting a file and re-ingesting removes its post; `--flush` + ingest reproduces identical content.
- The draft post from prototype 01's content is absent from the database entirely.

## Outcome

Built and validated 2026-08-06, same day. All criteria met. Notes against the plan:

- **The swap was small.** Copying prototype 01 and replacing its content layer took a `Post` model, a
  ~100-line ingest command, and simpler views. Templates needed no changes — the dataclass fields became
  model fields with the same names.
- **Added beyond plan**: a read-only admin for `Post` (inspection window; derived rows shouldn't be
  editable) and rewritten sample content, since the copied posts described prototype 01's behaviour.
- **The authoring loop regression is real.** Save–ingest–reload was annoying within minutes of use. This,
  not anything about the pipeline itself, is the main finding — see the learnings doc and the
  `integration-layer` project that picks it up.
