# Claude build prompt: AI Coding Agents, Part 1

Use this in Claude Code, or in any of the agents from this video, in a new test folder with only comparison-2026-11-12.csv in it. Start in plan mode, or the agent's read-only mode.

Goal: help me choose one AI coding agent from a dated comparison file, and write me a setup checklist. You install nothing and run nothing.
Steps, in order:
1. Find comparison-2026-11-12.csv in this folder. If it isn't there, stop and tell me to save it from the link in the video's description.
2. Ask me these questions one at a time and wait for each answer: Which paid AI plans do I already have (Claude, ChatGPT, Google AI, Gemini Code Assist through work, none)? Am I on Windows, Mac or Linux? Do I want the agent to ask before every command, or only when it leaves my folder? Do I want to try local models? What's my monthly budget?
3. Recommend one tool using only the facts in the CSV and my answers. Quote the CSV cells you relied on, with the checked date. Don't prefer any tool by default, including the one you are. If two tools tie, say so and say what would break the tie.
4. Tell me which facts in the CSV are prices or limits that may have changed since the checked date, and give me the source link for each, so I can check them myself.
5. Write my-agent-setup.md with: the tool, the plan or key I'll use, a test folder to start in (never my home folder), a throwaway key with a spend limit if I'm paying as I go, and the exact ask-first setting from the CSV's ask_first_setting column, written exactly as it appears there.
6. Show me my-agent-setup.md and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: create only my-agent-setup.md in this folder. Don't edit any other file, don't install anything, don't run commands and don't go online.
Output: my-agent-setup.md and a three-line summary of why you picked that tool.
