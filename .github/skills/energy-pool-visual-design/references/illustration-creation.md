# Illustration creation procedure

Details the five steps of [`SKILL.md`](../SKILL.md) for illustrations. Official decisions (§0) and style rules (F/V/S classes, colors, characters, objects, composition): [`STYLE_GUIDE.md`](../../../../illustrations/STYLE_GUIDE.md), the single source. AI creation is allowed; output needs a compliance check and human validation before official distribution. Inventory: [`CATALOG.md`](../../../../illustrations/CATALOG.md). Official rules and `TO BE PROVIDED` items: [`BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md). Colors: [`TOKENS.md`](../../../../guidelines/TOKENS.md). Checks: [`VISUAL_QA.md`](../../../../guidelines/VISUAL_QA.md#illustration-checklist).

## Use the images, not only the text

Open the reference image files themselves and look at them. If the environment cannot display images, or cannot pass them to a generator, say so in the report: no claim of having analyzed or faithfully reproduced a file that was not viewed. The text of `STYLE_GUIDE.md` alone is not enough to create a new illustration.

## Reuse first

Search `CATALOG.md` by subject. If a file fits, use it as is or on a copy outside `illustrations/` (cite the path; catalog usage suggestions are not approved uses, flag them). SVG: edit as text (recolor to tokens, hide or move elements, crop the viewBox); embedded base64 PNGs are not vector-editable. PNG: scale, crop or convert only.

## Creating a new illustration (7 steps)

1. **Understand** the subject, audience and use. List what must appear (people, objects, message).
2. **Identify** the 2 to 3 closest official illustrations in `CATALOG.md` (same sub-style: people/workplace or energy/technology; do not mix). Add them to the source manifest as viewed or not viewed.
3. **Analyze** them side by side: which `STYLE_GUIDE.md` traits are F (fundamental) in all of them, which are V, which are S. Note face, hair, clothing, hands, shading, object and composition choices.
4. **Choose** what to reuse: F traits always; V traits only if the closest references show them; S traits never. Brand colors from tokens per `TOKENS.md`; greys, skin, hair and shading from the closest references (`STYLE_GUIDE.md` §0.1), listed as non-token. Do not add text, third-party logos or flags without confirmation. Recurring characters, poses, objects and motifs may be reused. Logo and pictogram: from source files only, `BRAND_RULES.md` Logo.
5. **Design** a new scene: new poses, composition and props for the subject. Do not copy a reference composition. Without an image-generation tool or a designer, deliver the brief, the reference list and the token choices, not an imitation. Hand-written SVG only for simple shapes.
6. **Compare** the result with at least 2 references (view both): run the illustration checklist in `VISUAL_QA.md`. Resemblance, orange or a vector look alone is not proof of compliance.
7. **Correct** each deviation; re-run step 6. Deviations from OBSERVED traits that remain need human validation. Deliver as in `SKILL.md` step 5.
