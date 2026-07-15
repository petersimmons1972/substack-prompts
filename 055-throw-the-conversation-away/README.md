# When to throw the conversation away

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **055-throw-the-conversation-away**.

→ **Read the article:** <https://plutarchtx.substack.com/p/throw-the-conversation-away>

_Published: 2026-05-22_

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Save-Forward Handoff — Capture the Artifact, Not the Thread

Produces a save-forward handoff document for one current long conversation. The handoff is the artifact a fresh thread will inherit — typically 200–500 words — capturing the task, the relevant decisions made so far, the relevant files and paths, the current blocker (if any), and the explicit "what to try next." The handoff is *not* a summary of the conversation; it is the inputs a new session needs to continue the work without re-deriving anything that has already been figured out.

### [`prompt-2.md`](./prompt-2.md) — Fresh Thread — Compare Progress Per Turn

Produces a comparison protocol for evaluating a fresh-thread restart against the long conversation it is replacing. The operator runs a fresh Claude Code session using only the handoff as input, then logs the results. The output is a per-turn progress comparison: how many turns to first useful output, how many to the next coherent milestone, and whether the fresh thread improved on the previous one. The comparison turns "save-forward worked" from a feeling into a measurement.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
