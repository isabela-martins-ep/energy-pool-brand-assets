# Visual QA checklist for AI-generated assets

Run before delivering any generated or adapted visual. Definitions (OFFICIAL / OBSERVED / `TO BE PROVIDED`) are in [`BRAND_RULES.md`](BRAND_RULES.md); token method in [`TOKENS.md`](TOKENS.md).

**Statuses:** `Compliant`, `Non-compliant`, `Not verifiable` (say why). `Not verifiable` is never treated as compliant. If a rule is `TO BE PROVIDED`, the item is `Not verifiable`.

**Automatable:** Yes = a script or file read can check it; Partly = tool-assisted, then confirm; No = human only. Every visual still needs human approval before publication.

| # | Criterion | What to check | Source | Automatable | Human validation |
|---|---|---|---|---|---|
| 1 | Sources read | Listed files were actually read in this session; unreadable ones named | `BRAND_RULES.md`, token files, catalog | Yes (self-report) | Reviewer confirms the list |
| 2 | Color tokens | Each color maps to a token and its exact HEX (`resolve_token.py` or JSON); none estimated from images | `colors/*.json`, `TOKENS.md` | Yes (source file/HTML/SVG); Partly (raster) | Role of each color for this medium (`TO BE PROVIDED`) |
| 3 | Color usage | No state colors (success, danger, warning, info, link) or component tokens used decoratively; `energy-assets` only for their source | `TOKENS.md` | Partly | Yes |
| 4 | Contrast / legibility | Text/background contrast measured and stated; required level is `TO BE PROVIDED` | Output file | Partly (ratio from HEX) | Yes (print/projection legibility) |
| 5 | Fonts | Declared families are the documented ones; embedded or substituted is stated; Synonym/Noto Sans conflict flagged | `typography/Mode 1.tokens.json` | Partly (inspect file fonts) | Yes (rendering) |
| 6 | Type scale and weights | Sizes and weights from tokens; hierarchy clear | typography tokens | Partly | Yes (poster scale `TO BE PROVIDED`) |
| 7 | Text content | Text equals the user's text; spelling, accents and language right; nothing added or rewritten | User request | Yes (string comparison on source) | Yes (proofreading) |
| 8 | Logo | Official file used, or marked placeholder; nothing redrawn, recolored, stretched or generated; clear space and minimum size `TO BE PROVIDED` | `BRAND_RULES.md` Logo | Partly | Yes |
| 9 | Illustration reuse | Catalog checked first; existing file reused when suitable; originals untouched (`git status`) | `CATALOG.md` | Yes (git status, file hash) | Suitability of usage |
| 10 | Illustration style | One sub-style; compared with closest references and "Detail observations"; deviations listed; observed traits not presented as official | `STYLE_GUIDE.md` | No (needs image viewing) | Yes |
| 11 | Illustration content | No third-party logos, flags, new recurring characters or text added without confirmation | `STYLE_GUIDE.md` | Partly | Yes |
| 12 | Layout and spacing | Spacings use spacing tokens; format/grid follow an approved example, else flagged | `spacing/*.json`, `brand-examples/` | Partly | Yes (no grid is documented) |
| 13 | Composition | One focal element; text not over busy areas; nothing cropped or overlapping | Output | No | Yes |
| 14 | Governance | Labelled AI-generated or AI-assisted; stated as draft pending human approval | `BRAND_RULES.md` | Yes | Approver signs off |
| 15 | Honesty about checks | Only performed checks reported; output inspected or marked not verifiable; if no image tool, a brief was delivered instead | This list | Yes (self-report) | Reviewer |

## Report template

```
Overall: Compliant / Non-compliant / Not verifiable (partial)
Per item: <#> <status> <evidence or reason>
Tokens used: <role -> token -> HEX>
Sources read / not read: <files>
TO BE PROVIDED hit: <list>
Awaiting human validation: <decisions>
Label: AI-generated / AI-assisted. Draft pending human approval.
```

The overall status can be `Compliant` only if every item is `Compliant` or `N/A`.
