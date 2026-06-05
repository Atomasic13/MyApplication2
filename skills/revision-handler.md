# Skill: Revision Handler

## Purpose
Receive client feedback in any format (text, voice transcript, annotated screenshot, WhatsApp message, call notes) and turn it into a clear, actionable revision plan — then execute or route each change to the right tool.

## When to Use
- Client replies with feedback after receiving designs
- Stakeholder review produces a list of changes
- Internal review flags issues before delivery
- Client calls with verbal feedback (after transcript is provided)

## Input Formats Accepted
- Raw text feedback ("change the button color to blue")
- Voice note transcript from WhatsApp/Telegram
- Annotated screenshot (client drew on the image)
- Email thread with feedback
- List of bullet points from a meeting
- Figma comments

## Step 1: Parse the Feedback

Read all feedback and classify every item into one of these categories:

| Category | Definition | Examples |
|----------|-----------|---------|
| **Visual** | Color, size, shape, spacing, weight | "Make it bigger", "darker blue", "more padding" |
| **Copy** | Text changes, tone, wording | "Change CTA to 'Get Started'", "headline is too long" |
| **Layout** | Position, order, structure | "Move logo to top left", "stack these on mobile" |
| **Concept** | Fundamental direction change | "This doesn't feel like us", "start over" |
| **Missing** | Something not included | "We need a dark mode version", "add the app store badges" |
| **Unclear** | Ambiguous, needs clarification | "Make it pop", "more modern", "not sure about this" |

## Step 2: Build the Revision Log

Output a revision log before making any changes:

```
# Revision Log — [Client Name] — [Date]

## Source: [e.g. WhatsApp message, email, call notes]

| # | Feedback (verbatim) | Category | Action | Tool | Effort |
|---|---------------------|----------|--------|------|--------|
| 1 | "The logo is too small on mobile" | Visual | Increase logo size on mobile breakpoint | Figma | 15 min |
| 2 | "Change button text to 'Book Now'" | Copy | Update CTA copy across all screens | Figma | 5 min |
| 3 | "It doesn't feel premium enough" | Unclear | → Needs clarification (see questions) | — | — |
| 4 | "Can we see it in black and white?" | Missing | Create monochrome variant | Figma | 30 min |

## Unclear Items — Needs Client Response Before Proceeding
1. "It doesn't feel premium enough" — Can you point to a brand or example that has the right feel? Or describe what's missing: Is it the font, the colors, the imagery style?

## Total Estimated Effort: [X hours]
## Estimated Completion: [date/time]
```

Always send the revision log to the client before executing, unless the feedback is 100% clear.

## Step 3: Route to the Right Tool

Once revisions are confirmed, execute each one:

| Category | Tool | How |
|----------|------|-----|
| Visual / Layout in Figma | Figma MCP | Use `use_figma` to apply changes directly |
| Copy changes | Claude directly | Update text in Figma or code file |
| New image generation | Gemini / Midjourney | Regenerate with updated brief |
| Code changes | Edit tool | Modify relevant component/CSS |
| New variants | Figma MCP | Duplicate frame, apply variant changes |
| Concept-level change | Campaign Brief Parser skill | Re-run brief parser with new direction |

## Step 4: Version Control

Before applying any revision:
1. Duplicate the current Figma page and name it `[name] — v[n] ARCHIVED [date]`
2. Work on the current page only
3. When done, rename current page to `v[n+1] — [date]`
4. Update file version in the delivery log

Never delete old versions. Clients often change their mind and want to go back.

## Handling Concept-Level Feedback

If the client says anything like:
- "This isn't what I had in mind"
- "Start over"
- "The whole direction is wrong"
- "It doesn't feel like us"

Do NOT immediately start redesigning. Instead:

1. Acknowledge: "Got it — I want to make sure the next version is exactly right."
2. Ask 3 specific questions:
   - "Can you share 2–3 brands or designs that have the feeling you're looking for?"
   - "Which specific element is furthest from what you imagined — the colors, the fonts, or the overall layout?"
   - "Is the concept itself wrong, or is it the execution that needs adjusting?"
3. Only proceed once at least 2 of the 3 questions are answered.
4. Re-run the Campaign Brief Parser skill with the new direction.

This prevents wasted work and documents why the direction changed.

## Handling Scope Creep

If a revision request adds something that was not in the original brief (e.g., client asks for 5 new formats, an animation, or a whole new section), flag it:

```
Note: "[specific request]" goes beyond the original scope of [project name].

This is a separate deliverable. I can include it in this round for [estimated cost/time],
or we can treat it as a new mini-project. Let me know how you'd like to proceed.
```

Never add out-of-scope work silently. Always make it visible.

## Execution Steps

1. Read all feedback in full before categorizing anything
2. Build and output the revision log
3. Flag unclear items — do not guess what "make it pop" means
4. Get confirmation on unclear items before executing
5. Archive current version in Figma before making changes
6. Execute all clear revisions, routing each to the correct tool
7. Update delivery log with new version number
8. Send updated files using the Asset Delivery Packager skill

## Message Templates

### Acknowledging feedback received:
```
Thanks for the feedback on [project name]. I've gone through everything and here's my revision plan:

[paste revision log]

The only item I need clarification on before I can start: [unclear item + specific question]

Once you reply, I'll have the updated version to you by [date/time].
```

### Delivering revisions:
```
Here's v[n] of [project name] with all the changes applied:

✅ [change 1]
✅ [change 2]
✅ [change 3]

[If scope creep noted]: I've noted that [X] is outside the original scope — happy to discuss.

Files attached / see Figma link below.
```

## Quality Checks Before Marking Revision Complete
- [ ] Every piece of feedback has been addressed or explicitly flagged
- [ ] No unclear items were guessed — all were clarified or flagged
- [ ] Previous version archived in Figma before changes
- [ ] Scope creep flagged if any new requests appeared
- [ ] Revision log saved to `output/revisions/[client-slug]-revisions-v[n].md`
- [ ] Delivery done via Asset Delivery Packager skill
