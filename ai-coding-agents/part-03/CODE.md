# Full code: Codex CLI Install on Windows and Mac: Setup and Your First Task

Written for this video from OpenAI's Codex README and docs and the Codex 0.167.2 source (checked 2026-11-12). The TOML file was parsed with Python's tomllib; nothing was installed or run. Use a new, empty test folder, never your home folder.

### 1. setup-checklist.md
```
# Codex CLI setup checklist (facts checked 2026-11-12, Codex 0.167.2)

## 1. Can you use it?
- [ ] ChatGPT Plus or higher: the pricing page lists the CLI from Plus ($20 a month when checked). Free and Go list Codex in the desktop app only.
- [ ] Or an OpenAI key: billed at API prices, no cloud features.

## 2. Install (no Node.js needed for this route)
- [ ] Windows: open a new PowerShell window and paste: powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
- [ ] Mac: open Terminal and paste: curl -fsSL https://chatgpt.com/codex/install.sh | sh
- [ ] Open a new window and check: codex --version (0.167.2 or later). "codex is not recognized"? Open a new window and try again.

## 3. A key (if you use one), a test folder, then sign in
- [ ] Key users, first: with billing set up on the OpenAI platform, make a fresh key only for this (https://platform.openai.com/api-keys). Then Organization limits, Spend, Edit spend limit, a small Monthly spend limit, Enforce a hard limit on, Save. Alerts alone don't cap spending, and the limit isn't instant.
- [ ] mkdir codex-test, then cd codex-test, then codex. Never your home folder.
- [ ] Plus: Sign in with ChatGPT (the browser opens). Key: Sign in another way, then Use an OpenAI API key, and paste a fresh key made only for this.
- [ ] Your sign-in is kept in ~/.codex/auth.json or your system's password store. Treat auth.json like a password.
- [ ] "Trust this folder?": Trust and continue (it's your empty test folder). Codex saves this choice in ~/.codex/config.toml.
- [ ] Windows, if offered: Set up default sandbox (requires Administrator permissions), then wait for "Setting up sandbox...".

## 4. The Auto preset, written down
- [ ] Type /exit. ~/.codex/config.toml (Windows: %USERPROFILE%\.codex\config.toml) is most likely there already, holding your Trust choice. Open it with the line for your system in install-lines.txt (it makes the file if it's missing) and add to it, never replace it.
- [ ] Paste these at the very top, above any line in [square brackets], then save. If the file already has an approval_policy, sandbox_mode or sandbox_workspace_write line or a [sandbox_workspace_write] section, delete the old one first: a duplicate is an error.
      approval_policy = "on-request"
      sandbox_mode = "workspace-write"
      sandbox_workspace_write.network_access = false
- [ ] It edits and runs commands inside the folder by itself, and asks before editing outside it or going online.
- [ ] Start codex again in codex-test, then /status: next to Permissions, look for Workspace (Ask for approval).
- [ ] Anything else, such as look-only (Read Only)? /permissions, then Ask for approval. A folder Git doesn't track can start this way, asking before every change.

## 5. First task and house rules
- [ ] First task: make a page called index.html with a button that counts clicks, then tell me what you did.
- [ ] If it asks "Would you like to run the following command?", pick 1 (this time) or 3 / Esc (no). Avoid 2 for now.
- [ ] Save AGENTS.md in codex-test (inside your home folder): Notepad, Save as type All files; TextEdit, Make Plain Text first. Then /exit and start codex again so it picks the file up.

## 6. Re-check before you rely on it
- [ ] Plans, prices, versions and menu names change. Check the links in SOURCES.md.
```

### 2. Install and start lines (PowerShell on Windows, Terminal on Mac)
```
# Windows: open a new PowerShell window, paste this line, press Enter (from the Codex README, checked 2026-11-12):
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
# Mac: open Terminal, paste this line, press Enter:
curl -fsSL https://chatgpt.com/codex/install.sh | sh
# Then open a new window. Same on Windows and Mac:
codex --version
# If codex-test already exists, skip mkdir and go straight to cd codex-test.
mkdir codex-test
cd codex-test
codex
# Inside Codex: /status shows the session's settings, /permissions changes them, /exit quits.
# Before editing config.toml, type /exit to leave Codex. Each line below opens the file as plain text, or makes it if it's missing.
# Windows PowerShell (if Notepad offers to create the file, choose Yes):
notepad "$env:USERPROFILE\.codex\config.toml"
# Mac Terminal (opens it in TextEdit):
mkdir -p ~/.codex && touch ~/.codex/config.toml && open -e ~/.codex/config.toml
# Paste the config.toml lines at the very top, save (Ctrl+S or Command+S), then start codex again.
# Another way to start with the Auto preset for one session, named on the command line (docs, Agent approvals & security):
codex --sandbox workspace-write --ask-for-approval on-request
```

### 3. ~/.codex/config.toml (Windows: %USERPROFILE%\.codex\config.toml)
```
# The Auto preset, written down (OpenAI's Codex docs, checked 2026-11-12).
# Edits and commands inside the folder you start in run by themselves; edits outside it and network access ask first.
# Paste these lines at the very top of the file, above any line in [square brackets], and keep what Codex wrote below.
approval_policy = "on-request"
sandbox_mode = "workspace-write"
# network_access in the [sandbox_workspace_write] section, written on one line so it stays a top-level line:
sandbox_workspace_write.network_access = false
```

### 4. AGENTS.md (save in your test folder)
```
# AGENTS.md
## House rules for this folder
- Work only inside this folder.
- Ask me before deleting or renaming any file.
- Keep each change small.
- When you finish, explain each change in plain words.
```

### 5. Saving the files
```
# config.toml goes in the hidden .codex folder in your home folder, and Codex has most likely made it
# already: choosing Trust and continue saves your folder choice there. So open it and add to it, never replace it.
# Type /exit first, then open it with the line for your system in install-lines.txt (it makes the file if it's missing).
# Paste the config.toml lines at the very top, above any line in [square brackets]: a setting pasted below
# one of those belongs to that section instead. If the file already has an approval_policy or sandbox_mode line
# or a sandbox_workspace_write line or [sandbox_workspace_write] section, delete the old one first (a duplicate is an error), and remove any line
# that says approval_policy = "untrusted" (the docs say it's retired and can stop Codex starting).
# Save with Ctrl+S (Windows) or Command+S (Mac).
# AGENTS.md and setup-checklist.md are new files in your test folder (codex-test, inside your home folder):
#   Windows, Notepad: paste, then File, Save as. Set the box called Save as type to All files, and name it AGENTS.md.
#   Mac, TextEdit: Format, then Make Plain Text, then paste. Save it in codex-test as AGENTS.md; if TextEdit asks, choose Use .md.
#   (Shift-Command-G in the save box reaches any folder by its path, such as ~/codex-test.)
# Codex picks up AGENTS.md when a session starts, so type /exit and start codex again after saving it.
```
