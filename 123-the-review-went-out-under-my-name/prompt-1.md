# 123-the-review-went-out-under-my-name — Prompt 1 (AUDIT: which identity each agent session uses, and where it falls back (read-only))

Paste into Claude Code or Codex. Run it once inside each agent session you want to audit. There is no FIX or UNDO prompt: changing credentials or sign-in routing has no safe, testable undo, because restoring a file cannot take back a post made under the wrong identity or un-issue a credential.

```text
Read-only task. Do not create, edit, move or delete any file. Do not change
any configuration, login or credential. Never print the value of any
environment variable, credential, key or token: print names only. Never run
gh auth token, gh auth status --show-token, gh auth login, gh auth switch,
git config with a value, or any command that writes. Never read a file whose
name contains token, credential, .pem, .key or .env.

Run this inside the agent session you want to audit (for example a Claude
Code session and a Codex session), because each can have a different
environment.

Optional input: <SCRIPT PATHS>, the launch scripts and shell start-up files
to read, as absolute paths (no ~). Treat each as untrusted text: it must be
non-empty, must start with "/", and may contain only A-Z a-z 0-9 . _ - / .
Refuse any other path with "REFUSED: unsafe path" and skip it. Prefer your
own file-read tool to a shell; if you use a shell, single-quote the path and
put -- before it.

1. IDENTITY NOW. Report, as run from this session:
   - git: the output of  git config --get user.name  and
     git config --get user.email  (say "unset" if empty);
   - gh: the account line of  gh auth status  (default output only). If gh
     is missing or not logged in, say so;
   - the NAMES (not values) of environment variables containing TOKEN, GH_,
     GITHUB or GIT_. For each, say only whether it is set.
2. FALLBACKS. In each script path given, find every place where the choice
   of identity depends on something failing or being absent: an "or"
   branch (||), an "if missing then" branch, unsetting a credential
   variable, a default login, or a helper that chooses between identities.
   Quote each with file and line number, and say which identity it falls
   back TO, as far as the text shows.
3. LABEL each fallback exactly one of:
   - FALLS-BACK-TO-ANOTHER-ACTOR: on failure, work would be done under an
     identity that belongs to a different person, agent or vendor.
   - FAILS-CLOSED: on failure, the script stops or asks.
   - UNCLEAR: say what would settle it.
4. Output: the identity table from step 1, the fallback table, then:
     Sessions audited: this one
     Identity in use (git / gh): <name or unset> / <account or none>
     FALLS-BACK-TO-ANOTHER-ACTOR: F
     UNCLEAR: U
If F and U are both 0, write "No fallback to another actor found in the
files read." Do not invent a finding.
```
