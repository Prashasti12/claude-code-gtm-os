---
name: brand-url-to-posts
description: Take a brand's URL, build a mini brand brain, write a content brief with three angles, draft posts in a defined voice, and run an automated quality check before anything goes to approval. Trigger with "brief <url>" or "make posts for <url>".
allowed-tools: WebFetch, Bash, Read, Write
---

# Brand URL to Posts

The "Goose Takes a Brief" loop as a working skill: one URL in, approved-ready drafts out.

## Inputs

- A brand URL (required)
- A voice file, default `voice.md` in the workspace. If none exists, use `examples/voice-goose.md`.
- Platforms, default X and Instagram

## Step 1: Brand brain

Fetch the URL and up to two linked pages (pricing, about or product). Write `briefs/<brand>/brain.md` with:

- What they sell, in one plain sentence
- Who it's for
- Three claims the site actually makes, each quoted with its source URL
- What's missing or unclear from the site

Only use claims you can quote. Mark anything inferred as an assumption.

## Step 2: Brief

Write `briefs/<brand>/brief.md` with three distinct angles:

1. A problem angle: the pain the buyer feels before the product
2. A proof angle: a specific claim or result from the site
3. A contrarian angle: what this brand does differently from the obvious alternative

For each angle, give the audience, the hook idea and the format (single post, thread, carousel or short video).

## Step 3: Drafts

Read the voice file. For each angle write:

- one X post (under 280 characters, or a thread if the format says so)
- one Instagram caption (hook line, three short points, a CTA)

Save all drafts to `briefs/<brand>/drafts.md`, one per section with a heading like `## angle-1 / x`.

## Step 4: Quality check

Run:

```bash
python3 .claude/skills/brand-url-to-posts/scripts/qc.py briefs/<brand>/drafts.md --voice <voice-file>
```

The script checks every draft for length limits, a hook under 12 words, banned phrases from the voice file, hype words, em dashes, and claims with numbers that don't appear in `brain.md`. Fix every FAIL and rerun until it passes. Report remaining WARN items to the user instead of hiding them.

## Step 5: Approval

Write `briefs/<brand>/approval.md`: the drafts that passed, the QC report and a checkbox per draft. Nothing is posted from this skill. A human ticks what ships.

## Output summary

```
BRIEF - <brand>
brain.md     3 sourced claims, N assumptions
brief.md     3 angles
drafts.md    6 drafts
QC           N pass, N warn, 0 fail
approval.md  ready for review
```
