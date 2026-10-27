# Reusing this repository in Microsoft 365 Copilot

Microsoft 365 Copilot **cannot automatically read this GitHub repository and does not execute `SKILL.md`**. The content must be copied or uploaded manually into the agent you build. Which features, file types and size limits are available depends on your tenant and the tool (for example Copilot Studio or Agent Builder), so check them before starting.

## 1. Agent instructions

Paste the block below into the agent's instructions field. It is self-contained. If your tool limits instruction length, shorten it rather than dropping the rules.

```
You help Energy Pool team members create visuals consistent with the Energy Pool brand and Design System.

Rules:
- Use only the knowledge files you were given. Never invent brand colors, fonts, spacing values, logo variants or design rules.
- Official specifications come from the token files (colors, typography, spacing). BRAND_RULES.md separates OFFICIAL, OBSERVED and TO BE PROVIDED items. Observed traits of existing illustrations are not brand rules.
- If information is marked TO BE PROVIDED or is missing, say so and ask the user. Do not guess.
- Never redraw, recolor or generate the Energy Pool logo or pictogram. Use a supplied logo file or leave a marked placeholder.
- Reuse existing illustrations when one fits (see the illustration catalog). Distinguish the two illustration styles: energy/technology (objects, orange ring) and people/workplace (characters).
- You may not be able to see images or embed the brand fonts. Say which checks you could not perform.
- Before delivering, go through VISUAL_QA.md and report the result, including items that could not be verified.
- Label every AI-generated or AI-assisted visual as such, and state it is a draft requiring human review and approval before publication.
```

## 2. Knowledge files

Upload these files from the repository. Keep them as Markdown or JSON if your tool accepts them; otherwise convert them (e.g. to text or Word), keeping the content unchanged.

| File | Purpose |
|---|---|
| [`BRAND_RULES.md`](BRAND_RULES.md) | Mandatory rules, official vs observed vs missing |
| [`VISUAL_QA.md`](VISUAL_QA.md) | Pre-delivery checklist |
| [`../illustrations/CATALOG.md`](../illustrations/CATALOG.md) | What each illustration shows |
| [`../illustrations/STYLE_GUIDE.md`](../illustrations/STYLE_GUIDE.md) | Observed illustration traits |
| [`../colors/Default.tokens.json`](../colors/Default.tokens.json) | Color tokens (large, about 300 KB; may exceed upload limits, in which case split or summarize it without changing values) |
| [`../typography/Mode 1.tokens.json`](../typography/Mode%201.tokens.json) | Typography tokens |
| [`../spacing/Mode 1.tokens 2.json`](../spacing/Mode%201.tokens%202.json) | Spacing tokens |
| [`../brand-examples/README.md`](../brand-examples/README.md) | Register of approved examples (empty for now) |

Illustration images in [`../illustrations/`](../illustrations/) can be added if your tool accepts images, but the agent may not be able to interpret them; the catalog text is the reliable description.

## 3. Limits to expect

- Microsoft 365 Copilot may not be able to apply the Chillax or Synonym fonts, and image generation may not follow the illustration style reliably. Treat outputs as drafts and run `VISUAL_QA.md`.
- Keep the uploaded files in sync with this repository when it changes; there is no automatic synchronization.
