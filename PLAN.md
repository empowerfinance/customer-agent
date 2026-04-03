# Customer Agent — AI Sprint Plan

## Context

Tilt Finance's AI Sprint "Build Customer Agents" aims to create a tool that evaluates the mobile/web experience from a customer's perspective, identifies friction, and compares against competitors. Four team members have independently built pieces that can be unified into a single end-to-end product:

- **Pawel**: Claude Project with UX research knowledge files → qualitative screen/flow analysis
- **Dotan**: Claude dashboard that evaluates Statsig experiment variants using GitHub/Amplitude/Fullstory
- **Britney** (designer): Vision for the end product UX and report format

**Goal**: A Claude Project (browser) where a user inputs a Linear project ID + optional Statsig key + optional Amplitude dashboard → gets a unified quantitative + qualitative customer experience report.

---

## Architecture: Claude Project with Cloud MCP Orchestration

The product is a **single Claude Project on claude.ai** that orchestrates everything through MCP integrations. No CLI, no local tooling — the end-user just opens the project and types their request.

### MCP Connections Required

| Service | Available in claude.ai? | Purpose |
|---|---|---|
| **Linear** | Yes (already connected) | Fetch project context, issues, Figma URLs, experiment references |
| **Amplitude** | Yes (already connected) | Experiment data, funnels, session replays, AI insights |
| **Figma** | Yes (already connected) | Screenshots of designs referenced in Linear issues |
| **Slack** | Yes (already connected) | Post final reports |
| **GitHub** | Yes (already connected) | Find PRs associated with experiment, code changes |
| **Statsig** | No — CLI-only (`npx mcp-remote`) | **Workaround**: Use Amplitude experiment data instead. Amplitude already tracks Statsig experiment exposures and outcomes. |
| **Fullstory** | No MCP configured | **Workaround**: Use Amplitude's session replay tools (`get_session_replays`, `list_session_replays`, `get_session_replay_events`). If Amplitude session replay is insufficient, the community Fullstory MCP (`creevey-equals/fullstory-mcp`) can be added later. |

**Key insight**: Statsig and Fullstory gaps are solved by Amplitude, which already has rich MCP tools and is already connected. This eliminates two integration blockers.

### Knowledge Files (uploaded to the Claude Project)

**From Pawel (existing — copy from his project):**
1. `ux-researcher.md` — UX evaluation framework
2. `ux-anti-pattern-detection.md` — common UX anti-patterns
3. `tilt-ca-research-structured.md` — structured cash advance market research
4. `tilt-ca-research-raw.md` — raw research data
5. `tilt-archetypes-enriched.md` — user persona archetypes

**New files to create:**
6. `customer-agent-instructions.md` — system prompt / orchestration workflow (the main instruction set)
7. `experiment-analysis-guide.md` — ported from `amplitude-experiment-monitor.md` (statistical significance calculations, metric extraction rules)
8. `report-template.md` — unified output format for the final report

### Project System Prompt (high-level)

```
You are the Tilt Customer Agent. You evaluate product experiences from the
customer's perspective by combining quantitative experiment data with
qualitative UX analysis.

When given a Linear project ID (and optionally a Statsig key or Amplitude
dashboard URL), you run a structured analysis workflow and produce a unified
report. Follow the workflow in customer-agent-instructions.md.
```

---

## Orchestration Workflow (inside `customer-agent-instructions.md`)

### Input
User provides one or more of:
- Linear project ID or URL (required)
- Statsig experiment key (optional)
- Amplitude dashboard/chart URL (optional)

### Phase 1 — Context Gathering
1. **Linear**: Fetch the project (`get_project` with `includeMilestones: true, includeMembers: true`), list its issues, read issue descriptions for Figma URLs and experiment references
2. **Amplitude**: Call `get_context` to establish org/project context
3. Extract: Figma URLs, Statsig/experiment keys mentioned in issues, Amplitude event names from issue descriptions or PR references

### Phase 2A — Quantitative Analysis (Dotan's Track)
1. **Find the experiment**: Search Amplitude for the Statsig key or experiment name using `search` and `get_experiments`
2. **Pull variant data**: Use `query_experiment` to get conversion rates, user counts, significance per variant
3. **Compute significance**: If Amplitude doesn't provide p-values, use two-proportion z-test (methodology from `experiment-analysis-guide.md`)
4. **Funnel analysis**: Use `query_chart` on relevant funnel charts to see where users drop off
5. **Session replays**: Use `get_session_replays` filtered by experiment variant to find behavioral patterns. Use `get_session_replay_events` for interaction timelines.
6. **GitHub context**: Search for PRs associated with the experiment key to understand what code changes were made

Output: Structured quantitative findings (conversion rates, significance, funnel drop-offs, behavioral patterns from replays)

### Phase 2B — Qualitative Analysis (Pawel's Track)
1. **Get screenshots**: For each Figma URL found in Linear issues, use Figma MCP `get_screenshot` and `get_design_context`
2. **If no Figma URLs**: Ask the user to upload screenshots, or search Figma using `search_design_system` with the project/feature name
3. **UX evaluation**: Apply the frameworks from the knowledge files:
   - Evaluate each screen against UX heuristics (from `ux-researcher.md`)
   - Run anti-pattern detection (from `ux-anti-pattern-detection.md`)
   - Evaluate through each user archetype lens (from `tilt-archetypes-enriched.md`)
   - Consider cash advance market context (from `tilt-ca-research-structured.md`)
4. **Competitive comparison**: Using market research knowledge, note where competitors handle similar flows better

Output: Structured qualitative findings (UX scores per screen, anti-patterns detected, archetype-specific issues, competitive gaps)

### Phase 3 — Synthesis & Report
1. **Cross-reference**: Where quantitative data (e.g., 40% funnel drop-off at step 3) aligns with qualitative findings (e.g., step 3 screen has unclear CTA), flag as HIGH CONFIDENCE
2. **De-duplicate**: Merge findings that describe the same underlying issue from different angles
3. **Rank**: Score each finding by `severity x confidence x user impact`
4. **Format**: Generate the unified report (template in `report-template.md`)

### Phase 4 — Distribution (optional)
- Post to Slack channel via `slack_send_message`
- Post as Linear status update via `save_status_update`
- User can copy/paste from the conversation

---

## Report Template (`report-template.md`)

```markdown
# Customer Agent Report: [Project Name]
**Date**: [date] | **Linear Project**: [link] | **Experiment**: [key]

## Executive Summary
[2-3 sentences: overall health, biggest finding, recommended action]

## Quantitative Findings
### Experiment Performance
- Control vs Variant(s): conversion rates, significance, lift
- Sample sizes and confidence levels

### Funnel Analysis
- Step-by-step drop-off rates
- Biggest drop-off point with session replay evidence

### Session Replay Insights
- Behavioral patterns observed (rage taps, confusion, abandonment)
- [Links to specific replays]

## Qualitative Findings
### UX Evaluation by Screen
| Screen | Clarity | Trust | Friction | Anti-patterns | Score |
|--------|---------|-------|----------|---------------|-------|

### Archetype Analysis
- [For each relevant archetype: how does this experience serve them?]

### Competitive Gaps
- [Where competitors handle this better, with specifics]

## Integrated Findings (High Confidence)
[Findings where quant + qual converge — these are the most actionable]

## Recommendations
| Priority | Finding | Evidence | Suggested Fix |
|----------|---------|----------|---------------|
| P0 | ... | Quant: X, Qual: Y | ... |

## Appendix
- Amplitude charts referenced: [links]
- Figma frames analyzed: [links]
- Session replays reviewed: [links]
```

---

## Sprint Plan

### Day 1: Project Setup + Context Gathering
- [ ] Create the Claude Project on claude.ai
- [ ] Copy Pawel's 5 knowledge files from his existing project
- [ ] Configure MCP integrations (Linear, Amplitude, Figma, Slack) — these should already be available org-wide
- [ ] Write `customer-agent-instructions.md` (the orchestration workflow above)
- [ ] Test Phase 1: give it a real Linear project ID, verify it pulls context and finds Figma URLs
- **Owner**: Thomas + Pawel

### Day 2: Track A — Quantitative Analysis
- [ ] Write `experiment-analysis-guide.md` (port logic from `amplitude-experiment-monitor.md` at `/Users/thomasq/empower/empower-android/.claude/commands/amplitude-experiment-monitor.md`)
- [ ] Test with a real Statsig experiment: can Amplitude find it? Does the z-test math work?
- [ ] Test session replay integration: `get_session_replays` with experiment filters
- [ ] Have Dotan validate output against his dashboard — do the numbers match?
- **Owner**: Thomas + Dotan

### Day 3: Track B — Qualitative Analysis
- [ ] Test Figma screenshot extraction from Linear issue URLs
- [ ] Validate UX evaluation output with Pawel — is the quality comparable to his manual Claude Project?
- [ ] Test with a known problematic screen to verify the agent catches real issues
- [ ] Add competitive comparison prompting
- **Owner**: Thomas + Pawel

### Day 4: Track C — Synthesis + Report
- [ ] Build the synthesis logic (cross-referencing, de-duplication, ranking)
- [ ] Write `report-template.md`
- [ ] Run end-to-end on 2-3 real Linear projects
- [ ] Have Britney review the report format and output quality
- **Owner**: Thomas + Britney

### Day 5: Polish + Demo
- [ ] Edge cases: missing Figma URLs, no experiment, no Amplitude data
- [ ] Add Slack distribution
- [ ] Prepare demo: run live on a real project during presentation
- [ ] Document setup instructions for other teams
- **Owner**: All

---

## How Screenshots Get Into the Agent

Priority order (for the hackathon):
1. **Figma MCP** (`get_screenshot`) — extract Figma URLs from Linear issues, fetch screenshots automatically. This is the primary path.
2. **Manual upload** — user drags screenshots into the Claude conversation. Fallback when Figma URLs aren't in Linear.
3. **Amplitude session replays** — not screenshots per se, but behavioral data that complements visual analysis.

**Post-hackathon additions:**
4. **Paparazzi renders** — pre-generate screenshots of Composables, upload to the project or host somewhere accessible
5. **Maestro captures** — automated flow screenshots from running app, uploaded to the project
6. **Fullstory MCP** — if/when available, pull session replay screenshots via Puppeteer technique

---

## Open Questions for the Team

1. **Pawel**: Can you export your Claude Project's knowledge files (the 5 .md files) so we can copy them into the new unified project?
2. **Dotan**: What's the exact flow your dashboard uses? Does it start from Statsig API → GitHub search → Amplitude, or does it use Amplitude's experiment tools directly? We need to validate that Amplitude MCP can replicate your approach.
3. **Britney**: Any specific report sections or format preferences beyond what's in the template above?

---

## Post-Hackathon Evolution

1. **Claude Code CLI skill** (`/customer-agent`): Port to a `.claude/commands/customer-agent.md` skill following the `/pulse` pattern. This enables Statsig MCP (via `mcp-remote`), Paparazzi integration, and scheduled execution.
2. **Fullstory MCP**: Add when official MCP exits beta or set up community server.
3. **Automated Maestro pipeline**: Maestro flows → screenshots → auto-upload for analysis.
4. **Scheduled reports**: Use `/schedule` to run Customer Agent analysis weekly on active projects.
