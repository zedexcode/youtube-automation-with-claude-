#!/usr/bin/env python3
"""Build a YouTube description and tag list from a title and keywords.

Usage:
    python3 description-generator.py "Why the Titanic's lookouts had no binoculars" \\
        --keywords "titanic,history,shipwreck" \\
        --chapters "0:00 The night of the sinking,2:15 The missing binoculars,5:40 What changed after"

Prints a description (promise + keywords in the first 2 lines, chapters,
one-line call to action) and a comma-separated tag list. Edit the output
before pasting it into YouTube — the first 2 lines are the part that shows
in search, so check them twice.

No API key or internet needed.
"""

import argparse
import textwrap


def build_description(title: str, keywords: list[str], chapters: list[tuple[str, str]],
                      cta: str = "Subscribe for more stories like this.") -> str:
    """Return a description built from the title, keywords and chapters."""
    main_kw = keywords[0] if keywords else title
    lines = [
        f"{title} — the full story of {main_kw}.",
    ]
    if len(keywords) > 1:
        lines.append(
            f"Covering {', '.join(keywords[1:])}, explained simply and "
            "with the facts checked."
        )
    lines.append("")
    lines.append("In this video:")
    if chapters:
        for time, label in chapters:
            lines.append(f"  {time}  {label}")
    else:
        lines.append("  Watch the full story from start to finish.")
    lines.append("")
    lines.append(cta)
    return "\n".join(lines)


STOP_WORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "on", "for", "with",
    "why", "how", "what", "when", "who", "had", "has", "have", "is", "are",
    "was", "were", "no", "not", "do", "does", "did", "by", "at", "from",
    "this", "that", "it", "its", "you", "your",
}


def build_tags(title: str, keywords: list[str], max_tags: int = 15) -> list[str]:
    """Return a tag list: your keywords first, then words from the title."""
    tags: list[str] = []
    for item in keywords + title.lower().split():
        item = item.strip().strip(",.!?")
        if item and item not in tags and item not in STOP_WORDS:
            tags.append(item)
        if len(tags) >= max_tags:
            break
    return tags


def parse_chapters(raw: str) -> list[tuple[str, str]]:
    """Parse 'time label,time label' into (time, label) pairs."""
    out = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        time, _, label = part.partition(" ")
        if time and label:
            out.append((time, label.strip()))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="The video title")
    parser.add_argument("--keywords", default="",
                        help="Comma-separated keywords, e.g. 'titanic,history'")
    parser.add_argument("--chapters", default="",
                        help="Comma-separated 'time label' pairs, e.g. '0:00 Intro,2:15 The story'")
    parser.add_argument("--cta", default="Subscribe for more stories like this.",
                        help="One-line call to action")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    chapters = parse_chapters(args.chapters)

    description = build_description(args.title, keywords, chapters, args.cta)
    tags = build_tags(args.title, keywords)

    print("\n--- Description ---\n")
    print(description)
    print(f"\n({len(description)} characters)")
    print("\n--- Tags ---\n")
    print(", ".join(tags))
    print()


if __name__ == "__main__":
    main()
