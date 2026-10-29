# Poster, flyer, infographic and slide workflow

Details the eight steps of [`SKILL.md`](../SKILL.md) for single-page and slide supports (posters, flyers, infographics, presentations, social and HR visuals). Rule levels: [`BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md#rule-levels). It never overrides `BRAND_RULES.md`.

## 1. Understand

Take from the request: goal, audience, exact text and data, mandatory information (date, place, contact), supplied assets, medium. Ask, in one message, only what is essential and missing (typically the content itself). Do not ask about layout, composition or style: decide (level C).

- Format and size: if not given, choose the usual one for the medium and state it as a choice. No official format exists, so none is imposed.
- Text fidelity (`BRAND_RULES.md`, mandatory rule 5): use exactly the supplied text, or, when redoing a visual, exactly its existing text. Do not invent slogans, data or messages attributed to Energy Pool.

## 2. Consult and 3. Select references

Read the sources in `SKILL.md` step 2. Use approved examples from `brand-examples/` when they exist and follow them. Otherwise design an original layout from the brand rules; do not invent official grid or layout rules, and label the layout a proposal. For illustrations, use a catalogued file when one fits, else [`illustration-creation.md`](illustration-creation.md). Pictogram sets exist in `illustrations/` (`Pictograms _ Custom.svg`, `Pictograms _ Font Awesome.svg`) but are not catalogued: view them before use.

## 4. Graphic direction (keep it short)

| Item | Rule |
|---|---|
| Colors | The 8 palette colors and the charter colors of [`COLOR_PALETTE.md`](../../../../colors/COLOR_PALETTE.md) with exact HEX (role -> color name -> HEX), plus derived variations reported as such. Combine them freely, in any proportions, and choose where each goes yourself, with orange as the main identity color (do not present your choice as an official rule). Gradients: only the official ones, sparingly. |
| Typography | Chillax for titles, Synonym for other text, per `BRAND_RULES.md` Typography. Only the official weights; hierarchy, sizes, case and alignment follow the text-composition convention in `BRAND_RULES.md` Typography (no official scale). Say which font was actually rendered; an image generator does not guarantee them. |
| Logo | Follow the selection procedure in [`BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md#logo): variant by background, size and clear space checked. Record the file, background and placed width internally. |
| Illustration and pictograms | Catalogued files or new illustrations coherent with `STYLE_GUIDE.md`, placed on a white area (§0, decision 9); pictograms per [`BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md#pictograms) (Font Awesome Classic Solid; custom set to be provided, not available yet). Text in an illustration is allowed when it helps (same fonts rule). |
| Layout | Composition, hierarchy, whitespace, framing and background are creative choices adapted to the medium. Text over clear areas, legible. |
| Method | Compose from existing resources (exact text, logo, palette colors) whenever possible. A generated image is a proposal; it is not evidence of compliance. |

## 5. Create, 6. Verify, 7. Correct

Sketch two or three compositions mentally or briefly, keep the strongest, and deliver one file unless options are requested. Build the visual from the direction without altering brand values. For an existing poster, keep its content, structure, logo and resources unless the user named the element to change; never reconstitute an element from memory. Run [`VISUAL_QA.md`](../../../../guidelines/VISUAL_QA.md) on the produced file (if the environment cannot display it, visual checks are `Not verifiable`), marking non-applicable criteria `N/A`, then correct blocking non-compliances and style gaps.

## Infographics

Data, labels and units are exactly those supplied; no estimated or invented figures. Chart colors from the palette, or from [`energy-assets.json`](../../../../colors/energy-assets.json) only for their energy source. Any chart value that cannot be checked against the supplied data is reported.

## 8. Deliver

The file, a few lines on the main design decisions, and limits or points to validate, with the AI label. Detailed report only on request or if a compliance problem requires it.
