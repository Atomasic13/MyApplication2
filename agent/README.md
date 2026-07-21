# DECA Agent Pipeline

The orchestration layer that runs a client brief through the full skill chain.

## Flow

```
brief.md
   │
   ▼
 parse    → structured scope (deliverables, timeline, open questions)
   │
   ▼
 plan     → execution plan (skill per deliverable, specs, order)
   │
   ▼
 produce  → final content: copy, guidelines, flow maps + generation specs
   │         for every visual asset (ready for Figma / image models)
   ▼
 package  → file manifest, README.txt, Telegram + email delivery messages
```

Each phase is one Claude call (Opus 4.8, adaptive thinking, streaming).
The skill files in `../skills/` are loaded as a cached system prompt —
repeated runs pay ~10% of input cost on the skill library.

## Setup

```sh
cd agent
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...   # or `ant auth login`
```

## Run

```sh
# Full pipeline
python deca.py briefs/novabrand.md --client "NovaBrand"

# Single phase (e.g. re-run packaging after edits)
python deca.py output/novabrand/2026-07-21/produce.md --client "NovaBrand" --phase package
```

Outputs land in `../output/<client-slug>/<date>/` — one `.md` per phase
plus `run.json` with the run manifest.

## Next integrations (planned)
- **Figma MCP** — feed `produce` specs into Figma via `use_figma`
- **Image generation** — route visual specs to Gemini / Midjourney
- **Telegram Bot** — auto-send the `package` output with the ZIP
- **Revision loop** — pipe client feedback through `skills/revision-handler.md`
