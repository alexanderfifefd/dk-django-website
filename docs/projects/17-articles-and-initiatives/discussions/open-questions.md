# Open questions — prototype 17

**Project:** `articles-and-initiatives`
**Date:** 2026-09-03

Decisions to close before writing the build plan.

## Content model

1. **`updates.json` on initiatives — in v1 or deferred?**
   - *In favour:* detail page feels complete; same loader pattern as 07; reuses system update markup from 15 if we copy partials.
   - *Defer:* one less file type; pitch + related articles may be enough to validate the abstraction.
   - **Needs:** your call.

2. **External links (`loomio`, `matrix`) — store and render in v1?**
   - Cheap to ingest; detail page "Discussion" block is ~10 lines of template.
   - **Lean:** include fields + detail links if present; skip if you want maximum cut.

3. **`recruiting: open` — field only, or visible on index?**
   - Org model treats recruiting as separate from lifecycle (`docs/systems-and-initiatives.md`).
   - Recruiting *cards* on join/volunteer are out (needs 07-scale models).
   - Small badge on initiative card may still be worth it.
   - **Needs:** field-only vs badge on index.

4. **Taker display — slug as text or resolved display name?**
   - Without members, `daniel` renders as "daniel" unless we add an optional `taker_names` map (probably overkill).
   - Could use Title Case as a presentation fallback.
   - **Lean:** show slug strings; polish when members return.

## Sync and loaders

5. **Command name: `load_content`, `load_all`, or keep `load_articles` as orchestrator?**
   - Must sync initiatives → articles in order.
   - **Lean:** rename to `load_content` (07 vocabulary) or add `load_initiatives` called from middleware before articles.

6. **Strict vs soft cross-ref validation**
   - Strict: unknown `initiative:` slug aborts sync (07 behaviour).
   - Soft: warn and null the FK.
   - **Lean:** strict — matches 07 and catches authoring mistakes early.

## UI and scope

7. **Home page — how much initiative surfacing?**
   - A) One "Active initiatives" section (3 cards max) — mirrors 07 intent, minimal.
   - B) Initiatives mentioned in prose only; index is the hub.
   - C) Full 07 home block (active + proposed groups).
   - **Lean:** A.

8. **Nav — where does Initiatives go?**
   - A) Left group: Initiatives | Articles (07 pattern minus Systems).
   - B) Right group before About: Articles, Initiatives, About, Join (minimal change to 15 header).
   - **Needs:** preference.

9. **Design lab — keep `/design-lab/` unchanged?**
   - Fork copies it wholesale from 15.
   - **Lean:** yes — no initiative components in catalog until we know badge/card patterns.

10. **Project slug / prototype directory name**
    - `17-articles-and-initiatives` — descriptive, matches two nouns.
    - Alternatives: `17-initiatives`, `17-content-nouns`.
    - **Lean:** `17-articles-and-initiatives` unless you prefer shorter.

## Out of scope confirmation

Confirm these stay **out** for prototype 17 (call out if any should come back in):

- Systems collection and `Article.system`
- Members, groups, member-initiative links
- Forge issues/PRs
- Join-path recruiting integration
- Markdown shortcodes beyond what 15 already has

## Next step

Once the above are answered (even roughly), write:

`docs/projects/17-articles-and-initiatives/plans/2026-09-03-prototype-17-articles-and-initiatives.md`

Then fork 15 and build.
