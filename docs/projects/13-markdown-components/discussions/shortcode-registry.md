# Shortcode registry and package layout

**Project:** `markdown-components`
**Date:** 2026-08-22

## Question

How should ingest-time shortcodes be organised in Python as we add more block types?

## Problem

The first implementation put everything in one `shortcodes.py`: regex, dispatch, callout, CTA, and shared
helpers. That worked for two blocks but meant every new component touched the same file in three places
(pattern, `if name == …`, render function).

## Options considered

| Approach | Pros | Cons |
|---|---|---|
| **Single module** | Simple at n=2 | Does not scale; merge conflicts |
| **Package + explicit registry** | One file per component; grep-friendly list of supported blocks | Slightly more folders |
| **Auto-discovery** (import all modules in a folder) | Adding a file is enough | Magic; hard to see what's supported |
| **Markdown extension** (custom block processor) | Idiomatic for some stacks | Fights our order (shortcodes before markdown, callout body is markdown) |

## Decision

**Package + explicit registry** under `public/loaders/shortcodes/`:

```
shortcodes/
  __init__.py      # public API: expand_shortcodes()
  engine.py        # find ::: fences, loop, dispatch
  errors.py        # ShortcodeError, YAML helpers
  types.py         # Block, Context
  registry.py      # HANDLERS dict — the canonical list
  callout.py       # render(block, ctx)
  cta.py
```

Each component exposes one function: `render(block: Block, ctx: Context) -> str`.

`registry.py` maps name → handler. **No auto-discovery** — adding a block is deliberately two steps (new
module + one registry line) so supported syntax stays visible in code review.

The engine does not know callout from CTA — it only looks up `block.name` in `HANDLERS`.

## Ingest vs live shortcodes

The registry is for **ingest-time** blocks only (self-contained HTML at sync).

Cross-entity shortcodes (article callout, system badge) will **not** grow `Context` with catalog fields.
They get a separate render-time path — see [article-callout.md](./article-callout.md) and
[when-to-expand.md](./when-to-expand.md).

## Adding a new ingest shortcode

1. Add `shortcodes/<name>.py` with `render(block, ctx)`
2. Register in `registry.py`
3. Document author syntax in [v1-component-syntax.md](./v1-component-syntax.md)
4. CSS in `static/css/site.css`
5. Example in `content/articles/markdown-features.md`

## Outcome

Split landed in prototype 13 (2026-08-22). Import path unchanged:
`from public.loaders.shortcodes import expand_shortcodes`.
