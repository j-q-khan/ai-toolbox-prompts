# Claude build prompt: AI Coding Agents, Part 5

Use this in Claude Code, Codex or any coding agent, in a new test folder with only setup-checklist.md from this video in it. Start in plan mode, or the agent's read-only mode.

Goal: turn a dated checklist for running OpenCode 2 and Codex CLI on a local Ollama model into my own setup notes. You install nothing and run nothing.
Steps, in order:
1. Find setup-checklist.md in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Am I on Windows or Mac? Which agent do I use, OpenCode 2, Codex CLI or both? Did I already set up that agent's ask-first settings (Part 3 for Codex, Part 4 for OpenCode)? How much graphics memory (VRAM) does my computer have, if I know? How much free disk space do I have?
3. Using only the checklist and my answers, list my steps in order, quoting the checklist lines you relied on and their checked date. If I haven't set up the ask-first settings, tell me to do that first and stop.
4. Tell me plainly what the checklist says about speed, memory and disk space for my answers, without adding numbers it doesn't give.
5. Tell me which facts in the checklist may have changed since its checked date (versions, model names and sizes, context defaults, menu names, setting names), with the source link for each, so I can check them myself.
6. Write my-local-agent-setup.md with: my Ollama install line, the model pull line, the Context length setting at 64k and how to check it with ollama ps (CONTEXT and PROCESSOR), and for my agent: OpenCode's /models step with no config for a local Ollama, or Codex's oss_provider = "ollama" line at the very top of config.toml and codex --oss, keeping approval_policy = "on-request" and sandbox_mode = "workspace-write".
7. Show me my-local-agent-setup.md and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-local-agent-setup.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-local-agent-setup.md and a three-line summary of my setup.
