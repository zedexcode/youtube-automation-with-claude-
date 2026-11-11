#!/usr/bin/env python3
"""Check a YouTube title before you publish it.

Usage:
    python3 title-checker.py "Why the Titanic's lookouts had no binoculars"
    python3 title-checker.py "You WON'T BELIEVE this!!!" --keywords history,titanic

Checks: character length (aim under 60 so it is not cut off), word count,
clickbait words, all-caps shouting, excessive punctuation, and whether your
main keywords appear in the title. Prints a simple score and what to fix.

No API key or internet needed.
"""

import argparse
import re
import sys

CLICKBAIT_WORDS = [
    "you won't believe", "shocking", "insane", "unbelievable",
    "mind-blowing", "gone wrong", "gone sexual", "must watch",
    "100% free", "secret trick", "they don't want you to know",
    "what happens next", "amazing", "incredible",
]

SHOUT_WORDS = ["free", "new", "best", "top", "secret", "revealed"]


def check(title: str, keywords: list[str]) -> dict:
    """Return a dict of checks for `title`."""
    issues = []
    tips = []
    score = 100

    length = len(title)
    if length > 60:
        issues.append(f"Too long: {length} characters (over 60, will be cut off)")
        score -= 20
    elif length < 25:
        issues.append(f"Very short: {length} characters (under 25, may look vague)")
        score -= 5
    else:
        tips.append(f"Length OK: {length} characters")

    words = title.split()
    if len(words) < 3:
        issues.append("Too few words — the title says almost nothing")
        score -= 15
    elif len(words) > 12:
        issues.append(f"{len(words)} words is a lot — shorter titles usually win")
        score -= 5

    lowered = title.lower()
    for word in CLICKBAIT_WORDS:
        if word in lowered:
            issues.append(f"Clickbait phrase: '{word}' — only use it if the video truly delivers it")
            score -= 15
            break
    else:
        tips.append("No common clickbait phrases")

    caps_words = [w for w in words if w.isupper() and len(w) > 1]
    if caps_words:
        issues.append(f"ALL-CAPS words: {', '.join(caps_words)} — reads as shouting")
        score -= 10

    if title.count("!") > 1 or title.count("?") > 1:
        issues.append("More than one ! or ? — one is enough")
        score -= 5

    if re.search(r"\d", title):
        tips.append("Contains a number — numbers often raise curiosity")
    if "?" in title:
        tips.append("Asks a question — good for curiosity, if the video answers it")

    if keywords:
        found = [k for k in keywords if k.lower() in lowered]
        missing = [k for k in keywords if k.lower() not in lowered]
        if found:
            tips.append(f"Keywords in title: {', '.join(found)}")
        if missing:
            issues.append(f"Main keywords missing from title: {', '.join(missing)}")
            score -= 10

    return {"score": max(score, 0), "issues": issues, "tips": tips}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="The video title to check")
    parser.add_argument("--keywords", default="",
                        help="Comma-separated main keywords, e.g. 'history,titanic'")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    result = check(args.title, keywords)

    print(f"\nTitle: {args.title}\n")
    print(f"Score: {result['score']}/100\n")
    for tip in result["tips"]:
        print(f"  [+] {tip}")
    for issue in result["issues"]:
        print(f"  [!] {issue}")
    if not result["issues"]:
        print("  No issues found — this title is ready.")
    print()
    return 0 if result["score"] >= 70 else 1


if __name__ == "__main__":
    sys.exit(main())
