---
name: morning-run
description: Autonomous morning workflow that chains daily pulse, brand intel, content angles, opportunity scan and log update in one run. Trigger with "run morning".
allowed-tools: Bash, Read, Write, Edit, WebSearch
---

# Morning Run

Five steps in sequence with no input needed. If a step fails, log why and move on. A dead API should never kill the whole run.

## Setup

```bash
DATE=$(date +%Y-%m-%d)
```

Read `config/pulse.md` for queries, accounts and voice files. Create output folders as needed.

## Step 1: Daily pulse

Run the daily-pulse skill. Output goes to `research/$DATE-daily-pulse/output/daily-pulse.md`.

## Step 2: Brand intel

Search the last 24 hours for the brand you cover and its competitors:

```bash
bun run .claude/skills/x-research/x-search.ts search "<BRAND_QUERY>" --since 1d --sort likes --limit 10
bun run .claude/skills/x-research/x-search.ts watchlist check
```

Capture milestones, integrations, notable reactions and competitor moves, each with a source link. Save to `projects/<brand>/research/$DATE-intel.md`.

## Step 3: Content angles

No new API calls. Combine Steps 1 and 2 into:

- 3 angles for your main account, each with a hook, why it works and the signal behind it
- 2 fully drafted posts for any secondary account, in that account's voice file

Save to `projects/<brand>/content/$DATE-content-angles.md`.

## Step 4: Opportunity scan

Search for fresh opportunities you track, such as hiring posts, partnership calls or grant rounds:

```bash
bun run .claude/skills/x-research/x-search.ts search "<OPPORTUNITY_QUERY>" --since 1d --sort recent --limit 5
```

Save the top five as a table with link and a one-line fit assessment to `opportunities/$DATE.md`, or write "nothing new today".

## Step 5: Log

Append to `log.md`:

```markdown
## YYYY-MM-DD morning-run
- Pulse: top topic, or the failure reason
- Intel: key finding, or "no new signals"
- Angles: N generated
- Opportunities: N found
```

## End-of-run summary

```
MORNING RUN - YYYY-MM-DD
[ok] Daily pulse     -> research/...
[ok] Brand intel     -> projects/...
[ok] Content angles  -> projects/...
[ok] Opportunities   -> opportunities/...
[ok] Log updated

Top topic: ...
Best angle: ...
```

Mark failed steps with [fail] and the reason.

## Failure handling

| Failure | Action |
|---------|--------|
| X API 402, credits depleted | Note it, fall back to web search or skip |
| bun not found | Report the missing prerequisite and continue |
| Folder missing | Create it, then write |
