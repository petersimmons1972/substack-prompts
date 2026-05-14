# What you need to follow along

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **027-what-you-need-to-follow-along**.

→ **Read the article:** <https://plutarchtx.substack.com/p/what-you-need-to-follow-along>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Follow-Along Prompt — Set Up the Scratch Pattern and Prove Undo

Establishes the scratch-directory pattern every later article uses, then proves the pattern's undo on a throwaway test artifact you create, modify, and revert. By the time the prompt finishes, you have run the full create/modify/verify/undo cycle once, with eyes on, on a file you don't care about — so the next article that asks you to do it on a file you do care about is just repetition. The exercise also verifies your environment is correctly assembled: bash version, git presence, Claude Code presence, scratch directory writability, undo command idempotence.

### [`prompt-2.md`](./prompt-2.md) — Follow-Along Prompt — Personal Pre-Flight Checklist

Produces a single, reusable pre-flight checklist tailored to your environment — the bash version you have, the git version you have, the scratch path convention you use, the undo command shape you've now run twice. The checklist lives as a plain text file you copy into wherever you keep operational notes (`~/notes/`, a wiki, a Tana node, a sticky note). Every later article in the series begins with the words "before you start, run your pre-flight checklist." This prompt is what makes that instruction concrete.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
