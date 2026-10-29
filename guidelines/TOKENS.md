# Design tokens: how to use them

The **only OFFICIAL sources for color, typography and spacing values** are the 8-color palette [`colors/COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md) and the Figma exports in this repository. This file explains what each source contains and the method for picking and resolving a token. It does not copy values: read them from the files, or run the resolver (below).

## 1. Token tiers

| Tier | What it is | Where it is in this repository |
|---|---|---|
| **Primitive** | Raw values with no meaning attached (`rem`/`em` scales, font families) | [`spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json) `rem`, `em`; [`typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json) `font-variables` |
| **Semantic** | Values named for a role (`spacer`, heading/text roles, per-energy-source assets) | Colors: [`colors/COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md) (the 8-color graphic palette: plain color names, freely combinable) and [`colors/energy-assets.json`](../colors/energy-assets.json) (per energy source). Also `spacer` (spacing) and role tokens such as `heading`, `display`, `text-muted` (typography). Variants such as `body*`, `*-bg-subtle` or `*-text-emphasis` are not exported; they appear only as alias names (see §4) |
| **Component** | States, borders, focus, shadows, transitions for UI components | [`colors/Mode 1.tokens 3.json`](../colors/Mode%201.tokens%203.json): `state`, `state new`, `border`, `focus-ring`, `shadow`, `caret`, `transition`, `aspect-ratio` |

The file `colors/Mode 1.tokens 3.json` holds component tokens even though it sits in `colors/`. Do not rename it (original export).

## 2. Method to choose a token

1. **Name the role first** (e.g. "poster background", "heading text", "highlight box"), not a color.
2. **Look for a semantic token for that role.** If one is exported, use it. Prefer semantic over primitive.
3. **Colors:** choose and combine freely the 8 colors and the charter colors of [`COLOR_PALETTE.md`](../colors/COLOR_PALETTE.md) (backgrounds, sections, boxes, graphic elements), with their exact HEX, and derived variations reported as such; orange stays the main identity color. Gradients: only those in `COLOR_PALETTE.md`. They are not status colors. Colors outside the palette only in the cases listed there. Never describe your choice of where each color goes as an official rule. Ask only if the choice might break a level A rule.
4. **Component tokens are for UI components only.** Do not use `state`, `border` or `focus-ring` colors for decoration.
5. **`energy-assets` colors** ([`colors/energy-assets.json`](../colors/energy-assets.json)) are for the energy source or sector they name (chart, icon, background). Use them only for content about that source, for example in an infographic; do not use them as general brand colors.
6. **Typography and spacing:** take families, weights, sizes and spacers from the typography and spacing exports; the typography rules and the "units not stated" caveat in `BRAND_RULES.md` still apply.
7. **Record each choice** as `color or token name -> HEX` in the answer.

## 3. Resolving references

References look like `{border.border-default}` and follow the dotted path in the exports. Each color token also carries its resolved `hex`; use that exact value (do not round, convert or approximate it). Alias names starting with `palette/` point to a Figma palette that is not stored here; the `hex` next to them is the value.

Resolver (read-only, Python 3, no dependencies):

```
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py "state new.invalid-color"
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py --search solar
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py --audit
```

If you cannot run scripts, read the JSON directly. If a reference cannot be resolved, or only a Figma alias name is available, **report it as unresolved**; do not guess the value.

## 4. Known gaps (from the audit)

- All `{...}` references in the exports resolve (0 unresolved by `--audit`).
- Component and typography tokens alias **Figma variables that are not in any export**, for example `primary/primary-text-emphasis`, `secondary/secondary-bg-moderate`, `success/success-bg-subtle`, `body/*`, `spacer/spacer`, `transparent`. Only their resolved values are known; they are not extra brand colors, and these technical alias names are unrelated to the palette names.
- Units of typography and spacing numbers are not stated in the exports.
- `shadow` values reference `$black` (a SCSS variable), not a resolvable token.
- `colors/Mode 1.tokens 3.json` token `state new` duplicates part of `state` with different values (for example `secondary` hover). Which set is current is **TO BE PROVIDED**.
- Mode: only "Mode 1" exports exist; dark mode is not covered.
