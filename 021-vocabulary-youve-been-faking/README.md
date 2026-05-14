# The vocabulary you've been faking

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **021-vocabulary-youve-been-faking**.

→ **Read the article:** <https://plutarchtx.substack.com/p/vocabulary-youve-been-faking>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Vocabulary Prompt — Tokenize a Paragraph You Picked

Forces the abstract idea of a "token" into a concrete number you can hold in your head. You pick one paragraph from a file you already own — a README, an email draft, a code comment — drop it into a scratch file, and the model returns a token count, a byte-to-token ratio, a per-word ratio, and three short examples of how the same paragraph would tokenize differently if it were code, JSON, or Mandarin. You leave the prompt with a working intuition for "how much of my context does a paragraph cost" rather than a vague sense that tokens are real.

### [`prompt-2.md`](./prompt-2.md) — Vocabulary Prompt — Label a Conversation Export

Takes one of your own AI conversations and labels every segment of it with the vocabulary term that segment exemplifies — system prompt, memory injection, user turn, assistant turn, tool call, tool result. The goal is to see, in your own logs, that the words from the article correspond to actual structures in actual transcripts. You leave the prompt with a labeled artifact you can refer back to whenever a later article uses one of these terms casually.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
