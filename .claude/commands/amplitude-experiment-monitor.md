---
name: amplitude-experiment-monitor
description: Monitor iOS and Android A/B experiments in Amplitude. Use this skill whenever the user shares an Amplitude experiment URL, chart URL, or asks to monitor, summarize, analyze, or check the results of an experiment or A/B test. Also trigger when the user mentions experiment metrics like conversion rate, lift, significance, control vs variant, or flags like drops or errors in an experiment context.
argument-hint: "<linear-ticket-url or amplitude-url> [#slack-channel]"
---

# Amplitude Experiment Monitor

Analyzes an Amplitude experiment or chart and returns a Slack-ready summary covering conversion rates, statistical significance, errors, and variant drops.

## Prerequisites

The user must have the following MCP connectors enabled (check with `/mcp`):
- **Amplitude** — for querying charts and experiments
- **Linear** — for reading ticket context (optional, only if a Linear URL is provided)
- **Slack** — for posting reports (optional, only if a Slack channel is specified)

## Step-by-Step Workflow

### 0. Parse Arguments

The user provides input via `$ARGUMENTS`. Expected formats:
- A Linear ticket URL (e.g., `https://linear.app/empower/issue/SUBEX-181/...`)
- An Amplitude URL (chart, experiment, or dashboard)
- Optionally a Slack channel to post results to (e.g., `#channel-name`)

If `$ARGUMENTS` is empty or missing, ask the user:
> "Please provide an Amplitude experiment/chart URL or a Linear ticket URL. Optionally include a Slack channel to post results to (e.g., `#alerts`)."

### 1. Parse the URL

Extract identifiers from the provided URL:
- **Chart URL**: contains `/chart/` → extract chart ID
- **Experiment URL**: contains `/experiment/` → extract experiment key/ID
- **Dashboard URL**: contains `/dashboard/` → extract dashboard ID

### 2. Fetch the Data

Use the appropriate Amplitude MCP tool based on what was detected:

- For experiment URLs → use `get_experiments` with the experiment ID/key
- For chart URLs → use `get_charts` to retrieve the chart, then `query_charts` to get the underlying data
- If unsure, try `get_context` first to understand what the URL points to

Retrieve data for **both iOS and Android** if the experiment runs on both platforms. Check if the experiment is segmented by platform and fetch each segment if needed.

### 3. Extract Key Metrics

From the fetched data, extract for **control** and **each variant**:

- Number of users (exposure count)
- Number of conversions / events
- Conversion rate (%)
- p-value or confidence level (if available)
- Any error or exception events

If the data has multiple metrics or funnel steps, capture each step separately.

---

## Analysis Rules

### Conversion Rate
- Calculate: `conversions / users * 100`
- Report for control and each variant
- Include absolute numbers when available

### Delta Calculation
- **Absolute delta**: `variant_rate - control_rate` (in percentage points)
- **Relative lift**: `(variant_rate - control_rate) / control_rate * 100`
- **Guard**: If `control_rate` is 0, report lift as "N/A (control has 0% conversion)" instead of computing a division. Do not report a percentage lift in this case.
- Round to 2 decimal places

### Statistical Significance
- If Amplitude provides a p-value or confidence level, use it directly.
- **If Amplitude does NOT provide significance data, compute it yourself** using a two-proportion z-test:
  1. Let `p1 = control_conversions / control_users`, `p2 = variant_conversions / variant_users`
  2. Pooled proportion: `p = (control_conversions + variant_conversions) / (control_users + variant_users)`
  3. **Guard**: If `p` is 0 or 1, or if either group has 0 users, skip the z-test and report: "⚠️ Insufficient data to compute significance"
  4. Standard error: `SE = sqrt(p * (1 - p) * (1/control_users + 1/variant_users))`
  5. **Guard**: If `SE` is 0, report: "⚠️ Insufficient data to compute significance" (do not divide by zero)
  6. Z-score: `z = (p2 - p1) / SE`
  7. Interpret: |z| > 1.96 → significant at 95% CI; |z| > 2.58 → significant at 99% CI
- Report as: "✅ Significant (z = X.XX, p < 0.01)" or "⚠️ Not sig (z = X.XX)"
- **Never carry forward a significance label from prior findings** — always compute from the current data.

### Unexpected Errors
- Flag any error events, crash rates, or exception spikes
- Flag if a metric value looks broken (e.g., 0% conversion across the board, null values, sample size mismatch)
- Flag instrumentation issues (e.g., variant has far fewer users than expected)

### Drops in Variant
- Flag any metric/funnel step where variant performs **>10% relatively worse** than control
- Formula: `(control_rate - variant_rate) / control_rate > 0.10`
- **Guard**: If `control_rate` is 0, skip the drop check for that step and note "N/A (control baseline is 0%)"

---

## Output Format

Format the output as a **Slack-ready message** using the structure below. Use emoji for quick scanning. Keep it concise — this will be posted directly to Slack.

**Important Slack formatting rules (via Slack MCP tool):**
- The Slack MCP tool uses **standard markdown**, NOT Slack mrkdwn. Use `**text**` (double asterisks) for bold, NOT `*text*` (single asterisks, which renders as italic).
- Bold all key numbers so they stand out: conversion rates, lift percentages, percentage point deltas, and user counts.
- Do NOT use `---` horizontal rules — Slack doesn't render them and they cause formatting errors.
- Use blank lines between sections for visual separation instead.
- Avoid special unicode characters like `→` or `•` in links — use plain ASCII alternatives if needed.

```
📊 **AutoSave Upsell Experiments - Monitoring Update ([Date])**

**1. [Experiment Name] ([Ticket ID])** - [Running/Completed]
Platform: [Platform] | Since [start date] | [Chart]([chart_url])

👥 Control: **[N] users** | Enabled: **[N] users**

📈 **End-to-end conversion ([first step] to [last step]):**
- Control: **[X]%** ([conversions]/[users])
- Enabled: **[X]%** ([conversions]/[users]) -- **+[X] pp** | **+[X]% lift** [✅ Significant | ⚠️ Not sig]

**Funnel breakdown:**
- [Step A] to [Step B]: Control **[X]%** vs Enabled **[X]%** (**+[X]% lift**)
- [Step B] to [Step C]: Control **[X]%** vs Enabled **[X]%** (**+[X]% lift**)
- [Step C] to [Step D]: Control **[X]%** vs Enabled **[X]%** (flat)

⚠️ **Drops:** ✅ None detected
🚨 **Errors:** ✅ None
🛡️ **Guardrail ([metric name]):** ✅ Healthy | ⚠️ [description]

[Repeat for each experiment]

💡 **Summary:** [2-3 sentence plain-English summary: is the experiment winning, losing, or inconclusive? Call out the key lift number in bold. Any action recommended?]
```

---

## Edge Cases

- **Multiple variants**: Repeat the delta and significance rows for each variant (B, C, etc.)
- **Multiple platforms with different results**: Show iOS and Android separately if the results diverge meaningfully
- **Funnel experiments**: Report each funnel step as a separate metric row under Conversion Rates
- **No significance data**: Note it clearly rather than guessing
- **Experiment not found**: Tell the user the URL didn't resolve to a recognizable experiment or chart and ask them to double-check it
- **Slack MCP fallback**: If the Slack MCP is absent, unavailable, or misconfigured, do **not** try to find an alternate way to post to Slack. Instead, print the full summary to the terminal and play a chime (`afplay /System/Library/Sounds/Glass.aiff`) to notify the user. Note: `afplay` is macOS-only — on non-macOS machines, skip the chime and just print to the terminal.

$ARGUMENTS
