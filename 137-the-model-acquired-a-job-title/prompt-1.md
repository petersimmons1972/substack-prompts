# 137-the-model-acquired-a-job-title — Prompt (read-only: is a job title stored as the model's name?)

Paste into Claude Code or Codex. Replace `<DIRECTORY>` with the folder that holds your router, proxy and app configs (for the demo in the post, `embed-names-demo`). The prompt only reads; it changes nothing.

```text
Read-only: change no file, and call no model, router or network.

Look through the configs in <DIRECTORY>. If that is still a placeholder
or does not exist, stop and say so.

1. List every model name you find (aliases, served names, route
   entries), with file and line, and the model each one resolves to.
2. Find every place a model name is stored or compared as the model's
   identity, such as an embedder name saved with each vector.
3. Flag any stored name that contains a job or routing word (live, bulk,
   batch, reembed, fast, primary, latest, a host name or a port), or
   that is one of two names for the same model.

Use a list, not a table. End with one line: how many stored names are
really job titles.
```
