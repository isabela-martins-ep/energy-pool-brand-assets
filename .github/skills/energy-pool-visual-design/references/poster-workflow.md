# Poster workflow (events, internal communication, HR)

Applies to posters and similar single-page supports (flyers, infographics, slides, social visuals). Rules here complete [`guidelines/BRAND_RULES.md`](../../../../guidelines/BRAND_RULES.md); they never override it. If a step needs information marked `TO BE PROVIDED`, report it and ask.

## Phase A - Prepare

### Step 1 - Analyse the request
Collect: format and size (no official poster format is documented: ask), audience, goal, exact text (do not rewrite or invent copy; keep the user's accents and language), mandatory information (date, place, contact, call to action), supplied assets (official logo, photos, existing poster) and the output the tool can produce. Missing items: ask in one batch.

### Step 2 - Create a source manifest
Before generation or editing, write a short creation dossier containing:

- support type, dimensions and intended audience;
- exact text to preserve and mandatory fields;
- source files required and whether each was actually readable or viewable;
- selected token names and resolved HEX values;
- planned typography, including the font that can actually be embedded;
- selected illustration(s) and why they fit;
- official logo file and provenance, or a marked missing-logo placeholder;
- method of production (existing-resource composition or image generation);
- points requiring human validation.

An URL, a path, or a reference name is not proof that the file was consulted. If a required file cannot be read or viewed, record it as inaccessible and do not claim to have used it.

### Step 3 - Consult the sources
Read `BRAND_RULES.md`, [`guidelines/TOKENS.md`](../../../../guidelines/TOKENS.md), the token files you need, `brand-examples/` (state if empty), then `illustrations/CATALOG.md`, `STYLE_GUIDE.md` and the closest illustration files. Say which were read, which were viewed, and which were inaccessible.

### Step 4 - Choose the production method

**Method 1 — Composition from existing resources (preferred).** Use this for exact text, official logos, precise colors, and high-fidelity brand communication. Compose supplied assets in a design tool or an editable layout; do not redraw missing assets.

**Method 2 — Image generation.** Use for exploration, concepts and new illustration ideas when exact typography, logo integrity or token-level color control is not guaranteed. Image generation alone is never evidence of Design System compliance.

### Step 5 - Prepare the design direction
- **Colors:** list each role -> token -> resolved HEX. Roles for posters are `TO BE PROVIDED`: propose, but flag as requiring validation; never use state colors decoratively.
- **Typography:** hierarchy (title, subtitle, body, details) with the documented families and weights; note the Synonym/Noto Sans conflict and whether fonts can actually be embedded.
- **Composition:** hierarchy and placement, text over clear areas only; no official grid exists, so label it a proposal.
- **Illustration:** reuse a catalogued file when possible (for people scenes, the people/workplace PNGs); otherwise follow `references/illustration-creation.md`.
- **Logo:** official file if supplied, otherwise a marked placeholder. Never recreate the logo, wordmark or pictogram.

## Phase B - Produce

Build the composition from the direction above without changing brand values. Use only the listed tokens, fonts, assets. Do not modify files in `illustrations/`; work on copies. Label the output AI-generated or AI-assisted.

For an existing poster, preserve the original content, structure, logo and official resources unless the user explicitly requested a specific change. Do not reconstitute a logo, text or illustration from memory.

## Phase C - Verify

Run [`guidelines/VISUAL_QA.md`](../../../../guidelines/VISUAL_QA.md) against the produced output, not merely the prompt. Inspect the actual output if the environment supports it; otherwise mark visual checks `Not verifiable`.

## Phase D - Present

Give the creation dossier, the result, the label and draft status, the standardized QA table, tokens and files used, technical limits (fonts, image generation, logo) and the decisions awaiting human validation. Never call the result compliant if a check was not performed. A blocking failure means the result is not ready to publish.
