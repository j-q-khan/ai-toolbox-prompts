# Claude build prompt: AI Coding Agents, Part 4

Use this in Claude Code, Codex or any coding agent, in a new test folder with only setup-checklist.md from this video in it. Start in plan mode, or the agent's read-only mode.

Goal: turn a dated OpenCode 2 checklist into my own setup notes. You install nothing and run nothing.
Steps, in order:
1. Find setup-checklist.md in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Am I on Windows or Mac? On Windows, do I have Node.js, or do I want the standalone zip? Do I connect OpenCode Console's pay-as-you-go models or my own provider key? Have I set a spend limit yet? Do I already have a file at ~/.config/opencode/opencode.jsonc?
3. Using only the checklist and my answers, list my steps in order, quoting the checklist lines you relied on and their checked date. If I already have an opencode.jsonc, tell me to merge the rules into it rather than paste a second file.
4. Tell me which facts in the checklist may have changed since its checked date (versions, prices, menu names, permission names), with the source link for each, so I can check them myself.
5. Write my-opencode-setup.md with: my install line, a test folder to start in (never my home folder), the opencode.jsonc rules exactly as the checklist writes them (shell, external_directory and subagent set to ask for every agent; edit set to ask under agents, build) and where the file goes on my system, how to check them (the Permission required box on a first task), the plan agent (Shift+Tab), and my spend-limit steps.
6. Show me my-opencode-setup.md and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-opencode-setup.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-opencode-setup.md and a three-line summary of my setup.
