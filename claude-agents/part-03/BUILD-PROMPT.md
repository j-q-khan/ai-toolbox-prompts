Try it first on a test branch, or in a copy of your repo in a scratch folder: start Claude Code in the top folder of that branch or copy, then paste this. It doesn't need agent teams turned on, and it starts no teammates. It looks at your repo's file names, asks you for the job, then writes one new file: a plan that splits that job into teammate tasks, with each teammate owning different files. It changes nothing else and runs nothing. Written from Anthropic's Claude Code agent-teams and worktrees docs, checked 2026-11-24. Nothing here was run for the video.

Goal: plan an agent team for one job in this repo and write the plan to a file, without changing any code.
Steps, in order:
1. Ask me, in one question, which job I want a team for, and wait for my answer.
2. Look at this folder's file names and folders to see how the code is laid out. Only look; don't run any commands, tests or installs, and don't open files outside this folder.
3. Decide whether the job needs a team at all. If the helpers wouldn't need to talk to each other, say so and suggest one subagent, or two claude --worktree sessions, instead, and still write the plan.
4. Split the job into three teammates at most. Give each one a short name, one sentence on its role, and the exact files or folders it owns. No file may belong to two teammates.
5. For each teammate, list five or six small tasks, each with a clear result, and say which tasks wait on another task.
6. Write the spawn request I'd paste into Claude Code to start this team, asking for Sonnet for each teammate and telling them to stay inside their own files.
7. Add a short "Before you start" list: teams are experimental and turned on with CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS set to 1 in .claude/settings.json; check the status bar shows manual mode on, because every teammate starts in the main session's permission mode; a team uses more tokens than one session.
Save it as team-plan.md in the top folder. If that file already exists, don't touch it: write team-plan-2.md instead.
Safety: write only that one new file. Don't change any other file, don't start any teammates or subagents, don't change any settings, don't commit anything, and never suggest bypassPermissions or dontAsk.
Output: the new file, then show me the spawn request from step 6.
