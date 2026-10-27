# Brand rules for AI-generated visuals

Mandatory rules for anyone (human or AI) producing Energy Pool visuals from this repository. The Figma Design System and its coded components remain the source of truth; this file points to them and never redefines them.

## Status labels

| Label | Meaning |
|---|---|
| **OFFICIAL** | Taken from a Design System export stored in this repository (cite the file). |
| **OBSERVED** | Seen in existing assets. Describes what exists; **not** a brand rule. |
| **TO BE PROVIDED** | Not documented. Do not guess: ask the user, or state it as missing. |

Never promote an OBSERVED item to OFFICIAL. Never infer official colors or typography from illustration screenshots.

## Mandatory rules

1. Use only documented tokens, fonts and components. Never invent colors, fonts, spacing values, logo variants or design rules.
2. Reference colors, spacing and type by **token name** (with the value from the token file), not by eyeballed values.
3. Never redraw, recolor, stretch or generate the Energy Pool logo or pictogram. Use a supplied logo file only (none is in this repository yet, see [Logo](#logo)).
4. Never modify or overwrite files in `illustrations/` or other original assets. Work on copies outside the original folders.
5. If a rule you need is `TO BE PROVIDED`, say so in the answer and ask for it; do not fill the gap.
6. Label every AI-generated or AI-assisted visual as such. It is a draft until a human reviews and approves it before publication.
7. Before delivery, run [`VISUAL_QA.md`](VISUAL_QA.md) and report the result, including anything you could not verify.

## Colors

- **OFFICIAL source:** [`../colors/Default.tokens.json`](../colors/Default.tokens.json), a Figma variables export (mode "Default"). It holds `palette` (31 color families, most with `shades` 100-900 and `tints` 100-900, each with a `hex`) and `energy-assets` (chart/icon/background tokens per energy source and sector, referencing the palette). Confirm it is the current published version.
- **Snapshot of the export** (verify against the file before use):

| Token | HEX |
|---|---|
| `palette.orange-popsicle` | `#FF7F19` |
| `palette.vitamin-c` | `#FF9900` |
| `palette.white-smoke` | `#F5F5F5` |
| `palette.grey-russian` | `#8D949A` |
| `palette.dark-slate-gray` | `#355159` |
| `palette.white` / `palette.black` | `#FFFFFF` / `#000000` |

- **OBSERVED, SVG source colors vs tokens** (exact hex comparison; not a statement of intent): `#FFB84D` = `vitamin-c.tints.700`, `#FFE0B3` = `vitamin-c.tints.300`, `#FF9900` = `vitamin-c`. No token matches `#EA5B0C`, `#F7EAC6`, `#EFEFEF`, `#EDEDED`, `#D0D0D0`, `#B2B2B2`, `#FFC774`, `#FFB342`, `#FFA41E`, `#FF9C08`. Existing illustrations therefore cannot be assumed to use only tokens.
- **TO BE PROVIDED:**
  - Which palette families are brand colors versus data-visualization or status colors.
  - Primary/secondary roles, allowed combinations, text/background pairs and contrast requirements.
  - Dark-mode or other modes (the export has only "Default").
  - Gradient rules (existing illustrations use gradients).

## Typography

- **OFFICIAL source:** [`../typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json), a Figma variables export. It lists: heading and display font `Chillax`; body, base, monospace and code font `Synonym`; `Yu Gothic` (Japanese) and `Alexandria` (Arabic) variants; weights 300/400/500/600/700; base size 16, line heights 24/20/32; heading sizes h1-h6; display sizes 1-6; heading color `#181818`, muted text `#939393`. Headings use weight 500 and display uses weight 400 per the export. Units are not stated in the export.
- **Open conflict:** another Design System description mentions "Noto Sans" as the body font, while this export lists `Synonym`. **TO BE PROVIDED:** confirm which one is current.
- **TO BE PROVIDED:**
  - Font files, licenses and approved fallbacks for tools that cannot load Chillax or Synonym (many AI image tools and Microsoft 365 apps cannot).
  - Type scale for print and posters (the export targets UI), text case and alignment rules, maximum line length.
- Rule: if the real font cannot be used in the output, say so and name the fallback requested from the design team; never silently substitute.

## Logo

- Nothing official is stored in this repository: no logo files, clear-space, minimum-size, color-variant or forbidden-use rules. **TO BE PROVIDED:** all of the above, plus approved logo files for light/dark backgrounds.
- **OBSERVED:** a pictogram (black ring, orange dot, orange angle brackets) appears inside several illustrations (mugs, laptops, `SIRH.png`, `Forum.png`), and a wordmark appears in `Forum.png`. These are parts of artwork, not logo assets.
- Rule: leave a clearly marked placeholder where a logo is needed rather than drawing one.

## Illustration style

- **OBSERVED only:** see [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) (traits) and [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) (what each file shows). Two sub-styles exist: energy/technology (SVG, objects only, orange ring) and people/workplace (PNG, characters). Do not mix them unless a reference does.
- **TO BE PROVIDED:** official do/don't rules, permitted character and pose guidelines, rules for text in illustrations, backgrounds and cropping, and whether new illustrations may be created by AI at all.

## Layout and spacing

- **OFFICIAL source:** [`../spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json), a Figma variables export with `rem`, `em` and `spacer` scales (e.g. `spacer.spacers.1` to `6`, resolving to 4, 8, 12, 16, 24, 48 as numbers; units not stated). Use token names.
- **TO BE PROVIDED:** grid, margins and safe areas, formats and sizes for posters, slides and social media, hierarchy and composition rules, and how illustrations are placed relative to text.

## Approved visual examples

None yet. See [`../brand-examples/README.md`](../brand-examples/README.md). Until approved examples exist, there is no reference for what a compliant poster or screen looks like.

## Visual restrictions

- Process restrictions are the mandatory rules above.
- **TO BE PROVIDED:** explicit visual do-not rules (forbidden colors, effects, imagery, tone, representation of people, third-party logos in visuals, use of stock or photographic imagery). The existing illustrations include third-party tool logos and flags; whether that is allowed is not documented.

## Missing information register

| Area | Missing | Source to supply |
|---|---|---|
| Colors | Brand vs data-viz families, roles, contrast pairs, dark mode, gradients | Figma Design System |
| Typography | Confirmed body font, font files/licenses/fallbacks, print/poster scale | Figma Design System, brand team |
| Logo | Files, variants, clear space, minimum size, forbidden uses | Brand team |
| Illustration | Official rules, AI-creation policy, text-in-illustration rules | Design team |
| Layout | Grids, formats, poster/slide templates, placement rules | Figma Design System |
| Examples | Approved posters, UI screens, illustrations | Design team |
| Restrictions | Explicit visual do-not list | Brand team |
