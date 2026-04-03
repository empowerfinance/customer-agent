# Customer Agent — AI Sprint (April 2026)

A unified tool that evaluates Tilt's mobile experience from the customer's perspective by combining quantitative experiment data with qualitative UX analysis — all from a single Claude Project in the browser.

**Team**: Thomas (orchestration/pipeline), Pawel (UX evaluation agent), Dotan (experiment analysis), Britney (product vision/design)

## Vision

A user inputs a **Statsig flag key** (+ optional Linear project ID, Amplitude dashboard URL) into a Claude Project and gets a unified report combining:

- **Track A (Quantitative)**: Experiment variant performance — conversion rates, statistical significance, funnel drop-offs, real user session analysis (Dotan's work)
- **Track B (Qualitative)**: UX evaluation of the actual screens in the flow — heuristics, anti-patterns, user archetypes, competitive gaps (Pawel's work)
- **Track C (Synthesis)**: Cross-referenced findings — data anomalies explained by UX issues, de-duplicated, ranked by severity × user impact

```
User inputs: Statsig flag key
                    ↓
        ┌───────────┴───────────┐
        ↓                       ↓
   Track A (Quant)         Track B (Qual)
   StatSig → flag config   Screenshots of the flow
   GitHub → associated PRs  → UX heuristics
   Amplitude → experiment   → anti-pattern detection
   FullStory → sessions     → archetype analysis
   → variant breakdown      → competitive comparison
        ↓                       ↓
        └───────────┬───────────┘
                    ↓
            Track C: Synthesis
            → unified report with
              ranked, actionable findings
```

Everything runs in the browser via Claude.ai with MCP integrations. No CLI needed.

## Screenshot Capture for Track B

Track B needs screenshots of the screens in the flow being evaluated. We support multiple approaches:

### 1. Manual Screenshots (highest quality input)

Take screenshots directly from a real device, simulator, or emulator (Cmd+Shift+4, device screenshot, etc.) and upload them to the Claude Project. This produces the highest-quality images, which means the best UX feedback from the agent.

**Best for**: Demo, ad-hoc evaluation, when you want the cleanest possible input.

### 2. Fullstory Session Replays (real user data, in-browser)

Navigate to FullStory session replays in Chrome and capture screenshots of what actual customers experienced. This can be done manually (scrub + screenshot) or automated via the Claude Chrome extension (`/fullstory-capture`).

**Best for**: Seeing real user interactions from the actual user base — surfaces friction that mocks and test accounts miss.

**Current state**: Proven concept. Chrome automation can navigate replays and capture screenshots. Some friction remains (replay rendering lag, WebView gaps, extension disconnects during long sessions), but works well enough for targeted captures.

### 3. Explored: Maestro & Paparazzi (future automation)

We also explored two Android-specific capture methods that could enable fully automated, CI-integrated screenshot pipelines:

- **Maestro**: Drives the live app on an Android emulator via YAML flows. Captures real app state with real server data. We successfully captured 10 screenshots across the main app tabs. Friction: server-driven modals, lock screens, and WebViews break flows unpredictably. Needs dedicated backend test accounts to be reliable.
- **Paparazzi**: Renders Composable screens headlessly on the JVM — no device needed. We captured 19 screens (onboarding + cash advance). Limitation: shows static composables with fake data, not what real users see.

Both require the `empower-android` repo and CLI tooling. More engineering work is needed to make them fully automated and hands-off. See `SPRINT.md` for detailed findings.

## Quick Start

Open the **[Customer Agent Claude Project](https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d)** in your browser. That's it — all knowledge files, skills, and MCP connections are already configured.

### Option 1: Just UX evaluation (simplest)

1. Open the [Customer Agent project](https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d)
2. Take screenshots of the flow you want to evaluate (from device, emulator, or FullStory)
3. Drag screenshots into the chat, ask for UX evaluation
4. Get structured feedback

### Option 2: Full analysis (quant + qual + synthesis)

1. Open the [Customer Agent project](https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d)
2. Provide a Statsig flag key + screenshots or Figma links
3. The orchestrator runs Track A (experiment analysis) and Track B (UX evaluation) in parallel
4. Get a unified synthesis report

### Prerequisites

The Claude Project is pre-configured, but you'll need browser logins for services that Track A accesses via Chrome:

| Requirement | Purpose |
|------------|---------|
| Claude.ai account (Tilt org) | Access the project |
| StatSig login in Chrome | Flag configuration, variant details |
| FullStory login in Chrome | Real user sessions, behavioral patterns |
| GitHub login in Chrome | PR details associated with experiments |

MCP connections (Amplitude, Figma, GitHub, Linear, Slack, Notion) are already enabled on the project.

### Setting up your own Claude Project (optional)

If you want to create a separate project instead of using the shared one:

1. Create a new Claude Project on claude.ai
2. Upload all 8 files from `knowledge/`
3. Install skill files from `skills/` via Customize → Skills (flag-deep-dive, flag-ux-synthesis)
4. Enable MCP connections: Amplitude, Figma, Slack, Linear, GitHub
5. Set the system prompt: "You are the Tilt Customer Agent. Follow the workflow in customer-agent-instructions.md."

## Repo Structure

```
.claude/commands/                # Claude Code slash commands (run from this repo)
  fullstory-capture.md           # /fullstory-capture — browser-based session replay capture
  amplitude-experiment-monitor.md # /amplitude-experiment-monitor — A/B experiment analysis
  screenshot-screens.md          # /screenshot-screens — Paparazzi capture (requires empower-android)
  customer-agent-capture.md      # /customer-agent-capture — full pipeline (requires empower-android)

knowledge/                       # Claude.ai Project knowledge files (upload all 8)
  ux-researcher.md               # Pawel — UX evaluation framework
  ux-anti-pattern-detection.md   # Pawel — 13 UX anti-pattern categories
  tilt-ca-research-structured.md # Pawel — cash advance journey research (structured)
  tilt-ca-research-raw.md        # Pawel — raw user evidence + competitor data
  tilt-archetypes-enriched.md    # Pawel — 4 user archetypes with verbatim quotes
  customer-agent-instructions.md # Orchestration workflow for the Claude.ai project
  experiment-analysis-guide.md   # Statistical analysis methodology (z-test, deltas)
  report-template.md             # Unified report output format

skills/                          # Claude.ai skill files (.skill = zip)
  flag-deep-dive.skill           # Dotan — StatSig + Amplitude + FullStory + GitHub analysis
  flag-ux-synthesis-3.skill      # Britney — orchestrator that runs deep-dive + UX analysis

maestro/                         # Maestro emulator-based screenshot capture (explored)
  flows/                         # YAML flow definitions
  screenshots/                   # Captured PNGs from Maestro runs

pipeline/                        # Automation scripts (requires API key)
  customer-agent-pipeline.py     # Sends screenshots to Claude API for UX analysis
```

## Android Dependency (for Paparazzi/Maestro only)

The Paparazzi and Maestro capture methods require `~/empower/empower-android` on branch `customer-agent/internal-composables`. The Fullstory and manual screenshot flows do not need this.

```bash
cd ~/empower/empower-android
git fetch origin customer-agent/internal-composables
git checkout customer-agent/internal-composables
```

That branch contains:
- 531 `private → internal` Composable visibility changes (enables Paparazzi test access)
- Paparazzi snapshot PNGs for onboarding + cash advance
- `specs/SUBEX-16/IMPLEMENTATION_SUMMARY.md` — example Linear-to-flag mapping
