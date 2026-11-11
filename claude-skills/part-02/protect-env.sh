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
