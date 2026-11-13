# Claude build prompt: AI Coding Agents, Part 6

Use this in Claude Code, Codex or any coding agent, in a new test folder with only sandbox-checklist.md from this video in it. Start in plan mode, or the agent's read-only mode.

Goal: turn a dated checklist for running coding agents in a Docker sandbox into my own sandbox plan. You install nothing and run nothing.
Steps, in order:
1. Find sandbox-checklist.md in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Am I on Windows 11, Windows 10, an Apple silicon Mac or an Intel Mac? Which agent do I want to run: Claude Code, Codex or OpenCode 2? Do I have git installed? Do I have Docker Desktop? Do I already have a throwaway key with a spend limit for that agent's model company?
3. Using only the checklist and my answers, tell me which route fits: Docker's sbx (Windows 11 or an Apple silicon Mac, with Claude Code or Codex) or the do-it-yourself files (Docker Desktop, with OpenCode 2). Quote the checklist lines you relied on and their checked date. If I have neither the system for sbx nor Docker Desktop, say so and stop.
4. List my steps in order, including the test folder, the first git commit before the agent starts, and the git status, git diff and hooks-folder checks afterwards.
5. Tell me plainly, in the checklist's words, what my route protects and what it doesn't: the shared folder, the key, the network and the kernel.
6. Tell me which facts in the checklist may have changed since its checked date (sbx version, system requirements, startup lines, presets, the OpenCode image version, the OpenCode version in Docker's template), with the source link for each, so I can check them myself.
7. Write my-sandbox-plan.md with my route, my steps, the commands for my system and the checks afterwards. Show it to me and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-sandbox-plan.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-sandbox-plan.md and a three-line summary of my route.
