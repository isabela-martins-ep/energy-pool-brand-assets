# Illustration style guide

How to read this document:

- **Observed** = visible in the existing files in this folder (31 files, all reviewed visually). It describes what is there; it is **not** an official rule.
- **Official** = documented brand rule. **None is documented yet**; see [Official rules (to be provided)](#official-rules-to-be-provided).

Per-file details: [`CATALOG.md`](CATALOG.md). Colors, typography and spacing must come from the Design System tokens (see `../colors/`, `../typography/`, `../spacing/`), not from this document.

## Observed characteristics

### Overall style
- Flat vector look with no outlines around shapes. Soft linear gradients on some shapes (orange, grey) give slight volume; no hard shadows, textures or photographic detail.
- Simplified, rounded forms. Faces are reduced to dots or short strokes for eyes and brows and a small orange mouth.
- Backgrounds are transparent or white. Several people illustrations stand on a pale grey ground ellipse (e.g. `EP-Women-3`, `pause-café`, `Pause-café-plante`).

### Colors (visual observation; PNG values were not measured)
- Two families: **orange** (tints from pale peach to saturated orange) and **neutral greys** (very light to mid grey). Orange marks the focal subject (clothing, key object); grey is used for context (furniture, buildings, pylons, trousers, bubbles).
- Skin and hair tones are the only other colors (browns, tan, blond, dark brown/black), with varied skin tones.
- Hex values found in the source of the 8 SVG files (factual for these files only):
  - Oranges: `#ea5b0c`, `#ffb84d`, `#ffe0b3`; also `#ffc774`, `#ffb342`, `#ffa41e`, `#ff9c08` in `DR Program.svg`
  - Beige: `#f7eac6` (`Agregation.svg`)
  - Greys: `#efefef`, `#ededed`, `#d0d0d0`, `#b2b2b2`
- Whether these match Design System tokens is **not verified**; map them to tokens before reuse.
- Exceptions: `Compétences` and `Formation` include third-party tool logos (Python, Jira, Excel, AWS) in their own colors; `Equipe internationale` includes small flag icons.

### Two sub-styles
1. **Energy / technology (SVG, 8 files):** objects only (wind turbines, solar panels, pylons, battery, factory, dam, house, dashboards, circuit-board device). A thick **orange gradient ring or curved line** encircles or links the elements; in several files a **cloud icon with sync arrows** sits on it. Objects are mostly grey with orange accents, and orange tint varies from pale to strong to suggest depth or repetition. Some orange shapes have a thin white edge.
2. **People / workplace (PNG, 23 files):** characters wearing **orange tops** in several tints, with light grey or white trousers (dark trousers in one case). Props and furniture are grey, with occasional orange or brown (desk legs in `EP-Women-3`).

### Characters
- Simplified full-body or half-body figures with soft, darker-orange shapes for clothing folds.
- Visible diversity: skin tones, hair colors and styles, a bald bearded man, glasses, a wheelchair user (`Forum`).
- Friendly, active poses: waving, high-five, pointing, running, meditating, holding mugs.
- The same characters recur across scenes (bearded man, blond woman in a blazer, man in an open orange shirt over a white tee), which helps continuity.

### Brand elements inside illustrations
- The Energy Pool pictogram (black ring, orange dot, orange angle brackets) appears on mugs, laptops, a car, a wall screen and large in `SIRH` and `Forum`. The wordmark appears in `Forum`.
- Recurring props: lightbulb with orange stripes, plant with orange leaves, mugs with the pictogram.
- Speech or thought bubbles (`Compétences`, `EP-Women-2`, `entretien individuel-v2`) and a grey dashed trail (`Formation`) express dialogue and movement.

### Composition and proportions
- Mostly centred, isolated compositions without frame or border.
- Groups of 2–4 people shown side by side, standing or seated at a table.
- Conceptual scenes use floating icons around the subject (circles in `Compétences`, objects around the meditating man in `QVT`, a trail of circles in `Formation`).
- Aspect ratios vary widely (about 1:8 for `EP-Women-logo` to roughly square or portrait); no fixed canvas size is observed. See the catalog for pixel sizes.

### Level of detail
- Low to medium. Technology objects show only identifiable features (blades, panel grid, chimneys, +/- on battery, circuit lines).
- Text inside illustrations is rare and in French (`EP WOMEN`, `MÉTÉO DES ÉQUIPES`, `SIRH`, `Empowill`, `Energy Pool`). Typefaces were not identified.

### Technical observations
- The 8 SVG files contain embedded base64 PNG images in addition to vector shapes, so they are not fully editable vectors. Gradients are widely used (31 gradient references in `Agregation.svg`).
- PNG sizes range up to 6227 × 4433 px. Transparency was not verified per file.
- File naming is inconsistent (capitalization, accents, spaces, French/English mix).

## Using this guide to create new visuals
- Reuse an existing file when the subject matches; check [`CATALOG.md`](CATALOG.md) first.
- For new visuals, follow the observed patterns (flat vector, orange + grey, orange outfits, simple rounded shapes, diverse characters) and **verify colors against Design System tokens**.
- Do not introduce new colors, outlines, 3D or photographic styles. If a need isn't covered by the observations, ask the design team.

## Official rules (to be provided)

Not documented in this repository yet. Please fill in:

- **Figma source:** <link>
- **Official color tokens used for illustrations:** <token names>
- **Allowed / forbidden usages (do / don't):** <...>
- **Minimum sizes, clear space, backgrounds (dark mode, colored backgrounds):** <...>
- **Character guidelines (diversity, poses, outfit colors):** <...>
- **Use of the Energy Pool pictogram/wordmark and third-party logos in illustrations:** <...>
- **Preferred formats and naming convention:** <...> (proposal: SVG, lowercase kebab-case without accents)
- **Owner / license / creation tool:** <...>
