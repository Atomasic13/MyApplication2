# Skill: Client Presentation Generator

## Purpose
Wrap completed design work into a professional client-facing presentation that sells the work, explains the decisions, and makes approval easy. Output as PDF, Figma slides, or Google Slides.

## When to Use
- Presenting a brand identity for approval
- Delivering a UI design at end of a sprint
- Pitching a campaign concept before production starts
- Sending a mid-project check-in with design rationale
- Closing a project with a case study summary

## Presentation Types

### Type 1: Concept Presentation (pre-approval)
For showing design direction before finalizing. Goal: get buy-in.
Tone: confident, explanatory, invites dialogue.

### Type 2: Delivery Presentation (final handoff)
For showing completed work alongside files. Goal: close the project.
Tone: professional, clear, shows impact.

### Type 3: Pitch Presentation (before project starts)
For winning the brief. Goal: show understanding + capability.
Tone: strategic, shows insight, creates excitement.

## Slide Structure

### Brand Identity Presentation (10–14 slides)
```
1. Cover — Client name, project name, date, your logo
2. Brief Summary — What we set out to solve (2-3 bullets)
3. Research Insight — What we found about their audience/competitors
4. Design Direction — The strategic choice (1 mood board or direction statement)
5. Logo — Primary logo on white + dark backgrounds
6. Logo Variations — Horizontal, stacked, icon-only
7. Color Palette — Primary, secondary, neutrals with hex codes and usage rules
8. Typography — Font pairings with hierarchy examples (H1 → body → caption)
9. Brand in Use — 3 mockups showing the brand applied (phone, billboard, etc.)
10. Do / Don't — 2 examples of correct usage, 2 examples of what to avoid
11. Next Steps — What comes after approval (e.g. social templates, website)
12. Thank You — Contact, timeline for feedback
```

### UI/App Design Presentation (8–12 slides)
```
1. Cover
2. Problem Statement — What user problem are we solving
3. Design Principles — 3 guiding principles for this product's UX
4. Key Screens Overview — Grid of all screens
5. Core Flow — Step-by-step walkthrough of the main user journey
6. Component Highlights — Design system elements worth calling out
7. Accessibility — Contrast ratios, tap targets, screen reader notes
8. Prototype Link — Clickable Figma prototype
9. Open Items — Anything still TBD or needing client input
10. Next Steps + Timeline
```

### Campaign Presentation (6–10 slides)
```
1. Cover
2. Campaign Concept — The big idea in one sentence
3. Visual Direction — Mood board or style tile
4. Deliverables Overview — What's included
5. Mockups — Show assets in real context (phone, billboard, browser)
6. Copy + Design Together — Show headline + visual pairing
7. Formats — Grid of all sizes/variants
8. Production Timeline
9. Next Steps
```

## Writing Rationale for Each Design Decision

For every major design choice, write one sentence using this format:
> "[Choice] because [reason tied to client's goal or user insight]."

Examples:
- "We chose dark navy as the primary color because it signals trust and authority, which aligns with your target audience of finance professionals."
- "The single-column mobile layout because 73% of your users are on mobile and a dense layout creates friction at checkout."
- "We used a bold display typeface for headlines because your brand voice is confident and direct — it should feel that way visually."

Never say "we liked it" or "it looks good." Always connect to a strategic or user reason.

## Mockup Guidelines
- Always show work in context, never just flat files on white
- Use device mockups (phone, laptop, billboard, packaging) matching the medium
- Show at least one mockup in a real-world setting (outdoor, in-hand, on-screen)
- For social media: show the post as it would appear in an Instagram or LinkedIn feed
- Minimum 3 mockup slides per presentation

## Output Formats
| Client Type | Preferred Format | Why |
|-------------|-----------------|-----|
| Startup / tech | Figma Slides or PDF | Modern, easy to share |
| Corporate / enterprise | PowerPoint .pptx | Works in their systems |
| Small business | PDF only | Simple, no friction |
| Agency pitch | Both PDF + interactive prototype | Shows full range |

## Execution Steps

1. Identify presentation type (concept / delivery / pitch)
2. Pull all final design assets from `output/` folder
3. Select the correct slide structure from above
4. Write rationale for each major design decision (1 sentence per choice)
5. Select 3–5 best mockups — quality over quantity
6. Write the Next Steps slide with specific dates and action items
7. Export as PDF to `output/presentations/[client-slug]-presentation-v[n].pdf`
8. If Figma Slides: use the Figma MCP to create the presentation in the client's Figma file

## Tone and Language Rules
- Write for a non-designer: no jargon like "kerning", "hierarchy", "affordances"
- Use "we chose X because it helps your users do Y" not "this leverages UX best practices"
- Keep slide text minimal — one headline, three bullets max per slide
- The visuals carry the weight; text provides the reason
- Every slide must have a point — cut anything decorative

## Quality Checks Before Sending
- [ ] Presentation starts with the brief (shows you listened)
- [ ] Every major design decision has a written rationale
- [ ] At least 3 mockup slides showing work in context
- [ ] Next Steps slide has real dates, not "TBD"
- [ ] No placeholder text, no unfinished slides
- [ ] File exported and saved to output/presentations/
- [ ] PDF opens clean with all fonts embedded
