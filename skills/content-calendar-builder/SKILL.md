---
name: content-calendar-builder
description: Build a 4-week content calendar for a brand from a short brief. Use when someone asks for a content plan, posting schedule or monthly calendar for X, Instagram, LinkedIn, Telegram or similar.
---

# Content Calendar Builder

Turns a brand brief into a week-by-week content plan with post types, pillars, copy angles and posting times.

## Inputs

Ask for anything missing before you start:

- Brand name and one-liner
- Target audience
- Platforms
- Key dates this month (launches, events, campaigns)
- Content pillars, for example education, community, memes, product updates

If a `community-signals-*.md` file from the community-signal-scanner skill exists for this brand, read it first and use its topics.

## Steps

1. Restate the brief in two lines so the user can correct it.
2. Map each key date to the week it lands in and plan the build-up before it.
3. Spread pillars so no pillar runs more than two posts in a row on the same platform.
4. For every post, write a specific copy angle, not a topic. "Why our fees dropped 40%" beats "fees update".
5. Suggest a posting time per platform and say why.

## Output

A markdown table per week:

| Day | Platform | Pillar | Format | Copy angle | Time |
|-----|----------|--------|--------|------------|------|

End with three posts worth turning into a thread or reel, and one experiment to test this month.
