# Customer Agent — Demo Script (Loom Recording)

**Duration**: ~8-10 minutes
**Test case**: `mobile_next-gen-referrals-v2` flag (referral incentive program experiment)
**Format**: Screen recording of browser only — no CLI, no terminal

---

## Before You Start

### Browser logins required

Make sure you're logged into these in Chrome before recording:

- [ ] **Claude.ai** — [claude.ai](https://claude.ai) (Tilt org account)
- [ ] **FullStory** — [app.fullstory.com](https://app.fullstory.com/ui/o-234FQH-na1/) (org: `o-234FQH-na1`)
- [ ] **StatSig** — [console.statsig.com](https://console.statsig.com/uoZ3ukdQd6mgcenhMwCZG/) (only needed if showing flag config)

### Materials to prepare

- [ ] Pre-captured screenshots of the referral flow (share screen, invite screen, reward confirmation). Save these to a folder you can drag from during the demo.
- [ ] (Recommended) Pre-run the full analysis once in the Claude Project so you have completed outputs to fall back on if the live run is slow or fails.

### Key URLs (bookmark these)

| What | URL |
|------|-----|
| **Customer Agent Claude Project** | https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d |
| **Amplitude — Referral Success Funnel** | https://app.amplitude.com/analytics/empower/chart/3w120rls |
| **Amplitude — New Referral UX Conversion** | https://app.amplitude.com/analytics/empower/chart/yjcgvwwt |
| **Amplitude — Next Gen Referrals Dashboard** | https://app.amplitude.com/analytics/empower/dashboard/wc3wben1 |
| **FullStory** | https://app.fullstory.com/ui/o-234FQH-na1/ |
| **StatSig experiment** | https://console.statsig.com/uoZ3ukdQd6mgcenhMwCZG/experiments/mobile_next-gen-referrals-v2/setup |
| **Slack channel** | https://empower.enterprise.slack.com/archives/C0A2UN3QH7V |

---

## Act 1: The Experiment (~1 minute)

**What to show**: Amplitude chart

**What to do**:
1. Open https://app.amplitude.com/analytics/empower/chart/3w120rls (Referral Success Funnel)
2. Point out the variant breakdown

**What to say**:
> "We're running an experiment on our referral program — flag `mobile_next-gen-referrals-v2`. We're testing different incentive structures to see which one drives the most successful referrals."

**Key data on screen**:

| Variant | What the user gets | Referral Conversion | vs baseline |
|---------|-------------------|-------------------|-------------|
| **FiveForFive** | $5 referrer / $5 referee | 0.095% | baseline |
| **TwentyFiveForFive** | $25 referrer / $5 referee | 0.160% | +68% |
| **ThirtyForZero** | $30 referrer only | 0.226% | +138% |
| **FiftyForZero** | $50 referrer only | 0.289% | +204% |

> "Higher referrer-only rewards dramatically outperform the split model. The $50 variant converts 3x better than the $5-for-$5 split. But *why*? Is it just the dollar amount, or is there something in the UX? That's what the Customer Agent answers."

---

## Act 2: The Customer Agent Project (~1 minute)

**What to do**:
1. Open https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d
2. Show the project page — point out the knowledge files in the sidebar and the MCP connection icons

**What to say**:
> "This is our Customer Agent — a Claude Project that combines quantitative experiment analysis with qualitative UX evaluation. It has 8 knowledge files with our UX research, user archetypes, anti-pattern detection, and competitive analysis. It's connected to Amplitude, Figma, GitHub, Linear, and Slack via MCP."

> "Anyone in the org can use this — PMs, designers, engineers. No CLI, no code. You just open this URL and start a chat."

---

## Act 3: Screenshot Capture (~2 minutes)

### Part A: FullStory — Real User Sessions

**What to do**:
1. Open https://app.fullstory.com/ui/o-234FQH-na1/
2. Click **Search** (top-left, or Cmd+K)
3. Type `referral` and look for referral-related screen navigation events
4. Apply filters → show matching sessions
5. Click a session to open the replay
6. Scrub to the referral share/invite screen
7. Screenshot it (Cmd+Shift+4 on the phone viewport area)

**What to say**:
> "First, we need screenshots of what customers actually see. We go to FullStory and find real user sessions that went through the referral flow."

> "This is a real user going through our referral experience. We can see exactly what they saw — the share screen, the reward messaging, the invite mechanism."

### Part B: Manual Screenshots

**What to say**:
> "For the highest quality evaluation, we also use manually captured screenshots from a real device or emulator. The better the image, the better the feedback."

**What to do**: Show the pre-captured screenshots you prepared before recording.

---

## Act 4: Feed to the Agent (~1 minute)

**What to do**:
1. Go back to the Claude Project: https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d
2. Click the **+** button next to the chat input → **Add files or photos** → select your screenshots (or drag them from Finder into the chat)
3. Type this prompt (or paste it):

```
Deep dive on flag mobile_next-gen-referrals-v2.

Here are screenshots of the referral flow. The experiment tests four incentive structures:
- FiveForFive ($5 for referrer, $5 for referee)
- TwentyFiveForFive ($25 for referrer, $5 for referee)
- ThirtyForZero ($30 for referrer only)
- FiftyForZero ($50 for referrer only)

Evaluate the referral UX and correlate with the experiment data.
```

4. Hit Enter / Send

**What to say**:
> "Now we feed the flag key and screenshots to the Customer Agent. It runs two tracks in parallel — Track A pulls experiment data from Amplitude, cross-references FullStory sessions and GitHub PRs. Track B evaluates the screenshots against our UX research and user archetypes."

**Note**: The analysis may take 2-5 minutes. For a recorded demo, you can either wait or cut to a pre-completed output (see Backup Plan below).

---

## Act 5: The Output — Quantitative Findings (~1 minute)

**What to show**: Scroll to or show the Track A section of the output

**What to say**:
> "Here's what the quantitative analysis found."

**Key points to highlight**:
- Variant breakdown showing the 3x conversion difference
- Clear dose-response: higher incentive = more referrals
- Referrer-only models outperform split models
- FiftyForZero has the highest conversion but smallest sample (20K vs 60K)

> "The data shows a clear winner — higher referrer-only rewards drive significantly more referrals. But the quantitative data alone doesn't explain the UX dynamics. Why does removing the referee reward actually help?"

---

## Act 6: The Output — Qualitative Findings (~1 minute)

**What to show**: Scroll to or show the Track B section of the output

**What to say**:
> "The UX evaluation analyzed the referral flow through the lens of our user archetypes and competitive research."

**Key points to highlight** (expected findings):
- **Messaging clarity**: "Share and get $30" is simpler than "You get $5, your friend gets $5"
- **Archetype analysis**: Crisis archetype (needs money NOW) is most motivated by direct personal reward
- **Friction**: Explaining the split reward adds cognitive load at the share moment
- **Competitive comparison**: How competitor referral programs structure their incentives

> "The UX analysis suggests that simpler, self-interested messaging is more compelling. The user archetypes confirm this — our primary users are motivated by direct financial benefit, not altruistic splits."

---

## Act 7: The Output — Synthesis (~1 minute)

**What to show**: Scroll to or show the synthesis / recommendations section

**What to say**:
> "The synthesis cross-references both tracks into actionable findings."

**Key points to highlight**:
- Cross-referenced finding: "3x conversion lift correlates with simplified, self-interested reward messaging"
- The framing matters as much as the dollar amount — $30-for-referrer outperforms $25+$5 split despite similar total payout
- Ranked recommendations:
  1. **Ship**: Roll out ThirtyForZero or FiftyForZero as the default
  2. **Optimize**: Test messaging independently from amount
  3. **Strategic**: Consider whether referee incentives hurt by adding cognitive load

> "The Customer Agent didn't just confirm that higher rewards work — it explained *why* the referrer-only model wins and surfaced a hypothesis we can test next."

---

## Closing (~30 seconds)

**What to say**:
> "To recap: we started with a Statsig flag key. The Customer Agent pulled experiment data from Amplitude, found real user sessions in FullStory, evaluated the UX against our research frameworks, and produced a unified report with actionable recommendations — all from a single Claude Project in the browser."

> "Any PM, designer, or engineer can do this. No CLI. No code. Just open the project URL, give it a flag key and screenshots, and get a report."

---

## Backup Plan

If the live analysis is slow or fails during recording:

1. **Before recording**: Run the full analysis once and save the output (copy the chat, or screenshot each section)
2. **During recording**: Show yourself typing the prompt and attaching screenshots (this is the "input" part — record it live)
3. **Cut/transition**: Say "After a few minutes of analysis, here's what we get..." and show the pre-saved output
4. This is standard for demo recordings — the audience cares about the input and output, not watching a loading spinner
