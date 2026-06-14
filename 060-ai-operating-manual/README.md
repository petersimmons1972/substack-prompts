# Your AI operating manual

_Assembling the scattered artifacts from this series into one portable, versioned directory_

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **060-ai-operating-manual**.

→ **Read the article:** <https://plutarchtx.substack.com/p/ai-operating-manual>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Operating Manual — Assemble the Series Artifacts

Assembles the personal AI operating manual from the artifacts produced across the series. The manual is a single file (or small set of files) the operator can carry between projects and machines: tuned `CLAUDE.md`, the Article 023 baseline measurement script, the permission baseline from Article 050, the selection cheat sheet from Article 059, the personal `CLAUDE.md` library structure from Article 058, plus the convention-loop template from Article 048 and the recovery card from Article 054. The output is staged in scratch as a single repository-ready directory the operator can `git init` and version separately. Prompt 2 re-runs the canonical baseline against the assembled manual to verify the numbers match what the series promised.

### [`prompt-2.md`](./prompt-2.md) — Final Baseline — Verify the Numbers Against the Assembled Manual

Runs the canonical Article 023 baseline measurement one final time, this time against the *assembled manual* in scratch (rather than against the operator's live environment). The point is to verify the manual is a faithful, portable representation of the operator's tuned system: the same metrics should land within tolerance of Article 057's post-series measurement. Discrepancies are findings — either the manual is missing a load-bearing piece, or the live environment has drifted since Article 057. Either is worth knowing before declaring the series done.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
