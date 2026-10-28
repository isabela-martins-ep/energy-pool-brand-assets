# Visual QA checklist for AI-generated assets

Run before delivering any generated or adapted visual. Definitions (OFFICIAL / OBSERVED / `TO BE PROVIDED`) are in [`BRAND_RULES.md`](BRAND_RULES.md); token method in [`TOKENS.md`](TOKENS.md).

**Three kinds of resource, never confused:** an *officially validated resource* (logo files, token exports), a *creation inspired by references* (any AI output), and a *creation verified as compliant* (every criterion below checked `Compliant`). Visual resemblance to Energy Pool is not evidence of compliance.

**Statuses:** `Compliant`, `Non-compliant`, `Not verifiable` (say why). `Not verifiable` is never treated as compliant. If a rule is `TO BE PROVIDED`, the item is `Not verifiable`.

**Blocking rule:** a `Non-compliant` or `Not verifiable` result on a criterion marked **Blocking = Yes** prevents `Ready for human approval` and `Ready to publish`. It may be delivered only as an explicitly labelled `Exploration` or `Not verifiable` draft.

**Automatable:** Yes = a script or file read can check it; Partly = tool-assisted, then confirm; No = human only. Every visual still needs human approval before publication.

| # | Criterion | What to check | Source | Automatable | Human validation | Blocking |
|---|---|---|---|---|---|---|
| 1 | Source manifest and consultation | Required files are listed, actually read/viewed, and inaccessible files are named; a URL/path alone is not evidence | `SKILL.md` step 1 | Partly | Reviewer confirms the list | Yes |
| 2 | Color tokens | Each color maps to a token and its exact HEX (`resolve_token.py` or JSON); none estimated from images | `colors/*.json`, `TOKENS.md` | Yes for source/HTML/SVG; Partly for raster | Role of each color for this medium (`TO BE PROVIDED`) | Yes |
| 3 | Color usage | No state colors (success, danger, warning, info, link) or component tokens used decoratively; `energy-assets` only for their source | `TOKENS.md` | Partly | Yes | Yes |
| 4 | Contrast / legibility | Text/background contrast measured and stated; required level is `TO BE PROVIDED` | Output file | Partly | Yes (print/projection legibility) | Yes |
| 5 | Fonts | Titles in Chillax, subtitles/body in Synonym, verified on the produced file (rules: `BRAND_RULES.md` Typography). Fonts not verifiable: `Not verifiable`; a different font used: `Non-compliant` | `typography/Mode 1.tokens.json` | Partly | Yes (rendering) | Yes |
| 6 | Weights and hierarchy | Only SemiBold, Medium, Regular or Light are used; title/subtitle/body hierarchy is clear; no size rule is imposed | `BRAND_RULES.md` Typography | Partly | Yes | No |
| 7 | Text content | Text equals the user's text; spelling, accents and language are right; nothing added or rewritten | User request / original asset | Partly | Yes (proofreading) | Yes |
| 8 | Logo integrity | Logo rules in `BRAND_RULES.md` Logo are met: official file and correct variant for the background, allowed background, width at or above the minimum, clear space respected, unaltered; otherwise placeholder with status `Not verifiable` | `BRAND_RULES.md` Logo | Partly | Yes | Yes |
| 9 | Existing asset preservation | Existing poster/logo/text/official resources are preserved unless the requested change names the element; originals untouched | User request / `CATALOG.md` | Partly (git status, hashes) | Yes | Yes |
| 10 | Illustration consultation | Catalog checked first; closest files actually viewed where possible; one sub-style selected; deviations listed; checklist a-i below | `CATALOG.md`, `STYLE_GUIDE.md` | No (needs image viewing) | Yes | Yes |
| 11 | Illustration content | No third-party logos, flags, new recurring characters or text added without confirmation | `STYLE_GUIDE.md` | Partly | Yes | Yes |
| 12 | Layout and spacing | Spacings use tokens; format/grid follow an approved example, else flagged | `spacing/*.json`, `brand-examples/` | Partly | Yes (no grid is documented) | Yes |
| 13 | Composition | Focal hierarchy, clear text areas, no crop/overlap errors | Output | No | Yes | No |
| 14 | Governance | Labelled AI-generated/AI-assisted; stated as draft pending human approval | `BRAND_RULES.md` | Yes | Approver signs off | Yes |
| 15 | Output inspection and honesty | Actual output was inspected; otherwise checks are `Not verifiable`; no prompt-only compliance claim | This list | Partly | Reviewer | Yes |

## Illustration checklist

Details criteria #10 and #11. Traits and F/V/S classes are in [`STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md); compare against **at least 2 viewed reference illustrations** of the same sub-style (if fewer or none can be viewed: `Not verifiable`). Record per line: pass / deviation / not verifiable, and the reference used.

| # | Check | Compare with |
|---|---|---|
| a | One sub-style only (people/workplace or energy/technology) | `STYLE_GUIDE.md` §1 |
| b | Faces: dot eyes, thin brows, no or tiny nose, small orange mouth, no lashes or face shading | §3, references |
| c | Hair, skin, clothing and hands built as in the references (flat masses with gentle gradient, simple hands, orange tops, light grey trousers) | §3, references |
| d | Proportions and shapes: slim figures, rounded forms, no outlines | §2, §3, references |
| e | Palette: orange, white and greys from tokens or listed as unverified; no new hues | §5, `TOKENS.md` |
| f | Shading: soft linear gradients only; no hard shadows, textures, highlights | §2 |
| g | Detail level: objects reduced to identifiable parts; one idea; 1 to 4 people | §4, §6 |
| h | Composition: centered, isolated, empty space, orange on focal subject, readable when small | §6 |
| i | No S trait copied as a rule; no composition or character copied from a reference | §1 to §6 |

A line cannot be `pass` for the palette (e), proportions (d) or any style resemblance without the images being viewed. Orange plus a vector look does not make an illustration `Compliant`.

## Blocking criteria for publication

Criteria 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14 and 15 (Blocking = Yes). Any of them `Non-compliant` or `Not verifiable` means the visual cannot reach `Ready for human approval`.

## Standard report

Overall: `Ready for human approval` / `Exploration` / `Non-compliant` / `Not verifiable`.

| Criterion | Source | Verification (evidence, or why not possible) | Status |
|---|---|---|---|
| Colors (#2, #3, #4) | | | |
| Typography (#5, #6) | | | |
| Logo (#8) | | | |
| Illustrations (#10, #11) | | | |
| Content (#7, #9) | | | |
| Layout, composition (#12, #13) | | | |
| Governance, honesty (#1, #14, #15) | | | |

Then list: tokens used (role -> token -> HEX); files read / viewed / inaccessible; `TO BE PROVIDED` items hit; decisions awaiting human validation; label "AI-generated / AI-assisted, draft pending human approval".

`Ready for human approval` requires every blocking item `Compliant` (or `N/A`), the produced output inspected, and human approval still pending. `Ready to publish` is not an agent status; it requires documented human approval outside this checklist.
