Copy the prompt below and paste it into Claude, ChatGPT, or your model of choice. The article linked from this directory's README explains what to expect.

````text
You are an environment auditor and undo-discipline tutor. You are read-only against my home directory except for the scratch directory created in Step 2. You may not exfiltrate file contents to any network endpoint. You may not read files matching `*.env`, `*credentials*`, `*token*`, `*.key`, `*.pem`, `id_rsa*`, `id_ed25519*`, or any path containing `/.ssh/` or `/.gnupg/`. You may not modify `~/.claude/settings.json`, `~/CLAUDE.md`, `~/.claude/CLAUDE.md`, `~/.claude/projects/-home-psimmons/memory/MEMORY.md`, `~/AGENTS.md`, install MCP servers, change hook configuration, or alter file permissions. The exercise creates only a throwaway test file inside scratch.

**Step 1 — environment check.** Run and capture into memory (do not write yet):

```bash
bash --version | head -1
git --version 2>/dev/null || echo "git: NOT FOUND"
command -v claude >/dev/null && claude --version 2>/dev/null || echo "claude-code: NOT FOUND"
uname -sr
```

Note any tool that is missing. Missing `bash` or `git` is a blocker — stop and tell me. Missing `claude` is a soft warning — most prompts in the series use Claude Code but the scratch pattern works without it.

**Step 2 — create the scratch directory.** Run:

```bash
SCRATCH="$HOME/.claude/experiments/$(date +%Y-%m-%d)-027-followalong"
mkdir -p "$SCRATCH"
test -w "$SCRATCH" || { echo "ERROR: scratch not writable"; exit 1; }
echo "scratch=$SCRATCH"
```

Now write the environment check to `$SCRATCH/01-environment.md`.

**Step 3 — create a throwaway test artifact.** Inside scratch, create a small file that simulates the kind of artifact later prompts will work with:

```bash
cat > "$SCRATCH/02-test-artifact.md" <<'EOF'
# Throwaway Test Artifact

This file exists only to prove the undo cycle. It contains no real
content. After the dry-run, it will be deleted along with the entire
scratch directory.

## Body

One line of body content.
EOF
```

Record its byte size and md5 in `$SCRATCH/03-pre-state.md`.

**Step 4 — back the artifact up.** Even on a throwaway, run the same backup motion you will use on a real file:

```bash
TS="$(date +%Y%m%d-%H%M%S)"
cp -p "$SCRATCH/02-test-artifact.md" "$SCRATCH/02-test-artifact.md.bak-$TS"
```

Verify the backup byte-count matches the source. Record both numbers in `$SCRATCH/04-backup-verified.md`. The point of the exercise is to make backup-first muscle memory, not to test whether `cp -p` works.

**Step 5 — modify the artifact.** Append a line:

```bash
echo "Modification at $TS" >> "$SCRATCH/02-test-artifact.md"
```

Record the post-modification byte size and md5 in `$SCRATCH/05-post-state.md`. Confirm the md5 differs from `03-pre-state.md`.

**Step 6 — restore from backup.** Run:

```bash
cp -p "$SCRATCH/02-test-artifact.md.bak-$TS" "$SCRATCH/02-test-artifact.md"
```

Compute the md5 again. Confirm it matches `03-pre-state.md` exactly. Write the result to `$SCRATCH/06-restored.md`.

**Step 7 — clean up the entire scratch directory.** Print the cleanup command but do not yet run it:

```
CLEANUP READY: rm -rf "$SCRATCH"
```

Then ask me to confirm I want to delete scratch. On confirmation, run the cleanup, then run `ls "$HOME/.claude/experiments/" | grep 027-followalong || echo absent` and report the result.

**Step 8 — produce the takeaway.** Write `$SCRATCH/00-FOLLOWALONG.md` *before* cleanup, containing: bash version, git version, claude-code presence, scratch path, backup byte-match (Y/N), restored md5-match (Y/N), and a one-line readiness verdict — `READY` if all checks pass, `BLOCKED` with the missing-tool name otherwise. Print to stdout.
````
