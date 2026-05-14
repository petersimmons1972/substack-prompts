# Measure your baseline

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **023-measure-your-baseline**.

→ **Read the article:** <https://plutarchtx.substack.com/p/measure-your-baseline>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-2.md`](./prompt-2.md) — Baseline Prompt — Re-Run Against a Bloated Copy

Demonstrates the baseline's reusability by running it twice — once against a faithful copy of your live `CLAUDE.md` placed in scratch, once against a deliberately-bloated version of that copy with a useless 400-word paragraph appended. The two `00-BASELINE.md` files will differ in exactly one number — `memory_files_total_tokens` — and the size of that difference is the proof that the baseline measures what it claims to measure. The prompt establishes the comparison ritual that every later article uses: run the baseline, change something, re-run, diff.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
