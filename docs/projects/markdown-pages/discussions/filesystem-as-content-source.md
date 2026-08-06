# Discussion: the filesystem as the whole content layer

## The question

Can a Django site treat a folder of markdown files as its content layer — no database *for content*, no
build step — and still feel good to author with and fast enough to serve? (A database may well exist in the
project for other things; the question is whether written content needs one.)

Django's defaults pull the other way. The ORM, the admin, and most of the ecosystem assume content is rows.
Writing content as files instead means giving up the admin, migrations, and querying, and getting back plain
text files that live in git, diff cleanly, and can be edited without a running server.

## What "content as files" means here

- A file's **path** determines its URL. `content/notes/hello.md` is served at `/notes/hello/`.
- A file's **frontmatter** carries its metadata: title, date, tags, draft status.
- A file's **body** is markdown, converted to HTML at request time.
- Listing pages (an index, a tag page) come from walking the content tree, not from a query.

The build-step-free part is the deliberate difference from the static generators that popularised this
authoring model. Those tools resolve the whole content tree ahead of time and emit HTML. Here Django resolves
it per request, which keeps the authoring loop instant but moves all the cost to request time. Whether that
trade is acceptable is the main thing we want to find out.

## Options considered

**1. Read and parse per request, nothing cached.** Simplest possible thing. A request maps a URL to a file
path, reads that one file, parses it, renders it. Listing pages walk the directory. No state anywhere.

- Cheap to build, trivially correct, and edits appear the moment the file is saved.
- Every listing page pays for reading every file's frontmatter. Cost grows with the content tree.

**2. Filesystem as source of truth, sqlite as a derived index.** Files still own the content; a management
command (or a startup pass) walks the tree and writes metadata into sqlite so listings and filters can be
queried.

- Listing pages get cheap and the ORM comes back for anything relational.
- Reintroduces a sync step, staleness, and migrations — the things files were meant to avoid.

**3. Filesystem plus an in-memory index.** Walk the tree once at startup into a dict, invalidate on file
mtime.

- Fast listings without a database.
- Invalidation logic is the kind of thing that looks simple and isn't.

## Decision

**Start with option 1, and treat the storage question as unresolved on purpose.**

Prototype 01 builds the naive version — no cache, no index, no ORM — because it is the only option that can
tell us whether the other two are needed. Adding a cache before we've seen the uncached version is a guess.
If per-request reads turn out to be fine at the content sizes we care about, options 2 and 3 stay unbuilt.

What would push us to option 2 or 3: listing pages that feel slow with a realistic number of files, or a
content relationship (tags, backlinks, ordering across collections) that is genuinely awkward without a
query language.

## Constraints we're holding to

- Plain Django templates and hand-written CSS. No JavaScript build step. HTMX only if a page genuinely
  needs it — prototype 01 doesn't.
- Local development only. No deployment, no auth, no production settings.
- Prototypes stay standalone. When prototype 02 needs prototype 01's markdown code, it copies it.
