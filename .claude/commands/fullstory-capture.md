---
description: Capture screenshots from a Fullstory session replay by walking through the event timeline. Requires claude --chrome. Use when you want to capture the actual user experience for UX evaluation by the Customer Agent.
argument-hint: "<fullstory-session-url> [--output-dir=<path>] [--events=viewScreen,error] [--max=<N>]"
---

## User Input

```text
$ARGUMENTS
```

Parse arguments:

| Argument | Default | Description |
|---|---|---|
| `<url>` | _(required)_ | Fullstory session replay URL |
| `--output-dir=<path>` | `/tmp/fullstory-captures/` | Where to save screenshots |
| `--events=<filter>` | _(all key events)_ | Comma-separated event name substrings to filter for (e.g. `viewScreen,error,loginMFA`) |
| `--max=<N>` | `20` | Maximum number of screenshots to capture |
| `--gif` | `false` | Also export an animated GIF of the flow |

If no URL is provided, ask the user for one.

---

## Prerequisites

- **Chrome integration must be active** (`claude --chrome`). If Chrome tools are not available, tell the user to restart with `claude --chrome --resume`.
- User must be **logged into Fullstory** in Chrome.

---

## Step 1 — Open the Session

1. Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true` to get a tab.
2. Call `mcp__claude-in-chrome__navigate` to open the Fullstory session URL.
3. Wait 5 seconds for the replay to load.
4. Take a screenshot to verify the session loaded. If you see "Unable to retrieve session", report the error and stop.

---

## Step 2 — Read the Event Timeline

The Fullstory replay has a **right sidebar** showing the event timeline — a scrollable list of events like:
- `Navigate *Controller` — screen transitions
- `viewScreen` / `viewPasscodeResetSSN` / `loginMFA` — custom analytics events
- `didShowError *` — error events
- `Backgrounded *` / `Foregrounded *` — app lifecycle (skip these)
- `Network Error *` — network failures

**Read the sidebar** using `mcp__claude-in-chrome__read_page` with `filter: "all"` focused on the right sidebar area. Look for event names in the timeline.

If `read_page` doesn't capture the event names clearly enough, use `mcp__claude-in-chrome__computer` with `action: "screenshot"` and visually read the event names from the screenshot.

**Build an event list** by scrolling through the sidebar. For each event, note:
- Event name (e.g., `viewPasscodeResetSSN`, `Navigate AccountPinViewController`)
- Its approximate position in the sidebar (for clicking later)

**Filter the events:**
- If `--events` was specified, only keep events whose names contain any of the specified substrings.
- If no filter specified, keep all events that are: custom analytics events (lowercase camelCase like `viewScreen`, `loginMFA`, `passcodeResetSelect`) and `Navigate` events (screen transitions). Skip `Backgrounded`, `Foregrounded`, and `UITrackingElement` events as they are noise.
- Limit to `--max` events.

---

## Step 3 — Capture Screenshots

If `--gif` was passed, start GIF recording:
```
mcp__claude-in-chrome__gif_creator action: "start_recording"
```

For each event in the filtered list:

1. **Scroll the sidebar** if needed to make the event visible.
2. **Click on the event name** in the sidebar. This jumps the replay to that moment.
3. **Wait 3 seconds** for the replay to render the screen at that point.
4. **Take a screenshot** using `mcp__claude-in-chrome__computer action: "screenshot"`.
5. **Record the frame** — note the event name, timestamp (from the replay timeline at the bottom), and screenshot ID.

**Important interaction notes:**
- The event sidebar is on the right side of the screen (~940px to ~1300px x-coordinate range).
- Events are stacked vertically. Each event row is roughly 40-50px tall.
- Click on the event name text, not the icon.
- If the replay shows "Loading..." after clicking, wait an additional 3 seconds.
- The replay viewport is on the left side (~0px to ~920px). The actual app screen is rendered inside this area.

---

## Step 4 — Save Screenshots

Create the output directory:
```bash
mkdir -p {OUTPUT_DIR}/{SESSION_ID}
```

Where `SESSION_ID` is extracted from the URL (the numeric portion after `/session/`).

For saving screenshots to disk, use `mcp__claude-in-chrome__javascript_tool` to capture the replay viewport as an image, or instruct the user to save from the conversation.

**Alternative approach for saving**: Since Chrome screenshots are in-conversation only, the most reliable way to persist them is:

1. For each screenshot captured, use the `zoom` action on the **replay viewport area only** (approximately x: 30-620, y: 150-850) to get a cropped view of just the app screen without the Fullstory UI chrome.
2. If saving to disk is critical, use the GIF export approach (`--gif` flag) which downloads to the browser's Downloads folder.

---

## Step 5 — Export GIF (if --gif)

If `--gif` was passed:

1. Stop recording: `mcp__claude-in-chrome__gif_creator action: "stop_recording"`
2. Export and download:
```
mcp__claude-in-chrome__gif_creator action: "export"
  filename: "fullstory_{SESSION_ID}.gif"
  download: true
  options: {
    showClickIndicators: true,
    showActionLabels: true,
    showProgressBar: true,
    showWatermark: false,
    quality: 5
  }
```

---

## Step 6 — Report

Print a summary:

```
## Fullstory Session Capture Report

**Session URL**: {URL}
**User**: {user ID from sidebar, if visible}
**Device**: {device info from sidebar, e.g., "Mobile · iOS"}
**Events captured**: {count}

### Flow
| # | Event | Timestamp | Screenshot |
|---|---|---|---|
| 1 | viewScreen (Login) | 0:05 | ss_xxxxx |
| 2 | loginMFA | 0:12 | ss_xxxxx |
| 3 | viewPasscodeResetSSN | 0:45 | ss_xxxxx |
| ... | | | |

### Output
- Screenshots: {count} in conversation
- GIF: {path if --gif, otherwise "not requested"}

### UX Observations
Based on the captured flow, note any obvious issues:
- Error events encountered
- Unusual navigation patterns (going back, repeated screens)
- Long gaps between events (user confusion/waiting)
- Network errors
```

The screenshots in the conversation can be:
- Fed directly into Pawel's Customer Agent Claude Project (copy/paste)
- Downloaded as a GIF from the browser Downloads folder
- Uploaded to the shared Google Drive folder

---

## Tips for Effective Capture

1. **Start with a specific flow**: Use Fullstory segments to find sessions for a particular feature (e.g., "Cash Advance onboarding", "Login with MFA").
2. **Filter events**: Use `--events=viewScreen` to only capture screen transitions, which gives you the cleanest flow.
3. **Crop for analysis**: The `zoom` action on the replay viewport gives you just the app UI without Fullstory chrome — better for feeding into the Customer Agent.
4. **Multiple sessions**: Run the skill multiple times on different sessions for the same flow to see variation in user behavior.
5. **Error investigation**: Use `--events=error,Network` to specifically capture error states.
