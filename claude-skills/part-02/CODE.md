# Full code: Claude Skills vs Agents vs MCP vs CLAUDE.md: Which Do You Need?

The same rule, "never edit .env files", written three ways for this video from Anthropic's Claude Code docs (checked 2026-11-11), so you can see the difference: the CLAUDE.md line is a request Claude sees every session, the skill is a request Claude sees when a task matches, and the hook is the guarantee. The skill uses the portable format (name and description only). The hook follows the docs' protect-files example, rewritten to need only bash (no jq); on Windows, bash comes with Git for Windows. Hooks are a Claude Code feature. The JSON and the YAML frontmatter were parsed and the script passed bash -n; nothing was installed or run.

### 1. CLAUDE.md: a house rule, then the rule as a line (a request, loaded every session; CLAUDE.md goes in the top of your folder)
```
- Write dates as day, month, year, like 11 November 2026.
- Never edit, create or delete a .env file. They hold passwords and keys. If a change needs a new value, tell me the exact line and I'll add it myself.
```

### 2. The rule as a skill: .claude/skills/env-file-rules/SKILL.md (a request, loaded when a task matches)
```
---
name: env-file-rules
description: Rules for .env files, which hold passwords and keys. Use when a task touches a .env file, environment variables, API keys or secrets.
---

# Environment files

1. Never edit, create or delete a .env file, or any file named .env.something.
2. If a change needs a new value, tell the user the exact line to add, and let them add it.
3. Never print a value from a .env file in the chat.
```

### 3. The rule as a hook, part 1: .claude/settings.json (Claude Code only; merge into the file if it exists)
```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-env.sh"
          }
        ]
      }
    ]
  }
}
```

### 4. The rule as a hook, part 2: .claude/hooks/protect-env.sh (the guarantee)
```
#!/bin/bash
# protect-env.sh: Claude Code runs this before every Edit or Write.
# Put it in .claude/hooks/ in your folder. On macOS and Linux, make it runnable once:
#   chmod +x .claude/hooks/protect-env.sh
# It needs bash and nothing else: no jq. On Windows, bash comes with Git for Windows
# (free: https://git-scm.com/downloads/win), and you need it: without it, Claude Code
# runs hooks in PowerShell, this script can't run, and every Edit and Write gets blocked.
# Test it once: ask Claude to add a comment to your .env file. It should be refused with the reason below.
# It covers Claude's Edit and Write tools, not a shell command that writes the file.
set -euo pipefail

INPUT=$(cat)
FILE_PATH=""
PATTERN='"file_path"[[:space:]]*:[[:space:]]*"([^"]*)"'
if [[ "$INPUT" =~ $PATTERN ]]; then
  FILE_PATH="${BASH_REMATCH[1]}"
fi
NAME="${FILE_PATH##*/}"
NAME="${NAME##*\\}"

if [[ "$NAME" == ".env" || "$NAME" == .env.* ]]; then
  printf '%s\n' '{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Blocked by a hook: .env files hold passwords and keys."
  }
}'
fi
exit 0
```

**Windows: fix the line endings once (added 2026-11-12).** If you saved protect-env.sh in Notepad, it has Windows line endings, which break a bash script, so the hook can't run and your .env file is quietly no longer protected. Run this once in PowerShell, in your folder, to convert it:

```powershell
((Get-Content .claude/hooks/protect-env.sh -Raw) -replace "`r", "") | Set-Content -NoNewline -Encoding ascii .claude/hooks/protect-env.sh
```

A git clone of this repo already keeps .sh files with Linux line endings.

### 5. Where the files go
```
your-folder/
├── CLAUDE.md                      # section 1: the request, every session
├── .env                           # your secrets: Claude never opens it
└── .claude/
    ├── settings.json              # section 3: registers the hook
    ├── hooks/
    │   └── protect-env.sh         # section 4: the guarantee
    └── skills/
        └── env-file-rules/
            └── SKILL.md           # section 2: the request, when a task matches
```
