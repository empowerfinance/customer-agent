#!/usr/bin/env python3
"""
Customer Agent Pipeline — Maestro Screenshots → UX Evaluation → Structured Feedback

Takes screenshots captured by Maestro from the Android emulator and feeds them
to Claude for UX evaluation, simulating customer feedback and sentiment analysis.

Replicates what Pawel's Claude Project does with its UX research knowledge files.

Usage:
    python3 customer-agent-pipeline.py                          # all screenshots
    python3 customer-agent-pipeline.py --dir /path/to/screens   # custom directory
    python3 customer-agent-pipeline.py --screen 05-accounts-home.png  # single screen
    python3 customer-agent-pipeline.py --archetype young-cash-strapped  # specific persona
"""

import anthropic
import base64
import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# --- UX Research Knowledge (distilled from Pawel's knowledge files) ---

UX_RESEARCHER_PROMPT = """You are a senior UX researcher at a fintech company called Tilt (formerly Empower).
You evaluate mobile app screens from a real customer's perspective.

## Your Evaluation Framework

For each screen, assess against these heuristics:
1. **Clarity**: Is the purpose of the screen immediately obvious? Can the user understand what to do in <3 seconds?
2. **Trust & Safety**: Does this feel safe for handling money? Are security indicators present? Is language reassuring?
3. **Cognitive Load**: How many decisions does the user need to make? Are there too many options?
4. **Visual Hierarchy**: Is the most important element the most prominent? Does the eye flow naturally?
5. **Error Prevention**: Could a user easily make a mistake here? Are destructive actions guarded?
6. **Accessibility**: Text size, contrast, touch targets — would this work for users with vision/motor challenges?
7. **Emotional Design**: How does this screen make the user feel? Anxious? Confident? Confused?

## Anti-Patterns to Watch For
- Dark patterns (e.g., making cancellation hard, pre-selected upsells)
- Information overload on a single screen
- Unclear or missing CTAs
- Inconsistent navigation patterns
- Financial jargon without explanation
- Missing loading/error/empty states
- Tiny touch targets on mobile
- Excessive permissions requests without context
- Progress indicators that don't reflect actual progress
- Forced upgrades or subscription walls blocking core functionality

## User Archetypes to Consider

1. **Young & Cash-Strapped (18-25)**: Living paycheck to paycheck, needs cash advances, price-sensitive, skeptical of fees. Needs: speed, transparency, low/no fees.
2. **Rebuilding Credit (25-35)**: Had financial setbacks, trying to rebuild. Needs: credit-building features, encouragement, clear progress tracking.
3. **Busy Parent (30-45)**: Managing family finances, wants simplicity. Needs: quick actions, bill management, spending insights.
4. **New to Banking (any age)**: First bank account or new to US banking. Needs: education, simple language, step-by-step guidance.
5. **Power User (any age)**: Wants advanced features, detailed analytics. Needs: data density, customization, export capabilities.

## Cash Advance Market Context

Tilt competes with Dave, Earnin, Brigit, and MoneyLion for cash advance users.
Key competitive factors: advance limits ($50-$500), speed of delivery, fees/tips model, repayment flexibility.
Users often have multiple apps installed and compare experience quality.
"""

EVALUATION_INSTRUCTIONS = """Evaluate the provided app screenshot(s) as if you are a real customer using this fintech app.

For EACH screen, provide:

### Screen: [name/description]

**First Impression** (what a user thinks in the first 3 seconds):
> [Write this as an actual customer thought, in first person]

**Sentiment**: [Positive / Neutral / Negative / Mixed]
**Sentiment Score**: [1-10, where 1=very negative, 10=very positive]

**UX Findings**:
| # | Finding | Severity | Category | Archetype Most Affected |
|---|---------|----------|----------|------------------------|
| 1 | ... | Critical/Major/Minor/Enhancement | Clarity/Trust/CogLoad/... | ... |

**Customer Feedback Simulation**:
Write 2-3 realistic app store review snippets (1-2 sentences each) that a real user might write based on seeing this screen. Include star rating. Vary the archetypes.

**Competitive Gap**:
How would Dave, Earnin, or Brigit handle this same screen/flow differently? Any advantages they have?

---

After evaluating all screens, provide:

## Overall Flow Assessment

**Flow Sentiment**: [Overall sentiment across all screens]
**Flow Score**: [1-10]
**Top 3 Issues** (ranked by severity × user impact):
1. ...
2. ...
3. ...

**Top 3 Strengths**:
1. ...
2. ...
3. ...

**Recommended Actions** (prioritized):
1. [Quick win — can fix in a sprint]
2. [Medium effort — needs design review]
3. [Strategic — requires product decision]
"""

ARCHETYPE_PROMPTS = {
    "young-cash-strapped": "Evaluate ONLY from the perspective of an 18-25 year old living paycheck to paycheck who primarily uses this app for cash advances. They are price-sensitive, skeptical of fees and subscriptions, and compare this app against Dave and Earnin frequently.",
    "rebuilding-credit": "Evaluate ONLY from the perspective of a 25-35 year old who had financial setbacks (missed payments, low credit score) and is using this app to rebuild their credit. They need encouragement and clear progress indicators.",
    "busy-parent": "Evaluate ONLY from the perspective of a 30-45 year old parent managing family finances. They have limited time, want things done quickly, and get frustrated by unnecessary steps or upsells.",
    "new-to-banking": "Evaluate ONLY from the perspective of someone new to banking (either young or new to the US). Financial jargon confuses them, and they need clear guidance at every step.",
}


def load_screenshots(directory: str, specific_screen: str = None) -> list[tuple[str, bytes]]:
    """Load PNG screenshots from directory. Returns list of (filename, bytes)."""
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)

    if specific_screen:
        path = dir_path / specific_screen
        if not path.exists():
            print(f"Error: Screenshot {specific_screen} not found in {directory}")
            sys.exit(1)
        return [(path.name, path.read_bytes())]

    screenshots = sorted(dir_path.glob("*.png"))
    if not screenshots:
        print(f"Error: No PNG files found in {directory}")
        sys.exit(1)

    return [(s.name, s.read_bytes()) for s in screenshots]


def build_messages(screenshots: list[tuple[str, bytes]], archetype: str = None) -> list[dict]:
    """Build the API message with screenshots as images."""
    content = []

    # Add screen listing
    screen_list = "\n".join(f"- {name}" for name, _ in screenshots)
    content.append({
        "type": "text",
        "text": f"I'm evaluating {len(screenshots)} screen(s) from the Tilt fintech app (Android):\n{screen_list}\n\nHere are the screenshots:"
    })

    # Add each screenshot
    for name, img_bytes in screenshots:
        b64 = base64.standard_b64encode(img_bytes).decode("utf-8")
        content.append({
            "type": "text",
            "text": f"\n**Screen: {name}**"
        })
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": b64,
            }
        })

    # Add evaluation instructions
    instructions = EVALUATION_INSTRUCTIONS
    if archetype and archetype in ARCHETYPE_PROMPTS:
        instructions = ARCHETYPE_PROMPTS[archetype] + "\n\n" + instructions

    content.append({
        "type": "text",
        "text": instructions
    })

    return [{"role": "user", "content": content}]


def run_evaluation(screenshots: list[tuple[str, bytes]], archetype: str = None, output_dir: str = None):
    """Send screenshots to Claude and get UX evaluation."""
    client = anthropic.Anthropic()

    messages = build_messages(screenshots, archetype)

    print(f"Sending {len(screenshots)} screenshot(s) to Claude for UX evaluation...")
    if archetype:
        print(f"  Archetype focus: {archetype}")
    print()

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        system=UX_RESEARCHER_PROMPT,
        messages=messages,
    )

    result = response.content[0].text

    # Print to stdout
    print(result)

    # Save to file if output_dir specified
    if output_dir:
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        suffix = f"_{archetype}" if archetype else ""
        filename = f"ux-evaluation{suffix}_{timestamp}.md"
        filepath = out_path / filename
        filepath.write_text(f"# UX Evaluation Report\n\n**Generated**: {datetime.now().isoformat()}\n**Archetype**: {archetype or 'all'}\n**Screens**: {len(screenshots)}\n\n---\n\n{result}\n")
        print(f"\n--- Report saved to: {filepath} ---")

    return result


def main():
    parser = argparse.ArgumentParser(description="Customer Agent Pipeline — Screenshot → UX Evaluation")
    parser.add_argument("--dir", default="/tmp/maestro-screenshots", help="Screenshot directory")
    parser.add_argument("--screen", help="Evaluate a specific screenshot file")
    parser.add_argument("--archetype", choices=list(ARCHETYPE_PROMPTS.keys()), help="Evaluate from specific persona")
    parser.add_argument("--output", default="/tmp/customer-agent-reports", help="Output directory for reports")
    parser.add_argument("--all-archetypes", action="store_true", help="Run evaluation for each archetype separately")
    parser.add_argument("--json", action="store_true", help="Also output structured JSON")
    args = parser.parse_args()

    screenshots = load_screenshots(args.dir, args.screen)
    print(f"Loaded {len(screenshots)} screenshot(s) from {args.dir}")
    for name, data in screenshots:
        print(f"  {name} ({len(data) // 1024}KB)")
    print()

    if args.all_archetypes:
        for archetype in ARCHETYPE_PROMPTS:
            print(f"\n{'='*60}")
            print(f"  ARCHETYPE: {archetype}")
            print(f"{'='*60}\n")
            run_evaluation(screenshots, archetype=archetype, output_dir=args.output)
    else:
        run_evaluation(screenshots, archetype=args.archetype, output_dir=args.output)


if __name__ == "__main__":
    main()
