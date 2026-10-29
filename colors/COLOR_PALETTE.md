# Energy Pool color palette

**OFFICIAL.** The 8 colors of the Energy Pool graphic palette (supplied by the design team, 2026-10-29). This file is the single source for brand color values; other files link here instead of copying them. Usage rules: [`../guidelines/BRAND_RULES.md`](../guidelines/BRAND_RULES.md#colors).

| Name | HEX |
|---|---|
| `orange` | `#FF9900` |
| `cream` | `#FFEBCC` |
| `green` | `#3EBE90` |
| `red` | `#CD4B25` |
| `yellow` | `#F2C628` |
| `lavender` | `#F0E7FE` |
| `light-gray` | `#DDDDDD` |
| `dark` | `#181818` |

```json
{"orange":"#FF9900","cream":"#FFEBCC","green":"#3EBE90","red":"#CD4B25","yellow":"#F2C628","lavender":"#F0E7FE","light-gray":"#DDDDDD","dark":"#181818"}
```

This is a graphic palette, not a set of status colors: green, red, yellow and the others are not reserved for success, error or warning. Combine them freely to create original visuals; **orange is the main identity color**, without having to dominate every creation. Proportions and combinations are a creative choice.

## Variations

Agents may derive lighter, darker or less saturated variations of these 8 colors (and of the charter colors below) to build harmonious compositions, adapted to each project. Rules:

- A variation is derived from a listed color, never a new hue.
- It is **not** an official color: report it as derived (for example `orange, lighter -> #FFC266`), never under an official name.
- No set of variations is defined; do not create or publish a palette of shades.
- Use the exact listed HEX when you use an official color itself.

## Charter identity colors

**OFFICIAL.** Energy Pool brand charter, p. 10 "Colors - Palette" ([`Colors _ Palette.svg`](Colors%20_%20Palette.svg), original page, do not modify). Kept alongside the 8-color palette, which it does not replace. Charter text: "Our color palette is built around vibrant orange tones, reflecting the energy, dynamism, and warmth at the core of our industry. [...] Complementary grey tones may be used alongside the orange palette to provide balance, structure, and visual clarity."

| Group | Charter name | HEX | Same value in the 8-color palette |
|---|---|---|---|
| Primary tones | Vitamin | `#FF9900` | `orange` |
| Primary tones | Black | `#181818` | `dark` |
| Primary tones | White | `#FFFFFF` | none |
| Orange tones | Power | `#F66000` | none |
| Orange tones | Solar | `#FFBB44` | none |
| Orange tones | Windy | `#FFEBCC` | `cream` |
| Grey tones | 60% | `#666666` | none |
| Grey tones | 45% | `#8C8C8C` | none |
| Grey tones | 20% | `#CCCCCC` | none |
| Grey tones | 5% | `#F2F2F2` | none |

Grey HEX values are read from the SVG source (the page shows only the percentages).

## Gradients

**OFFICIAL.** Brand charter, p. 11 "Colors - Gradient" ([`Colors _ Gradient.svg`](Colors%20_%20Gradient.svg)). Charter text: "To complement our palette, we also use gradients for different media. It should be used sparingly and is always used horizontally, from the primary color "Vitamin" towards "Power". Grey tones can also be used in gradients, but only in similar shades."

- **Orange gradient:** horizontal, from Vitamin `#FF9900` to Power `#F66000`. Shown as not allowed: Windy `#FFEBCC` to Power.
- **Grey gradient:** horizontal, between similar grey tones (example shown: 5% `#F2F2F2` to 20% `#CCCCCC`). Shown as not allowed: 5% to 60% `#666666`.
- Use gradients sparingly; no other gradient is documented. Shading inside illustrations follows [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0, decision 2.

## Colors outside this palette

Beyond the 8 colors, the charter colors and their variations, only these cases, each documented in its own file:

- **White (`#FFFFFF`):** a charter primary tone, also required by the logo rules (white backgrounds and white panels, [`BRAND_RULES.md` Logo](../guidelines/BRAND_RULES.md#logo)) and by illustration placement ([`STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0, decision 9).
- **Illustrations:** colors needed to depict people and objects (skin, hair, secondary clothing, greys, shading), per [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0, decision 1.
- **Energy-source data:** [`energy-assets.json`](energy-assets.json) (chart, icon and background color per energy source and sector), only for content about that source.
- **UI components:** [`Mode 1.tokens 3.json`](Mode%201.tokens%203.json) (states, borders, focus), not for decoration.
