# Rate limits, retries, and throttling

Prompts referenced in [Plutarch TX](https://plutarchtx.substack.com) article **035-rate-limits-retries**.

→ **Read the article:** <https://plutarchtx.substack.com/p/rate-limits-retries>

## How to use

Each `prompt-N.md` file is the prompt itself, with the teaching wrapper
stripped. Open the file, copy the contents, paste into Claude / ChatGPT /
your model of choice. The article (linked above) explains what the prompt
does and what to expect when you run it.

## Prompts in this article

### [`prompt-1.md`](./prompt-1.md) — Rate Limits Prompt — Classify Recent API Failures

Inspects recent API failures (or simulates them via a low-rate-limit test client running against scratch) and classifies each into three buckets — transient (retry will succeed), persistent (retry will not), and quality-degradation (response landed but is worse than baseline). The point is to stop blindly retrying everything. Two of the three classes need different responses, and treating quality-degradation as a transient is how you end up paying for bad output at full price.

### [`prompt-2.md`](./prompt-2.md) — Rate Limits Prompt — Class-Aware Retry Wrapper + Synthetic Load Test

Implements a small class-aware retry wrapper in scratch and runs it against a synthetic load that triggers each failure class deliberately. The wrapper is not installed in the operator's production code; it is staged for review. The synthetic load generator is the test bed — no live API key, no real provider call. The point is to give the operator a verified-working reference implementation they can adapt, not a copy-paste mystery.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution
to Plutarch TX appreciated when republishing.
