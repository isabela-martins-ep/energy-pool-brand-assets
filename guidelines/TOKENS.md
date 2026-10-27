# Design tokens: how to use them

The Figma exports in this repository are the **only OFFICIAL source for color, typography and spacing values**. This file explains what each export contains and the method for picking and resolving a token. It does not copy values: read them from the files, or run the resolver (below).

## 1. Token tiers

| Tier | What it is | Where it is in this repository |
|---|---|---|
| **Primitive** | Raw values with no meaning attached (palette families, `rem`/`em` scales, font families) | [`colors/Default.tokens.json`](../colors/Default.tokens.json) `palette`; [`spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json) `rem`, `em`; [`typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json) `font-variables` |
| **Semantic** | Values named for a role (`body`, `primary`, `secondary`, `success`, `danger`, `spacer`, heading/text roles, per-energy-source assets) | **Mostly not exported.** Present: `energy-assets` (colors), `spacer` (spacing), role tokens such as `heading`, `display`, `text-muted` (typography). The color roles `primary`, `secondary`, `body*`, `success`, `danger` exist in Figma only; they appear here solely as alias names (see §4) |
| **Component** | States, borders, focus, shadows, transitions for UI components | [`colors/Mode 1.tokens 3.json`](../colors/Mode%201.tokens%203.json): `state`, `state new`, `border`, `focus-ring`, `shadow`, `caret`, `transition`, `aspect-ratio` |

The file `colors/Mode 1.tokens 3.json` holds component tokens even though it sits in `colors/`. Do not rename it (original export).

## 2. Method to choose a token

1. **Name the role first** (e.g. "poster background", "heading text", "valid-state message"), not a color.
2. **Look for a semantic token for that role.** If one is exported, use it. Prefer semantic over primitive.
3. **If no semantic token is exported**, use a primitive token only when the role is documented in `BRAND_RULES.md` or in an approved example. Otherwise the role-to-color mapping is `TO BE PROVIDED`: say so and ask. Existing in the palette is not permission to use it for a poster.
4. **Component tokens are for UI components only.** Do not use `state`, `border` or `focus-ring` colors for decoration.
5. **State colors are not decoration.** Never use success/valid (`#3EBE90` family), danger/invalid, warning, info or link colors as decorative or brand colors in posters, illustrations or infographics. Use them only for the state they mean (validation, alerts), as the component tokens do.
6. **`energy-assets` colors** are for the energy source or sector they name (chart, icon, background). Use them only for content about that source, for example in an infographic; do not use them as general brand colors.
7. **Typography and spacing:** take families, weights, sizes and spacers from the typography and spacing exports; the "Units not stated" and font questions in `BRAND_RULES.md` still apply.
8. **Record each choice** as `token name -> resolved HEX` in the answer.

## 3. Resolving references

References look like `{palette.chili-oil.tints.800}` and follow the dotted path in the exports. Each color token also carries its resolved `hex`; use that exact value (do not round, convert or approximate it).

Resolver (read-only, Python 3, no dependencies):

```
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py "state new.invalid-color"
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py --search orange
python3 .github/skills/energy-pool-visual-design/scripts/resolve_token.py --audit
```

If you cannot run scripts, read the JSON directly. If a reference cannot be resolved, or only a Figma alias name is available, **report it as unresolved**; do not guess the value.

## 4. Known gaps (from the audit)

- All `{...}` references in the three exports resolve (0 unresolved by `--audit`).
- Many tokens alias **Figma variables that are not in any export**: `primary/*`, `secondary/*`, `body/*`, `body-tertiary/*`, `body-disabled/*`, `success/*`, `danger/*`, `spacer/spacer`, `transparent`. Only their resolved values are known, not the semantic definitions or the full set (for example `warning`, `info`, `link`, `light`, `dark` appear only in `focus-ring`). **TO BE PROVIDED:** the semantic color export.
- No token states which palette colors are brand colors for communication material (posters, slides, HR visuals). **TO BE PROVIDED.**
- Units of typography and spacing numbers are not stated in the exports.
- `shadow` values reference `$black` (a SCSS variable), not a resolvable token.
- `colors/Mode 1.tokens 3.json` token `state new` duplicates part of `state` with different values (for example `secondary` hover). Which set is current is **TO BE PROVIDED**.
- Mode: only "Default" / "Mode 1" exports exist; dark mode is not covered.
