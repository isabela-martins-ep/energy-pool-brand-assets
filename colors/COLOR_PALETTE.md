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

This is a graphic palette, not a set of status colors: green, red, yellow and the others are not reserved for success, error or warning. Combine them freely to create original visuals; **orange is the main identity color**. Use these exact values. No tints, shades or other variants of these colors are defined: do not create any.

## Colors outside this palette

Only these cases, each documented in its own file:

- **White (`#FFFFFF`):** not one of the 8 tokens. The official logo rules use white backgrounds and white panels ([`BRAND_RULES.md` Logo](../guidelines/BRAND_RULES.md#logo)), so white stays allowed for those uses.
- **Illustrations:** colors needed to depict people and objects (skin, hair, secondary clothing, greys, shading), per [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) §0, decision 1.
- **Energy-source data:** [`energy-assets.json`](energy-assets.json) (chart, icon and background color per energy source and sector), only for content about that source.
- **UI components:** [`Mode 1.tokens 3.json`](Mode%201.tokens%203.json) (states, borders, focus), not for decoration.
