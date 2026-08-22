---
title: Markdown and article components
date: 2026-08-22
author: Alexander
summary: A living reference for authors — base markdown, callouts, CTA banners, and syntax-highlighted code.
---

This article lists everything you can use in `content/articles/*.md` today. Edit this file, reload the
browser (in dev), and see the result.

## Headings

Use `#` through `######` for section structure. Only use one `#` per page — the title comes from
frontmatter.

## Emphasis and links

Write *italic* with asterisks, **bold** with double asterisks, and
[links](/articles/) with standard markdown syntax.

Smart typography converts `--` to an en dash — like this — and straight quotes to curly quotes.

## Lists

Unordered lists:

- First item
- Second item with **bold**
- Third item with `inline code`

Ordered lists:

1. Sync markdown from git
2. Validate frontmatter and shortcodes
3. Store rendered HTML in the database

## Blockquote

> Plain blockquotes still work for simple quotations or asides that do not need a styled callout box.

## Inline and fenced code

Use `inline code` for short fragments. For longer snippets, use a fenced block without a language tag:

```
load_articles reads content/articles/*.md
```

## Syntax-highlighted code

Add a language tag to the fence for Pygments highlighting:

```python
def greet(name: str) -> str:
    return f"hello, {name}"
```

```html
<aside class="callout callout-note" role="note">
  <p>Highlighted HTML example.</p>
</aside>
```

## Tables

| Feature | Author syntax |
| --- | --- |
| Headings | `#` … `######` |
| Callout | `:::callout type="note"` |
| CTA | `:::cta` with YAML fields |
| Code | ` ```python ` fenced block |

## Callouts

Callouts draw attention to a note, warning, or tip. Markdown inside the block is parsed normally.

:::callout type="note"
This is a **note** callout. Use it for neutral context that helps the reader.
:::

:::callout type="warning"
This is a **warning** callout. Use it when the reader should slow down before continuing.
:::

:::callout type="tip"
This is a **tip** callout. Handy for shortcuts like running `load_articles` manually when middleware
is off.
:::

## CTA banner

A CTA banner is four fields — header, subheader, button label, and url — in YAML inside the fence:

:::cta
header: Join the collective
subheader: We maintain shared infrastructure and publish what we learn along the way.
button: See how to join
url: /join/
:::

## Not supported yet

These are planned or deferred to other projects:

- Article link cards (see project plan — render-time, not ingest)
- Figures with captions (needs a media/assets path)
- Timeline blocks
- Tabbed API examples
- POST forms inside articles (newsletter signup, etc.)
- Live data from the ORM (system badges, forge issues)

For site-wide CTAs that repeat on every page, use templates — not markdown shortcodes.
