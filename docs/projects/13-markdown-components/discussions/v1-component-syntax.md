# V1 component syntax

**Project:** `markdown-components`
**Date:** 2026-08-22

## Question

What should authors write in `.md` files for callout, CTA banner, and syntax-highlighted code — and what
HTML should ingest produce?

## Syntax choices

We considered:

- **Pymdown-style fences** — `:::note` … `:::` (familiar from MkDocs, Material)
- **WordPress-style** — `{% callout %}…{% /callout %}` (looks like Django; confusing)
- **YAML inside fences** — structured CTAs without inventing a parser

**Decision:** pymdown-style **`:::type`** fences for block components; standard **fenced code** for
highlighting (no new syntax for code).

## Callout

```markdown
:::callout type="note"
Markdown **inside** the callout is allowed — parsed as markdown before the block is wrapped.
:::

:::callout type="warning"
Keep backups before you run migrations.
:::

:::callout type="tip"
Use `load_articles` manually when middleware is off.
:::
```

| Field | Required | Values |
|---|---|---|
| `type` | yes | `note`, `warning`, `tip` |

**Ingest output (shape):**

```html
<aside class="callout callout-note" role="note">
  …inner HTML from markdown…
</aside>
```

Unknown `type` → validation error at sync.

## CTA banner

```markdown
:::cta
header: Join the collective
subheader: We maintain shared infrastructure and publish what we learn.
button: See how to join
url: /join/
:::
```

| Field | Required | Notes |
|---|---|---|
| `header` | yes | Short heading |
| `subheader` | yes | One or two sentences |
| `button` | yes | Label on the primary button |
| `url` | yes | Path or absolute URL; rendered as `<a class="btn btn-primary">` |

Inner content below the YAML header is **not** supported in v1 — four fields only.

**Ingest output (shape):**

```html
<aside class="article-cta">
  <h2 class="article-cta-header">…</h2>
  <p class="article-cta-subheader">…</p>
  <p><a class="btn btn-primary" href="…">…</a></p>
</aside>
```

Reuse visual language from home/join CTA panels (`--bg-code`, primary button tokens).

## Article callout (planned — render-time)

Not implemented in v1. Author syntax will be:

```markdown
:::article
slug: building-the-collective-homepage
:::
```

At **ingest**, this becomes a placeholder (`data-article-slug`). At **render**, title and summary are read
from the `Article` ORM row. See [article-callout.md](./article-callout.md).

## Syntax-highlighted code

No new author syntax — standard fenced blocks with a language tag:

````markdown
```python
def hello(name: str) -> str:
    return f"hello, {name}"
```
````

**Ingest:** enable a highlighting extension on the existing `render_markdown()` path (e.g. Python-Markdown
`codehilite` with Pygments). Store highlighted `<pre><code class="language-python">…</code></pre>` in
`body_html`.

| Concern | Choice |
|---|---|
| Line numbers | off in v1 |
| Unknown language | fall back to unhighlighted fenced block |
| CSS | `.highlight` / `.codehilite` rules aligned with `--bg-code` and `--text` |

## Base markdown (unchanged)

The showcase article should also demonstrate what already works via `MARKDOWN_EXTENSIONS`:

| Feature | Author syntax |
|---|---|
| Headings | `#` … `######` |
| Emphasis | `*italic*`, `**bold**` |
| Links | `[text](url)` |
| Lists | `-` / `1.` |
| Blockquote | `>` |
| Inline code | `` `code` `` |
| Fenced code | ` ``` ` (plain, no lang) |
| Tables | pipe tables |
| Smart typography | `smarty` extension (quotes, dashes) |

## Showcase article

Add `content/articles/markdown-features.md` (slug TBD) — a deliberate style guide / living reference:

1. Intro — this page lists what authors can use
2. Section per base markdown feature (minimal example each)
3. Section per component (callout variants, one CTA, highlighted code in two languages)
4. Short “what is not supported yet” — figures, timeline, forms

Link from home or articles index is optional; the article itself is the primary deliverable for authors.

## Validation

- Callout and CTA blocks: Pydantic models parsed from the YAML header line(s) inside the fence
- Malformed fences: error message includes article filename and line context
- Nesting callouts: not supported in v1
