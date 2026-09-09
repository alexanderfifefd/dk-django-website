# Discussion: content model — initiatives and articles

**Project:** `articles-and-initiatives`
**Date:** 2026-09-03
**Builds on:** `docs/systems-and-initiatives.md`, prototype 07 content shape, prototype 15 article loader
**Status:** open — draft model for discussion

## The question

What is the **minimum initiative abstraction** that still pairs meaningfully with articles, when copied
from 07 onto prototype 15's simpler stack?

## Content tree (draft)

```
content/
  articles/
    why-governance-documents.md      # initiative: governance-documents
    building-the-collective-homepage.md
    …
  initiatives/
    governance-documents/
      initiative.md
      updates.json                   # TBD — include in v1?
    build-website/
      initiative.md
    build-sso/
      initiative.md
```

No `content/systems/`, no `content/members/` in prototype 17.

## Initiative — `initiative.md`

### Frontmatter (draft)

```yaml
---
title: Governance documents
summary: Establish governance documents for the collective.
status: active          # proposed | active | paused | completed
start_date: 2026-07-01
end_date:               # optional
takers: [daniel]        # slug strings; displayed as text, not linked
recruiting: open        # optional; TBD whether UI shows it in v1
loomio: https://…       # optional; TBD whether detail page links it
matrix: "#room:…"        # optional
---
```

Body markdown → pitch HTML (same pipeline as articles).

### Fields explicitly deferred

| Field | In 07 | In 17 (draft) | Reason |
|---|---|---|---|
| `systems: [website]` | M2M to System | **Out** | No systems collection |
| `takers` → Member FK | Yes | **String/slug list** | No members collection |
| `updates.json` | Yes | **TBD** | Useful on detail page; adds loader complexity |
| `recruiting` | Yes | **Field yes, UI maybe** | Field is cheap; cards deferred |
| `loomio`, `matrix` | Yes | **TBD** | External links on detail — low cost if present |

### ORM sketch (draft)

```python
class Initiative(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    body_html = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices)
    recruiting = models.CharField(max_length=20, blank=True, default="")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    takers = models.JSONField(default=list, blank=True)  # slug strings
    loomio_url = models.URLField(blank=True)
    matrix_room = models.CharField(max_length=200, blank=True)
    updates = models.JSONField(default=list, blank=True)  # if updates.json in scope
```

## Article — extend prototype 15

### Frontmatter change

```yaml
---
title: Why we need governance documents
date: 2026-07-15
author: Daniel              # plain string (unchanged from 15)
initiative: governance-documents   # NEW — optional slug; validated at sync
summary: …
draft: false
---
```

No `system` field — no systems in this prototype.

### ORM change

```python
class Article(models.Model):
    …
    initiative = models.ForeignKey(
        Initiative, on_delete=models.PROTECT,
        related_name="articles", null=True, blank=True,
    )
```

### Sync validation

On article sync:

- if `initiative` is set, slug must exist in `Initiative` table
- unknown slug → abort with readable error in dev (same pattern as 15 frontmatter validation)

**Order:** initiatives loaded first, then articles.

## Site surfaces (draft)

| URL | Template | Content |
|---|---|---|
| `/` | `home.html` | Hero + initiatives teaser + articles teaser (extend 15 home) |
| `/initiatives/` | `initiatives/index.html` | All initiatives grouped by status |
| `/initiatives/<slug>/` | `initiatives/detail.html` | Pitch, status, takers, related articles, updates (if in scope) |
| `/articles/` | existing | Add initiative badge when FK set |
| `/articles/<slug>/` | existing | Link back to initiative |

**Navigation (draft):** add **Initiatives** to header nav — placement TBD (left of Articles like 07's
pattern, or all right-aligned like current 15).

## Seed content (candidates from 07)

**Initiatives**

| Slug | Status | Notes |
|---|---|---|
| `governance-documents` | `active` | Pairs with article `why-governance-documents` |
| `build-website` | `active` | Pairs with `building-the-collective-homepage` |
| `build-sso` | `completed` | Shows completed state on index |

**Articles** — port a small set with `initiative:` set where 07 had it; drop `author` member slugs →
display names.

## CSS impact

Prefer reusing prototype 15 primitives:

- Initiative index → `card` list (same as article index)
- Status → badge modifier on card or detail header (new small rules in `components.css` or `pages.css`)
- Detail layout → `content-section` + existing prose styles

No new CSS layer; extend 15's files surgically.

## What would prove the abstraction works

1. Edit `initiative.md` in git → reload → detail page updates
2. Add `initiative:` to an article → article shows badge; initiative detail lists it
3. Reference unknown initiative slug in article → sync error in dev
4. Index groups by status; completed initiative visually distinct
5. Home surfaces at least one active initiative without systems/members on the page

## Decisions needed before plan

- [ ] Include `updates.json` in v1?
- [ ] Show Loomio/Matrix links on detail when set?
- [ ] Show `recruiting: open` on index cards?
- [ ] Nav placement for Initiatives
- [ ] `load_content` vs extended middleware naming
