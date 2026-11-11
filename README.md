# YouTube Automation with Claude

Learn how to run a faceless YouTube channel with the help of AI — from
picking a niche to publishing your first videos. Built for students who
want a practical, step-by-step introduction to YouTube automation.

## What you will learn

1. What YouTube automation is (and what it is not)
2. How to pick and validate a niche
3. How to write video scripts with Claude
4. How to turn a script into a finished video (voiceover, visuals, editing)
5. How to upload, optimise, and grow a channel
6. What a real channel's first week actually looks like (case study)

## Who this is for

Students and beginners with no prior YouTube experience. No paid tools are
required to start — every step has a free option.

## Folder structure

```
guides/
  01-getting-started.md        What automation really means
  02-niche-and-research.md     Picking and validating a niche
  03-script-writing.md         Writing scripts with Claude
  04-voiceover-and-editing.md  Voiceover, visuals, and editing
  05-upload-seo-and-growth.md  Titles, thumbnails, and growing
  06-case-study.md             A real channel's first week, with numbers
prompts/
  claude-prompts.md            Copy-paste prompts for every stage
scripts/
  video-ideas-generator.py     Generate video title ideas for a niche
  title-checker.py             Check a title before you publish it
  description-generator.py     Build a description and tag list
CONTRIBUTING.md                How to improve this repo
```

## How to use this repo

Read the guides in order, then use the prompts in `prompts/` while working
on your own channel. Run the scripts in `scripts/` whenever you need them:

```bash
# Fresh video ideas for a niche
python3 scripts/video-ideas-generator.py "history"

# Check a title before publishing (score 0-100, lists what to fix)
python3 scripts/title-checker.py "Why the Titanic's lookouts had no binoculars" --keywords "titanic,history"

# Build a description and tag list
python3 scripts/description-generator.py "Why the Titanic's lookouts had no binoculars" \
  --keywords "titanic,history,shipwreck" \
  --chapters "0:00 The night of the sinking,2:15 The missing binoculars"
```

All scripts need only Python 3.8+ and the standard library — no API key,
no extra packages, no internet.

## A real example, not just theory

Guide 06 is a case study of the author's own channel, Ember & Oath
Stories — an AI-movie channel whose first full movie got 97 views and a
2.1% click-through rate in its first 3 days. It shows what the numbers
really look like at the start, and what was learned from them. Read it
before you decide what "success" should look like in your first month.

## Important: follow YouTube's rules

Automation must follow YouTube's policies. Do not upload spam, misleading
content, or reused content with no added value. AI can help you create, but
the final video should be original, accurate, and genuinely useful to
viewers. Monetisation through the YouTube Partner Program currently
requires 1,000 subscribers and 4,000 valid public watch hours (check
YouTube's current requirements, as they change).

## Contributing

Found a mistake, tried a prompt that works better, or have real numbers
from your own channel? See `CONTRIBUTING.md`.

## License

MIT — free to use, share, and adapt for learning. See `LICENSE`.
