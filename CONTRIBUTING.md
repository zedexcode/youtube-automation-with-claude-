# Contributing

This repo is a teaching project: it helps students learn YouTube automation
with Claude. Contributions are welcome — especially from students who tried
the guides and found something that works better.

## What to contribute

- **Fixes and clarifications** to the guides (wrong facts, unclear steps,
  outdated tool names or limits).
- **New prompts** for `prompts/claude-prompts.md` — only prompts you have
  actually tried and that produced useful output.
- **New scripts** for `scripts/` — small, single-purpose tools that help
  with one stage of the workflow (ideas, titles, descriptions, checklists).
  A script must run with the Python standard library only, no extra
  packages.
- **Case studies** like `guides/06-case-study.md` — real numbers from a
  real channel, with dates and sources. Do not invent figures.

## What not to contribute

- "Get rich quick" claims, guaranteed-growth promises, or spam tactics.
- Prompts or scripts that help copy other creators' videos, fake views,
  or break YouTube's policies.
- Anything that needs a paid tool or an API key to run.

## How to contribute

1. Fork the repo and create a branch for your change.
2. Make one change per pull request, and explain in the PR description
   what you changed and why.
3. If you change a guide, check that the README's folder structure and
   the guide's own cross-references still match.
4. If you add or change a script, run it at least twice (once with a
   normal input, once with an unusual one) and paste the output in the PR.

## Rules for scripts

- Python 3.8+ and standard library only.
- A `--help` text that explains what the script does and shows an example.
- No network access, no API keys, no writing files unless the script
  says so in its help text.
- Handle bad input with a clear error message, not a crash traceback.

## Rules for facts

Every number, date, and policy claim in the guides must be checkable.
If you are unsure about a fact, say so in the text ("check YouTube's
current requirements") instead of stating it as certain. AI tools invent
facts — this repo must not.
