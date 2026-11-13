# Full code: What Is Hermes Agent? The Open-Source AI Agent That Learns, Explained

A defaults sheet and a checklist written for this video from Hermes Agent's own README and docs (checked 2026-11-12, version 0.23.1). Defaults change between versions; check the source link in each row before you rely on one. Nothing was installed or run.

### 1. hermes-defaults-2026-11-12.md
```
# Hermes Agent defaults, in the docs' own words (checked 2026-11-12, v0.23.1)

| Area | Setting | Default | What the docs say | Source |
|---|---|---|---|---|
| Where commands run | terminal.backend | local | "Isolation: None — runs on host" | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| Command approval | approvals.mode | smart | "Use an auxiliary LLM to assess risk." Low-risk commands are approved for that command only, "Genuinely dangerous commands are auto-denied. Uncertain cases escalate to a manual prompt." | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| The manual setting | approvals.mode: manual | not the default | "Always prompt the user for approval on dangerous commands." Only commands that match "a curated list of dangerous patterns" are checked. | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| File edits | HERMES_WRITE_SAFE_ROOT (optional) | unset; protected paths always blocked for write_file and patch | write_file and patch are checked against a denylist (for example ~/.ssh/ and ~/.aws/), with "no approval prompt"; other writes don't go through command approval. The docs add that the terminal tool "can still `cat` or overwrite denied paths via shell commands." | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| Memory saves | memory.write_approval | false | "By default the agent saves memory freely — including from the background self-improvement review" | https://hermes-agent.nousresearch.com/docs/user-guide/features/memory |
| Skill saves | skills.write_approval | false | "false = write freely (default)" | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills |
| Background review | auxiliary.background_review | your main chat model | "The review runs on your main chat model by default" | https://hermes-agent.nousresearch.com/docs/user-guide/features/memory |
| Borrowed logins | auth.adopt_external_logins | true | Hermes can borrow Claude Code's and Codex CLI's logins when it has none of its own. | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| Memory size | memory.memory_char_limit, memory.user_char_limit | 2200, 1375 | MEMORY.md "2,200 chars", USER.md "1,375 chars" | https://hermes-agent.nousresearch.com/docs/user-guide/features/memory |

Part 2 of the series sets up the careful version: Blank Slate setup, approvals.mode set to manual, a test folder (the local backend still has no isolation), and a throwaway key with a spend limit.
```

### 2. is-hermes-agent-for-me.md
```
# Is Hermes Agent for me? A checklist (facts checked 2026-11-12, v0.23.1)

## 1. It suits you if
- [ ] You do the same kinds of jobs again and again, and you're tired of explaining your setup every time.
- [ ] You're happy to type a few commands in a terminal (PowerShell on Windows, Terminal on a Mac).
- [ ] You want to choose your own model: a provider's key, Nous Portal, or a free model on your own computer (needs a strong machine).
- [ ] You'd like to message your agent from Telegram, Discord, Slack, WhatsApp or Signal (the gateway, which you start on purpose).

## 2. It's worth waiting if
- [ ] You only need quick answers: a chat assistant does that well.
- [ ] You'd rather not let a program run commands on your main computer until you know its settings (Part 2 covers them).

## 3. Know these defaults before you install
- [ ] Commands run straight on your computer ("Isolation: None").
- [ ] Approvals default to smart: a second model judges risky commands and asks you only when unsure.
- [ ] The manual setting asks only for commands on its dangerous-pattern list, not before every action.
- [ ] Memory and skills save freely, including from the background review, which runs on your main model.
- [ ] It borrows Claude Code and Codex logins by default when it has none of its own.

## 4. Want to compare first?
- [ ] The alternative to look at is OpenClaw, another open-source agent from a different team (Part 3 of the series).

## 5. Next video
- [ ] Part 2: Hermes Agent Setup: Install It on Windows and Mac the Safe Way.
```
