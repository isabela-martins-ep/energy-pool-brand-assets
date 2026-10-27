# Visual QA checklist for AI-generated assets

Run this before delivering any generated or adapted visual. Rules and statuses (OFFICIAL / OBSERVED / TO BE PROVIDED) are defined in [`BRAND_RULES.md`](BRAND_RULES.md).

Mark each item **Pass**, **Fail**, **Not verifiable** (say why, e.g. no image access or font not embedded) or **N/A**. "Not verifiable" is never a Pass.

## 1. Sources
- [ ] The relevant source files were actually read: [`BRAND_RULES.md`](BRAND_RULES.md), the token files in [`../colors/`](../colors/), [`../typography/`](../typography/) and [`../spacing/`](../spacing/), and for illustrations [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) and [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md).
- [ ] Reference files and tokens used are listed in the answer.
- [ ] Missing information was reported as `TO BE PROVIDED`, not filled in.

## 2. Colors
- [ ] Every color maps to a token in `colors/Default.tokens.json` (name + HEX noted), or is flagged as not matching a token.
- [ ] No invented or eyeballed colors, and none taken from screenshots of illustrations.
- [ ] Text/background contrast is legible; required contrast level is `TO BE PROVIDED`, so state what was checked.

## 3. Typography
- [ ] Fonts are the documented ones (headings/display `Chillax`, body `Synonym` per the export, pending the open question in `BRAND_RULES.md`), or the fallback is declared.
- [ ] Weights and sizes come from the typography tokens; no extra typefaces.
- [ ] Text content is correct (spelling, accents, language of the request) and no text was added to an illustration without asking.

## 4. Logo
- [ ] The logo and pictogram were not redrawn, recolored, distorted or AI-generated; a supplied file or a marked placeholder is used.
- [ ] Clear space, minimum size and background rules: `TO BE PROVIDED`, flagged.

## 5. Illustrations
- [ ] An existing illustration was reused or adapted when one fits (catalog checked first); originals in `illustrations/` are untouched.
- [ ] One sub-style is used consistently (energy/technology or people/workplace), matching the closest reference files.
- [ ] Compared with the observed traits in `STYLE_GUIDE.md`; deviations listed. Observed traits are not presented as official rules.
- [ ] No third-party logos, flags or new characters unless a reference does the same and this is flagged for review.

## 6. Layout and spacing
- [ ] Spacing uses tokens from `spacing/`.
- [ ] Format, grid and margins follow an approved example in [`../brand-examples/`](../brand-examples/) if one exists; otherwise flagged `TO BE PROVIDED`.
- [ ] Hierarchy is clear: one focal element, text not over busy areas.

## 7. Governance
- [ ] Output is labelled AI-generated or AI-assisted.
- [ ] Marked as a draft pending human review and approval before publication.

## 8. Verification honesty
- [ ] Only checks that were actually performed are reported. If the generated image could not be inspected, say so.
- [ ] If no image-generation tool was available, say so and deliver a brief or prompt instead of pretending.

## Report template

```
Result: Pass / Pass with open points / Fail
Sources used: <files and tokens>
Failed or not verifiable: <item, reason>
TO BE PROVIDED items hit: <list>
Label: AI-generated / AI-assisted. Draft pending human approval.
```
