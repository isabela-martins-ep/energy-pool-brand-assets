---
name: energy-pool-visual-design
description: Create Energy Pool visuals consistent with the existing visual identity and Design System - posters (event, internal communication, HR), illustrations, infographics, presentations and user interfaces - or adapt an existing illustration. Use when asked to create or update an Energy Pool poster, illustration, visual asset or UI, or to design with Energy Pool's brand, tokens and illustration style.
---

# Energy Pool visual design

Entry point for creating or modifying Energy Pool brand visuals (posters, illustrations, HR visuals, infographics, slides). The Figma exports and [`guidelines/BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md) hold the rules; this file only gives the order of actions and where to read. Goal: original, brand-coherent proposals made autonomously, without the user guiding each aesthetic choice. Web UI components are out of scope: use the coded Design System.

## Route the request

| Request | Procedure to follow |
|---|---|
| Poster, flyer, infographic, slide, social visual, HR visual | [`references/poster-workflow.md`](references/poster-workflow.md) |
| New illustration or adaptation of an existing one | [`references/illustration-creation.md`](references/illustration-creation.md) |

## Three levels of rules

Defined once in [`BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md#rule-levels): **A** mandatory (logo, fonts, token colors, user content, charter prohibitions), **B** visual coherence (illustration style in [`STYLE_GUIDE.md`](../../../illustrations/STYLE_GUIDE.md), guidance, not a template), **C** creative freedom (composition, layout, format, poses, scenery, hierarchy: decide without asking).

## Process (all requests)

1. **Understand** the request and the constraints supplied (text, format, audience, assets). Act on aesthetic choices; ask, in one message, only for missing essential information or when a choice might break a level A rule.
2. **Consult** the relevant rules and resources: `BRAND_RULES.md`, [`TOKENS.md`](../../../guidelines/TOKENS.md) and the token files it names, [`brand-examples/`](../../../brand-examples/README.md) (logos, approved examples), and for illustrations [`CATALOG.md`](../../../illustrations/CATALOG.md) and `STYLE_GUIDE.md`. Keep an internal source manifest (each file: read, viewed or inaccessible). A path or URL is not proof of consultation.
3. **Select references**: the closest approved example or catalogued illustrations (same sub-style), and open the actual images. Reuse an existing file when it fits.
4. **Define a graphic direction** coherent with Energy Pool: colors (confirmed brand tokens; you pick the roles), fonts, logo, illustration approach, layout idea. Keep it short. Consider two or three compositions and keep the strongest; deliver one file unless the user asks for options, and do not ask for validation between them.
5. **Create an original proposal** with the available tools. Never assume image generation, font embedding or Figma access. Work on copies; never alter originals, logos or token exports. When modifying an existing visual, change only what was requested.
6. **Verify the produced output**, not the prompt, with [`VISUAL_QA.md`](../../../guidelines/VISUAL_QA.md); mark non-applicable criteria `N/A`. Say what you could not inspect.
7. **Correct** blocking non-compliances and style gaps; re-verify.
8. **Deliver** the requested file, a few lines on the main design decisions, and limits or points needing human validation, labelled AI-generated / AI-assisted, draft pending approval. A draft is deliverable even when official validations are pending. A detailed report only if the user asks or a compliance problem requires it (`VISUAL_QA.md`).

Optional helper: [`scripts/resolve_token.py`](scripts/resolve_token.py) (read-only token lookup; not available in Microsoft 365 Copilot).

## Always

- Use exactly the text supplied by the user, or the text already present on a visual being redone: no added, removed, reworded or translated text ([`BRAND_RULES.md`](../../../guidelines/BRAND_RULES.md#mandatory-rules-level-a-and-honesty), rule 5).
- Do not invent brand colors, fonts, logo variants or official rules, and do not take official values from images.
- Do not present OBSERVED traits as official, or a result as compliant when a check was not performed. A difference from existing examples is not a non-compliance.
- Say you looked at an image only if its content was accessible.
