---
name: energy-pool-visual-design
description: Create Energy Pool visuals consistent with the existing visual identity and Design System - posters (event, internal communication, HR), illustrations, infographics, presentations and user interfaces - or adapt an existing illustration. Use when asked to create or update an Energy Pool poster, illustration, visual asset or UI, or to design with Energy Pool's brand, tokens and illustration style.
---

# Energy Pool visual design

Entry point for creating or modifying Energy Pool brand visuals (posters, illustrations, HR visuals, infographics, slides). The Figma exports and [`guidelines/BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md) hold the rules; this file only gives the order of actions and where to read. Web UI components are out of scope: use the coded Design System.

## Route the request

| Request | Procedure to follow |
|---|---|
| Poster, flyer, infographic, slide, social visual, HR visual | [`references/poster-workflow.md`](references/poster-workflow.md) |
| New illustration or adaptation of an existing one (7-step process; style rules in `illustrations/STYLE_GUIDE.md`) | [`references/illustration-creation.md`](references/illustration-creation.md) |

## Process (all requests)

1. **Consult.** Read, in this session: `BRAND_RULES.md` (rules, source priority, official vs observed vs `TO BE PROVIDED`), [`TOKENS.md`](../../../guidelines/TOKENS.md) (method) and the token files it names, [`brand-examples/`](../../../brand-examples/README.md) (logo files, approved examples), and for illustrations [`CATALOG.md`](../../../illustrations/CATALOG.md) and [`STYLE_GUIDE.md`](../../../illustrations/STYLE_GUIDE.md). Write a source manifest: each file, and whether it was read, viewed or inaccessible. A path or URL is not proof of consultation.
2. **Select.** Colors, fonts and spacing: tokens per `TOKENS.md`. Logo: the official files only (`BRAND_RULES.md` Logo). Illustration: an existing catalogued file first, else a new AI-created one under the official decisions in `illustrations/STYLE_GUIDE.md` §0 (non-token colors, gradients, reuse, proportions). If a required source is inaccessible or a rule is `TO BE PROVIDED`, report it and ask; do not fill the gap.
3. **Create or modify** with the tools available. Prefer composing existing resources over generating images. Never assume image generation, font embedding or Figma access. Work on copies; never alter originals, logo files or token exports. When modifying an existing visual, change only what was requested.
4. **Verify the produced output** (not the prompt) with [`VISUAL_QA.md`](../../../guidelines/VISUAL_QA.md). Fix failures. Say what you could not inspect.
5. **Deliver** with the QA report, the manifest, tokens and files used, limits, decisions awaiting human validation, the AI label and the overall status defined in `VISUAL_QA.md`.

Optional helper: [`scripts/resolve_token.py`](scripts/resolve_token.py) (read-only token lookup; not available in Microsoft 365 Copilot).

## Always

- Do not invent brand colors, fonts, spacing, logo variants or rules, and do not take official values from images.
- Do not present OBSERVED traits as official, or a result as compliant when a check was not performed.
- Say you looked at an image only if its content was accessible.
- Label every AI-generated or AI-assisted visual and treat it as a draft until a human approves it.
