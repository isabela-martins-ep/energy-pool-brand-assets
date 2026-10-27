---
name: energy-pool-visual-design
description: Create Energy Pool illustrations and user interfaces consistent with the existing visual identity and Design System. Use when asked to create a new Energy Pool illustration, generate a visual asset inspired by existing illustrations, design a UI or components/layouts with Energy Pool's look, or adapt an existing illustration to a new context.
---

# Energy Pool visual design

Helps produce illustrations and UIs consistent with Energy Pool's identity. The Design System (Figma + coded components) is the source of truth; this skill only points to repository resources and never redefines them.

## Resources

| Need | File |
|---|---|
| Rules for agents | [`.github/copilot-instructions.md`](../../copilot-instructions.md) |
| What each illustration shows | [`illustrations/CATALOG.md`](../../../illustrations/CATALOG.md) |
| Observed illustration traits (not official rules) | [`illustrations/STYLE_GUIDE.md`](../../../illustrations/STYLE_GUIDE.md) |
| Illustration files (SVG, PNG) | [`illustrations/`](../../../illustrations/) |
| Mandatory rules; official vs observed vs `TO BE PROVIDED` | [`guidelines/BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md) |
| Pre-delivery checklist | [`guidelines/VISUAL_QA.md`](../../../guidelines/VISUAL_QA.md) |
| Color tokens | [`colors/Default.tokens.json`](../../../colors/Default.tokens.json) |
| Typography tokens | [`typography/Mode 1.tokens.json`](../../../typography/Mode%201.tokens.json) |
| Spacing tokens | [`spacing/Mode 1.tokens 2.json`](../../../spacing/Mode%201.tokens%202.json) |
| UI examples | [`ui-references/`](../../../ui-references/) |
| Approved visual examples (empty until supplied) | [`brand-examples/`](../../../brand-examples/) |
| Using this repo in Microsoft 365 Copilot | [`guidelines/M365_COPILOT.md`](../../../guidelines/M365_COPILOT.md) |

## Required before producing a result

You must read these files in the current session before generating, not rely on memory:

1. `guidelines/BRAND_RULES.md` always.
2. The token file for each of colors, typography and spacing you use. Quote token names and values from the file.
3. For illustrations: `illustrations/CATALOG.md` and `illustrations/STYLE_GUIDE.md`, then the 2-3 closest illustration files.
4. `brand-examples/` for an approved model of the same format (posters, slides, screens). If none exists, say so.

If a file cannot be read, say so and do not answer as if it had been. Anything marked `TO BE PROVIDED` must be reported and asked for, not filled in.

## Workflow

1. **Classify** the request: illustration, UI design, or adaptation of an existing asset.
2. **Consult** the relevant docs above. Read the files fully before generating.
3. **Select** existing assets: for illustrations, match the subject in `CATALOG.md`, then open the 2–3 closest files.
4. **Apply the Design System** for colors, typography, spacing and components, using token/component names rather than raw values.
5. **Reuse** existing components and assets whenever possible; only create what is missing.
6. **Generate** using what the current environment offers (see below).
7. **Verify** by going through `guidelines/VISUAL_QA.md` item by item. Do not deliver a final result before this check, and fix failures first.
8. **Report** the QA result (Pass / Fail / Not verifiable per item), the files and tokens relied on, limitations, and `TO BE PROVIDED` items hit. Label the output AI-generated or AI-assisted and as a draft pending human approval.

## Illustrations

- Choose the sub-style as defined in `.github/copilot-instructions.md`: **energy/technology** (objects only, orange ring) or **people/workplace** (characters). Do not mix them unless a reference does.
- Reuse as is when a catalog file fits; link the path.
- Adaptation: work on a **copy** outside `illustrations/`. SVGs can be edited as text (recolor, hide/move elements, crop viewBox), but embedded base64 PNGs are not editable as vectors. PNGs: only scaling, cropping or format conversion with command-line tools.
- New scenes, characters or compositions need an image-generation tool or a designer. If none is available, say so and provide a brief/prompt listing the reference files instead. Hand-written SVG suits only simple shapes.
- Do not add text to illustrations without asking (existing text is French, typeface unidentified).

## UI design

- Prefer existing coded Design System components when accessible (repository, package or docs available to you). Do not copy their code here or rebuild them.
- Use Figma only if a Figma connection is actually available; otherwise say so.
- Take colors, fonts and spacing from the token files, never from illustrations. `ui-references/` may contain only placeholders. If a needed token, component or reference is not documented (see `TO BE PROVIDED` in `BRAND_RULES.md`), **ask the user** rather than guessing.
- Never redraw or generate the logo or pictogram; use a supplied file or a marked placeholder.

## Constraints

- Never invent brand colors, typography, spacing values, or official design rules.
- `STYLE_GUIDE.md` is observational: never present its patterns as official brand rules. Its hex values are not verified tokens.
- Never modify originals in `illustrations/`.
- Label every visual generated or materially altered with AI as AI-generated or AI-assisted, and require human review and approval before publication or distribution.
- Only claim to have looked at an image if its content was actually accessible (image input supported); otherwise rely on catalog text/SVG source and state that.
- Do not assume image generation is available.
- Generated visuals are drafts that need designer review.
