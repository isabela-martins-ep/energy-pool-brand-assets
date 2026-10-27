# Copilot instructions — Energy Pool brand assets

Energy Pool already has an established Design System (Figma + implemented code). This repository holds the visual references that help you generate UIs, prototypes and visuals consistent with it.

## Rules

1. **Design System first.** Prioritize existing components, design tokens and guidelines. Reference them; never duplicate or redefine them here.
2. **Use this repository's resources.** Before generating anything, read the relevant folder:
   - `colors/` — brand colors and token references
   - `typography/` — font families, weights, hierarchy
   - `spacing/` — spacing and layout values
   - `illustrations/` — illustration style and existing assets
   - `ui-references/` — existing interfaces, layouts, components
   - `guidelines/` — visual principles and usage rules
3. **Do not invent** brand colors, typography, spacing values, illustration styles or visual styles. Use only documented tokens/values.
4. **Ask when information is missing.** If a token, component or reference isn't documented, ask for clarification instead of assuming.
5. **Prefer tokens over raw values** (token names rather than hex codes or pixel values) whenever a token exists.
6. **Accessibility:** respect contrast and legibility rules from `guidelines/`.
7. **Cite sources:** mention which reference files/tokens you relied on.

## Illustrations

Sources: `illustrations/CATALOG.md` (what each file shows), `illustrations/STYLE_GUIDE.md` (observed characteristics). The style guide is **observational**: it describes the existing files, and **no official illustration rules are documented yet**. Never present observed patterns as official brand rules.

### Selecting references
1. Read `illustrations/CATALOG.md` first and match the request's subject to the "Subject" column (the "Suggested usage" column is unconfirmed).
2. Decide the sub-style (below), then open the 2–3 closest files and the matching sections of `STYLE_GUIDE.md`.
3. Name the files you relied on in your answer. If nothing in the catalog fits, say so and ask rather than guessing.
4. Colors: use Design System tokens. The hex values in `STYLE_GUIDE.md` come from SVG source and are not verified as tokens.

### Two sub-styles
| | Energy / technology | People / workplace |
|---|---|---|
| Files | `Agregation`, `DR Program`, `HPP`, `Islanded microgrids`, `Producers`, `Prosumer`, `Technology`, `Utilities` (SVG) | All PNG files in the catalog under "People & workplace" |
| Content | Objects only (turbines, panels, pylons, battery, factory, dashboards, circuit device) | Characters in orange tops, grey/white trousers, grey props |
| Signature | Thick orange gradient ring or curve linking grey objects with orange accents; cloud + sync icon on the ring in several files | Diverse characters, friendly poses, pictogram on mugs/laptops, bulb and plant props |
| Avoid | Adding people | Mixing in the energy ring motif unless a reference does |

Both: flat vector, no outlines, soft gradients, transparent/white background, orange + neutral greys.

### Reuse, adapt or generate
- **Reuse as is:** when a catalog file matches the subject. Link or copy the file path; do not modify originals in `illustrations/`.
- **Adapt an SVG (Copilot can edit text/code):** for small changes to the 8 SVG files, such as recoloring to tokens, hiding or moving a vector element, resizing or cropping the viewBox. Work on a **copy** outside the original. These SVGs embed base64 PNGs, so those parts cannot be edited as vectors.
- **Adapt a PNG:** Copilot cannot edit pixels. Only trivial operations (scaling, cropping, format conversion) with a command-line tool, on a copy.
- **Needs a dedicated image-generation tool or a designer:** new scenes, new characters, new poses, or compositions with new objects. Copilot can write the brief/prompt and list the references, but cannot guarantee the output matches the brand. Generated results must be reviewed by a designer.

### Limitations
- Copilot can inspect an image only if the model/runtime supports image input; if not, it can rely only on the catalog text and SVG source and must say so.
- Copilot cannot measure PNG colors exactly, and cannot generate raster or vector artwork by itself; hand-written SVG is only suitable for simple shapes and will not match the existing illustrations.
- Generated visuals are drafts: they are not validated against official guidelines, which are not documented here.
- Text embedded in illustrations is French in existing files; typefaces are unidentified, so do not add text without asking.

### Example prompts
1. **Reuse:** "I need an illustration for a slide about our hybrid power plant offer. Which existing file fits?" → expected: `HPP.svg`, with rationale from the catalog.
2. **Adapt an SVG:** "Make a copy of `Producers.svg` without the dam, keep the ring and the other objects as they are." → edit a copy; originals untouched; embedded PNG limits noted.
3. **Brief for a new energy illustration (generation tool):** "Write a prompt for an image tool to illustrate energy storage in the energy/technology style: grey battery, orange accents, thick orange gradient ring, no people. References: `HPP.svg`, `Islanded microgrids.svg`, `Technology.svg`."
4. **Brief for a new people illustration:** "Write a prompt for a new scene of two colleagues at a whiteboard in the people/workplace style: orange tops, light grey trousers, grey furniture, flat vector, no outlines, diverse characters. References: `EP-Women-3.png`, `Réunion-équipe.png`, `entretien individuel-v2.png`."
5. **Consistency check:** "Compare this draft illustration with `STYLE_GUIDE.md` and list where it differs from the observed characteristics. Do not judge it against official rules." → list deviations and flag anything needing designer review.

## Contributing

Keep files small and in the right folder. Do not copy Design System code or Figma content; link to them. Use the templates in `illustrations/` and `ui-references/`.
