# Brand rules for AI-generated visuals

Mandatory rules for anyone (human or AI) producing Energy Pool visuals from this repository. The Figma Design System and its coded components remain the source of truth; this file points to them and never redefines them.

## Status labels

| Label | Meaning |
|---|---|
| **OFFICIAL** | Taken from a Design System export or an official file supplied by the design team and stored in this repository (cite the file). |
| **OBSERVED** | Seen in existing assets. Describes what exists; **not** a brand rule. |
| **TO BE PROVIDED** | Not documented. Do not guess: ask the user, or state it as missing. |

## Source priority

When sources conflict, apply in this order:

1. **Explicit human instruction from Energy Pool's design team** for the current request, or an approved item in [`../brand-examples/`](../brand-examples/README.md).
2. **OFFICIAL resources**: the palette [`COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md), the Figma token exports, the logo and font files. Exact HEX/values always beat colors estimated from images.
3. **This file** and the medium-specific rules (e.g. the poster workflow), which complete the general rules and never contradict them.
4. **OBSERVED** traits ([`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md), [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md)): descriptive only.

If two OFFICIAL sources disagree and no priority is documented (for example `state` vs `state new` tokens), **stop and ask for human validation**; do not pick one.

Never promote an OBSERVED item to OFFICIAL. Never infer official colors or typography from illustration screenshots.

## Rule levels

Single definition; other files point here.

| Level | Content | How to apply |
|---|---|---|
| **A. Mandatory** | Official logos and their rules ([Logo](#logo)); Chillax for titles and Synonym for other text ([Typography](#typography)); brand colors from the palette ([Colors](#colors)); content supplied by the user; prohibitions the charter defines | Strictly. A violation blocks delivery as approved. |
| **B. Visual coherence** | Illustration style and construction, characters, faces, clothing, objects, color balance, detail level, subtle shading, legibility, hierarchy ([`STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md)) | As guidance with judgment: reproduce the graphic language, not the references' composition. |
| **C. Creative freedom** | Composition and layout, framing, page format and proportions, poses and interactions, scenery and objects, content hierarchy, color combinations, proportions and derived variations ([`COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md#variations)), adaptation to the medium | The agent decides alone; no confirmation needed. |

Permissions are not obligations: an illustration may have no text, no scenery or no gradient. Ask the user only when essential information is missing or a choice might break a level A rule. Where this file says `TO BE PROVIDED` for a level C item (grid, poster format), that is not a blocker: choose, label it a proposal, and never present it as an official rule. Types of QA findings: [`VISUAL_QA.md`](VISUAL_QA.md#types-of-findings).

## Mandatory rules (level A and honesty)

1. Use only documented tokens, fonts and components. Never invent colors, fonts, spacing values, logo variants or design rules.
2. Reference colors by **palette name** with the exact HEX from `COLOR_PALETTE.md`, and spacing and type by **token name** with the value from the export; never by eyeballed values.
3. Logo: use only the official files in `brand-examples/` and never redraw, recolor, stretch, crop, repeat or generate the logo or pictogram (see [Logo](#logo)).
4. Never modify or overwrite files in `illustrations/` or other original assets. Work on copies outside the original folders.
5. **Text fidelity (level A).** When the user supplies text, use exactly that text: same words, order, spelling, accents, punctuation, capitalization of names, numbers, dates and times, and language. When redesigning or adapting an existing visual, use exactly the text already on it. Never add, remove, translate, reword, shorten, correct or complete any text, and never add a tagline or slogan (a tagline inside an official logo file is part of the logo). Only layout may change (size, weight, line breaks, position, case styling consistent with the Typography convention). If the text seems wrong or incomplete, keep it as is and flag it in the delivery; if a needed text (date, place) is missing, ask. If the tool cannot render the text reliably, leave the text as live or placeholder text to add at final composition rather than approximating it.
6. If a level A rule or fact you need is `TO BE PROVIDED`, say so and ask; do not fill the gap (choosing where each palette color goes is not a gap: it is a creative choice, see Colors). For level B and C items, decide and, if it matters, mention the choice.
7. Label every AI-generated or AI-assisted visual as such. It is a draft until a human reviews and approves it before publication.
8. Before delivery, run [`VISUAL_QA.md`](VISUAL_QA.md) and report the result, including anything you could not verify. Visual resemblance to Energy Pool is not proof of compliance.

## Colors

- **OFFICIAL source:** [`../colors/COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md): the 8-color graphic palette (`orange`, `cream`, `green`, `red`, `yellow`, `lavender`, `light-gray`, `dark`), the charter identity colors (Vitamin, Black, White, Power, Solar, Windy, grey tones), the official gradients, the rules for derived variations and the only other colors allowed. Read values there, not from memory.
- **Other color files:** [`../colors/energy-assets.json`](../colors/energy-assets.json) (per energy source, for content about that source) and [`../colors/Mode 1.tokens 3.json`](../colors/Mode%201.tokens%203.json) (component tokens: states, borders, focus, shadows; UI only). Selection method: [`TOKENS.md`](TOKENS.md).
- **Brand orange (confirmed by the design team, 2026-10-27):** `orange` = `#FF9900`, the same value as the orange in the official logo files. It is the main identity color; it does not have to dominate every creation.
- **Choosing colors for a medium:** the 8 colors are a graphic palette, not status colors; the agent combines them freely (with the charter colors and derived variations), in varied proportions, and decides without asking where each goes (backgrounds, sections, boxes, graphic elements), looking at existing references to see how colors are used, and uses the exact HEX. The choice is a creative decision, never presented as an official rule.
- **OBSERVED, SVG source colors vs palette** (exact hex comparison; not a statement of intent): only `#FF9900` (`orange`) matches. `#FFB84D`, `#FFE0B3`, `#EA5B0C`, `#F7EAC6`, `#EFEFEF`, `#EDEDED`, `#D0D0D0`, `#B2B2B2`, `#FFC774`, `#FFB342`, `#FFA41E`, `#FF9C08` are not palette colors (PNG measurement: `STYLE_GUIDE.md` §5). Existing illustrations therefore cannot be assumed to use only palette colors.
- **TO BE PROVIDED:**
  - Allowed combinations, text/background pairs and contrast requirements.
  - Dark-mode or other modes (the exports have only "Mode 1").

## Typography

Single source for typography rules. Official source: Energy Pool brand charter, p. 13 "Typography - Chillax & Synonym" (supplied by the design team, 2026-10-27).

- **Chillax:** all titles.
- **Synonym:** subtitles and body text.
- Both apply to web and print.
- Available weights, both families: SemiBold, Medium, Regular, Light. No other weight, and no other family, is official for these roles.
- **Export check:** [`../typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json) (Figma export, unmodified) is consistent: heading/display `Chillax`, body `Synonym`. It also lists `Yu Gothic` and `Alexandria` variants, numeric weights, sizes, line heights and colors, with units not stated; use those values only by token name, and do not turn them into mandatory sizes, line heights or weights for posters. No poster type scale is required or defined: do not invent one.
- **Backup fonts (OFFICIAL, brand charter p. 14 "Typography - Backup fonts", [`Typography _ Backup fonts.svg`](../typography/Typography%20_%20Backup%20fonts.svg)):** Chillax and Synonym stay the primary fonts and are never replaced when available.
  - **Aptos:** "used for all documents sent to people external to Energy Pool who will not have access to the primary Chillax and Synonym fonts" (for example editable documents sent outside).
  - **Alexandria:** Arabic content. **Yu Gothic:** Japanese content. "Both applied across internal tools and client-facing platforms."
  - These font files are not stored in this repository. No other backup font exists: Noto Sans is not an Energy Pool font; do not use it or any other font as a substitute.
- **Image generators** do not necessarily render the exact official fonts. Do not state that Chillax or Synonym was used unless the real fonts were embedded or the rendering was checked. Prefer composing text in an editable layout with the real fonts.
- **If the fonts are unavailable** (outside the backup-font cases above): do not substitute silently. Say so, name any font actually used, and ask the user to supply the real fonts or finalize the text in a tool that has them.
- **Status:** typography is `Compliant` only if the fonts actually used were verified as Chillax for titles and Synonym for subtitles/body, or as the backup font documented for that case. Fonts that cannot be verified: `Not verifiable`. Any other font actually used: `Non-compliant`.
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

**Noemys logos** (Energy Pool's Energy Management Platform) ([`../brand-examples/third-party-logos/`](../brand-examples/third-party-logos/)): same authorized and prohibited backgrounds and same selection procedure; `logo-noemys.svg` on light, `logo-noemys-negative.svg` on dark. Never recolor or redraw. No official minimum size or clear space (keep it legible and uncluttered; the Energy Pool values do not apply).

**Logo supplied (level A):** when the user attaches or names a logo file, or the visual being redone already contains one, place exactly that file, unaltered; do not regenerate, redraw or approximate it, and do not replace it with a repository file unless it is not an official Energy Pool logo. With no file supplied, use the official files above. A logo generated inside an image by a generator is never acceptable: if the tool cannot place the file, reserve a clear, marked empty area (respecting clear space and minimum size) for a human to place it.

**Selection procedure**
1. Decide whether the area behind the logo is light or dark.
2. Check that it is visually uniform (no mix of light and dark, not strongly colored, not orange).
3. Use only the official file for that background: positive on light, negative on dark. On dark, use `Logo-small-negative.svg`; never invert or recolor a positive file. On dark, only the small logo exists in negative: use it (the tagline version is not available on dark).
4. If no version guarantees legibility or the background is prohibited, change the composition or add a dedicated white area for the positive logo (a white panel behind the logo is allowed; the logo itself is never altered).
5. Large vs small: no official rule (`TO BE PROVIDED`). Use the version the user requests; otherwise choose by layout (proposed convention: small for compact or tight spaces, large for signature or prominent placement) and note the choice in the delivery. Check that the placed width meets the minimum for the chosen file.
6. If the tool cannot embed SVG/PDF, say so, leave a marked placeholder ("LOGO - official file required") and mark the logo criterion `Not verifiable`.
7. On an existing visual, keep the logo already present.

**TO BE PROVIDED:** negative PDF/PNG of the small logo, official large vs small rule.

## Pictograms

**OFFICIAL**, brand charter pp. 16-17 (original pages in `illustrations/`: [`Pictograms _ Font Awesome.svg`](../illustrations/Pictograms%20_%20Font%20Awesome.svg), [`Pictograms _ Custom.svg`](../illustrations/Pictograms%20_%20Custom.svg)).

- **Font Awesome:** "We use the Font Awesome icon library, which offers a wide range of symbols. Only the Classic – Solid style is used across all our media. The Regular (outline) style may be reserved for limited use in web products." For brand visuals, use Font Awesome **Classic Solid** only.
- **Custom set:** "A custom set of pictograms has been created to visually support the brand across different themes, including energy, industrial equipment, Energy Pool tools, and various complementary icons." The page shows the set; individual icon files are not supplied (`TO BE PROVIDED`). Do not redraw them as if official.
- New pictograms an agent draws are proposals in the same solid style; never present them as part of the official set.

## Illustration style

- **OFFICIAL decisions** (colors outside the palette, gradients, AI creation, reuse, proportions, do/don't, text, third-party logos and flags, backgrounds and framing): [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0. Brand colors still come only from the palette ([`COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md)).
- **OBSERVED only:** see [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) (single source for illustration traits: fundamentals, variations, specifics) and [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) (what each file shows). Two sub-styles exist: energy/technology (SVG, objects only, orange ring) and people/workplace (PNG, characters). Do not mix them unless a reference does.
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
| Colors | Semantic color export of the UI Design System (`body`, `*-bg-subtle`, ...), contrast pairs, dark mode; `state` vs `state new` precedence | Figma Design System |
| Typography | Official text case, alignment and line-length rules (if any) | Brand charter, brand team |
| Pictograms | Individual files of the custom pictogram set | Design team |
| Logo | Negative PDF/PNG of the small logo, official large vs small rule | Brand team |
| Layout | Grids, formats, poster/slide templates, placement rules | Figma Design System |
| Examples | Approved posters, slides, illustrations in context | Design team |
| Restrictions | Explicit visual do-not list | Brand team |
