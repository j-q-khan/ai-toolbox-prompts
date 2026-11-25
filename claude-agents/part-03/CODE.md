# Full code: Claude Agents Teams: Run Several Claude Code Agents at Once

The scratch repo commands, the settings files, the team request, the worktree commands and a worktree subagent, written from Anthropic's Claude Code docs, checked 2026-11-24. They were written from the docs, not run for this video. Try them only in a scratch repo.

### 1. Make the scratch repo (PowerShell on Windows or Terminal on a Mac)
```
# Run these one at a time, in the folder where you keep test work.
# git commit needs your git name and email set once; if they aren't, git tells you how.
mkdir test-bakery-team
cd test-bakery-team
git init
git commit --allow-empty -m "First commit"
mkdir .claude
# Then start Claude Code here once and say yes when it asks whether you trust the folder:
claude
```

### 2. .claude/settings.json (save it in the .claude folder of the scratch repo; Windows: in Notepad, set the box called Save as type to All files; Mac: in TextEdit, choose Format, then Make Plain Text, first)
```
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 3. .claude/settings.json with split panes (the same file, one line added, for chapter 03; quit Claude Code and check claude --version shows 2.1.317 or later first; if it's older, run claude update)
```
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "teammateMode": "auto"
}
```

### 4. .gitignore (save it in the top folder of the scratch repo, with the same Notepad or TextEdit steps)
```
.claude/worktrees/
```

### 5. The team request (type it in Claude Code, in the scratch repo, with the status bar showing manual mode on)
```
Create an agent team to explore an order-tracking tool for Test Bakery, a made-up shop. Spawn three teammates: one on the customer's side, one on the technical design, one playing devil's advocate. Use Sonnet for each teammate. Have them message each other to challenge each other's ideas, then give me one summary. Don't create, change or delete any files.
```

### 6. Two worktree sessions (no experimental setting needed)
```
# Terminal 1, in the top folder of the scratch repo:
claude --worktree menu

# Terminal 2, in the same folder:
claude --worktree tests

# They land in .claude/worktrees/menu and .claude/worktrees/tests, on new branches worktree-menu and worktree-tests.
# See your worktrees:
git worktree list
```

### 7. .claude/agents/test-writer.md (a worktree subagent; it gets its own worktree only while agent teams are off, file 8)
```
---
# Save this as test-writer.md inside .claude/agents/ in the scratch repo, with the same Notepad or TextEdit steps as file 2.
# A worktree holds only what's committed, so commit the code you want tests for first.
# Nothing may go above the first line of dashes. No Bash, so it can write test files in its worktree but can't run commands.
name: test-writer
description: Writes new test files for the code named in its task, working in its own worktree. Use when asked to add tests.
tools: Read, Glob, Grep, Edit, Write
isolation: worktree
model: sonnet
---

You write tests. You work only in your own worktree.

When you are asked for tests:
1. Look at the files named in your task.
2. Write new test files next to them. Don't change the code you are testing, and never delete a file.
3. You can't run commands, so finish with the command that runs the tests, for me to run myself.
```

### 8. .claude/settings.json with agent teams off (the docs' way back to plain subagents)
```
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "0"
  }
}
```
