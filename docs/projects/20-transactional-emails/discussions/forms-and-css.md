# Forms and CSS

**Project:** `transactional-emails`
**Date:** 2026-09-11
**Status:** decided (prototype 20)

How join-path POST forms are built and styled. Read alongside [technical-scope.md](./technical-scope.md).

## Validation: Django Forms

**Use Django Forms for POST data.** Not Pydantic — that stays the pattern for git ingest (frontmatter, loaders) elsewhere in the repo, not for HTML forms on this site.

Three form classes in `public/forms.py`, one per path — intentionally separate even where fields match:

| Form | Path | Fields |
|---|---|---|
| `FollowForm` | `/join/follow/` | email, newsletter (optional checkbox) |
| `MemberForm` | `/join/member/` | email, newsletter |
| `BuildForm` | `/join/build/` | email, interest (textarea) |

Conventions on each form:

- `label_suffix = ""` — no trailing colon on labels (Django default is `:`).
- Widget `attrs` for `placeholder` and `autocomplete` — presentation hints live in `forms.py`, not the template.
- `clean_*` methods for non-obvious rules (e.g. `BuildForm.clean_interest` strips whitespace).

**Rejected for this project:**

- Pydantic models + manual `request.POST` parsing
- `django-crispy-forms` — fights hand-written CSS; adds dependency
- One shared form class for follow + member — split for clarity and room to diverge
- `_handle_submission` view helper — three explicit views instead

## Templates: `{{ form.as_div }}`

Each join page inlines the form (no shared partial):

```django
<form method="post" action="" novalidate>
  {% csrf_token %}
  {{ form.as_div }}
  <div class="form-actions">
    <button type="submit" class="btn btn--primary">…</button>
  </div>
</form>
```

- **`as_div`** — Django wraps each field in a `<div>` with `<label>` then input. Not `as_p`, not `{{ form }}` (table), not per-field `{{ form.email }}` unless we need an exception.
- **`novalidate`** — server-side validation only; Django `EmailField` etc. handle errors.
- **Submit button** — outside `as_div`; Django does not render it.
- **Thank-you state** — view sets `submitted` / `submitted_email`; template swaps form for notice (unchanged pattern).

Django renders validation errors as `<ul class="errorlist">` above the field — not hand-placed `.field-error` spans.

## CSS: cascade from context, not form classes

Form styling does **not** use `form-stack` / `form-checkbox` classes on the `<form>` element (prototype 15 used those). Instead, rules cascade from where the form sits:

```css
.form-card__body form { … }
.form-card__body form > div { … }
.form-card__body form label { … }
.form-card__body form input:not([type="checkbox"]), …
.form-card__body form .errorlist { … }
```

Defined in `static/css/components.css`. Any form inside `.form-card__body` picks up join styling without extra classes on the markup.

**Checkbox layout:** Django `as_div` emits label then checkbox as **siblings**, not `<label><input>…</label>`. Flex + `order` on the field div puts the checkbox visually first; `label for="…"` still toggles the box:

```css
.form-card__body form > div:has(input[type="checkbox"]) {
  display: flex;
  …
}
/* input order: 1, label order: 2 */
```

**Accepted differences** from the old hand-written markup:

- Field wrappers are `<div>` (from `as_div`), not `<p>`
- Errors are `.errorlist`, not `.field-error`
- Checkbox DOM order differs; visual result is close enough

To style forms elsewhere on the site, either wrap them in `.form-card` > `.form-card__body` or extend the cascade with a new scoped parent — do not rely on a class on `<form>` itself.

## View wiring (reminder)

One view per path. Pattern: instantiate form from `request.POST`, `form.is_valid()`, `notify_onboarding_inbox(..., context=form.cleaned_data)`, render with `form` in context. Sync send; `try/except/else` for send failure vs success.

No ORM — mailbox is the record. No rate-limit table in v1.

## Promoting to the real site

When merging join flows into a richer prototype (e.g. 15):

1. Copy `forms.py` pattern (three classes, `label_suffix`, widget attrs).
2. Copy cascade block from `components.css` or merge into prototype 15's form-card section.
3. Keep `as_div` + inline template unless a specific field needs manual rendering.
4. Do not introduce Pydantic for POST bodies on the public site.
