# Claude build prompt: AI Coding Agents, Part 3

Use this in Claude Code, Codex or any coding agent, in a new test folder with only setup-checklist.md from this video in it. Start in plan mode, or the agent's read-only mode.

Goal: turn a dated Codex CLI checklist into my own setup notes. You install nothing and run nothing.
Steps, in order:
1. Find setup-checklist.md in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Am I on Windows or Mac? Do I sign in with ChatGPT Plus (or a higher plan), or with an OpenAI key? If a key, have I set a hard monthly spend limit yet? Do I already have a file at ~/.codex/config.toml?
3. Using only the checklist and my answers, list my steps in order, quoting the checklist lines you relied on and their checked date. If my answers don't fit (for example, a Free or Go plan with no key), say so plainly.
4. Tell me which facts in the checklist may have changed since its checked date (plans and prices, the version, menu names), with the source link for each, so I can check them myself.
5. Write my-codex-setup.md with: my install line, a test folder to start in (never my home folder), the three config.toml settings exactly as the checklist writes them (approval_policy = "on-request", sandbox_mode = "workspace-write", sandbox_workspace_write.network_access = false) and where they go (at the very top of the file, which Codex has most likely made already), how to check them with /status, what to do if Codex starts look-only (/permissions, then Ask for approval), and my spend-limit steps if I use a key.
6. Show me my-codex-setup.md and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-codex-setup.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-codex-setup.md and a three-line summary of my setup.
