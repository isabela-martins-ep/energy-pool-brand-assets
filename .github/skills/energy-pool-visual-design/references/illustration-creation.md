# Illustration creation procedure

Used by the skill for new illustrations and adaptations. Facts about the existing artwork live in [`illustrations/STYLE_GUIDE.md`](../../../../illustrations/STYLE_GUIDE.md) and [`illustrations/CATALOG.md`](../../../../illustrations/CATALOG.md); this file does not repeat them.

1. **Classify the sub-style:** energy/technology (SVG, objects, orange ring) or people/workplace (PNG, characters). Do not mix them unless a reference does.
2. **Reuse first.** Search `CATALOG.md` by subject. If a file fits as is, use it and cite the path. Not every suggested usage is approved; flag it for confirmation.
3. **Open the 2-3 closest reference files** and look at them if your environment can display images (state clearly whether you did). If not, work only from the catalog text and SVG source, and say that visual comparison was not possible.
4. **Adapt only on a copy outside `illustrations/`.**
   - SVG: edit as text (recolor to documented tokens, hide or move elements, crop the viewBox). Embedded base64 PNGs are not vector-editable.
   - PNG: scale, crop or convert only.
5. **New scenes or characters** need an image-generation tool or a designer. Use the "Detail observations" table in `STYLE_GUIDE.md` as the brief (proportions, shapes, faces, colors, shading, composition). If no generator is available, deliver the brief and the reference file list, not an imitation. Hand-written SVG is acceptable for simple shapes only.
6. **Colors:** the illustrations use hex values that mostly do not match tokens. For new work, choose tokens per [`guidelines/TOKENS.md`](../../../../guidelines/TOKENS.md); do not copy colors from screenshots. If the orange/grey roles for illustrations are `TO BE PROVIDED`, say it.
7. **Do not add** text, third-party logos, flags, new recurring characters, the logo or the pictogram without confirmation.
8. **Check consistency** with the references (same sub-style, outline-free, face simplicity, orange focal / grey context, gradients no stronger than references), list deviations, then run the QA gate. Any deviation from OBSERVED traits needs human validation; none of these traits is official.
