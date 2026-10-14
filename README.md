# claude-code-gtm-os

The GTM operating system I run my marketing work out of, built in Claude Code.

I'm a growth and content marketer. I grew a crypto platform's X from 1K to 14K+ followers and a creator community from 50 to 50,000 with zero paid spend. This repo is the system behind how I work now: a workspace Claude Code reads every session, plus skills that turn recurring marketing work into one-line commands.

## What's inside

```
claude-code-gtm-os/
├── templates/CLAUDE.md        # session rules, briefing format, read-before-you-work routing
└── skills/
    ├── morning-run/           # chains 5 steps into one autonomous daily run
    ├── daily-pulse/           # 24h scan of your niche on X -> 5 topics + post ideas
    ├── community-signal-scanner/
    ├── content-calendar-builder/
    ├── content-repurposer/    # one piece -> 6 platform-native versions
    ├── kol-researcher/
    ├── kol-dm-writer/
    ├── campaign-brief/
    ├── web3-campaign-brief/   # adds KOL strategy and on-chain KPIs
    └── performance-summary/
```

## How the system works

**One workspace, one routing file.** `CLAUDE.md` tells Claude what to read before each kind of task (voice file before content, project status before project work), how to brief me at session start, and what to update at the end. Context never gets lost between sessions.

**raw, wiki, output.** Every area of the workspace has the same three folders. Raw inputs get distilled into wiki knowledge, and finished work goes to output. Skills read from wiki and write to output.

**Skills chain.** `community-signal-scanner` feeds `content-calendar-builder`. `kol-researcher` feeds `kol-dm-writer`. `morning-run` chains `daily-pulse`, brand intel, content angles, an opportunity scan and a log update every morning, and keeps going if one step fails.

## Install

```bash
git clone https://github.com/Prashasti12/claude-code-gtm-os.git
mkdir -p your-workspace/.claude/skills
cp -r claude-code-gtm-os/skills/* your-workspace/.claude/skills/
cp claude-code-gtm-os/templates/CLAUDE.md your-workspace/CLAUDE.md
```

Then open Claude Code in `your-workspace` and say "run morning" or "build a content calendar for ...".

`daily-pulse` and `morning-run` use the open-source [x-research](https://github.com/rohunvora/x-research-skill) CLI by @rohunvora for X search. Install it into `.claude/skills/x-research/` and add an X API bearer token. Without it, both skills fall back to web search.

## Built with this system

- **Portfolio site:** generated from my Notion page through the API, rebuilding embedded tweets, reels and decks into one single-file site. https://prashasti-chauhan-portfolio.netlify.app
- **The Boring Growth Stack:** a growth playbook published to Webflow through its API. https://prashastis-portfolio.webflow.io/growth-stack

## Credits

- X search: [rohunvora/x-research-skill](https://github.com/rohunvora/x-research-skill)

## About me

Prashasti Chauhan, growth and content marketer. X [@0xPrashasti](https://x.com/0xPrashasti)

MIT licensed.
