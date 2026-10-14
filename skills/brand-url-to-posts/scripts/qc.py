#!/usr/bin/env python3
"""Quality check for drafts.md produced by the brand-url-to-posts skill.

Usage: qc.py drafts.md [--voice voice.md] [--brain brain.md]
Exits 1 if any draft FAILs.
"""
import argparse, os, re, sys

HYPE = ["game-changer", "revolutionary", "revolutionize", "unlock", "supercharge",
        "next-level", "cutting-edge", "seamless", "synergy", "10x your"]

def read(path):
    return open(path, encoding="utf-8").read() if path and os.path.exists(path) else ""

def banned_from_voice(text):
    m = re.search(r"## Banned phrases\n(.*?)(\n## |\Z)", text, re.S)
    if not m:
        return []
    return [l.strip("- ").strip().lower() for l in m.group(1).splitlines() if l.strip()]

def split_drafts(text):
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]

def check(name, body, banned, brain):
    fails, warns = [], []
    low = body.lower()
    first = next((l for l in body.splitlines() if l.strip()), "")
    platform = name.split("/")[-1].strip().lower()

    if platform == "x" and len(body) > 280 and "1/" not in body:
        fails.append(f"{len(body)} chars, over 280 for a single X post")
    if platform in ("instagram", "ig") and len(body) > 2200:
        fails.append("caption over 2,200 chars")
    if len(first.split()) > 12:
        warns.append(f"hook is {len(first.split())} words, aim for 12 or fewer")
    for p in banned:
        if p and p in low:
            fails.append(f"banned phrase: '{p}'")
    for h in HYPE:
        if h in low:
            warns.append(f"hype word: '{h}'")
    if "—" in body or "–" in body:
        fails.append("contains an em or en dash")
    if brain:
        for num in re.findall(r"\d[\d,.]*%?", body):
            if num not in brain:
                warns.append(f"number '{num}' not found in brain.md, check the source")
    return fails, warns

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("drafts")
    ap.add_argument("--voice")
    ap.add_argument("--brain")
    a = ap.parse_args()

    brain_path = a.brain or os.path.join(os.path.dirname(a.drafts), "brain.md")
    banned = banned_from_voice(read(a.voice))
    brain = read(brain_path)
    drafts = split_drafts(read(a.drafts))
    if not drafts:
        print("No drafts found. Use '## angle-1 / x' style headings.")
        sys.exit(1)

    total_fail = 0
    for name, body in drafts:
        fails, warns = check(name, body, banned, brain)
        status = "FAIL" if fails else ("WARN" if warns else "PASS")
        total_fail += bool(fails)
        print(f"[{status}] {name}")
        for f in fails:
            print(f"    fail: {f}")
        for w in warns:
            print(f"    warn: {w}")
    print(f"\n{len(drafts)} drafts, {total_fail} failing")
    sys.exit(1 if total_fail else 0)

if __name__ == "__main__":
    main()
