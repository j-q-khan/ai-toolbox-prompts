# OpenCode 2 setup checklist (facts checked 2026-11-12, OpenCode 2.2.7)

## 1. What it costs
- [ ] OpenCode itself is free (MIT, by Anomaly). You bring the model.
- [ ] Either OpenCode Console's pay-as-you-go models (some free for a limited time; OpenCode Go was $10 a month when checked), or your own provider's key.

## 2. Install (version 2 only)
- [ ] Windows: install Node.js (https://nodejs.org), open PowerShell and paste: npm install -g @opencode/cli
- [ ] Red error in PowerShell saying running scripts is disabled? Type npm.cmd install -g @opencode/cli instead, and later type opencode.cmd wherever this checklist says opencode.
- [ ] Windows without Node.js: download the standalone zip (https://opencode.ai/update/api/latest/cli/opencode/opencode-windows-x64.zip), extract it, and start opencode.exe by its full path (see install-lines.txt).
- [ ] Mac: open Terminal and paste: curl -fsSL https://opencode.ai/v2/install | bash  (or, with Homebrew: brew install anomalyco/tap/opencode-v2)
- [ ] Open a new window and check: opencode --version (2.2.7 or later). Starts with 1? That's version 1: follow https://opencode.ai/docs/migrate-v1

## 3. Make it ask first, before the first start
- [ ] Windows: paste the Notepad line from install-lines.txt into PowerShell. Notepad asks to create the file: Yes.
- [ ] Mac: paste the TextEdit line from install-lines.txt into Terminal.
- [ ] The file: ~/.config/opencode/opencode.jsonc (Windows: %USERPROFILE%\.config\opencode\opencode.jsonc). Already has text in it? Merge the rules into it; never paste a second { }.
- [ ] Paste opencode.jsonc from this folder, then save (Ctrl+S or Command+S).
- [ ] Every agent: shell, external_directory and subagent set to ask. The build agent: edit set to ask.
- [ ] Mac, to find the file in Finder: Shift-Command-G, then ~/.config/opencode

## 4. A test folder and a model
- [ ] mkdir opencode-test, then cd opencode-test, then opencode. Never your home folder.
- [ ] /connect, then either: OpenCode's pay-as-you-go provider (sign in at https://opencode.ai/console, add billing details and credits, copy your key, paste it), or your own provider with a fresh key made only for this.
- [ ] /models, then pick one. Some say Free; a few free models' providers may keep what you send to improve the model (Console docs, Privacy).
- [ ] Spend limit: Console, Controls, Add policy, Entire workspace, a Budget rule with a monthly amount, Save. Own key: that provider's own spend limit. Running requests finish, so spend can end slightly above a budget.

## 5. First task, the plan agent and house rules
- [ ] First task: make a page called index.html with a button that counts clicks, then tell me what you did.
- [ ] Expect "Permission required" and "Edit index.html": pick Allow once (or Reject). Avoid Always allow for now: it saves a lasting allow rule for this folder.
- [ ] No box, and the file was made anyway? The settings file isn't where it should be, or has the wrong name (opencode.jsonc, in the folder above).
- [ ] Shift+Tab switches Build to Plan (explores and plans without editing your files). Shift+Tab again for Build.
- [ ] Save AGENTS.md in opencode-test: Notepad, Save as type All files; TextEdit, Make Plain Text first. Then Ctrl+X, then N, for a new session.

## 6. Re-check before you rely on it
- [ ] Versions, prices, menu names and permission names change. Check the links in SOURCES.md.
