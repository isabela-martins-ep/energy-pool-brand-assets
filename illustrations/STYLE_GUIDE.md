# Illustration style guide

**Single source for illustration style.** Other files point here; they do not copy it.

## 0. Official decisions (design team, 2026-10-28)

These nine decisions are **OFFICIAL** and apply to everything below. The rest of the file is OBSERVED.

1. **Colors.** Brand colors come from the tokens. Colors needed to depict people and objects (skin, hair, secondary clothing, greys, shading) may be used if consistent with the existing official illustrations (§5). They are not brand colors and must not be used for backgrounds, titles or other communication elements.
2. **Gradients.** Subtle gradients are allowed when they reproduce the treatment observed in the references (§2). Avoid complex gradients, realistic lighting, pronounced shadows and 3D effects.
3. **AI creation.** AI agents may create new Energy Pool illustrations following the references and this Skill. Each new creation needs a compliance check (`VISUAL_QA.md`) and human validation before official distribution.
4. **Reuse.** Recurring characters, poses, objects and graphic motifs may be reused or adapted for new coherent scenes. Official logos and symbols must be placed from the source files, never redrawn, distorted or reinterpreted (`BRAND_RULES.md` Logo).
5. **Proportions.** No fixed numeric proportions. The official illustrations are the reference for heads, bodies, limbs and faces; consistency with the existing graphic family has priority.
6. **Do.** Flat-design vector illustrations; simple, geometric, slightly rounded shapes; stylized, expressive, inclusive characters with simplified faces; palette consistent with the official illustrations, orange and greys dominant; limited detail and readable compositions; subtle gradients only when consistent with the references.
7. **Don't.** Photorealism and 3D; complex textures and material effects; strong shadows, dramatic lighting, metallic effects; thick black outlines; characters with realistic proportions or exaggerated cartoon style; decorative elements with no visual or narrative function.
8. **Text, third-party logos, flags.**
   - Text is allowed in an illustration when it is relevant (screen, poster, signage, title). Chillax for titles, Synonym for other text (`BRAND_RULES.md` Typography). Keep it short and check spelling and the rendered font; where a generator is unreliable with text, adding it as live text at final composition is a practical option, not a requirement.
   - Never invent slogans, data or messages attributed to Energy Pool.
   - Third-party logos and flags may appear when the context needs them. Use official files when available (supplied ones: [`brand-examples/third-party-logos/`](../brand-examples/third-party-logos/)); never invent, distort or alter them. If the official file is missing, report it instead of generating an imitation.
9. **Backgrounds and framing.** Prefer transparent or white background. Simplified backgrounds are allowed when they help understand the scene; avoid realistic, busy or over-detailed settings. Adapt the framing to the use (full figure, close-up, group, full scene); keep the scene readable and do not crop essential elements by accident.

Status of every rule below: **OBSERVED** = measured or seen in the 31 reference files of this folder (all viewed; colors measured on the 23 PNG and read from the 8 SVG sources). It is **not** an official brand rule. Official rules and missing decisions: [`../guidelines/BRAND_RULES.md`](../guidelines/BRAND_RULES.md). Per-file inventory: [`CATALOG.md`](CATALOG.md). Procedure: [`illustration-creation.md`](../.github/skills/energy-pool-visual-design/references/illustration-creation.md). Checklist: [`VISUAL_QA.md`](../guidelines/VISUAL_QA.md#illustration-checklist).

Classes used: **F** = fundamental (present in nearly all references of the sub-style), **V** = acceptable variation (seen in some, same family), **S** = specific to one file; never turn an S into a rule.

Sections 1 to 6 are **guidance (level B, see [`BRAND_RULES.md`](../guidelines/BRAND_RULES.md#rule-levels))**: reproduce the graphic language, not a reference's composition. Permissions in §0 (text, scenery, gradients, backgrounds, third-party logos) are not obligations. Composition, poses, framing and format are the agent's creative choice.

The agent must compare against the reference images themselves, not only this text. Proportions are described qualitatively; exact ratios were **not determinable** and must not be invented.

## 1. Two sub-styles (do not mix in one file)

| Sub-style | Files | Content |
|---|---|---|
| People / workplace | 23 PNG | Characters in orange tops, grey context objects |
| Energy / technology | 8 SVG | Objects only, orange ring, cloud with sync arrows |

## 2. Graphic treatment (both sub-styles)

- **F** No outlines or strokes around shapes; shapes are filled areas with rounded corners.
- **F** Soft linear gradients inside shapes (orange: lighter to darker left to right or top to bottom; grey: near-white to light grey top to bottom). No hard shadows, textures, highlights or photographic detail.
- **F** Orange marks the focal subject; light greys are context (furniture, trousers, devices, buildings).
- **F** White or transparent background; no frame or border.
- **V** Fade-out: a shape dissolves to transparent at its edge (thought-bubble figure in `QVT`, translucent pale leaves).
- **V** Thin lighter or darker lines inside a shape to show folds, hair strands, hands, seams (grey lines on a white shirt in `EP-Women-1`, orange fold lines on sleeves).
- **S** Detailed gradients with white edges and a darker orange `#EA5B0C` appear in the SVG energy files only.

## 3. People / workplace characters

- **F Body:** simplified, slim, long limbs; torso and sleeves as single smooth shapes; hands as simple rounded shapes (thumb and finger groups, no joints); full-body figures end in small grey rounded shoes or are cropped at the torso. Head size relative to the body: small to medium, ratio not determinable.
- **F Face:** oval or round head, two dark dot eyes, thin dark brows, no or almost no nose (a tiny line at most), one small mouth in orange (smile, filled when open), small ear shapes at the sides. No eyelashes, no cheeks, no shading on the face other than a soft skin gradient.
- **V Face:** closed eyes as short arcs (`QVT`); teeth shown in a broad smile (`EP-Women-1`); round dark glasses (`EP-Women-1`); beard in dark brown (`entretien individuel-v2`).
- **F Hair:** one or two flat masses with a gentle gradient; strand details only as a few lighter or darker lines (bangs, ponytail, curls). Hair colors seen: dark brown, black, grey-brown, blond, light orange-blond.
- **F Skin:** a range of light peach to dark brown, filled with a subtle gradient; the same skin tone is used for face, neck and hands. Skin tones do not match any token.
- **F Clothing:** tops in orange tints (light to saturated), trousers light grey to white with a vertical gradient, shirts or jackets with a collar or lapel shown by a lighter line or a lighter orange shape; folds as thin darker-orange lines. Dark trousers and a white shirt exist (`EP-Women-1`, `Forum`) as **V**.
- **F Poses:** relaxed and active (waving, fist raised, arms crossed, hand on hip, cross-legged, holding a device or a document); body orientation toward the interaction; groups overlap slightly or sit side by side.
- **F Diversity:** skin tones, hair, ages, glasses, a bald bearded man, a wheelchair user (`Forum`, **S**).
- **V** Recurring characters (bearded man, blond woman in a blazer) may be reused or adapted (decision 4).

## 4. Objects and scenes

- **F** Objects are reduced to identifiable parts: laptop (grey screen, base), mug, plant (pale orange leaves, white or grey pot), table (large pale grey plane), chairs (grey back), bubbles (orange or grey with a short tail and a few lines or one icon).
- **F** Context objects in `#EFEFEF`-like light grey with a slightly darker grey edge or side; orange used for one or two accents (stripes on a lightbulb, a stripe, an arrow).
- **F** A pale grey ground ellipse under standing groups (`EP-Women-3`, `pause-café`, `Pause-café-plante`).
- **V** Conceptual scenes: small floating icons around a central figure (`QVT`, `Compétences`, `Formation`); a dashed trail of circles (`Formation`).
- **Energy / technology (F in the 8 SVG):** wind turbines, panels, battery with + and −, pylons, factory, dams, dashboards; mostly grey objects with orange parts in several tints (pale to saturated) to show repetition or depth; a thick orange gradient ring or line linking them, often with a cloud icon holding sync arrows. Some orange shapes have a thin white edge (**V**). The 8 SVG embed base64 PNGs and are not fully vector.
- **S** Third-party logos (`Compétences`, `Formation`), flags (`Equipe internationale`), product names in text (`Empowill`, `SIRH`).
- The Energy Pool pictogram appears on mugs, laptops, screens as existing artwork (**V**). In new illustrations, place it from the official files per `BRAND_RULES.md` Logo; never redraw it (decision 4).

## 5. Colors (measured; compare with tokens)

Measured on 1.16 M opaque pixels of the 23 PNG; only **18.2 %** equal a token exactly.

| Role | Observed values | Token match |
|---|---|---|
| Brand orange | `#FF9900` | `vitamin-c` |
| Mid orange | `#FFB84D` | `vitamin-c` tint 700 |
| Pale orange | `#FFE0B3` (and `#FEE0B3`) | `vitamin-c` tint 300 |
| White | `#FFFFFF` | `white` |
| Light greys | `#EFEFEF`, `#EDEDED`, `#EEEEEE`, `#D0D0D0`, `#CFCFCF` | none |
| Dark grey (hair, details) | `#3C3C3B`, `#3C3C3C` | none |
| Skin and hair browns | `#BE926E`, `#966B3D`, `#916D45`, `#A67356`, `#432E1D` | none |
| SVG energy | `#EA5B0C`, `#FFC774`, `#FFB342`, `#FFA41E`, `#FF9C08`, `#F7EAC6` | none |

- Observed distribution: light greys about 30 % of pixels, orange family about 15 %, white about 4 %, remainder skin, hair and gradient intermediates.
- A color close to a token is **not** a match. Token selection: [`../guidelines/TOKENS.md`](../guidelines/TOKENS.md).
- Orange and white: tokens. Greys, skin, hair, secondary clothing and shading: take the values from the closest references (decision 1); list them in the report as non-token, reference-derived colors. Never use them for backgrounds, titles or other communication elements.

## 6. Composition and legibility

- **F** (typical, not required) One subject or one small group, centered, isolated; generous empty space around.
- **F** 1 to 4 people; 3 to 6 secondary objects at most; one idea per illustration.
- **F** Orange area concentrated on the people or the key object; context stays grey.
- **V** Seated scenes around a table seen from the front; back-view figures have no face (`Forum`).
- **F** Remains readable when small because shapes are large and simple; no fine detail is needed to read the scene.
- Reference backgrounds are white or transparent with at most a ground ellipse, a table or a stand; simplified backgrounds (decision 9) go beyond what the 31 files show: keep them as minimal as those objects.
- No fixed canvas ratio is observed (see `CATALOG.md`). Text inside the artwork is rare and in French; decision 8 governs new text.

## 7. Not determinable from the references

Head-to-body ratio, exact line widths, gradient angles and stops, minimum size, corner radii. Do not invent numbers (decision 5); match the closest references by viewing them.

## 8. Official rules

Beyond §0, not in this file. The remaining missing official information (none; naming convention for new files and the absence of an official owner: BRAND_RULES.md) is in [`../guidelines/BRAND_RULES.md`](../guidelines/BRAND_RULES.md).
