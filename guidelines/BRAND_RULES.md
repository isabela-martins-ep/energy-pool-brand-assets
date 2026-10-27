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

## Mandatory rules

1. Use only documented tokens, fonts and components. Never invent colors, fonts, spacing values, logo variants or design rules.
2. Reference colors, spacing and type by **token name** (with the value from the token file), not by eyeballed values.
3. Logo: use only the official files in `brand-examples/` and never redraw, recolor, stretch, crop, repeat or generate the logo or pictogram (see [Logo](#logo)).
4. Never modify or overwrite files in `illustrations/` or other original assets. Work on copies outside the original folders.
5. If a rule you need is `TO BE PROVIDED`, say so in the answer and ask for it; do not fill the gap.
6. Label every AI-generated or AI-assisted visual as such. It is a draft until a human reviews and approves it before publication.
7. Before delivery, run [`VISUAL_QA.md`](VISUAL_QA.md) and report the result, including anything you could not verify. Visual resemblance to Energy Pool is not proof of compliance.

## Colors

- **OFFICIAL source:** [`../colors/Default.tokens.json`](../colors/Default.tokens.json), a Figma variables export (mode "Default"). It holds `palette` (31 color families, most with `shades` 100-900 and `tints` 100-900, each with a `hex`) and `energy-assets` (chart/icon/background tokens per energy source and sector, referencing the palette). Confirm it is the current published version.
- **Component tokens:** [`../colors/Mode 1.tokens 3.json`](../colors/Mode%201.tokens%203.json) (states, borders, focus, shadows; UI only). Tiers, selection method and resolution: [`TOKENS.md`](TOKENS.md). Read values from the files, not from memory.
- **Brand orange (confirmed by the design team, 2026-10-27):** `palette.vitamin-c` = `#FF9900`, the same value as the orange in the official logo files. `palette.orange-popsicle` (`#FF7F19`) is in the palette but is not designated as the brand orange; do not use it as such unless the design team says so.
- **Never decorative:** state colors (success/valid, danger/invalid, warning, info, link) are for their UI state only. A color existing in the palette is not permission to use it on a poster.
- **OBSERVED, SVG source colors vs tokens** (exact hex comparison; not a statement of intent): `#FFB84D` = `vitamin-c.tints.700`, `#FFE0B3` = `vitamin-c.tints.300`, `#FF9900` = `vitamin-c` (brand orange). No token matches `#EA5B0C`, `#F7EAC6`, `#EFEFEF`, `#EDEDED`, `#D0D0D0`, `#B2B2B2`, `#FFC774`, `#FFB342`, `#FFA41E`, `#FF9C08`. Existing illustrations therefore cannot be assumed to use only tokens.
- **TO BE PROVIDED:**
  - Which palette families are brand colors versus data-visualization or status colors.
  - Primary/secondary roles, allowed combinations, text/background pairs and contrast requirements.
  - Dark-mode or other modes (the export has only "Default").
  - Gradient rules (existing illustrations use gradients).

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
- **TO BE PROVIDED:** text case, alignment and line-length rules.

## Logo

Source: Energy Pool brand charter (rules below supplied by the design team, 2026-10-27). This is the only place where logo rules are defined.

**Files** in [`../brand-examples/`](../brand-examples/README.md): `Logo-large.svg|pdf|png` (wordmark, pictogram and tagline "Smart Energy Management") and `Logo-small.svg|pdf|png` (wordmark and pictogram only). Large/small is a size/content choice; it is not the positive/negative choice.

**Variants**

| Variant | Use on | Available file |
|---|---|---|
| Positive | White background, or a light photograph that is sufficiently uniform | Both files, large and small. Verified in the SVG source: black (`black`) and `#FF9900` fills, no background. |
| Negative | Dark background, or a dark photograph that is sufficiently uniform | **Missing.** No negative file is in the repository. |

**Prohibited**
- Any orange background, and any colored background not explicitly authorized (no authorization list exists: ask).
- An all-black or all-white version.
- A photographic background mixing light and dark areas that harms legibility.
- Redrawing, tracing, recoloring, stretching, cropping, adding effects, generating it with an image tool, repeating it as a motif, or copying the pictogram/wordmark seen inside illustrations or on objects.

**Size and protection**
- Minimum width: 100 px on screen, 36 mm in print. Prefer SVG/PDF. `Logo-large.png` is 280 px and `Logo-small.png` 62 px wide: never upscale a PNG; `Logo-small.png` is below the 100 px digital minimum, so use the SVG on screen.
- Clear space: all around the logo, equal to the height of the capital "E" of "Energy" in the logo. No typographic element may enter it.
- Keep the original proportions and colors.

**Selection procedure**
1. Identify the background (white, light uniform photo, dark, colored).
2. Light background: use the positive file. Dark background: the negative file is missing, so do not invert or recolor the positive one; report the missing resource and ask the design team for it, or change the background.
3. Large vs small: `TO BE PROVIDED`. Use the version the user requests, otherwise ask. Check that the placed width meets the minimum for the chosen file.
4. If the tool cannot embed SVG/PDF, say so, leave a marked placeholder ("LOGO - official file required") and mark the logo criterion `Not verifiable`.
5. On an existing visual, keep the logo already present.

**TO BE PROVIDED:** negative logo files, list of authorized colored backgrounds, large vs small rule.

## Illustration style

- **OBSERVED only:** see [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) (traits) and [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) (what each file shows). Two sub-styles exist: energy/technology (SVG, objects only, orange ring) and people/workplace (PNG, characters). Do not mix them unless a reference does.
- **TO BE PROVIDED:** official do/don't rules, permitted character and pose guidelines, rules for text in illustrations, backgrounds and cropping, and whether new illustrations may be created by AI at all.

## Layout and spacing

- **OFFICIAL source:** [`../spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json), a Figma variables export with `rem`, `em` and `spacer` scales (e.g. `spacer.spacers.1` to `6`, resolving to 4, 8, 12, 16, 24, 48 as numbers; units not stated). Use token names.
- **TO BE PROVIDED:** grid, margins and safe areas, formats and sizes for posters, slides and social media, hierarchy and composition rules, and how illustrations are placed relative to text.

## Approved visual examples

Only the logo files are supplied. No approved poster, slide or UI example exists yet (see [`../brand-examples/README.md`](../brand-examples/README.md)), so there is no reference for what a compliant poster looks like.

## Visual restrictions

- Process restrictions are the mandatory rules above.
- **TO BE PROVIDED:** explicit visual do-not rules (forbidden colors, effects, imagery, tone, representation of people, third-party logos in visuals, use of stock or photographic imagery). The existing illustrations include third-party tool logos and flags; whether that is allowed is not documented.

## Missing information register

| Area | Missing | Source to supply |
|---|---|---|
| Colors | Semantic color export (`primary`, `secondary`, `body`, ...), brand vs data-viz families, roles for communication material, contrast pairs, dark mode, gradients; `state` vs `state new` precedence | Figma Design System |
| Typography | Text case, alignment and line-length rules | Brand charter, brand team |
| Logo | Negative logo files, authorized colored backgrounds, large vs small rule | Brand team |
| Illustration | Official rules, AI-creation policy, text-in-illustration rules | Design team |
| Layout | Grids, formats, poster/slide templates, placement rules | Figma Design System |
| Examples | Approved posters, slides, illustrations in context | Design team |
| Restrictions | Explicit visual do-not list | Brand team |
