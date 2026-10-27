---
name: energy-pool-visual-design
description: Create Energy Pool visuals consistent with the existing visual identity and Design System - posters (event, internal communication, HR), illustrations, infographics, presentations and user interfaces - or adapt an existing illustration. Use when asked to create or update an Energy Pool poster, illustration, visual asset or UI, or to design with Energy Pool's brand, tokens and illustration style.
---

# Energy Pool visual design

The Figma Design System (tokens, components) is the source of truth. This skill points to repository resources and never redefines them. One skill is enough: the medium-specific procedures are in `references/`, loaded only when needed.

## Source priority (when sources conflict)

1. Explicit instruction from Energy Pool's design team for this request, or an approved item in [`brand-examples/`](../../../brand-examples/).
2. OFFICIAL Figma token exports (exact values beat colors estimated from images).
3. [`guidelines/BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md) and the medium-specific procedure below.
4. OBSERVED traits in `illustrations/` docs: descriptive, never rules.

Two official sources in conflict with no documented priority: ask for human validation.

## Route the request

| Request | Read, then follow |
|---|---|
| Poster, flyer, infographic, slide, social visual | [`references/poster-workflow.md`](references/poster-workflow.md) |
| New illustration, adaptation of an existing one | [`references/illustration-creation.md`](references/illustration-creation.md) |
| UI / components / layouts | "UI design" below |

## Sources (read in the current session before generating)

| Need | File |
|---|---|
| Mandatory rules, OFFICIAL / OBSERVED / `TO BE PROVIDED`, missing info | [`guidelines/BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md) |
| Token tiers, selection and resolution method | [`guidelines/TOKENS.md`](../../../guidelines/TOKENS.md) |
| Colors (primitive, `energy-assets`) / component tokens | [`colors/Default.tokens.json`](../../../colors/Default.tokens.json) / [`colors/Mode 1.tokens 3.json`](../../../colors/Mode%201.tokens%203.json) |
| Typography / spacing | [`typography/Mode 1.tokens.json`](../../../typography/Mode%201.tokens.json) / [`spacing/Mode 1.tokens 2.json`](../../../spacing/Mode%201.tokens%202.json) |
| Illustration subjects / observed style | [`illustrations/CATALOG.md`](../../../illustrations/CATALOG.md) / [`illustrations/STYLE_GUIDE.md`](../../../illustrations/STYLE_GUIDE.md) |
| Illustration files | [`illustrations/`](../../../illustrations/) |
| Approved examples (empty until supplied), UI examples | [`brand-examples/`](../../../brand-examples/), [`ui-references/`](../../../ui-references/) |
| Pre-delivery checklist | [`guidelines/VISUAL_QA.md`](../../../guidelines/VISUAL_QA.md) |
| Token resolver (optional) | [`scripts/resolve_token.py`](scripts/resolve_token.py) |

Say which files you could not read. Do not answer as if you had.

## Workflow

1. **Classify** the request (illustration, poster/other support, UI, adaptation) and clarify missing inputs (format, text, assets).
2. **Consult** the sources above; pick tokens with the method in `TOKENS.md` (semantic before primitive, no decorative use of state colors, report unresolved references).
3. **Select** existing assets first (catalog, approved examples, coded components).
4. **Produce** with what the environment offers; do not assume image generation, font embedding or Figma access.
5. **Verify** with `VISUAL_QA.md` and fix failures before answering.
6. **Present**: result, QA status, tokens and files used, limits, items for human validation.

## UI design

Prefer existing coded Design System components when accessible; do not copy or rebuild them here. Use Figma only if a connection exists. Take colors, type and spacing from the token files, with component tokens only for component states. Missing component or token: ask.

## Hard constraints

- Never invent colors, fonts, spacing, logo variants or rules; never infer official values from images.
- Never draw, trace or approximate the logo, wordmark or pictogram: use an official file or a marked placeholder.
- Never claim a font was used unless the tool guarantees it; flag the Synonym / Noto Sans conflict.
- Never modify originals in `illustrations/` or the token exports; adapt copies.
- Never present OBSERVED traits as official, or a result as compliant if a check was not performed. "Not verifiable" is not "compliant".
- Only say you looked at an image if its content was accessible.
- Label every AI-generated or AI-assisted visual as such; it is a draft until a human approves it before publication.
