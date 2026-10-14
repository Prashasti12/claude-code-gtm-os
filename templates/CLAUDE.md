# CLAUDE.md - GTM workspace

Claude Code reads this at the start of every session.

## Rules that are always on

- **Capture:** when I mention a goal, number, person or decision, write it to the right file without being asked.
- **Connect:** when new information arrives, update every file it touches. Nothing lives in isolation.
- **Surface:** at session start, read the last entries of `log.md` and `inbox.md`, then give me a briefing before any work.
- **Reflect:** at session end, update `log.md`, the relevant project `CLAUDE.md` and `index.md`.

## Session start briefing (under 150 words)

```
ACTIVE PROJECTS
-> project: one-line status from its CLAUDE.md

OPEN FROM LAST SESSION
-> what was left unfinished

INBOX
-> N items, or "clear"

NEEDS ATTENTION
-> anything with a deadline
```

Be specific. "Batch 06 not started, angle ready" beats "project is ongoing".

## Read before you work

| Before... | Read |
|-----------|------|
| Any content | `brand/voice.md`, `brand/content-strategy.md` |
| Project work | `projects/<name>/CLAUDE.md` first, then its wiki |
| Strategy | `wiki/frameworks/` and `wiki/index.md` to avoid duplicates |
| A new wiki page | `wiki/index.md`, and update instead of duplicating |

## Folder pattern

Every area uses the same three folders:

- `raw/`: unprocessed inputs, transcripts, scraped posts
- `wiki/`: distilled, reusable knowledge
- `output/`: finished deliverables

## Skills

GTM skills live in `.claude/skills/`. Run `morning-run` daily, and pair `community-signal-scanner` with `content-calendar-builder`.
