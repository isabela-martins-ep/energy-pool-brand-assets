# Brand rules for AI-generated visuals

Mandatory rules for anyone (human or AI) producing Energy Pool visuals from this repository. The Figma Design System and its coded components remain the source of truth; this file points to them and never redefines them.

## Status labels

| Label | Meaning |
|---|---|
| **OFFICIAL** | Taken from a Design System export stored in this repository (cite the file). |
| **OBSERVED** | Seen in existing assets. Describes what exists; **not** a brand rule. |
| **TO BE PROVIDED** | Not documented. Do not guess: ask the user, or state it as missing. |

## Source priority

When sources conflict, apply in this order:

1. **Explicit human instruction from Energy Pool's design team** for the current request, or an approved item in [`../brand-examples/`](../brand-examples/README.md).
2. **OFFICIAL Figma exports** (tokens): exact HEX/values always beat colors estimated from images.
3. **This file** and the medium-specific rules (e.g. the poster workflow), which complete the general rules and never contradict them.
4. **OBSERVED** traits ([`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md), [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md)): descriptive only.

If two OFFICIAL sources disagree and no priority is documented (for example `state` vs `state new` tokens), **stop and ask for human validation**; do not pick one.

Never promote an OBSERVED item to OFFICIAL. Never infer official colors or typography from illustration screenshots.

## Rule levels

Single definition; other files point here.

| Level | Content | How to apply |
|---|---|---|
| **A. Mandatory** | Official logos and their rules ([Logo](#logo)); Chillax for titles and Synonym for other text ([Typography](#typography)); brand colors from the tokens ([Colors](#colors)); content supplied by the user; prohibitions the charter defines | Strictly. A violation blocks delivery as approved. |
| **B. Visual coherence** | Illustration style and construction, characters, faces, clothing, objects, color balance, detail level, subtle shading, legibility, hierarchy ([`STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md)) | As guidance with judgment: reproduce the graphic language, not the references' composition. |
| **C. Creative freedom** | Composition and layout, framing, page format and proportions, poses and interactions, scenery and objects, content hierarchy, adaptation to the medium | The agent decides alone; no confirmation needed. |

Permissions are not obligations: an illustration may have no text, no scenery or no gradient. Ask the user only when essential information is missing or a choice might break a level A rule. Where this file says `TO BE PROVIDED` for a level C item (grid, poster format), that is not a blocker: choose, label it a proposal, and never present it as an official rule. Types of QA findings: [`VISUAL_QA.md`](VISUAL_QA.md#types-of-findings).

## Mandatory rules (level A and honesty)

1. Use only documented tokens, fonts and components. Never invent colors, fonts, spacing values, logo variants or design rules.
2. Reference colors, spacing and type by **token name** (with the value from the token file), not by eyeballed values.
3. Logo: use only the official files in `brand-examples/` and never redraw, recolor, stretch, crop, repeat or generate the logo or pictogram (see [Logo](#logo)).
4. Never modify or overwrite files in `illustrations/` or other original assets. Work on copies outside the original folders.
5. If a level A rule or fact you need is `TO BE PROVIDED`, say so and ask; do not fill the gap (exception: the color-to-role mapping, see Colors). For level B and C items, decide and, if it matters, mention the choice.
6. Label every AI-generated or AI-assisted visual as such. It is a draft until a human reviews and approves it before publication.
7. Before delivery, run [`VISUAL_QA.md`](VISUAL_QA.md) and report the result, including anything you could not verify. Visual resemblance to Energy Pool is not proof of compliance.

## Colors

- **OFFICIAL source:** [`../colors/Default.tokens.json`](../colors/Default.tokens.json), a Figma variables export (mode "Default"). It holds `palette` (31 color families, most with `shades` 100-900 and `tints` 100-900, each with a `hex`) and `energy-assets` (chart/icon/background tokens per energy source and sector, referencing the palette). Confirm it is the current published version.
- **Component tokens:** [`../colors/Mode 1.tokens 3.json`](../colors/Mode%201.tokens%203.json) (states, borders, focus, shadows; UI only). Tiers, selection method and resolution: [`TOKENS.md`](TOKENS.md). Read values from the files, not from memory.
- **Brand orange (confirmed by the design team, 2026-10-27):** `palette.vitamin-c` = `#FF9900`, the same value as the orange in the official logo files. `palette.orange-popsicle` (`#FF7F19`) is in the palette but is not designated as the brand orange; do not use it as such unless the design team says so.
- **Choosing colors for a medium:** with no semantic token for a role, the agent may choose confirmed brand colors itself: `vitamin-c` and its shades and tints, plus white and neutral palette tokens, using the exact token hex. Other palette families may be used as accents only from the token files, and the choice is reported as a point for validation; it is never presented as an official rule or palette. The role-to-color mapping stays undocumented (below) and is a creative choice, not a fact about the charter.
- **Never decorative:** state colors (success/valid, danger/invalid, warning, info, link) are for their UI state only. A color existing in the palette is not permission to use it on a poster.
- **OBSERVED, SVG source colors vs tokens** (exact hex comparison; not a statement of intent): (PNG measurement: only 18.2 % of opaque pixels equal a token; details in `STYLE_GUIDE.md` §5) `#FFB84D` = `vitamin-c.tints.700`, `#FFE0B3` = `vitamin-c.tints.300`, `#FF9900` = `vitamin-c` (brand orange). No token matches `#EA5B0C`, `#F7EAC6`, `#EFEFEF`, `#EDEDED`, `#D0D0D0`, `#B2B2B2`, `#FFC774`, `#FFB342`, `#FFA41E`, `#FF9C08`. Existing illustrations therefore cannot be assumed to use only tokens.
- **TO BE PROVIDED:**
  - Which palette families are brand colors versus data-visualization or status colors.
  - Official primary/secondary roles, allowed combinations, text/background pairs and contrast requirements.
  - Dark-mode or other modes (the export has only "Default").
  - Gradient rules outside illustrations (illustration gradients: `STYLE_GUIDE.md` §0).

## Typography

Single source for typography rules. Official source: Energy Pool brand charter, p. 13 "Typography - Chillax & Synonym" (supplied by the design team, 2026-10-27).

- **Chillax:** all titles.
- **Synonym:** subtitles and body text.
- Both apply to web and print.
- Available weights, both families: SemiBold, Medium, Regular, Light. No other weight, and no other family, is official for these roles.
- **Export check:** [`../typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json) (Figma export, unmodified) is consistent: heading/display `Chillax`, body `Synonym`. It also lists `Yu Gothic` and `Alexandria` variants, numeric weights, sizes, line heights and colors, with units not stated; use those values only by token name, and do not turn them into mandatory sizes, line heights or weights for posters. No poster type scale is required or defined: do not invent one.
- **No fallback fonts:** none is needed or defined. Noto Sans is not an Energy Pool font; do not use it or any other font as a substitute.
- **Image generators** do not necessarily render the exact official fonts. Do not state that Chillax or Synonym was used unless the real fonts were embedded or the rendering was checked. Prefer composing text in an editable layout with the real fonts.
- **If the fonts are unavailable:** do not substitute silently. Say so, name any font actually used, and ask the user to supply the real fonts or finalize the text in a tool that has them.
- **Status:** typography is `Compliant` only if the fonts actually used were verified as Chillax for titles and Synonym for subtitles/body. Fonts that cannot be verified: `Not verifiable`. A different font actually used: `Non-compliant`.
- **Font files** (Fontshare, ITF Free Font License, copy in each folder): [`../typography/fonts/Chillax/`](../typography/fonts/Chillax/) and [`../typography/fonts/Synonym/`](../typography/fonts/Synonym/), OTF for print/design tools and WOFF2 for web. The packages also contain Bold and Extralight, which are **not** official weights: do not use them. Install the OTF files to render posters; check the license terms before redistributing them outside Energy Pool.
- **Text composition (no official rule; typographic good practice, a proposed convention, not a charter rule and never a blocker):** natural sentence case by default; capitals where they serve the graphic hierarchy (short titles, labels); left alignment for long text; centered alignment allowed for short titles or compositions that suit it; line length adapted to the format and legibility, with no numeric value imposed.
- **TO BE PROVIDED:** official text case, alignment and line-length rules, if the charter defines any.

## Logo

Source: Energy Pool brand charter (rules below supplied by the design team, 2026-10-27). This is the only place where logo rules are defined.

**Files** in [`../brand-examples/`](../brand-examples/README.md): `Logo-large.svg|pdf|png` (wordmark, pictogram and tagline "Smart Energy Management") and `Logo-small.svg|pdf|png` (wordmark and pictogram only), plus `Logo-small-negative.svg` (negative of the small logo). Large/small is a size/content choice; it is not the positive/negative choice.

**Variants**

| Variant | Use on | Available file |
|---|---|---|
| Positive (dark text, orange elements) | White background, or a light photograph where the area behind the logo is light and uniform enough for legibility | Both files, large and small. Verified in the SVG source: black (`black`) and `#FF9900` fills, no background. |
| Negative (white text, orange elements) | Plain dark background, or a dark photograph where the area behind the logo is dark and uniform enough for legibility | `Logo-small-negative.svg` (wordmark and pictogram; verified in the SVG source: `white` and `#FF9900` fills, no background). **No negative large version (with tagline) exists; none is planned.** |

**Prohibited**
- Any orange background, and any strongly colored background, even if the contrast seems sufficient. The only authorized backgrounds are those in the table above.
- An all-black or all-white version.
- An area behind the logo mixing light and dark parts, notably on a photograph.
- Redrawing, tracing, recoloring, stretching, cropping, adding effects, generating it with an image tool, repeating it as a motif, or copying the pictogram/wordmark seen inside illustrations or on objects.

**Size and protection**
- Minimum width: 100 px on screen, 36 mm in print. Prefer SVG/PDF. `Logo-large.png` is 280 px and `Logo-small.png` 62 px wide: never upscale a PNG; `Logo-small.png` is below the 100 px digital minimum, so use the SVG on screen.
- Clear space: all around the logo, equal to the height of the capital "E" of "Energy" in the logo. No typographic element may enter it.
- Keep the original proportions and colors.

**Noemys offer logos** ([`../brand-examples/third-party-logos/`](../brand-examples/third-party-logos/)): same authorized and prohibited backgrounds and same selection procedure; `logo-noemys.svg` on light, `logo-noemys-negative.svg` on dark. Never recolor or redraw. No minimum size (keep it legible); clear space: `TO BE PROVIDED`.

**Selection procedure**
1. Decide whether the area behind the logo is light or dark.
2. Check that it is visually uniform (no mix of light and dark, not strongly colored, not orange).
3. Use only the official file for that background: positive on light, negative on dark. On dark, use `Logo-small-negative.svg`; never invert or recolor a positive file. On dark, only the small logo exists in negative: use it (the tagline version is not available on dark).
4. If no version guarantees legibility or the background is prohibited, change the composition or add a dedicated white area for the positive logo (a white panel behind the logo is allowed; the logo itself is never altered).
5. Large vs small: no official rule (`TO BE PROVIDED`). Use the version the user requests; otherwise choose by layout (proposed convention: small for compact or tight spaces, large for signature or prominent placement) and note the choice in the delivery. Check that the placed width meets the minimum for the chosen file.
6. If the tool cannot embed SVG/PDF, say so, leave a marked placeholder ("LOGO - official file required") and mark the logo criterion `Not verifiable`.
7. On an existing visual, keep the logo already present.

**TO BE PROVIDED:** negative PDF/PNG of the small logo, official large vs small rule.

## Illustration style

- **OFFICIAL decisions** (colors outside tokens, gradients, AI creation, reuse, proportions): [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0. Brand colors still come only from tokens.
- **OBSERVED only:** see [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) (single source for illustration traits: fundamentals, variations, specifics) and [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) (what each file shows). Two sub-styles exist: energy/technology (SVG, objects only, orange ring) and people/workplace (PNG, characters). Do not mix them unless a reference does.
- **OFFICIAL decisions** also cover do/don't, text, third-party logos and flags, backgrounds and framing: `STYLE_GUIDE.md` §0.
- **File naming (technical convention for new files, proposed, not a charter rule):** `illustration-subject-description.png` or `.svg`: lowercase, no spaces, hyphens between words, no accents, descriptive. Existing files in `illustrations/` keep their names (originals are never renamed).
- **Owner:** there is no official illustration owner. Do not invent one; approval of new illustrations is by the human reviewer of the delivery.

## Layout and spacing

- **OFFICIAL source:** [`../spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json), a Figma variables export with `rem`, `em` and `spacer` scales (e.g. `spacer.spacers.1` to `6`, resolving to 4, 8, 12, 16, 24, 48 as numbers; units not stated). Use token names.
- **No official layout rules exist** (grid, margins, safe areas, formats and sizes for posters, slides and social media, hierarchy and composition, placement of illustrations relative to text). This is level C: the agent decides and labels the result a proposal; it is not a blocker and not an official rule.

## Approved visual examples

Only the logo files are supplied. No approved poster, slide or UI example exists yet (see [`../brand-examples/README.md`](../brand-examples/README.md)), so there is no reference for what a compliant poster looks like.

## Visual restrictions

- Process restrictions are the mandatory rules above.
- **TO BE PROVIDED:** explicit visual do-not rules (forbidden colors, effects, imagery, tone, representation of people, third-party logos in visuals, use of stock or photographic imagery). Illustrations: see `STYLE_GUIDE.md` §0.

## Missing information register

| Area | Missing | Source to supply |
|---|---|---|
| Colors | Semantic color export (`primary`, `secondary`, `body`, ...), brand vs data-viz families, roles for communication material, contrast pairs, dark mode, non-illustration gradients; `state` vs `state new` precedence | Figma Design System |
| Typography | Official text case, alignment and line-length rules (if any) | Brand charter, brand team |
| Logo | Negative PDF/PNG of the small logo, official large vs small rule | Brand team |
| Layout | Grids, formats, poster/slide templates, placement rules | Figma Design System |
| Examples | Approved posters, slides, illustrations in context | Design team |
| Restrictions | Explicit visual do-not list | Brand team |
