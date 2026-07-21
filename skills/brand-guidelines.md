# Skill: Brand Guidelines Generator

## Purpose
Take a client's brand inputs (or create them from scratch) and produce a complete, professional brand guidelines document — the deliverable every branding project ends with, and the reference every future deliverable depends on.

## When to Use
- A brand identity project is reaching final delivery
- A client has scattered brand assets but no formal guidelines
- Before starting social/campaign work for a client with no documented brand
- A client asks for "brand book", "style guide", or "brand manual"

## Inputs Accepted
- Existing logo files (SVG/PNG) and any color/font choices already made
- The output of the Campaign Brief Parser skill (brand direction section)
- Competitor references and mood boards
- Nothing at all — the skill can propose a full identity from a brief

## Output: Brand Guidelines Document Structure

Produce a Markdown master (converted to PDF for delivery) with these sections:

```
1. Brand Overview
   - Mission statement (1 sentence)
   - Brand personality (3 adjectives with one line each explaining how they show up visually)
   - Tone of voice (how the brand writes and speaks)

2. Logo
   - Primary logo + construction/clearspace rules (minimum clearspace = height of one logomark unit)
   - Variations: horizontal, stacked, icon-only, monochrome
   - Minimum sizes (print: 20mm wide; digital: 120px wide)
   - Incorrect usage: 4 explicit don'ts with visual examples

3. Color System
   - Primary palette: 1-2 colors with HEX, RGB, CMYK, Pantone
   - Secondary palette: 2-3 supporting colors
   - Neutrals: background and text colors
   - Usage ratios (e.g. 60% neutral / 30% primary / 10% accent)
   - Accessibility: every text/background pairing must pass WCAG AA (4.5:1 body, 3:1 large text) — state the contrast ratio next to each approved pairing

4. Typography
   - Display typeface: name, weights used, where to get it (Google Fonts link if free)
   - Body typeface: same details
   - Type scale: H1 → caption with exact sizes and weights for digital and print
   - Fallback stack for email/web

5. Imagery & Iconography
   - Photography style: 3 rules (e.g. natural light, real people, candid not posed)
   - Illustration/icon style if applicable
   - Do/don't image examples

6. Applications
   - How the brand appears on: social profile, business card, email signature, website header
   - At least 3 mockups showing the system working together

7. Design Tokens (for dev handoff)
   - JSON block with color, spacing, radius, and type tokens
```

## Design Tokens Format
Always include this machine-readable block so developers and future automation can consume the brand directly:

```json
{
  "color": {
    "primary":   { "value": "#______" },
    "secondary": { "value": "#______" },
    "background":{ "value": "#______" },
    "text":      { "value": "#______" },
    "accent":    { "value": "#______" }
  },
  "font": {
    "display": { "family": "______", "weights": [700, 800] },
    "body":    { "family": "______", "weights": [400, 500] }
  },
  "radius": { "sm": "6px", "md": "10px", "lg": "16px" },
  "spacing": { "unit": "8px" }
}
```

## Rules for Proposing New Identities
When creating from scratch (no existing assets):
1. Always propose the color palette WITH reasoning tied to the client's audience and industry — never "blue because it's trustworthy" alone; connect to the specific positioning.
2. Never default to: purple gradients, Inter/Roboto as display type, generic geometric sans + teal combos. Choose type with a point of view.
3. Check color accessibility before presenting — reject any body-text pairing under 4.5:1.
4. Present 2 directions maximum. More options create decision paralysis; two forces a real choice.
5. Every direction needs a one-line concept statement (e.g. "Direction A: engineered warmth — precision layouts with a humanist type voice").

## Execution Steps
1. Gather all existing brand inputs; list what exists and what's missing
2. Fill gaps: propose missing elements following the rules above
3. Build the document section by section using the structure
4. Generate the design tokens JSON from the final choices
5. Export: Markdown master → `output/brand/[client-slug]-guidelines-v[n].md`, PDF for client delivery
6. If Figma access exists: create a styles library (color styles + text styles) in the client's Figma file

## Quality Checks
- [ ] Every color has HEX + RGB + CMYK
- [ ] Every text/background pairing lists its contrast ratio and passes AA
- [ ] Logo don'ts section has at least 4 concrete examples
- [ ] Type scale covers digital AND print sizes
- [ ] Design tokens JSON is valid and matches the document
- [ ] At least 3 application mockups included
