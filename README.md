# dk-django-website

Prototypes for a Django website whose written content lives in **markdown files in git** — not in an admin
or CMS. Each prototype is a standalone experiment you can run and explore directly — pick one, `cd` in,
start the server. See [`docs/overview.md`](docs/overview.md) for the full picture.

The repo is also scaffolded for **rapid prototyping with AI**: isolated prototypes, written conventions,
and a project log under `docs/projects/` so experiments produce learnings, not just throwaway code. None
of that is required to browse or hack on a prototype — it is there when you want the *why* behind a
decision, or when an agent is helping you iterate.

## Quick start

Requires [uv](https://docs.astral.sh/uv/) and Python 3.12+.

```bash
uv sync                              # once, from the repo root

cd prototypes/NN-<slug>              # pick a prototype (see below)
uv run python manage.py migrate      # if that prototype uses the ORM
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

**Which prototype?** [`docs/projects/index.md`](docs/projects/index.md) lists them all — what each one
tests, which are active, and the matching `prototypes/NN-<slug>/` path. For onboarding detail on a
specific prototype, check for a `README.md` inside that directory first.

**Content loading:** Many prototypes keep git-owned markdown in sqlite and need a **sync or load step**
before pages show real content. Some re-sync on every request in `DEBUG`; others need explicit management
commands run once after `migrate`. The prototype's `README.md` has the exact command(s) — see below if
there isn't one yet.

## How this repo is organised

```
pyproject.toml          # shared Python environment (all prototypes use this)
prototypes/
  NN-<slug>/            # standalone Django project — manage.py, config/, apps, content, static
docs/
  overview.md           # stack, conventions, non-goals
  projects/
    index.md            # which prototype answers which question
    NN-<slug>/          # reasoning and decisions for that project
```

- **Prototypes never import from each other.** Copy code between them if needed; don't share it.
- **Internal layout varies by prototype** — app names, content folders, sync commands. That belongs in
  the prototype's own README or its docs under `docs/projects/NN-<slug>/`.
- **Everything is disposable** — sqlite files, migrations, and synced content can be deleted and rebuilt.

## Stable entry points

These paths exist in every prototype; what lives inside them does not:

| Path | Role |
|---|---|
| `prototypes/NN-<slug>/manage.py` | Run Django commands from this directory |
| `prototypes/NN-<slug>/config/` | Settings and root URL routing |
| `prototypes/NN-<slug>/README.md` | Onboarding and content-loading commands for that prototype |
| `docs/projects/index.md` | Authoritative list of prototypes and project docs |
| `docs/overview.md` | Repo-wide stack and conventions |

## AI-assisted workflow (optional)

In Cursor, **`/init`** kickstarts an agent with the same orientation a human would follow — overview,
project index, then the relevant prototype. See [`.cursor/commands/init.md`](.cursor/commands/init.md).

## Read next

- [`docs/overview.md`](docs/overview.md) — tech stack, layout, what we explicitly don't build
- [`docs/projects/index.md`](docs/projects/index.md) — active work and completed experiments
- [`docs/organizational-context.md`](docs/organizational-context.md) — what the target site is for (when
  working on public-facing pages)
