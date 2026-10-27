# energy-pool-brand-assets

Centralized library of graphic resources for **all Energy Pool employees** creating visual materials: illustrations, posters, flyers, presentations, internal communications, HR visuals and more. It also serves as a reference for AI tools (such as GitHub Copilot) so that what they generate stays consistent with our brand identity.

## Purpose

This repository gathers brand assets, guidelines and design references that give AI tools the context they need. It is **not** a recreation of the Design System.

## Relationship with the Design System

Energy Pool's Design System lives in **Figma** and is implemented in **code**. Those remain the source of truth. This repository documents and points to them (tokens, components, guidelines) and stores exported visual references. Link to the source rather than duplicating it.

## Structure

| Folder | Content |
|---|---|
| `colors/` | Official brand colors and references to color tokens |
| `typography/` | Font families, weights, hierarchy |
| `spacing/` | Spacing and layout guidelines (Design System values) |
| `illustrations/` | Illustrations exported from Figma, plus style guide template |
| `ui-references/` | Examples of existing interfaces, layouts and components |
| `guidelines/` | Brand rules, visual QA checklist, Microsoft 365 Copilot reuse guide |
| `brand-examples/` | Official logo files; approved visual references (none supplied yet) |
| `.github/` | Instructions for GitHub Copilot |

## Contributing

**Designers**
- Export assets from Figma (SVG preferred, PNG for screenshots) into the matching folder.
- Name files in lowercase kebab-case (e.g. `dashboard-overview.png`).
- Describe each asset with the templates (`illustrations/STYLE_GUIDE.md`, `ui-references/TEMPLATE.md`) and link the Figma frame.

**Developers**
- Reference tokens and components by name, with a link to the code or Figma source.
- Never copy Design System code here.

Open a pull request for any change, focused on one topic.

## Visual design skill

[`.github/skills/energy-pool-visual-design/SKILL.md`](.github/skills/energy-pool-visual-design/SKILL.md) is an Agent Skill that guides AI agents when creating or adapting Energy Pool illustrations and UIs: it defines a workflow (classify, consult references, reuse assets, follow the Design System, verify, report limitations) and the constraints to respect.

- **Use:** compatible agents can discover it from `.github/skills/` when a request matches its description (e.g. "create an Energy Pool illustration"), or you can point the agent to the file.
- **Dependencies:** it relies on the resources in this repository (`illustrations/CATALOG.md`, `illustrations/STYLE_GUIDE.md`, `.github/copilot-instructions.md`, etc.) and does not duplicate them.
- **Structure:** `SKILL.md` routes requests to [`references/poster-workflow.md`](.github/skills/energy-pool-visual-design/references/poster-workflow.md) and [`references/illustration-creation.md`](.github/skills/energy-pool-visual-design/references/illustration-creation.md); [`guidelines/TOKENS.md`](guidelines/TOKENS.md) explains token tiers, and an optional read-only script ([`scripts/resolve_token.py`](.github/skills/energy-pool-visual-design/scripts/resolve_token.py)) resolves token references.
- **Verification:** before delivering a visual, agents run [`guidelines/VISUAL_QA.md`](guidelines/VISUAL_QA.md); missing official information is marked `TO BE PROVIDED` in [`guidelines/BRAND_RULES.md`](guidelines/BRAND_RULES.md).
- **Microsoft 365 Copilot:** it cannot read this repository or run `SKILL.md` automatically; see [`guidelines/M365_COPILOT.md`](guidelines/M365_COPILOT.md) to copy instructions and upload knowledge files manually.
- **Availability:** discovery, installation and image-generation capabilities depend on the AI tool used.

## How Copilot uses these resources

Copilot follows [`.github/copilot-instructions.md`](.github/copilot-instructions.md): it prioritizes the Design System, reads the references in this repository, never invents colors, typography, spacing or styles, and asks for clarification when information is missing.
