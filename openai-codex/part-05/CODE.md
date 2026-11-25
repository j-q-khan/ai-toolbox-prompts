# Full code: OpenAI Codex CLI Tutorial: Permissions, AGENTS.md and Daily Commands

The starter AGENTS.md files, the settings lines and the daily-commands checklist from this video, written from OpenAI's official Codex docs (checked 2026-11-24). They were written from the docs, not run for this video. The test command in the starter file is an example for a made-up test-bakery repo: change it to your repo's own.

### 1. AGENTS.md (save at your repo's root)
```
# AGENTS.md (test-bakery)
<!-- To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files,
     as AGENTS.md (capital letters, then .md) in your repo's root folder.
     On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
     Or type /init in Codex at your repo's root for OpenAI's own starter, then add these sections to it.
     test-bakery and npm test are examples: use your own repo's test command. -->

## How to check your work
- Run the tests with: npm test
- If you change a file, run the tests again before saying you're done.

## Don't change
- Never change, print or commit .env files, keys, tokens or passwords.
- Leave the generated build folder alone.

## How to work
- Ask before deleting or renaming any file.
- Keep each change small and focused on the task.
- Explain each change in plain words when you finish.

## Before you say it's done
- The tests pass.
- Show the changed files with /diff.
```

### 2. ~/.codex/AGENTS.md (your global file, for every repo)
```
# ~/.codex/AGENTS.md (global: applies to every repo you open)
<!-- Save in the hidden .codex folder in your home folder:
     Windows: C:\Users\YOU\.codex\AGENTS.md   Mac: /Users/YOU/.codex/AGENTS.md
     Keep it short: Codex stops adding AGENTS.md files once their combined size reaches 32 KiB by default.
     For a temporary change, put it in ~/.codex/AGENTS.override.md instead, and delete that file to go back. -->

## Working agreements
- Ask before deleting or renaming files.
- Keep changes small, and explain each one in plain words.
- Never print, commit or paste keys, tokens or passwords.
```

### 3. config.toml (two lines: make Auto your default)
```
# ~/.codex/config.toml  (Windows: C:\Users\YOU\.codex\config.toml   Mac: /Users/YOU/.codex/config.toml)
# OpenAI's lower-risk local preset ("Auto"): Codex edits and runs routine commands inside your folder,
# and asks before editing outside it or using the network (network access is off by default).
# If the file already exists, add these two lines at the very top, above any line in [square brackets].
# Save as plain text (Notepad: Save as type set to All files; TextEdit: Format, then Make Plain Text).
sandbox_mode    = "workspace-write"
approval_policy = "on-request"
```

### 4. codex-cli-daily-checklist.md
```
# Codex CLI: daily-commands checklist (checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. Plans, prices and commands change often: check https://learn.chatgpt.com/docs/pricing and https://learn.chatgpt.com/docs/developer-commands?surface=cli

## Install (once)
- [ ] Windows, in a new PowerShell window: powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
- [ ] Mac, in Terminal: curl -fsSL https://chatgpt.com/codex/install.sh | sh
- [ ] Latest stable release when checked 2026-11-24: 0.172.0.

## Sign in (once)
- [ ] ChatGPT sign-in: your plan's included usage. The README lists "Plus, Pro, Business, Edu, or Enterprise". Plus was $20 a month when checked 2026-11-24. Free and Go: Codex "in the desktop app, subject to rollout" (pricing page).
- [ ] API key: "Codex uses standard API pricing instead of included ChatGPT plan credits." "Codex cloud requires signing in with ChatGPT."
- [ ] Key route, Mac and Linux only (the docs' line; never type the key itself into a command or a file): printenv OPENAI_API_KEY | codex login --with-api-key
- [ ] Your data: with ChatGPT, usage follows your ChatGPT workspace's permissions and retention settings; with a key, "your API organization's retention and data-sharing settings".
- [ ] Check: codex login status
- [ ] Your login is cached in ~/.codex/auth.json "or in your OS-specific credential store". Treat auth.json "like a password". Never commit it or paste it anywhere.

## Every session
- [ ] Start Codex in a folder Git tracks: codex
- [ ] /status: "the active model, approval policy, writable roots, and current token usage", and your remaining limits.
- [ ] /permissions: Auto for edits; Read Only to plan "without making changes". Never full access ("not recommended").
- [ ] Approving a request? "choose the narrowest scope that lets the task continue."
- [ ] Automatic review is off by default (approvals_reviewer = "user"). Turn it on and "it can add to Codex usage."
- [ ] Git checkpoints "before and after a task so you can revert changes."

## AGENTS.md
- [ ] Global: ~/.codex/AGENTS.override.md if it exists, otherwise ~/.codex/AGENTS.md ("only the first non-empty file").
- [ ] Repo: from the root down to your folder, "at most one file per directory" (AGENTS.override.md, then AGENTS.md).
- [ ] Nearer files win: they "appear later in the combined prompt".
- [ ] Size: the total stops at "32 KiB by default" (project_doc_max_bytes). Keep the root file short; nest the detail.
- [ ] /init writes a starter AGENTS.md in the current folder: look it over, edit, commit.
- [ ] After an edit: /exit, start codex again in the folder you're checking (for example codex --cd services/payments), then ask "List the instruction sources you loaded."

## The daily loop
- [ ] /model: "For a complex debugging task, select GPT-6.2 Astra. For everyday coding, select GPT-6.2 Sol." Then /status to check.
- [ ] Plus figures (not fixed limits): about 6-50 local messages per five hours on GPT-6.2 Astra, 17-180 on GPT-6.2 Sol.
- [ ] /review: issues in your working tree, "focusing on behavior changes and missing tests".
- [ ] /diff: staged, unstaged and untracked changes, "so you can decide what to keep".
- [ ] Tomorrow: codex resume --last (this folder), or codex resume --last --all (every folder).
- [ ] Limits: /status, or https://chatgpt.com/codex/settings/usage ; /statusline can put limits in the footer.
- [ ] Out of plan usage: "All users may also run extra local chats using an API key, with usage charged at standard API rates."

Sources: learn.chatgpt.com/docs/codex/cli ; learn.chatgpt.com/docs/auth ; learn.chatgpt.com/docs/permission-modes ; learn.chatgpt.com/docs/sandboxing ; learn.chatgpt.com/docs/agent-approvals-security ; learn.chatgpt.com/docs/agent-configuration/agents-md ; learn.chatgpt.com/docs/developer-commands?surface=cli ; learn.chatgpt.com/docs/pricing ; github.com/openai/codex
```
