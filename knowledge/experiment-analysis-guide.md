# Experiment Analysis Guide

Statistical methodology and output format for quantitative experiment analysis. Use this as a reference when computing significance, deltas, and interpreting experiment results.

---

## Conversion Rate

```
rate = conversions / users * 100
```

Report for control and each variant with absolute numbers.

## Delta Calculation

- **Absolute delta**: `variant_rate - control_rate` (in percentage points, "pp")
- **Relative lift**: `(variant_rate - control_rate) / control_rate * 100` (as "%")
- **Guard**: If `control_rate` is 0, report lift as "N/A (control has 0% conversion)" — do not divide by zero
- Round to 2 decimal places

## Statistical Significance (Two-Proportion Z-Test)

Use this when Amplitude does not provide p-values or confidence levels.

1. Let `p1 = control_conversions / control_users`, `p2 = variant_conversions / variant_users`
2. Pooled proportion: `p = (control_conversions + variant_conversions) / (control_users + variant_users)`
3. **Guard**: If `p` is 0 or 1, or if either group has 0 users → "Insufficient data"
4. Standard error: `SE = sqrt(p * (1 - p) * (1/control_users + 1/variant_users))`
5. **Guard**: If `SE` is 0 → "Insufficient data"
6. Z-score: `z = (p2 - p1) / SE`
7. Interpret:
   - |z| > 2.58 → significant at 99% CI → "✅ Significant (z = X.XX, p < 0.01)"
   - |z| > 1.96 → significant at 95% CI → "✅ Significant (z = X.XX, p < 0.05)"
   - |z| ≤ 1.96 → "⚠️ Not significant (z = X.XX)"

**Never carry forward significance labels from prior analysis** — always compute fresh from current data.

## Drop Detection

Flag any metric where variant performs >10% relatively worse than control:

```
(control_rate - variant_rate) / control_rate > 0.10
```

**Guard**: If `control_rate` is 0, skip and note "N/A (control baseline is 0%)"

## Error Flagging

Flag:
- 0% conversion across all variants (possible instrumentation issue)
- Variant with far fewer users than expected given allocation split
- Null values or sample size mismatches
- Error/exception event spikes correlated with the experiment

## Variant Breakdown Table Format

Build a table for each funnel step and key metric:

| Variant | Users | Conversions | Rate | Delta (pp) | Lift (%) | Significance | Drops |
|---------|-------|-------------|------|-----------|----------|-------------|-------|
| Control | N | N | X.X% | — | — | — | — |
| variantA | N | N | X.X% | +X.X | +X.X% | ✅/⚠️ (z=X.XX) | ✅/🔴 |

## Slack Summary Format

```
📊 **[Experiment Name] — Analysis ([Date])**

**Experiment:** `[flag-key]` | **Status:** [Running/Not Started/etc.]
**Platform:** [iOS/Android/Both] | **Since:** [start date]

👥 **Exposure:** Control **[N] users** | [VariantA] **[N] users**

📈 **[Primary Metric]:**
• Control: **[X]%** ([conversions]/[users])
• [VariantA]: **[X]%** ([conversions]/[users]) → **+[X] pp** | **+[X]% lift** [✅ Significant | ⚠️ Not sig]

⚠️ **Drops:** [✅ None | 🔴 description]
🚨 **Errors:** [✅ None | 🔴 description]

💡 **Summary:** [2-3 sentences]
```

**Slack formatting rules:**
- Use `**text**` for bold (standard markdown)
- Do NOT use `---` horizontal rules
- Bold all key numbers
- Use blank lines between sections
