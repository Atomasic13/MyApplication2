# Skill: Campaign Brief Parser

## Purpose
Parse a client brief (PDF, doc, text, voice transcript) and output a structured design scope document with deliverables, timelines, and open questions — ready to execute or send to the client for approval.

## When to Use
- Client sends any form of brief (PDF, email copy, WhatsApp message, voice note transcript)
- Kickoff meeting notes need to be turned into an actionable scope
- You need to quote a project before starting design work

## Input Formats Accepted
- Raw text pasted into the prompt
- File path to a .md, .txt, .pdf, or .docx brief
- Bullet-point notes from a call
- Voice-to-text transcript

## Output
A structured Markdown document with the following sections:

```
# [Client Name] — Design Brief Summary
Date: [today]
Prepared by: DECA Agent

## Project Overview
[2–3 sentence summary of what the client wants and why]

## Business Goals
- [goal 1]
- [goal 2]

## Target Audience
[Who is this designed for — age, context, device, pain point]

## Deliverables
| # | Deliverable | Format | Size / Specs | Quantity | Priority |
|---|-------------|--------|-------------|----------|----------|
| 1 | Social posts | PNG    | 1080x1080   | 12       | High     |
...

## Timeline
| Phase         | Start      | End        | Owner  |
|---------------|------------|------------|--------|
| Research      | [date]     | [date]     | Agent  |
| Design        | [date]     | [date]     | Agent  |
| Review        | [date]     | [date]     | Client |
| Final Export  | [date]     | [date]     | Agent  |

## Design Direction
- Style: [e.g. minimal, bold, editorial]
- Color palette: [if mentioned or inferred]
- Typography mood: [e.g. modern sans-serif, expressive display]
- Reference brands: [any mentioned]

## Open Questions (must resolve before starting)
1. [question]
2. [question]

## Out of Scope
- [anything the brief implies but was not confirmed]

## Estimated Hours (for internal use)
[breakdown by phase]
```

## Execution Steps

1. Read the full brief without interrupting. Extract all facts first.
2. Identify: WHO the client is, WHAT they need, WHEN it's due, WHY it matters.
3. List every deliverable mentioned, even implicitly. Flag ambiguous ones.
4. Estimate a timeline by working backwards from the stated deadline.
   - If no deadline: assume 5 business days for campaign, 15 for full brand.
5. Write open questions for anything that blocks design from starting.
6. Never invent specs that weren't in the brief — flag them as TBD.
7. Output the document to a file: `output/briefs/[client-slug]-brief-[date].md`

## Examples of Good Parsing

**Input**: "We need posts for our product launch next Friday. It's a new coffee brand, very premium, targeting professionals. Instagram and LinkedIn."

**Output deliverables**:
- Instagram feed post (1080x1080) × 3
- Instagram Story (1080x1920) × 2
- LinkedIn post (1200x627) × 2
- Brand: premium, professional, coffee
- Open question: Do you have a logo and brand colors ready?

## Quality Checks Before Outputting
- [ ] Every deliverable has a format and size
- [ ] Timeline has at least one review/approval step for the client
- [ ] Open questions are specific, not vague
- [ ] Nothing invented — only what was in the brief or a safe industry default
- [ ] Document saved to output/briefs/
