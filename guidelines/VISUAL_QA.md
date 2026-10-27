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
| 5 | Fonts | Declared families are documented; actual embedded/rendered font is identified; substitutions are explicit; the body font (`Synonym`) is pending design-team confirmation | `typography/Mode 1.tokens.json` | Partly | Yes (rendering) | Yes |
| 6 | Type scale and weights | Sizes and weights come from tokens; hierarchy is clear | Typography tokens | Partly | Yes (poster scale `TO BE PROVIDED`) | No |
| 7 | Text content | Text equals the user's text; spelling, accents and language are right; nothing added or rewritten | User request / original asset | Partly | Yes (proofreading) | Yes |
| 8 | Logo integrity | Logo rules in `BRAND_RULES.md` Logo are met: official file and correct variant for the background, allowed background, width at or above the minimum, clear space respected, unaltered; otherwise placeholder with status `Not verifiable` | `BRAND_RULES.md` Logo | Partly | Yes | Yes |
| 9 | Existing asset preservation | Existing poster/logo/text/official resources are preserved unless the requested change names the element; originals untouched | User request / `CATALOG.md` | Partly (git status, hashes) | Yes | Yes |
| 10 | Illustration consultation | Catalog checked first; closest files actually viewed where possible; one sub-style selected; deviations listed | `CATALOG.md`, `STYLE_GUIDE.md` | No (needs image viewing) | Yes | Yes |
| 11 | Illustration content | No third-party logos, flags, new recurring characters or text added without confirmation | `STYLE_GUIDE.md` | Partly | Yes | Yes |
| 12 | Layout and spacing | Spacings use tokens; format/grid follow an approved example, else flagged | `spacing/*.json`, `brand-examples/` | Partly | Yes (no grid is documented) | Yes |
| 13 | Composition | Focal hierarchy, clear text areas, no crop/overlap errors | Output | No | Yes | No |
| 14 | Governance | Labelled AI-generated/AI-assisted; stated as draft pending human approval | `BRAND_RULES.md` | Yes | Approver signs off | Yes |
| 15 | Output inspection and honesty | Actual output was inspected; otherwise checks are `Not verifiable`; no prompt-only compliance claim | This list | Partly | Reviewer | Yes |

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
