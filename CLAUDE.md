# Customer Agent — Claude Code Project

This is the central repo for Tilt's Customer Agent AI Sprint. It contains knowledge files, skills, Maestro flows, and automation scripts for evaluating the mobile app experience from a customer's perspective.

## Slash Commands

All commands are in `.claude/commands/`. Run them with `/command-name` from this directory.

### No dependencies (browser-only)
- `/fullstory-capture <session-url>` — Capture screenshots from Fullstory session replays using Chrome automation. Requires `claude --chrome`.
- `/amplitude-experiment-monitor` — Monitor A/B experiment performance via Amplitude MCP.

### Requires empower-android repo
These commands need `~/empower/empower-android` checked out to branch `customer-agent/internal-composables`:
- `/screenshot-screens` — Generate Paparazzi screenshots of Composable screens headlessly.
- `/customer-agent-capture <LINEAR-ID>` — Full pipeline: Linear issue → flag → screens → Paparazzi capture → output package.

## Key URLs
- **Pawel's Claude Project**: https://claude.ai/project/019d547f-2434-775a-b9fc-20bb0dfbef6d
- **Fullstory**: https://app.fullstory.com/ui/o-234FQH-na1/ (org: `o-234FQH-na1`)
- **Amplitude**: Project ID `152808` (Empower production)
- **Google Drive**: https://drive.google.com/drive/folders/195aWeXklTh1IbSoK-orNKmeXhCSsexgC
