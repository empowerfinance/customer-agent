# Customer Agent Report Template

Use this template for the unified report output. Adapt content to what was actually found — omit sections with nothing to say. Lead with the most actionable finding, not the methodology.

---

## Template

```markdown
# Customer Agent Report: [Project/Feature Name]

**Date**: [date]
**Linear**: [issue ID + link]
**Experiment**: `[flag key]`
**Platform**: [iOS/Android/Both]
**Amplitude**: [dashboard or chart link]
**Screenshots**: [N] screens analyzed

---

## Executive Summary

[2-3 sentences: overall health of the feature/experiment, biggest finding, recommended action. Lead with the conclusion — "The variant is winning by +X pp on the primary metric, but has a significant drop at [step] that affects [archetype] users. Recommend fixing [specific issue] before rolling out to 100%."]

---

## Integrated Findings (High Confidence)

[These are the most valuable findings — where quantitative data and qualitative UX analysis converge on the same issue. List them first because they're the most actionable.]

| Priority | Finding | Quant Evidence | Qual Evidence | Recommended Fix |
|----------|---------|---------------|---------------|-----------------|
| P0 | [Finding] | [Data: X% drop at step Y] | [UX: anti-pattern Z on screen W] | [Specific fix] |
| P1 | ... | ... | ... | ... |

---

## Quantitative Findings

### Experiment Performance

| Variant | Users | Conversion | Delta (pp) | Lift (%) | Significance |
|---------|-------|-----------|-----------|----------|-------------|
| Control | N | X.X% | — | — | — |
| VariantA | N | X.X% | +X.X | +X.X% | ✅/⚠️ (z=X.XX) |

### Funnel Analysis

| Step | Control | Variant | Delta | Drop? |
|------|---------|---------|-------|-------|
| [Step 1] → [Step 2] | X.X% | X.X% | +X.X pp | ✅/🔴 |
| [Step 2] → [Step 3] | X.X% | X.X% | -X.X pp | 🔴 |

**Biggest drop-off**: [Step N] → [Step N+1] — [X]% of users lost here.

### Session Replay Insights

[If available — behavioral patterns from Amplitude session replays or FullStory]
- [Pattern 1]: [description + link to session]
- [Pattern 2]: [description + link to session]

---

## Qualitative Findings

### UX Evaluation by Screen

[For each screen analyzed:]

#### Screen: [Screen Name]
- **Flow step**: [which step in the user journey]
- **Key elements**: [CTAs, forms, copy, loading states]
- **Anti-patterns detected**: [specific issues from the 13 categories]
- **Archetype impact**: [which user types are most affected and why]
- **Copy notes**: [framing mismatches, trust issues, CTA clarity]
- **User voice**: *"[1-2 sentence reaction a real user might have, grounded in research]"*

### Archetype Analysis

[Only include if data shows >5pp differential between user segments]

| Archetype | Impact | Key Issue |
|-----------|--------|-----------|
| Crisis | [High/Medium/Low] | [Specific issue for this user type] |
| Liquidity Stabilizer | [High/Medium/Low] | [Specific issue] |
| Strategic Optimizer | [High/Medium/Low] | [Specific issue] |

### Competitive Gaps

[Where competitors handle similar moments better, with specifics]
- [Competitor]: [What they do differently + why it matters]

---

## Recommendations

| Priority | Action | Owner | Evidence |
|----------|--------|-------|----------|
| P0 | [Specific action] | [Engineering/Design/PM] | [Finding reference] |
| P1 | [Specific action] | [Owner] | [Finding reference] |
| P2 | [Specific action] | [Owner] | [Finding reference] |

---

## Appendix

- **Amplitude charts**: [links to charts/dashboards created during analysis]
- **Figma frames**: [links to design files analyzed]
- **Session replays**: [links to notable sessions]
- **Screens analyzed**: [list of PNGs with source files]
- **Screens not captured**: [list of screens that were skipped and why]
```

---

## Formatting Rules

1. **Lead with integrated findings** — these are where quant + qual converge and are the most actionable
2. **Be specific, not generic** — "the fee disclosure is below the fold on iPhone SE" not "the screen is confusing"
3. **Omit empty sections** — if no session replays, don't include the section
4. **Archetype analysis is earned** — only include when data shows >5pp differential
5. **User voice reactions** must be grounded in the Tilt user research, not invented
6. **Copy notes are exploratory** — label them as such
7. **Include links** — every Amplitude chart, Figma frame, and session replay should be clickable
