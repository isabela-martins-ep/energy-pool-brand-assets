# Illustration creation procedure

Details the five steps of [`SKILL.md`](../SKILL.md) for illustrations. Facts about existing artwork are in [`STYLE_GUIDE.md`](../../../../illustrations/STYLE_GUIDE.md) (observed, not official) and [`CATALOG.md`](../../../../illustrations/CATALOG.md); rules are in [`BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md).

1. **Consult.** Classify the sub-style: energy/technology (SVG, objects, orange ring) or people/workplace (PNG, characters); do not mix them unless a reference does. Write the manifest: `CATALOG.md`, `STYLE_GUIDE.md`, the 2-3 closest files, token files. Open the closest files and look at them if the environment can display images; state whether you did. Without image viewing, work from the catalog text and SVG source and say visual comparison was not possible.
2. **Select.** Reuse first: search `CATALOG.md` by subject; if a file fits, use it and cite the path (catalog usage suggestions are not approved uses: flag them). Colors come from tokens per [`TOKENS.md`](../../../../guidelines/TOKENS.md), not from existing artwork, which mostly does not match tokens (see `BRAND_RULES.md`). Illustration color roles and the AI-creation policy are `TO BE PROVIDED`: say so.
3. **Create or modify**, on a copy outside `illustrations/`.
   - SVG: edit as text (recolor to tokens, hide or move elements, crop the viewBox). Embedded base64 PNGs are not vector-editable.
   - PNG: scale, crop or convert only.
   - New scene or character: needs an image-generation tool or a designer. Use the "Detail observations" table in `STYLE_GUIDE.md` as the brief. Without a generator, deliver the brief and the reference list, not an imitation. Hand-written SVG only for simple shapes.
   - Do not add text, third-party logos, flags or new recurring characters without confirmation. Logo and pictogram: `BRAND_RULES.md` Logo.
4. **Verify** against the references (same sub-style, face simplicity, orange focal / grey context, gradients no stronger than references) and list deviations; deviations from OBSERVED traits need human validation. Then run [`VISUAL_QA.md`](../../../../guidelines/VISUAL_QA.md).
5. **Deliver** as in `SKILL.md` step 5.
