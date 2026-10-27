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
| Colors / typography / spacing | [`colors/`](../../../colors/), [`typography/`](../../../typography/), [`spacing/`](../../../spacing/) |
| UI examples | [`ui-references/`](../../../ui-references/) |
| Visual principles | [`guidelines/`](../../../guidelines/) |

## Workflow

1. **Classify** the request: illustration, UI design, or adaptation of an existing asset.
2. **Consult** the relevant docs above. Read the files fully before generating.
3. **Select** existing assets: for illustrations, match the subject in `CATALOG.md`, then open the 2–3 closest files.
4. **Apply the Design System** for colors, typography, spacing and components, using token/component names rather than raw values.
5. **Reuse** existing components and assets whenever possible; only create what is missing.
6. **Generate** using what the current environment offers (see below).
7. **Verify** against the documented guidelines (contrast and legibility from `guidelines/`; for illustrations, compare with `STYLE_GUIDE.md`).
8. **Report** the files and tokens relied on, plus limitations and missing information.

## Illustrations

- Choose the sub-style as defined in `.github/copilot-instructions.md`: **energy/technology** (objects only, orange ring) or **people/workplace** (characters). Do not mix them unless a reference does.
- Reuse as is when a catalog file fits; link the path.
- Adaptation: work on a **copy** outside `illustrations/`. SVGs can be edited as text (recolor, hide/move elements, crop viewBox), but embedded base64 PNGs are not editable as vectors. PNGs: only scaling, cropping or format conversion with command-line tools.
- New scenes, characters or compositions need an image-generation tool or a designer. If none is available, say so and provide a brief/prompt listing the reference files instead. Hand-written SVG suits only simple shapes.
- Do not add text to illustrations without asking (existing text is French, typeface unidentified).

## UI design

- Prefer existing coded Design System components when accessible (repository, package or docs available to you). Do not copy their code here or rebuild them.
- Use Figma only if a Figma connection is actually available; otherwise say so.
- `colors/`, `typography/`, `spacing/` and `ui-references/` may contain only placeholders. If a needed token, component or reference is not documented, **ask the user** rather than guessing.

## Constraints

- Never invent brand colors, typography, spacing values, or official design rules.
- `STYLE_GUIDE.md` is observational: never present its patterns as official brand rules. Its hex values are not verified tokens.
- Never modify originals in `illustrations/`.
- Only claim to have looked at an image if its content was actually accessible (image input supported); otherwise rely on catalog text/SVG source and state that.
- Do not assume image generation is available.
- Generated visuals are drafts that need designer review.
