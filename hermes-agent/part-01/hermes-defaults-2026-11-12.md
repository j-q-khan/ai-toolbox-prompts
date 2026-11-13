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
