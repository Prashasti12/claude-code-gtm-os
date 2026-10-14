---
name: daily-pulse
description: Morning scan of what your niche on X is talking about in the last 24 hours, turned into five topics with a post idea each. Trigger with "run daily pulse".
allowed-tools: Bash, Read, Write, WebSearch
---

# Daily Pulse

Run before posting anything that day. The pulse decides what to say, not the other way round.

## Configure once

Edit `config/pulse.md` in your workspace:

- `NICHE_QUERIES`: two or three X search queries for your space
- `BRAND_QUERY`: a query for the brand or product you cover
- `VOICE_FILE`: path to your voice notes

## Requires

- The open-source [x-research](https://github.com/rohunvora/x-research-skill) CLI installed at `.claude/skills/x-research/`
- `bun` and an X API bearer token in your environment

If the X API is out of credits, fall back to web search and note that in the output.

## Steps

1. For each niche query run:
   `bun run .claude/skills/x-research/x-search.ts search "<query>" --since 1d --sort likes --limit 10 --no-replies`
2. Run the brand query with `--limit 10`.
3. Pick the five topics with the most signal: many distinct accounts talking, high engagement, and a conversation that's still open.
4. Prefer topics where you have a real take, not just a reaction.

## Output

Create `research/<YYYY-MM-DD>-daily-pulse/output/daily-pulse.md`:

```markdown
# Daily Pulse - YYYY-MM-DD

## Top 5 topics
### 1. Topic
What it is: one sentence
Why people are talking about it: the trigger
Post idea: one specific post you could write today
Source: link

## Brand mentions today
Two or three lines, or "nothing notable"

## Do this first
The single highest-value post or reply for today
```
