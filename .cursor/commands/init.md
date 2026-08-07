# Init Command

Build a working mental model of this repo before doing anything else. This is a collection of standalone
Django prototypes exploring markdown-driven content, so orientation means two things: understanding the
repo-wide conventions, and understanding the one prototype you're about to work in.

## Process

1. **Read the overview**
   - Read `docs/overview.md`. It is the source of truth for the stack, repo layout, conventions, and
     non-goals.
   - For the active project (or when the task touches the real target site), also skim
     `docs/high-level-goals.md` and `docs/organizational-context.md`.
   - Note especially: prototypes are standalone and never import from each other, there is one shared uv
     environment at the repo root, and there is no JavaScript build step.

2. **Read the project index**
   - Read `docs/projects/index.md` to see which prototypes exist, which are active, and what question each
     one answers.
   - Identify which project the current task belongs to. If it isn't obvious, ask before reading further.
   - If the task is a new line of enquiry, don't force it into an existing project: check the open questions
     list and follow "Starting a new project" in the index instead. Steps 3, 4 and 6 below then apply to the
     nearest prior prototype (the one the new work builds on) rather than a project of its own.

3. **Read that project's docs, and only that project's**
   - Read the relevant `docs/projects/<project>/discussions/*.md` for the reasoning and decisions.
   - Read the newest `docs/projects/<project>/plans/*.md` for what is being built and what is still open.
   - Do not read other projects' docs. They are procedural logs of superseded thinking.

4. **Explore the prototype directory**
   - Each project usually maps to one directory under `prototypes/`. The project docs describe how that
     prototype is organised internally — follow them rather than assuming a layout, since structure is
     allowed to differ between prototypes.
   - List the directory, then read its settings and root URLs to see what the prototype actually uses and
     what it leaves out.

5. **Check dependencies**
   - Read the root `pyproject.toml` for the shared dependency set.
   - Dependencies are managed with `uv`. Commands run as `uv run python manage.py <cmd>` from inside a
     prototype directory; `uv add <pkg>` from the repo root.

6. **Trace one path end to end**
   - Pick a single request path and follow it from URL pattern through view to template.
   - Read the one or two files the trace shows to matter most.

7. **Synthesise and confirm**
   - Present a summary in this shape:

     ```
     Based on `docs/overview.md`, the `<project>` project docs, and `prototypes/<dir>/`, here is my
     understanding:

     - **Repo purpose:** [markdown-driven Django, prototype collection]
     - **This prototype's question:** [the assumption it exists to test]
     - **Stack in play:** [what's actually used here, and what's deliberately absent]
     - **Request flow:** [URL → view → content loading → template]
     - **Key files:** [the handful of files that matter for the current task, and why]
     - **Open questions I'd flag:** [anything the docs leave unresolved that affects the task]

     Is this correct, and where should I focus?
     ```

   - For a new project, swap the prototype-specific lines for: the question the new project answers, which
     open questions it claims, and what it inherits from the prior prototype.

## Guidelines

- **Overview first, then project, then code.** Don't start in the source tree.
- **Stay inside one prototype.** Cross-prototype abstraction is an explicit non-goal. If code needs sharing,
  copy it.
- **The project docs describe the structure.** Prototypes are free to organise themselves differently, so
  read their docs instead of assuming file names or layout.
- **Respect the non-goals.** No deployment, auth, API, or JS tooling — don't propose them.
- **High-level context is the goal.** Enough to act correctly, not exhaustive knowledge.
- **Ask rather than guess** when the project docs and the code disagree; note the disagreement, since the
  docs are authoritative for intent and may simply need updating.
