# Customer Agent — Demo Script (Loom Recording)

**Duration**: ~8-10 minutes
**Test case**: `mobile_next-gen-referrals-v2` flag (referral incentive program experiment)
**Format**: Screen recording of browser only — no CLI, no terminal

---

## Pre-Recording Checklist

- [ ] Claude Project set up with all 8 knowledge files from `knowledge/`
- [ ] Skills installed: `flag-deep-dive.skill`, `flag-ux-synthesis-3.skill`
- [ ] MCP connections enabled: Amplitude, Figma, GitHub, Linear, Slack
- [ ] Logged into Chrome: StatSig, FullStory, GitHub
- [ ] Pre-captured screenshots of the referral flow (share screen, invite screen, reward confirmation)
- [ ] Pre-run Track A and Track B outputs saved (in case live run fails)
- [ ] FullStory: find sessions where users go through the referral flow (search "ReferralCreated" or referral screens)

---

## Act 1: The Experiment (~1 minute)

**What to show**: Amplitude dashboard / charts

**Script**:
> "We're running an experiment on our referral program — flag `mobile_next-gen-referrals-v2`. We're testing different incentive structures to see which one drives the most successful referrals. Let me show you what we're seeing in Amplitude."

**Action**: Open the Amplitude charts:
- Referral Success Funnel (`3w120rls`)
- New Referral UX Conversion (`yjcgvwwt`)
- Next Gen Referrals dashboard (`wc3wben1`)

**Key data to highlight**:

| Variant | Users | Referral Conversion | Relative to baseline |
|---------|-------|-------------------|---------------------|
| **FiveForFive** ($5/$5 split) | 61,108 | 0.095% | baseline |
| **TwentyFiveForFive** ($25/$5) | 60,772 | 0.160% | +68% |
| **ThirtyForZero** ($30 referrer only) | 60,697 | 0.226% | +138% |
| **FiftyForZero** ($50 referrer only) | 20,095 | 0.289% | +204% |

> "There's a clear signal here — higher referrer-only rewards dramatically outperform the split reward model. The $50-for-referrer variant converts 3x better than the $5-for-$5 split. But *why* does the referrer-only model work so much better? Is it just the dollar amount, or is there something in the UX that amplifies or diminishes the incentive? That's what the Customer Agent answers."

---

## Act 2: The Customer Agent Project (~1 minute)

**What to show**: The Claude Project on claude.ai

**Script**:
> "This is our Customer Agent — a Claude Project that combines quantitative experiment analysis with qualitative UX evaluation. It has access to our UX research, user archetypes, anti-pattern detection frameworks, and competitive analysis through these knowledge files."

**Action**: Show the project page with:
- 8 knowledge files visible in the sidebar
- MCP connections (Amplitude, Figma, GitHub, Slack, Linear icons)
- Mention the two skills (flag-deep-dive for quant, flag-ux-synthesis for the orchestrator)

> "It's connected to Amplitude, Figma, GitHub, Linear, and Slack via MCP. Anyone in the org can use this — PMs, designers, engineers. No CLI, no code."

---

## Act 3: Screenshot Capture (~2 minutes)

### Part A: FullStory — Real User Sessions

**What to show**: FullStory session replay in Chrome

**Script**:
> "First, we need screenshots of what customers actually see in the referral flow. We go to FullStory and find real user sessions."

**Action**:
1. Open FullStory (already logged in)
2. Search for the referral screen activity or "ReferralCreated" event
3. Apply filters — show matching sessions
4. Click into a session replay showing the referral flow

> "This is a real user going through our referral flow. We can see exactly what they experienced — the share screen, the invite mechanism, and the reward messaging."

**Action**: Scrub through the session, screenshot 2-3 key screens (the share screen, the invite/reward screen)

### Part B: Manual Screenshots (highest quality)

**Script**:
> "For the highest quality evaluation, we also use manually captured screenshots. The better the image quality, the better the UX feedback from the agent."

**Action**: Show pre-captured clean screenshots of the referral flow variants

---

## Act 4: Feed to the Agent (~1 minute)

**What to show**: Claude Project chat

**Script**:
> "Now we feed the flag key and screenshots to the Customer Agent. It runs two tracks in parallel."

**Action**: Type the prompt into the Claude Project:

```
Deep dive on flag mobile_next-gen-referrals-v2.

Here are screenshots of the referral flow. The experiment tests four incentive structures:
- FiveForFive ($5 for referrer, $5 for referee)
- TwentyFiveForFive ($25 for referrer, $5 for referee)
- ThirtyForZero ($30 for referrer only)
- FiftyForZero ($50 for referrer only)

Evaluate the referral UX and correlate with the experiment data.

[attach screenshots]
```

> "Track A pulls the experiment data from Amplitude — referral creation rates, successful conversion rates, variant performance — and cross-references with FullStory sessions and GitHub PRs."

> "Track B evaluates the screenshots against our UX research, user archetypes, and competitive analysis — how does our referral experience compare to Dave, Earnin, and Brigit?"

**Note**: If running live, wait for the analysis. If pre-recorded, cut to the completed output.

---

## Act 5: The Output — Quantitative Findings (~1 minute)

**What to show**: Track A output (flag-deep-dive results)

**Script**:
> "Here's what the quantitative analysis found."

**Key points to highlight**:
- Variant breakdown showing the 3x conversion difference
- Clear dose-response: higher incentive = more referrals
- Referrer-only models (ThirtyForZero, FiftyForZero) outperform split models
- FiftyForZero has the highest conversion but smallest sample (20K vs 60K)
- FullStory session links showing how users interact with the referral share screen

> "The data shows a clear winner — higher referrer-only rewards drive significantly more referrals. But the quantitative data alone doesn't explain the UX dynamics. Why does removing the referee reward actually help?"

---

## Act 6: The Output — Qualitative Findings (~1 minute)

**What to show**: Track B output (UX evaluation results)

**Script**:
> "The UX evaluation analyzed the referral flow through the lens of our user archetypes and competitive research."

**Key points to highlight** (expected findings):
- **Messaging clarity**: Referrer-only rewards are simpler to communicate — "Share and get $30" vs "You get $5, your friend gets $5"
- **Archetype analysis**: The Crisis archetype (needs money NOW) is most motivated by direct personal reward, not altruistic split
- **Friction in the share flow**: Any complexity in explaining the split reward reduces share intent
- **Competitive comparison**: How competitor referral programs structure their incentives
- Simulated app store sentiment around the referral experience

> "The UX analysis suggests that simpler, self-interested messaging ('Get $30 when you refer a friend') is more compelling than the altruistic split ('You both get $5'). The user archetypes confirm this — our primary users are motivated by direct financial benefit."

---

## Act 7: The Output — Synthesis (~1 minute)

**What to show**: Track C output (unified report)

**Script**:
> "The synthesis cross-references both tracks into actionable findings."

**Key points to highlight**:
- Cross-referenced finding: "3x conversion lift correlates with simplified, self-interested reward messaging"
- The dollar amount matters, but the framing matters too — $30-for-referrer outperforms $25+$5 split despite being a similar total payout
- Ranked recommendations:
  1. **Ship**: Roll out ThirtyForZero or FiftyForZero as the default referral program
  2. **Optimize**: Test the messaging independently from the amount — is "$25 for you" better than "$25 for you + $5 for your friend" at the same referrer payout?
  3. **Strategic**: Consider whether referee incentives hurt by adding cognitive load to the share moment

> "The Customer Agent didn't just confirm that higher rewards work — it explained *why* the referrer-only model wins and surfaced a hypothesis we can test next: that the complexity of split rewards actually reduces share intent, independent of the dollar amount."

---

## Closing (~30 seconds)

**Script**:
> "To recap: we started with a Statsig flag key. The Customer Agent pulled experiment data from Amplitude, found real user sessions in FullStory, evaluated the UX against our research frameworks, and produced a unified report with actionable recommendations — all from a single Claude Project in the browser."

> "Any PM, designer, or engineer can do this. No CLI. No code. Just a flag key and screenshots."

> "We also explored automated screenshot capture through Maestro and Paparazzi for future CI integration, but the core flow works today with manual screenshots or FullStory session replays."

---

## Backup Plan

If the live analysis fails or takes too long during recording:

1. **Pre-run all three tracks** before recording and save the outputs
2. **Screen record the input** (typing the prompt, attaching screenshots) live
3. **Cut to the pre-recorded outputs** with narration: "After a few minutes of analysis, here's what we get..."
4. This is standard practice for demo recordings — the audience cares about the output, not watching a spinner

## Key URLs for the Demo

- **Claude Project**: https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d
- **Amplitude — Referral Success Funnel**: https://app.amplitude.com/analytics/empower/chart/3w120rls
- **Amplitude — New Referral UX Conversion**: https://app.amplitude.com/analytics/empower/chart/yjcgvwwt
- **Amplitude — Next Gen Referrals Dashboard**: https://app.amplitude.com/analytics/empower/dashboard/wc3wben1
- **StatSig flag**: `mobile_next-gen-referrals-v2`
- **StatSig console**: https://console.statsig.com/uoZ3ukdQd6mgcenhMwCZG/experiments/mobile_next-gen-referrals-v2/setup
- **Slack channel**: https://empower.enterprise.slack.com/archives/C0A2UN3QH7V
