# `CLAUDE.md` as a contract

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **037-claude-md-as-contract**.

→ **Read the article:** <https://plutarchtx.substack.com/p/claude-md-as-contract>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — `CLAUDE.md` as a Contract — Tag Every Line

Walks your `CLAUDE.md` line by line and labels every non-blank, non-heading line as one of four categories: **RULE** (a constraint the model would otherwise miss), **DOCUMENTATION** (descriptive prose explaining context the model can infer), **HISTORY** (notes about past decisions or sessions), or **DERIVABLE** (information the model can recover from the repo or environment). The output is a tagged copy plus a category-count table. The prompt does not modify any live file. Everything written goes inside a dated scratch directory you delete with one command. Prompt 2 consumes the tagging output to produce a rewritten contract.

### [`prompt-2.md`](./prompt-2.md) — `CLAUDE.md` as a Contract — Rewrite to RULE-Only

Reads the line-tagging produced by Prompt 1 and stages a rewritten `CLAUDE.md` in scratch that contains only the RULE lines plus the structural headings needed for readability. Computes the token delta between the live file and the rewrite, names the savings, and produces a single-line undo. The prompt does not touch the live `CLAUDE.md`. You review the staged file, copy it over manually if you agree, and have a tested rollback path before you change anything.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
