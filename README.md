# YouTube Automation with Claude

Learn how to run a faceless YouTube channel with the help of AI — from picking a
niche to publishing your first videos. Built for students who want a practical,
step-by-step introduction to YouTube automation.

## What you will learn

1. What YouTube automation is (and what it is not)
2. How to pick and validate a niche
3. How to write video scripts with Claude
4. How to turn a script into a finished video (voiceover, visuals, editing)
5. How to upload, optimise, and grow a channel

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
prompts/
  claude-prompts.md            Copy-paste prompts for every stage
scripts/
  video-ideas-generator.py     Generate video title ideas for a niche
```

## How to use this repo

Read the guides in order, then use the prompts in `prompts/` while working on
your own channel. Run the script in `scripts/` whenever you need fresh video
ideas:

```bash
python3 scripts/video-ideas-generator.py "history"
```

## Important: follow YouTube's rules

Automation must follow YouTube's policies. Do not upload spam, misleading
content, or reused content with no added value. AI can help you create, but
the final video should be original, accurate, and genuinely useful to viewers.
Monetisation through the YouTube Partner Program currently requires 1,000
subscribers and 4,000 valid public watch hours (check YouTube's current
requirements, as they change).

## License

MIT — free to use, share, and adapt for learning. See `LICENSE`.
