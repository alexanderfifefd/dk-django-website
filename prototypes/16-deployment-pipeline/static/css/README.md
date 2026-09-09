# CSS structure

Hand-written CSS, no build step. Load order is fixed in `base.html`:

```
tokens.css      → variables only
base.css        → reset, body, typography, links
layout.css      → header, stripe, footer
components.css  → reusable UI (empty here)
pages.css       → route-specific rules (empty here)
```

## Rules

- No hex outside `tokens.css` — use `var(...)`.
- No selectors in `tokens.css`.

Full reasoning lives in prototype 15: `docs/projects/15-css-structure/`.
