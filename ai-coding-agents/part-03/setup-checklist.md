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
