Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are a surface-instruments cataloguer. You are read-only against my home directory. You may write only inside the scratch directory created in Step 1. You may not exfiltrate any file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, any memory file, any hook, or install MCP servers. You only invoke documented read-only instruments.

**Step 1 — create scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-031-instruments"
mkdir -p "$SCRATCH"
echo "scratch=$SCRATCH"
```

**Step 2 — identify the primary surface.** Detect the operator's primary surface by environment cues: presence of `~/.claude/settings.json` → Claude Code; presence of `OPENAI_API_KEY` env var without Claude Code → API/OpenAI; `$CLAUDECODE=1` confirms Claude Code session. Write detected surface to `$SCRATCH/00-surface.md`. If detection is ambiguous, default to Claude Code and note both candidates.

**Step 3 — enumerate instruments per surface.** Build an enumeration table appropriate to the detected surface. For Claude Code, instruments include: `/status`, `/cost`, `/context`, `/permissions`, hook-emitted state files in `~/.claude/.engram-*`, `~/.claude/.validator-bash-guard`, settings allow/deny rule counts, enabled MCP server list, recent transcript file size. For ChatGPT, instruments include: settings → personalization → custom instructions, conversation list, message export. For API surfaces, instruments include: `/v1/usage`, response `usage` field, request log retention. Write the candidate list to `$SCRATCH/01-instruments-list.md`.

**Step 4 — run each instrument once.** For each instrument in the enumeration, invoke its read-only form and capture output to a numbered file `$SCRATCH/02-NN-<instrument>.md`. Examples:

- `/status` output → `02-01-status.md`
- `~/.claude/settings.json` allow/deny count via `jq` → `02-02-settings-counts.md`
- hook state files → list filenames + byte sizes only, never bodies → `02-03-hook-state.md`
- enabled MCP servers (count + names) → `02-04-mcp-servers.md`
- latest transcript size + path basename → `02-05-transcript.md`

If an instrument is not available on the detected surface, mark `N/A` with a one-clause reason — do not skip silently.

**Step 5 — flag unrun instruments.** Any instrument the operator has not invoked in the last 30 days (heuristic: if the prompt cannot find evidence of recent use, flag) gets marked `UNRUN_BEFORE_TODAY` in the index. Write `$SCRATCH/03-unrun.md`.

**Step 6 — write the index.** Produce `$SCRATCH/00-INSTRUMENTS.md` with a markdown table: `id`, `instrument`, `surface`, `available` (Y/N/N-A), `value_signal` (one of: `cost`, `context-shape`, `security-surface`, `health`, `usage-history`), `output_file`, `unrun_today` (Y/N). Sort by surface then by id. Print to stdout.
````
