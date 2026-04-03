---
description: Resolve a Linear issue to its feature flag, discover the Android screens it gates, and capture screenshots — packaged for the Customer Agent Claude Project.
argument-hint: "<LINEAR-ID> [--flag=<KEY_CONSTANT>] [--feature=<package-substring>] [--capture=<method>] [--amplitude-url=<url>] [--stitch]"
---

## User Input

```text
$ARGUMENTS
```

Parse arguments:

| Argument | Default | Description |
|---|---|---|
| First positional arg | _(required unless --flag provided)_ | Linear issue ID (e.g., `SUBEX-16`, `THR-1540`, `MOB-474`) |
| `--flag=<KEY_CONSTANT>` | _(auto-resolved)_ | Skip resolution — use this ExperimentConfig constant directly |
| `--feature=<substring>` | _(auto-discovered)_ | Skip discovery — target screens in packages matching this substring |
| `--capture=<method>` | `paparazzi` | Screenshot capture method: `paparazzi`, `maestro`, `fullstory`, or `manual` |
| `--amplitude-url=<url>` | _(none)_ | Include this Amplitude chart/experiment URL in the manifest for Phase 2 |
| `--stitch` | `false` | Combine all PNGs into a single montage image |

---

## Overview

This skill is **Phase 1** of the Customer Agent pipeline. It has two concerns:

1. **Resolution & Discovery** (Steps 1–3): Linear ID → flag key → feature package → screen list. This is stable.
2. **Screenshot Capture** (Step 4): Pluggable — currently supports Paparazzi, Maestro, or manual. This is the part under active development.

```
Linear ID → Flag Key → Feature Package → Screen List → [capture method] → PNGs + Manifest
```

The output is a capture package (PNGs + manifest) that the user uploads to the **Customer Agent Claude Project** (on claude.ai) for unified quantitative + qualitative analysis.

---

# PART A: Resolution & Discovery (Stable)

These steps are the same regardless of capture method.

## Step 1 — Validate Environment

1. **Android repo dependency**: This command requires `~/empower/empower-android` on branch `customer-agent/internal-composables`. Check that `~/empower/empower-android/empower-app/build.gradle` exists. If not, stop and tell the user: "This command requires ~/empower/empower-android on branch customer-agent/internal-composables."
   Then `cd ~/empower/empower-android` before proceeding.
2. Check the current git branch:
   ```bash
   git branch --show-current
   ```
   - Note the branch in the manifest output — it affects which screens are accessible

---

## Step 2 — Resolve Linear ID to Flag Key

**Skip this step if `--flag` was provided.**

Try each resolution strategy in order until a flag key is found:

### Strategy 2a — Local specs/

Check for an implementation summary:

```bash
# Direct match
cat specs/{LINEAR_ID}/IMPLEMENTATION_SUMMARY.md 2>/dev/null

# Broader search across all specs
grep -rl "{LINEAR_ID}" specs/ 2>/dev/null
```

If found, read the file and extract flag key references. Look for:
- `KEY_EXP_*` or `KEY_FG_*` constant names
- Statsig key strings (patterns like `"mobile.*"`, `"android.*"`, `"android_*"`)
- Mentions of "feature flag", "feature gate", "experiment"

### Strategy 2b — Linear MCP

If no local spec found, fetch the issue from Linear:

Use the Linear MCP tool `get_issue` with the Linear ID to fetch the issue description, comments, and linked PRs. Parse the response for:
- Statsig flag keys or experiment names
- ExperimentConfig constant references
- Amplitude experiment/chart URLs
- Figma URLs (note these for the manifest — useful for Phase 2)

### Strategy 2c — User Fallback

If no flag key was found automatically:

> "I couldn't automatically find a feature flag for {LINEAR_ID}. Please provide one of:
> - A `KEY_EXP_*` or `KEY_FG_*` constant name from ExperimentConfig.kt
> - A Statsig flag key string (e.g., `android.autosave-upsell-after-ca-draw-enabled`)
> - Or say `skip` to proceed with `--feature` package-based discovery only"

### Confirm the flag exists in code

Once a flag key is identified, verify it exists:

```bash
grep -n "{FLAG_CONSTANT_OR_STRING}" empower-app/src/main/java/finance/empower/android/app/experiments/ExperimentConfig.kt
```

If found, extract BOTH:
- **Constant name**: e.g., `KEY_FG_AUTOSAVE_UPSELL_AFTER_CA_DRAW_ENABLED`
- **String value**: e.g., `"android.autosave-upsell-after-ca-draw-enabled"`

If not found in ExperimentConfig.kt, search the broader codebase:
```bash
grep -rn "{FLAG_KEY}" empower-app/src/main/java/ --include="*.kt" -l
```

Record both the constant name and string value. The string value is the Amplitude experiment name (used in Phase 2).

---

## Step 3 — Discover Gated Screens

**Skip this step if `--feature` was provided** — go directly to Step 4 using the provided feature substring.

### 3a — Find files referencing the flag

```bash
grep -rn "{FLAG_CONSTANT_NAME}" empower-app/src/main/java/ --include="*.kt" -l
```

This typically returns ViewModels, Presenters, Activities, and Component classes that gate behavior on the flag.

### 3b — Extract the feature package

For each file found, extract the feature-level package directory. The convention is:

```
finance.empower.android.app.{feature}.{subpackage}
                              ↑ this is the feature root
```

Examples:
- `finance.empower.android.app.banking.autosave.details` → feature = `banking/autosave`
- `finance.empower.android.app.cashadvance.pre.enroll` → feature = `cashadvance`
- `finance.empower.android.app.loans.closure` → feature = `loans`

Collect the unique feature directories.

### 3c — Find screens in the feature

For each feature directory, find all `@Preview` functions and Activity classes:

```bash
# Find @Preview functions (for Paparazzi)
grep -rn "@Preview" empower-app/src/main/java/finance/empower/android/app/{feature}/ --include="*.kt" -l

# Find Activities (for Maestro)
grep -rn "class.*Activity" empower-app/src/main/java/finance/empower/android/app/{feature}/ --include="*.kt" -l
```

For each file with `@Preview`, extract:
1. **Package**: from the `package` declaration
2. **Preview function name**: the `@Composable` function annotated with `@Preview`
3. **Preview body**: the content of the preview function
4. **Visibility of the called Composable**: `private`, `internal`, or public
5. **Renderable via Paparazzi?**: public/internal = yes, private = skip

### 3d — Build the screen manifest

| # | File | Package | Screen/Preview | Type | Capturable? |
|---|---|---|---|---|---|
| 1 | AutoSaveDetailsScreen.kt | banking.autosave | AutoSaveDetailsPreview | @Preview | Yes (internal) |
| 2 | AutoSaveDetailsActivity.kt | banking.autosave | AutoSaveDetailsActivity | Activity | Yes (Maestro) |
| 3 | SomePrivateScreen.kt | banking.autosave | PrivatePreview | @Preview | Paparazzi: No (private), Maestro: Yes |

The manifest captures everything available — the capture method determines which subset is used.

If zero screens are found:
> "No screens found in the feature packages gated by {FLAG_KEY}. You can:
> 1. Try `--feature=<broader-package>` to cast a wider net
> 2. Use `/screenshot-screens --feature=<name>` directly
> 3. Manually capture screenshots and upload to the Customer Agent project"

---

# PART B: Screenshot Capture (Pluggable)

## Step 4 — Capture Screenshots

Based on `--capture` argument, use one of the methods below. Each method produces PNGs in the same output directory.

```bash
LINEAR_ID="{LINEAR_ID}"
OUTPUT_DIR=".claude/screen-captures/${LINEAR_ID}"
mkdir -p "$OUTPUT_DIR"
```

---

### Method: `paparazzi` (default)

**Best for**: Static Compose previews with fake data. Fast, headless, no device needed.
**Limitations**: Only renders @Preview functions with public/internal Composables. Shows synthetic data, not real server state.
**Prerequisite**: Works best on `customer-agent/internal-composables` branch.

Reuse the logic from `/screenshot-screens`:

1. Generate a temporary Paparazzi test class at `empower-app/src/test/java/finance/empower/android/app/CustomerAgentScreenshotTest.kt`
2. One `@Test` per renderable @Preview (public/internal only)
3. Each test uses `paparazzi.snapshot("NNN_ScreenName") { TiltTheme { ... } }`
4. Copy preview body exactly — same data construction, callbacks (`= {}`), parameters
5. Add all necessary imports from each source file

**Build:**
```bash
./gradlew :empower-app:recordPaparazziDevelopmentDebug \
  --tests "finance.empower.android.app.CustomerAgentScreenshotTest" \
  2>&1
```

**Error recovery**: Up to 5 fix-and-retry cycles. Comment out problem screens rather than blocking the batch.

**Collect:**
```bash
for f in empower-app/src/test/snapshots/images/finance.empower.android.app_CustomerAgentScreenshotTest_*.png; do
  name=$(basename "$f" | sed 's/finance.empower.android.app_CustomerAgentScreenshotTest_//' | sed 's/.png$//')
  cp "$f" "$OUTPUT_DIR/${name}.png"
done
```

**Clean up:**
```bash
rm -f empower-app/src/test/java/finance/empower/android/app/CustomerAgentScreenshotTest.kt
rm -f empower-app/src/test/snapshots/images/finance.empower.android.app_CustomerAgentScreenshotTest_*.png
```

---

### Method: `maestro`

**Best for**: Live app screenshots with real UI state, navigation flows, server-driven content. Shows what users actually see.
**Limitations**: Requires Android emulator running with debug build installed. Slower than Paparazzi.
**Prerequisite**: Maestro installed (`maestro --version`), emulator running (`adb devices`), debug APK installed.

> **This method is under active development.** The instructions below are a starting point — adapt as the Maestro workflow is refined.

1. **Verify setup:**
   ```bash
   maestro --version
   adb devices  # should show an emulator
   ```

2. **For each Activity found in Step 3**, generate a Maestro flow YAML or use `maestro studio` to navigate to the screen.

3. **Take screenshots** using Maestro's screenshot command:
   ```bash
   maestro screenshot "$OUTPUT_DIR/NNN_ScreenName.png"
   ```

4. **Or record a flow** and extract frames:
   ```bash
   maestro record --output "$OUTPUT_DIR/flow.mp4" flow.yaml
   ```

When this method matures, the Maestro flow generation and screenshot logic will be documented here in detail. For now, use the screen manifest from Step 3 as a guide for which screens to capture.

---

### Method: `fullstory`

**Best for**: Real user session screenshots showing actual behavior, edge cases, errors, and server-driven content. Shows what users *really* see.
**Limitations**: Requires `claude --chrome`, user logged into Fullstory, a session URL or segment. Screenshots live in the conversation — GIF export is the most reliable way to persist. WebView screens (subscription, Plaid) show "Internal Error: WebView not captured."
**Prerequisite**: Chrome integration active (`claude --chrome`), logged into Fullstory (org `o-234FQH-na1`).

This method reuses the logic from `/fullstory-capture`. It requires a Fullstory session URL — either provided by the user or discovered via Fullstory segments for the feature.

1. **Get a session URL.** If the user didn't provide one, suggest finding one:
   > "To capture real user screenshots via Fullstory, I need a session URL. You can find relevant sessions at:
   > https://app.fullstory.com/ui/o-234FQH-na1/segments
   >
   > Filter by events related to `{FLAG_STRING_VALUE}` or the feature screens found in Step 3.
   > Paste a session URL to continue, or say `skip` to use a different capture method."

2. **Open the session** in Chrome:
   - Call `mcp__claude-in-chrome__tabs_context_mcp` to get a tab
   - Call `mcp__claude-in-chrome__navigate` to open the session URL
   - Wait for the replay to load

3. **Read the event timeline** from the right sidebar using `mcp__claude-in-chrome__read_page`. Build a list of events, filtering for:
   - Custom analytics events (camelCase: `viewScreen`, `viewCashAdvanceOfferSelection`, etc.)
   - `Navigate` events (screen transitions)
   - Skip noise: `Backgrounded`, `Foregrounded`, `UITrackingElement`
   - If the feature package from Step 3 suggests specific screen names, prioritize matching events

4. **For each event**, click it in the sidebar to jump the replay to that moment, wait 3 seconds for rendering, then screenshot:
   - Use `mcp__claude-in-chrome__computer action: "screenshot"` for the full view
   - Use `zoom` on the replay viewport (approx x: 30-620, y: 150-850) to crop to just the app UI

5. **Save to output directory.** Fullstory screenshots are conversation-only by default. Two options:
   - **GIF export** (recommended): Start recording with `mcp__claude-in-chrome__gif_creator`, walk through events, then export:
     ```
     mcp__claude-in-chrome__gif_creator action: "export"
       filename: "fullstory_{LINEAR_ID}.gif"
       download: true
     ```
     The GIF downloads to the browser's Downloads folder. Move it to `$OUTPUT_DIR/`.
   - **Manual save**: Tell the user to save screenshots from the conversation to `$OUTPUT_DIR/`, naming them `001_ScreenName.png`, etc.

6. **Note in manifest**: Record the Fullstory session URL, user ID (if visible), device info, and which events were captured. This context is valuable for Phase 2 analysis.

**Tip**: Manual scrubbing through Fullstory replays and using Cmd+Shift+4 to screenshot is often faster and more reliable than automated event clicking. If automation is fighting you, switch to `--capture=manual` and use the Fullstory replay as your visual guide.

---

### Method: `manual`

**Best for**: Quick demos, ad-hoc evaluation, screens that can't be reached programmatically.
**Limitations**: No automation — relies on the user.

1. Print the screen manifest from Step 3d
2. Tell the user:
   > "Here are the {N} screens gated by {FLAG_KEY}. Please capture screenshots manually and save them to:
   > `.claude/screen-captures/{LINEAR_ID}/`
   >
   > Name them `001_ScreenName.png`, `002_ScreenName.png`, etc. When done, say `continue` and I'll generate the manifest."
3. Wait for the user to confirm, then proceed to Step 5.

---

## Step 4b — Stitch (optional, all methods)

If `--stitch` was passed and ImageMagick is available:
```bash
MAGICK=$(which magick 2>/dev/null || which convert)
$MAGICK montage "$OUTPUT_DIR"/*.png \
  -tile 3x -geometry 400x800+10+10 \
  -label '%f' -font Helvetica -pointsize 14 \
  "$OUTPUT_DIR/montage.png"
```

---

# PART C: Package & Report (Stable)

## Step 5 — Generate Capture Manifest

Create a `capture-manifest.md` file in the output directory:

```markdown
# Customer Agent Capture: {LINEAR_ID}

**Captured**: {date}
**Capture method**: {paparazzi|maestro|manual}
**Branch**: {git branch}
**Linear Issue**: {LINEAR_ID} — https://linear.app/empower/issue/{LINEAR_ID}
**Feature Flag**: `{FLAG_CONSTANT_NAME}` → `"{FLAG_STRING_VALUE}"`
**Amplitude Experiment Name**: `{FLAG_STRING_VALUE}`
{if --amplitude-url: **Amplitude URL**: {url}}
{if Figma URLs found in Linear: **Figma**: {urls}}

## Screens Captured

| # | Screen | Source File | Method |
|---|--------|------------|--------|
| 001 | {ScreenName} | {relative/path/to/file.kt} | {paparazzi/maestro/manual} |
| ... | | | |

## Screens Skipped

| Screen | Reason |
|--------|--------|
| {name} | private — not accessible from test |
| ... | |

## Feature Packages Scanned

- `finance.empower.android.app.{feature1}`
- `finance.empower.android.app.{feature2}`

## Next Steps

Upload the PNG files from this directory to the **Customer Agent** Claude Project
along with this message:

> Analyze {LINEAR_ID}. The experiment key is `{FLAG_STRING_VALUE}`.
> [attach the PNG screenshots]
```

Ensure the output directory is gitignored:
```bash
grep -qxF '.claude/screen-captures/' .gitignore 2>/dev/null \
  || echo '.claude/screen-captures/' >> .gitignore
```

---

## Step 6 — Report

Print a summary to the user:

```
## Customer Agent Capture Complete

**Linear Issue**: {LINEAR_ID}
**Flag**: {FLAG_CONSTANT_NAME} → "{FLAG_STRING_VALUE}"
**Capture method**: {method}
**Screens captured**: {N}
**Screens skipped**: {M}
**Output**: .claude/screen-captures/{LINEAR_ID}/

### Next Steps

1. Open the **Customer Agent** Claude Project on claude.ai
2. Type: "Analyze {LINEAR_ID}. The experiment key is `{FLAG_STRING_VALUE}`."
3. Upload the {N} PNG files from `.claude/screen-captures/{LINEAR_ID}/`
4. The project will run quantitative (Amplitude) + qualitative (UX) analysis
   and produce a unified report.

{if --stitch: Montage available at: .claude/screen-captures/{LINEAR_ID}/montage.png}
```
