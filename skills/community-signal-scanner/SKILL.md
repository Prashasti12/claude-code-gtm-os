---
name: community-signal-scanner
description: Find what a community is talking about right now (top topics, repeat questions, winning formats, FUD) before planning content. Use weekly before content planning.
---

# Community Signal Scanner

Listen first, then post.

## Inputs

- Niche or project category
- Platforms to scan: X, Reddit, Telegram, Discord
- Time window, seven days by default
- Optional hashtags, community names or competitor handles

## Steps

1. Search each platform for the niche in the time window. Use an X research tool if one is installed, otherwise web search.
2. Cluster posts into topics and rank them by how many distinct accounts are discussing them, not just by likes.
3. Pull out questions people keep asking. These are your best content prompts.
4. Note which formats get the most engagement: threads, memes, explainers or data posts.
5. Flag negative sentiment worth addressing.

## Output

Save to `research/community-signals-<project>-<YYYY-MM>.md` with:

- Top 5 topics, each with a source link
- Recurring questions
- Formats that are winning
- FUD or risks to watch

Feed this file into content-calendar-builder.
