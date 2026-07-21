#!/usr/bin/env python3
"""DECA — design agency agent pipeline.

Takes a client brief and runs it through the full skill chain:

    brief -> parse -> plan -> produce deliverables -> package -> delivery message

Each phase is one Claude call. The skill files in ../skills/ are loaded into
the system prompt (with prompt caching, so repeated runs for the same client
only pay for the brief and outputs, not the skill library).

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python deca.py path/to/brief.md --client "NovaBrand"
    python deca.py path/to/brief.md --client "NovaBrand" --phase parse   # single phase
"""

import argparse
import datetime
import json
import pathlib
import re
import sys

from anthropic import Anthropic

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
OUTPUT_DIR = ROOT / "output"

MODEL = "claude-opus-4-8"

# Phase -> (skills to load, instruction)
PHASES = {
    "parse": (
        ["campaign-brief-parser.md"],
        "Parse the client brief below into the structured scope document "
        "defined by the Campaign Brief Parser skill. Output only the document.",
    ),
    "plan": (
        ["campaign-brief-parser.md", "brand-guidelines.md",
         "social-media-pack.md", "ui-screen-gen.md"],
        "You are given a parsed design scope. Produce an execution plan: for "
        "each deliverable, name which skill produces it, the exact specs, the "
        "order of production, and any dependency between deliverables. "
        "Output as a Markdown checklist grouped by skill.",
    ),
    "produce": (
        ["brand-guidelines.md", "social-media-pack.md", "ui-screen-gen.md",
         "client-presentation-generator.md"],
        "Execute the plan below. For every text deliverable (copy, captions, "
        "guidelines document, flow maps, presentation content) produce the "
        "complete final content now, following each skill's structure and "
        "quality checks. For every visual deliverable, produce a complete "
        "generation spec (layout, exact copy, colors, type, dimensions) ready "
        "to hand to Figma or an image model. Separate each deliverable with a "
        "line: === FILE: <suggested-filename> ===",
    ),
    "package": (
        ["asset-delivery-packager.md"],
        "Given the produced deliverables below, output: (1) the final file "
        "manifest with correct naming per the Asset Delivery Packager "
        "convention, (2) the README.txt content, (3) the delivery messages "
        "for Telegram and email, personalized to this client and project.",
    ),
}

PHASE_ORDER = ["parse", "plan", "produce", "package"]


def load_skills(names: list[str]) -> str:
    parts = []
    for name in names:
        path = SKILLS_DIR / name
        parts.append(f"<skill name=\"{path.stem}\">\n{path.read_text()}\n</skill>")
    return "\n\n".join(parts)


def run_phase(client: Anthropic, phase: str, payload: str, client_name: str) -> str:
    skill_names, instruction = PHASES[phase]

    # Skills are the stable prefix -> cache them. The volatile payload goes in
    # the user turn after the breakpoint.
    system = [
        {
            "type": "text",
            "text": (
                "You are DECA, an AI design agent operating a professional design "
                "studio. You follow the skill documents below exactly — their "
                "structures, naming conventions, and quality checks are "
                "non-negotiable. You never invent client requirements that are "
                "not in the brief; you flag them as open questions instead.\n\n"
                + load_skills(skill_names)
            ),
            "cache_control": {"type": "ephemeral", "ttl": "1h"},
        }
    ]

    user = f"Client: {client_name}\n\n{instruction}\n\n---\n\n{payload}"

    with client.messages.stream(
        model=MODEL,
        max_tokens=64000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=system,
        messages=[{"role": "user", "content": user}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        response = stream.get_final_message()

    print()  # newline after stream
    usage = response.usage
    print(
        f"[{phase}] tokens: in={usage.input_tokens} out={usage.output_tokens} "
        f"cache_read={usage.cache_read_input_tokens} "
        f"cache_write={usage.cache_creation_input_tokens}",
        file=sys.stderr,
    )
    return "".join(b.text for b in response.content if b.type == "text")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main() -> None:
    ap = argparse.ArgumentParser(description="DECA design agent pipeline")
    ap.add_argument("brief", help="Path to the client brief (.md/.txt)")
    ap.add_argument("--client", required=True, help="Client name")
    ap.add_argument("--phase", choices=PHASE_ORDER, help="Run a single phase only")
    args = ap.parse_args()

    brief = pathlib.Path(args.brief).read_text()
    slug = slugify(args.client)
    date = datetime.date.today().isoformat()
    run_dir = OUTPUT_DIR / slug / date
    run_dir.mkdir(parents=True, exist_ok=True)

    client = Anthropic()  # ANTHROPIC_API_KEY or ant auth profile

    phases = [args.phase] if args.phase else PHASE_ORDER
    payload = brief
    results: dict[str, str] = {}

    for phase in phases:
        print(f"\n===== PHASE: {phase} =====\n", file=sys.stderr)
        result = run_phase(client, phase, payload, args.client)
        results[phase] = result
        (run_dir / f"{phase}.md").write_text(result)
        payload = result  # each phase feeds the next

    manifest = {
        "client": args.client,
        "date": date,
        "phases": list(results),
        "output_dir": str(run_dir),
    }
    (run_dir / "run.json").write_text(json.dumps(manifest, indent=2))
    print(f"\nDone. Outputs in {run_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
