# Customer Agent — AI Sprint Progress

> **Sprint**: "Build Customer Agents" (Research workspace)  
> **Dates**: April 2026  
> **Team**: Thomas (orchestration/pipeline), Pawel (UX evaluation agent), Dotan (experiment analysis), Britney (product vision/design)

## Problem Statement

Identify opportunities and issues from a customer POV; improve the happy path, investigate unhappy paths, and ensure corner cases are working; compare to competitors.

## Vision

A user inputs a **Linear project ID** (+ optional Statsig key and Amplitude dashboard) and gets a unified report combining:
- **Track A (Quantitative)**: Experiment performance via Statsig/Amplitude/Fullstory (Dotan's work)
- **Track B (Qualitative)**: UX evaluation of actual screens from the user flow (Pawel's work)
- **Track C (Synthesis)**: De-duplicated, ranked findings with actionable recommendations

The end-user should be able to initiate this from a **Claude Project in the browser**.

---

## What's Been Built

### 1. Pawel's Customer Agent (Claude Project) ✅ Working

A Claude.ai project that evaluates screenshots/Figma links against UX research, cash advance market context, competitor analysis, and user archetypes.

**Knowledge files:**
- `ux-researcher.md`
- `ux-anti-pattern-detection.md`
- `tilt-ca-research-structured.md`
- `tilt-ca-research-raw.md`
- `tilt-archetypes-enriched.md`

**How to use:** Open the Claude Project, paste a screenshot or Figma link, get structured UX feedback.

**Sample conversation:** https://claude.ai/share/5bec78c6-136b-4e2e-a7ce-b07fa32794af

---

### 2. Dotan's Experiment Dashboard ✅ Working

A Claude dashboard that given a Statsig key and access to Statsig, GitHub, Fullstory and Amplitude, produces a report of experiment variant success.

**How it works:** Statsig key → finds associated PRs → finds associated events → cross-evaluates with Fullstory and Amplitude → uses Amplitude results as success metric.

---

### 3. Paparazzi Screenshot Skill ✅ Working

**Location:** `empower-android/.claude/commands/screenshot-screens.md`  
**Branch:** `customer-agent/internal-composables` (committed, not merged)

Discovers `@Preview` functions in Android Compose code, generates temporary Paparazzi tests, renders Composables to PNG headlessly on the JVM. No device or emulator needed.

#### Setup

1. Switch to the branch:
   ```bash
   cd ~/empower/empower-android
   git checkout customer-agent/internal-composables
   ```

2. Paparazzi is already configured (plugin `app.cash.paparazzi` v2.0.0-alpha01 in `build.gradle`).

3. The branch includes 531 `private → internal` Composable visibility changes across 223 files to make content functions accessible from test files.

#### Usage

```bash
# From empower-android directory with Claude Code:
/screenshot-screens                                    # all screens
/screenshot-screens --feature=onboarding               # just onboarding
/screenshot-screens --feature=cashadvance --stitch     # cash advance + montage
/screenshot-screens --list-only                        # just list discoverable screens
/screenshot-screens --max=5                            # limit to 5 screens
```

**Or run manually:**
```bash
./gradlew :empower-app:recordPaparazziDevelopmentDebug \
  --tests "finance.empower.android.app.screenshots.OnboardingScreenshotTest"
```

Screenshots land in `empower-app/src/test/snapshots/images/`.

#### Results

| Feature | Screens Captured | Status |
|---|---|---|
| Onboarding | 10 | ✅ Working |
| Cash Advance | 9 | ✅ Working |
| Other features | — | Not yet attempted |

#### Current Friction

- **Import collisions**: Features with many subpackages (e.g., `cashadvance`) have conflicting type names (`Content`, `ViewContract`, `PaymentAccount`). Requires per-file fully qualified names or per-package test files.
- **Private Composables**: 6 files couldn't be changed from `private → internal` due to private parameter types or overload ambiguity. These screens are skipped.
- **Screens without @Preview**: ~83 files (21%) have no `@Preview` at all — these need manual data construction.
- **Static data only**: Screenshots show Composables with fake/default data, not what real users see (experiments, variants, server-driven content may differ significantly).

#### Files

- Skill: `.claude/commands/screenshot-screens.md`
- Onboarding test: `empower-app/src/test/java/finance/empower/android/app/screenshots/OnboardingScreenshotTest.kt`
- Cash advance test: `empower-app/src/test/java/finance/empower/android/app/screenshots/CashAdvanceScreenshotTest.kt`

---

### 4. Fullstory Chrome Capture Skill ⚠️ Proven, Has Friction

**Location:** `empower-android/.claude/commands/fullstory-capture.md`

Uses `claude --chrome` to navigate Fullstory session replays in the browser, click through the event timeline, and screenshot the replay viewport. Captures what **real users actually see**.

#### Setup

1. Install the [Claude in Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) (v1.0.36+)
2. Log into Fullstory in Chrome (org: `o-234FQH-na1`)
3. Start Claude Code with Chrome integration:
   ```bash
   claude --chrome
   ```

#### Usage

```bash
/fullstory-capture <fullstory-session-url>
/fullstory-capture <url> --events=viewScreen,error --gif
```

**Or manually:** Navigate to a Fullstory session URL, use the event filter (type "view" in the Filter events box), click events to jump to screens, use `zoom` action to crop the app viewport.

#### Results

- Successfully authenticated to Fullstory via existing Chrome login
- Captured cropped screenshots of real user sessions:
  - "What's your number?" (phone entry)
  - "When's your birthday?" (DOB entry)  
  - Home tab (Thrive + Cash Advance sections)
- Exported GIF walkthrough (~18MB, 40 frames) to Downloads

#### Current Friction

- **Replay rendering lag**: Clicking an event in the sidebar doesn't always advance the visible screen immediately. The DOM reconstruction takes time.
- **WebView gaps**: Screens rendered via WebView (subscription page, Plaid bank linking) show "Internal Error: WebView not captured."
- **Chrome extension drops**: The connection between Claude Code and the Chrome extension can disconnect during long sessions. Reconnects by calling `tabs_context_mcp`.
- **No screenshot save-to-disk**: Screenshots live in the conversation only. GIF export is the most reliable way to persist output.
- **Manual scrubbing is faster**: For now, manually scrubbing through Fullstory replays and taking screenshots (Cmd+Shift+4) is more reliable than automated event clicking.

#### Key Fullstory Details

- **Org ID**: `o-234FQH-na1`
- **Segment for onboarding**: "Mobile Onboarding Direct to Cash iOS v10" (838 users)
  - URL: `https://app.fullstory.com/ui/o-234FQH-na1/segments/M5u7EFTpahTs/people:search`
- **No screenshot API**: All replay URLs require browser authentication. No programmatic screenshot endpoint exists.
- **Community MCP**: `creevey-equals/fullstory-mcp` — has `list_sessions`, `get_session_events`, `get_session_summary` tools (not yet configured)

---

### 5. Paparazzi/Figma Visual Validation Reference (PR #5925)

**PR**: https://github.com/empowerfinance/empower-android/pull/5925

A `/validate-compose-figma` skill (by Brijesh, separate from this sprint) that renders Composables headlessly via Paparazzi, compares against a Figma design screenshot, and self-corrects the code until they match. Referenced as inspiration for our Paparazzi integration.

---

### 6. Sprint Architecture Plan 📋 Drafted

**Location:** `/Users/thomasq/.claude/plans/tender-swimming-donut.md`

Detailed plan for the unified Claude Project including MCP connections, knowledge files, orchestration workflow, report template, and 5-day sprint schedule.

---

### 7. Maestro Emulator Screenshot Capture ⚠️ Proven, Needs Test Account Infrastructure

**Installed**: Maestro 2.4.0 (`~/.maestro/bin/maestro`)
**Emulator**: `emulator-5554` running `finance.empower.development`
**Flows**: `~/empower/customer-agent/maestro/flows/capture-screens.yaml`
**Screenshots**: `~/empower/customer-agent/maestro/screenshots/` (10 PNGs, 1080x2400, ~1.1MB total)

#### What It Captures

| # | Screen | File | Status |
|---|--------|------|--------|
| 01 | More/Profile tab | `01-more-profile.png` | Good |
| 02 | Account details (sub-screen) | `02-account.png` | Good |
| 03 | Personal info (sub-screen) | `03-personal.png` | Good |
| 04 | Support (sub-screen) | `04-support.png` | Suspect — may show Plaid OAuth page from failed run |
| 05 | Home/Accounts tab | `05-accounts-home.png` | Good |
| 05b | Home scrolled | `05b-accounts-home-scrolled.png` | Good |
| 06 | Analysis tab | `06-analysis.png` | Good |
| 06b | Analysis scrolled | `06b-analysis-scrolled.png` | Good |
| 07 | More tab (re-captured) | `07-more.png` | Good |
| 08 | Home final | `08-home-final.png` | Good |

#### What Works

- **Full-resolution real screenshots**: 1080x2400 PNG with actual server data, experiment variants, and real account state — huge upgrade over Paparazzi's static fake data
- **Repeatable YAML flows**: Once a flow works, `maestro --device emulator-5554 test flow.yaml` runs it in one command
- **`adb screencap` fallback**: `adb -s emulator-5554 exec-out screencap -p > screenshot.png` works for single ad-hoc captures
- **UI inspection**: `adb exec-out uiautomator dump` provides resource IDs, text, content-desc for building selectors

#### Friction Points

1. **Server-driven modals break flows**: "New account available" (Wells Fargo institution refresh) appeared unpredictably and blocked all navigation. Had to dismiss manually between runs.
2. **Lock screen after app restart**: App requires 6-digit passcode (`111111`) after backgrounding. Can't easily skip in flows.
3. **Plaid/WebView navigation**: Tapping "Support" opened a Plaid OAuth WebView that Maestro can't drive. Had to `KEYCODE_BACK` out, which sometimes exited the app entirely.
4. **Element selectors are fragile**: Resource IDs like `navigation_home` weren't available on sub-screens (only on the main HomeActivity). Content descriptions varied.
5. **No scroll intelligence**: `scroll` just scrolls once — no way to know if content extends further or if you've reached the bottom.
6. **Three separate runs required**: Flow 1 got 2 screenshots before "Personal" wasn't found. Flow 2 got 4 before navigation_home failed (modal appeared). Flow 3 got 6. Total: 10 screenshots from 3 attempts.

#### Coverage Gaps

Not yet captured (would need dedicated flows + correct account state):
- Onboarding flow (needs unregistered phone number)
- Cash Advance flow (needs CA-eligible account with no active advance)
- Thrive / Credit card screens (needs active subscription/card)
- Transaction details, spending breakdown
- Settings, billing, legal
- Any error/empty states

#### Recommended: Dedicated Maestro Test Accounts

The single biggest unlock for reliable Maestro automation is **backend-configured test accounts** with stable, predictable state:

| Account | Purpose | Requirements |
|---------|---------|-------------|
| `maestro-home` | Clean happy path | Funded, no pending modals, no institution refresh prompts, passcode disabled |
| `maestro-cash-advance` | CA flow capture | CA eligible ($200-400), no active advance, Plaid sandbox bank |
| `maestro-thrive` | Thrive/credit screens | Active Thrive subscription, credit card active with transactions |
| `maestro-onboarding` | Full onboarding | New phone number per run (or reset-able test account) |
| `maestro-delinquent` | Unhappy paths | Missed payment, overdue balance, restricted features |
| `maestro-empty` | Empty states | Funded but no features activated |

Each account should: use Plaid sandbox institutions (never expire), be excluded from Statsig experiments, have passcode disabled, and never trigger server-driven modals.

#### Pipeline Script

A Python script was created at `~/empower/customer-agent/pipeline/customer-agent-pipeline.py` to automate feeding screenshots to Claude for UX evaluation. Requires `ANTHROPIC_API_KEY` (not available on enterprise accounts). Alternative: manually upload screenshots to Pawel's Claude Project ("Product Design Agent (UI & UX)" at `https://claude.ai/project/019d40c9-7310-77e3-86fc-236d769dfb99`).

---

## Screenshot Strategy Comparison

### 1. Manual Screenshots (highest quality input, no dependencies)

Take screenshots directly from a real device, simulator, or emulator. Produces the highest-quality images, which means the best UX feedback from the agent. Best for demos and ad-hoc evaluation.

### 2. Fullstory Session Replays (real user data, in-browser)

Navigate to FullStory session replays in Chrome and capture what actual customers experienced. Can be manual (scrub + Cmd+Shift+4) or automated via Claude Chrome extension (`/fullstory-capture`). Best for seeing real user interactions from the actual user base.

**Current state**: Proven concept. Some friction (replay rendering lag, WebView gaps, extension disconnects) but works for targeted captures.

### 3. Explored: Maestro & Paparazzi (future automation, requires Android repo)

Both require `empower-android` on branch `customer-agent/internal-composables` + CLI tooling.

| Approach | What You See | Status |
|---|---|---|
| **Maestro** | Live emulator with real server data | 10 screenshots captured; needs dedicated test accounts to be reliable |
| **Paparazzi** | Static Composables with fake data | 19 screens captured (onboarding + cash advance); no device needed |

More engineering work needed to make these fully automated and hands-off. See sections 3 and 7 above for detailed findings.

---

## What's Missing

### High Priority (for hackathon demo)
- [x] **Maestro exploration**: Installed, connected to emulator, captured 10 screenshots across 3 tabs + sub-screens
- [ ] **Demo the Fullstory → Claude Project flow**: Fullstory session replay → screenshot key screens → upload to Pawel's Claude Project → get UX evaluation (this is the default/recommended approach — all in-browser, no CLI)
- [ ] **Unified report template**: Combine quant (Dotan) + qual (Pawel) into one output
- [ ] **Competitor comparison**: Screenshot Dave/Earnin/Brigit flows, feed alongside Tilt screenshots for comparative analysis

### Medium Priority
- [ ] **Fullstory MCP setup**: Configure `creevey-equals/fullstory-mcp` for session discovery
- [ ] **Figma design comparison**: Use Figma MCP to compare intended design vs actual screenshots
- [ ] **Archetype inference layer**: Optional enrichment using Amplitude user properties (age, hasCashAccount, returning_user flags)
- [ ] **Claude Project integration**: Set up the unified Claude Project with all MCP connections

### Lower Priority / Post-Sprint
- [ ] **Dedicated Maestro test accounts**: Backend-configured accounts that eliminate modal/auth/state friction (see Maestro section 7)
- [ ] **Paparazzi for all features**: Generate screenshots for loans, credit card, line of credit, banking
- [ ] **Scheduled reports**: Periodic Customer Agent analysis on active Linear projects
- [ ] **iOS coverage**: iOS Simulator via Maestro for parity

---

## Amplitude Reference

**Project ID**: `152808` (Empower production)

### Key Events for Onboarding Flow
```
viewLandingPage → viewLandingCarouselScreen → signup_options → 
appOnboardingStarted → viewOnboardingPhoneEntryScreen → 
viewOnboardingNameEntryScreen → viewOnboardingEmailEntryScreen → 
viewOnboardingBirthdayEntryScreen → viewOnboardingAddressInputScreen → 
viewOnboardingSurveyScreen → viewOnboardingAccountSetup → 
NuxOnboardingOffersReturned → viewOnboardingTrialExplainerScreen → 
paintedDoorSubscribe → viewHomeTab
```

### Key Events for Cash Advance Flow
```
viewCashAdvanceAmountExplainer → viewPaycheckAccountSelectionScreen → 
viewCashAdvanceOfferSelectionScreen → viewCashAdvanceOfferSelection
```

### User Properties for Archetype Inference
- `age`, `birthDate`
- `hasCashAccount`, `hasFundedAccount2019`
- `cash_advance_400_max_enabled`
- `ViewedSubscriptionPageNewSub` / `ViewedSubscriptionPageReSub`
- `returning_user_subscription_screen_enabled`
- `payroll_cash_advance_eligible_enabled`

---

## Google Drive

Shared folder for screenshots and outputs:
https://drive.google.com/drive/folders/195aWeXklTh1IbSoK-orNKmeXhCSsexgC

---

## How to Resume This Work

### Default: Fullstory → Claude Project (no CLI needed)

1. Open [Fullstory](https://app.fullstory.com/ui/o-234FQH-na1/) — find a session replay
2. Scrub to key screens, Cmd+Shift+4 to screenshot each one
3. Open [Pawel's Claude Project](https://claude.ai/project/019d40c9-7310-77e3-86fc-236d769dfb99)
4. Drag screenshots into chat + paste evaluation prompt
5. Get structured UX feedback

### CLI alternatives

```bash
# All non-Android artifacts are in the customer-agent repo:
cd ~/empower/customer-agent

# Fullstory capture with Claude Chrome automation:
claude --chrome
# Then: /fullstory-capture <session-url>

# Maestro (emulator-based):
export PATH="$PATH:$HOME/.maestro/bin"
adb devices  # Verify emulator is running
maestro --device emulator-5554 test ~/empower/customer-agent/maestro/flows/capture-screens.yaml

# Paparazzi (headless Composable rendering):
cd ~/empower/empower-android
git checkout customer-agent/internal-composables
# Then: /customer-agent-capture <LINEAR-ID> or /screenshot-screens
```
