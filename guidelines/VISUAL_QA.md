# Visual QA checklist for AI-generated assets

Run on the produced output before delivering any generated or adapted visual. Keep the results internal; share them as in [Delivery](#delivery). Definitions (OFFICIAL / OBSERVED / `TO BE PROVIDED`) are in [`BRAND_RULES.md`](BRAND_RULES.md); token method in [`TOKENS.md`](TOKENS.md).

**Three kinds of resource, never confused:** an *officially validated resource* (logo files, color palette, token exports), a *creation inspired by references* (any AI output), and a *creation verified as compliant* (every criterion below checked `Compliant`). Visual resemblance to Energy Pool is not evidence of compliance.

**Statuses:** `Compliant`, `Non-compliant`, `Not verifiable` (say why), `N/A` (criterion does not apply, e.g. no logo, no text, no illustration; say so in one line). `Not verifiable` is never treated as compliant; `N/A` is not a failure. If a level A rule is `TO BE PROVIDED`, the item is `Not verifiable`; for level B or C items it is not a blocker.

**Blocking rule:** a `Non-compliant` or `Not verifiable` result on a criterion marked **Blocking = Yes** prevents `Ready for human approval` and `Ready to publish`. The visual can still be delivered as a draft, labelled `Exploration` or `Not verifiable` with the pending validations listed; only the approval-ready status is withheld.

**Automatable:** Yes = a script or file read can check it; Partly = tool-assisted, then confirm; No = human only. Every visual still needs human approval before publication.

| # | Criterion | What to check | Source | Automatable | Human validation | Blocking |
|---|---|---|---|---|---|---|
| 1 | Source manifest and consultation | Required files are listed, actually read/viewed, and inaccessible files are named; a URL/path alone is not evidence | `SKILL.md` step 2 | Partly | Reviewer confirms the list | Yes |
| 2 | Colors | Each color is a palette or charter color with its exact HEX, a derived variation reported as such (not presented as official), or an allowed exception listed in `COLOR_PALETTE.md`; none presented as official when estimated from images | `colors/COLOR_PALETTE.md`, `TOKENS.md` | Yes for source/HTML/SVG; Partly for raster | Role of each color for this medium (no official mapping: agent's choice, reported) | Yes |
| 3 | Color usage | Palette colors combined freely with orange as the main identity color (not necessarily dominant); gradients only as in `COLOR_PALETTE.md` Gradients, used sparingly; no component tokens used decoratively; `energy-assets` only for their source | `COLOR_PALETTE.md`, `TOKENS.md` | Partly | Yes | Yes |
| 4 | Contrast / legibility | Text is legible on its background; contrast measured and stated (no official threshold exists) | Output file | Partly | Yes (print/projection legibility) | No |
| 5 | Fonts | Titles in Chillax, subtitles/body in Synonym, or the documented backup font for its case (Aptos, Alexandria, Yu Gothic), verified on the produced file (rules: `BRAND_RULES.md` Typography). Fonts not verifiable: `Not verifiable`; any other font used: `Non-compliant` | `typography/Mode 1.tokens.json` | Partly | Yes (rendering) | Yes |
| 6 | Weights and hierarchy | Only SemiBold, Medium, Regular or Light are used; hierarchy is clear; no size rule is imposed | `BRAND_RULES.md` Typography | Partly | Yes | No |
| 7 | Text content | Text equals exactly the supplied text, or the existing text of the redone visual, character by character (words, order, spelling, accents, punctuation, numbers, dates, language); nothing added, removed, translated or rewritten, no added tagline; any generated-image text misspelling is a blocking non-compliance | User request / original asset | Partly | Yes (proofreading) | Yes |
| 8 | Logo integrity | The supplied (or already present, or official) logo file is placed unaltered, never generated or redrawn; logo rules in `BRAND_RULES.md` Logo are met: official file and correct variant for the background, allowed background, width at or above the minimum, clear space respected, unaltered; otherwise placeholder with status `Not verifiable` | `BRAND_RULES.md` Logo | Partly | Yes | Yes |
| 9 | Existing asset preservation | Existing poster/logo/text/official resources are preserved unless the requested change names the element; originals untouched | User request / `CATALOG.md` | Partly (git status, hashes) | Yes | Yes |
| 10 | Illustration consultation | Catalog checked first; closest files actually viewed where possible; one sub-style selected; deviations listed; checklist a-k below | `CATALOG.md`, `STYLE_GUIDE.md` | No (needs image viewing) | Yes | No (level B; if images cannot be viewed: `Not verifiable`, reported as a point for validation) |
| 11 | Illustration content | No invented slogans, data or messages; text only when relevant, exactly as supplied (`BRAND_RULES.md` rule 5); third-party logos and flags from official files or their absence reported; Energy Pool logos from source files; AI-created work labelled and pending human validation | `STYLE_GUIDE.md` | Partly | Yes | Yes |
| 12 | Layout and spacing | Spacings use tokens where applicable; an approved example is followed if one exists; otherwise the layout is an original proposal (no official grid exists) and is not a defect | `spacing/*.json`, `brand-examples/` | Partly | Yes | No |
| 13 | Composition | Clear hierarchy, legible text areas, no unintended crop or overlap | Output | No | Yes | No |
| 14 | Governance | Labelled AI-generated/AI-assisted; stated as draft pending human approval | `BRAND_RULES.md` | Yes | Approver signs off | Yes |
| 15 | Output inspection and honesty | Actual output was inspected; otherwise checks are `Not verifiable`; no prompt-only compliance claim | This list | Partly | Reviewer | Yes |

## Illustration checklist

Details criteria #10 and #11. Lines a-h and k are level B (style gaps, not blockers); i and j apply the official do/don't. Traits and F/V/S classes: [`STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md). Compare against **at least 2 viewed references** of the same sub-style (if fewer can be viewed: `Not verifiable`, a point for validation). Record per line: consistent / gap / not verifiable, and the reference used. Differences in composition, pose or scenery are creative choices.

| # | Check | Compare with |
|---|---|---|
| a | One sub-style only (people/workplace or energy/technology) | `STYLE_GUIDE.md` §1 |
| b | Faces simplified as in the references (dot eyes, thin brows, no or tiny nose, small mouth), no realistic facial rendering | §3, references |
| c | Hair, skin, clothing and hands built in the references' language (flat masses, gentle gradient, simple hands); outfit colors balanced like the references (orange tops are typical, not required) | §3, references |
| d | Proportions and shapes match the references visually (no numeric ratio is checked); rounded forms, no outlines | §2, §3, references |
| e | Palette: brand orange (`orange`) from the palette; white per `COLOR_PALETTE.md`; other oranges, greys, skin, hair, shading consistent with references and listed as outside the palette; none used for backgrounds or titles | §5, `COLOR_PALETTE.md` |
| f | Shading: subtle gradients as in the references; no complex gradients, realistic lighting, pronounced shadows, 3D | §2 |
| g | Detail level: objects reduced to identifiable parts; one clear idea; people and object counts suited to the subject (1 to 4 people is typical, not a limit); no decorative element without function | §4, §6 |
| h | Readable when small; clear focal point; orange as accent and light greys as context are typical of the references | §6 |
| i | Do/Don't (§0.6, §0.7): flat vector, no photorealism, 3D, texture, strong shadow, metallic effect, thick black outline, realistic or exaggerated-cartoon proportions | §0 |
| j | File background transparent or white; placed on a white area of the medium, never a colored or grey block; scenery minimal and useful; framing suits the use; essential elements not cropped | §0.9, §6 |
| k | No S trait copied as a rule; no composition copied from a reference (reused characters, poses and motifs are allowed) | §1 to §6 |

A style line cannot be marked consistent without the images being viewed. Orange plus a vector look does not make an illustration `Compliant`.

## Types of findings

Classify every finding; only the first kind blocks. Rule levels: [`BRAND_RULES.md`](BRAND_RULES.md#rule-levels).

| Type | Meaning | Action |
|---|---|---|
| **Blocking non-compliance** | Level A violation: wrong or altered logo, non-official font, brand color not from the palette, wrong or invented content, charter prohibition | Fix; cannot be delivered as approved |
| **Style gap to correct** | Level B: illustration too far from the references, inconsistent treatment, unreadable composition | Fix before delivery |
| **Acceptable creative choice** | Level C: different framing, pose, scenery, layout or format that respects the identity | None; never a defect |
| **Point for human validation** | Important decision with no official rule to conclude (new AI creation, unverifiable item) | State it in the delivery |

A difference from existing examples is never `Non-compliant` by itself.

## Blocking criteria for publication

Criteria 1, 2, 3, 5, 7, 8, 9, 11, 14 and 15 (Blocking = Yes). Any of them `Non-compliant` or `Not verifiable` means the visual cannot reach `Ready for human approval`.

## Delivery

A proposal with pending official validations is delivered as a draft, not withheld. By default give the user only: the file, a few lines on the main design decisions, and the limits or points for human validation, with the label "AI-generated / AI-assisted, draft pending human approval". Give the detailed report below only if the user asks or a blocking non-compliance, or an unverifiable blocking criterion, must be explained.

## Detailed report (on request or when a compliance problem requires it)

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

Then list: colors used (role -> palette name or token -> HEX); files read / viewed / inaccessible; `TO BE PROVIDED` items hit; decisions awaiting human validation; label "AI-generated / AI-assisted, draft pending human approval".

`Ready for human approval` requires every blocking item `Compliant` (or `N/A`), the produced output inspected, and human approval still pending. `Ready to publish` is not an agent status; it requires documented human approval outside this checklist.
