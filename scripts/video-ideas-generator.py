#!/usr/bin/env python3
"""Generate YouTube video title ideas for a niche.

Usage:
    python3 video-ideas-generator.py "history"
    python3 video-ideas-generator.py "space" --count 10

No API key or internet needed. The ideas come from proven title patterns;
pick the ones that fit your niche and research the facts before scripting.
"""

import argparse
import random

PATTERNS = [
    "Why {topic} {twist}",
    "The hidden story of {topic}",
    "What nobody tells you about {topic}",
    "How {topic} changed the world",
    "{topic}: explained in {minutes} minutes",
    "The rise and fall of {topic}",
    "Why {topic} still matters today",
    "The mystery of {topic}, solved",
    "{topic} vs {rival}: who really won?",
    "What if {topic} never happened?",
    "The biggest mistake in the history of {topic}",
    "How {topic} actually works",
    "The untold story behind {topic}",
    "Why everyone gets {topic} wrong",
    "{topic} in {minutes} minutes: the full story",
]

TWISTS = [
    "almost failed",
    "was nearly forgotten",
    "changed everything",
    "nobody expected",
    "went wrong",
    "shocked the world",
]

RIVALS = [
    "its biggest rival",
    "the competition",
    "the old way",
    "what came before",
]


def generate(topic: str, count: int = 12, seed: int | None = None) -> list[str]:
    """Return `count` title ideas for `topic`."""
    rng = random.Random(seed)
    ideas = []
    patterns = PATTERNS[:]
    rng.shuffle(patterns)
    for pattern in patterns:
        if len(ideas) >= count:
            break
        ideas.append(
            pattern.format(
                topic=topic,
                twist=rng.choice(TWISTS),
                rival=rng.choice(RIVALS),
                minutes=rng.choice([5, 8, 10]),
            )
        )
    return ideas


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic", help="Your niche or topic, e.g. 'history'")
    parser.add_argument("--count", type=int, default=12,
                        help="How many ideas to generate")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed for repeatable output")
    args = parser.parse_args()

    print(f"\nVideo ideas for: {args.topic}\n")
    for i, idea in enumerate(generate(args.topic, args.count, args.seed), 1):
        print(f"{i:2}. {idea}")
    print("\nTip: research the facts behind an idea before scripting it.\n")


if __name__ == "__main__":
    main()
