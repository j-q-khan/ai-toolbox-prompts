# Claude build prompt: AI Coding Agents, Part 2

Use this in Claude Code, or in any coding agent, in a new test folder with only setup-checklist.md from this video in it. Start in plan mode, or the agent's read-only mode.

Goal: help me pick Gemini CLI or Antigravity CLI from a dated checklist, and write my own setup notes. You install nothing and run nothing.
Steps, in order:
1. Find setup-checklist.md in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Is my Google account personal (free, Pro or Ultra), or does my company give me Gemini Code Assist Standard or Enterprise? Am I on Windows or Mac? If Windows, which version? Will I pay as I go with a key?
3. Pick one tool using only the checklist and my answers, and quote the lines you relied on with their checked date. If my answers don't fit either tool, say so.
4. Tell me which facts in the checklist may have changed since its checked date (prices, quotas, the starting mode, model lists), with the source link for each, so I can check them myself.
5. Write my-google-agent-setup.md with: the tool, my install line, a test folder to start in (never my home folder), the ask-first setting written exactly as the checklist writes it (Agent Mode default and Tool Permission request-review for Antigravity CLI, or --approval-mode default for Gemini CLI), the data-sharing switch, and a monthly spend cap if I pay as I go.
6. Show me my-google-agent-setup.md and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-google-agent-setup.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-google-agent-setup.md and a three-line summary of why you picked that tool.
