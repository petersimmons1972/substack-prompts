# 131-filter-was-at-the-vendor — Prompt (read-only: where do my AI safeguards run, and is a local model on this machine?)

Paste into Claude Code or Codex, on the machine you want checked. Replace `<SAFEGUARDS>` with your own list of the AI safeguards you rely on, one per line. The prompt only reads; it changes nothing.

```text
Read-only, on this machine only. Do not create, change or delete any
file. Do not open any file you find, and do not connect to anything,
not even localhost.

My AI safeguards:
<SAFEGUARDS>

1. For each safeguard, say where it runs: at the model vendor, on our
   network, or on this machine. Then say whether it would see a request
   to a model running on this machine: YES, NO or UNKNOWN, and why.

2. Look for local model runtimes: ollama, gpt4all, msty, lms and
   llama-server on PATH or running, anything listening on port 11434,
   and the folders ~/.ollama and ~/.config/Msty. Report each as FOUND
   or NOT FOUND, with the path, process or port.

End with two lines:
Safeguards that would not see a local request: N
Local runtimes found: M
```
