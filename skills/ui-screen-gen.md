# Skill: UI Screen Generator

## Purpose
Turn a product brief or feature description into structured UI screen designs — wireframes to high-fidelity — delivered as Figma files (via Figma MCP) and/or coded prototypes (HTML/React).

## When to Use
- Client needs app or web screens designed
- A feature description needs to become a clickable flow
- Redesign of an existing product screen
- Landing page design for a product

## Process: Always Flow Before Screens

Never design a screen in isolation. The order is fixed:

1. **User goal** — one sentence: who is on this screen and what are they trying to do
2. **Flow map** — list the screens in the journey and what moves the user between them
3. **Screen inventory** — for each screen: purpose, key action (the ONE thing), content blocks
4. **Wireframe** — structure without style
5. **High fidelity** — apply the design system / brand tokens
6. **States** — empty, loading, error, success for every screen with dynamic content
7. **Prototype** — connect screens into a clickable flow

Skipping to step 5 produces pretty screens that don't work. Do not skip.

## Screen Anatomy Rules
- **One primary action per screen.** It gets the filled button. Everything else is secondary/ghost.
- **Content hierarchy = user priority**, not org chart. The thing users came for goes first, not the thing the company wants to show.
- **Tap targets ≥ 44×44pt** (mobile) / click targets ≥ 32px (desktop).
- **Text contrast:** 4.5:1 body, 3:1 large text/icons — check every pairing.
- **Thumb zone:** on mobile, primary actions live in the bottom half of the screen.
- **8pt spacing grid.** All spacing values are multiples of 8 (4 permitted for tight icon gaps).
- **Form rules:** one column, labels above fields, inline validation, error text tells the user how to fix it.

## Standard Breakpoints
| Name | Width | Design canvas |
|---|---|---|
| Mobile | 320–767 | Design at 375×812 |
| Tablet | 768–1023 | Design at 768×1024 |
| Desktop | 1024+ | Design at 1440×900 |

Design mobile first. Desktop is an expansion, not the source.

## Component Checklist (per project)
Before screens, establish these in the design system:
- Buttons: primary / secondary / ghost / destructive × default / hover / pressed / disabled
- Inputs: text field, select, checkbox, radio, toggle × default / focus / error / disabled
- Cards, nav bar / tab bar, modal / sheet, toast / snackbar
- Typography styles and color styles mapped from brand tokens

## States Are Not Optional
Every screen with dynamic content ships with 4 states:
| State | Must include |
|---|---|
| Empty | Explanation + the action that fills it (never just "No items") |
| Loading | Skeleton preferred over spinner for content areas |
| Error | What went wrong + how to recover |
| Success/Populated | The design everyone focuses on — realistic data, not lorem ipsum |

Use realistic content: real-length names, real prices, real dates. Lorem ipsum hides layout bugs.

## Output Targets

### Figma (primary — via Figma MCP)
- Load `/figma-generate-design` skill before writing into Figma
- One page per flow; frames named `[flow]/[screen]/[state]`
- Components from the established library, not detached copies

### Code prototype (when client wants clickable/real)
- Single-file HTML/CSS/JS for landing pages and simple flows
- React + Tailwind for product UI (matches v0/Locofy handoff conventions)
- Real breakpoints, real hover/focus states, `prefers-reduced-motion` respected

## Execution Steps
1. Run brief through Campaign Brief Parser if not already structured
2. Write the flow map and screen inventory — this is a deliverable, save it: `output/ui/[client]/flow-map.md`
3. Establish/verify the component set and tokens
4. Wireframe all screens (fast, grayscale)
5. Client checkpoint on wireframes if the flow is non-trivial (>4 screens)
6. High fidelity + all 4 states per dynamic screen
7. Prototype connections
8. Export screens PNG @2x for the presentation; keep Figma as source of truth
9. Hand off via Client Presentation Generator + Asset Delivery Packager

## Quality Checks
- [ ] Every screen has exactly one primary action
- [ ] All 4 states designed for dynamic screens
- [ ] Contrast checked on every text/background pairing
- [ ] Spacing on the 8pt grid
- [ ] Realistic content throughout, zero lorem ipsum
- [ ] Mobile designed first; desktop is derived
- [ ] Flow map saved as a deliverable
