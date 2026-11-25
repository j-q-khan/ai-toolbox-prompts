# Full code: Claude Agents in Claude Code: Make Your First Subagent

The reviewer subagent file, a starter AGENTS.md, the CLAUDE.md import and the folder commands, written from Anthropic's Claude Code docs, checked 2026-11-24. They were written from the docs, not run for this video.

### 1. .claude/agents/reviewer.md
```
---
# Save this as reviewer.md inside .claude/agents/ at the top of your repo (Anthropic's Claude Code docs, checked 2026-11-24).
# Windows: in Notepad, set the box called Save as type to All files. Mac: in TextEdit, choose Format, then Make Plain Text, first.
# Nothing may go above the first line of dashes. The tools line lists no Edit, Write or Bash, so it can look but can't change files.
name: reviewer
description: Reviews code for bugs, security problems and readability without changing any files. Use after writing or changing code.
tools: Read, Glob, Grep
model: sonnet
---

You are a careful code reviewer. You can look at files, but you never change them.

When you are asked for a review:
1. Review the files named in your task. If none are named, look over the folder you started in.
2. For each problem, give the file name and line number, say what is wrong and why it matters, and suggest a fix in words or as a short snippet.
3. Put security problems first, then bugs, then readability.
4. If something looks fine, say so in one line. Don't invent problems.

Finish with the three changes you would make first.
```

### 2. AGENTS.md (example for a made-up repo, Test Bakery; save it at the top of your repo, with the same Notepad or TextEdit steps as file 1)
```
# Test Bakery: instructions for coding agents

## Setup
- Install dependencies: npm install

## Tests
- Run all tests: npm test

## Code style
- Small functions and clear names.
- Comments only where the reason isn't obvious.

## Reviews
- Point out each problem with its file name and line number.
```

### 3. CLAUDE.md (only if your repo needs one too; the docs' import, so AGENTS.md still loads; same save steps as file 1)
```
@AGENTS.md

## Claude Code
- Use the reviewer subagent after you change code.
```

### 4. Make the folders from your terminal (if you save the file yourself)
```
# Windows PowerShell, in the top folder of your repo:
mkdir .claude\agents

# Mac Terminal, in the top folder of your repo:
mkdir -p .claude/agents

# Then check your version (AGENTS.md loads directly from v2.1.277):
claude --version
```
