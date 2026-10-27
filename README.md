# energy-pool-brand-assets

Centralized visual reference library for Energy Pool, helping team members use GitHub Copilot to generate interfaces, prototypes and illustrations consistent with our brand identity.

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
| `guidelines/` | Visual principles, brand consistency rules, usage recommendations |
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

## How Copilot uses these resources

Copilot follows [`.github/copilot-instructions.md`](.github/copilot-instructions.md): it prioritizes the Design System, reads the references in this repository, never invents colors, typography, spacing or styles, and asks for clarification when information is missing.
