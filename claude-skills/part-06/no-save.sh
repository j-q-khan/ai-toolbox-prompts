#!/bin/bash
# no-save.sh: Claude Code runs this before every call to a tool from the openscad server,
# in your chat and inside the model-check fork. It stops the two calls a settings file can't
# tell apart from safe ones: a model call that would create, change or delete a .scad file,
# and a validate call with autofix set to anything but false. export_model is denied in settings.json.
# It needs bash and nothing else: no jq. On Windows, bash comes with Git for Windows
# (free: https://git-scm.com/downloads/win). On macOS and Linux, make it runnable once (section 6).
# onFailure "block" in settings.json (Claude Code 2.1.295 or later) means a hook that can't run blocks the call.
set -euo pipefail

INPUT=$(cat)
INPUT=${INPUT//$'\n'/ }

field() {
  local pattern="\"$1\"[[:space:]]*:[[:space:]]*\"([^\"]*)\""
  if [[ "$INPUT" =~ $pattern ]]; then
    printf '%s' "${BASH_REMATCH[1]}"
  fi
}

TOOL=$(field tool_name)
REASON=""

case "$TOOL" in
  mcp__openscad__model)
    ACTION=$(field action)
    if [[ "$ACTION" != "get" && "$ACTION" != "list" ]]; then
      REASON="Blocked by a hook: in this folder the model tool may only get or list files."
    fi
    ;;
  mcp__openscad__validate)
    AUTOFIX='"autofix"[[:space:]]*:'
    AUTOFIX_OFF='"autofix"[[:space:]]*:[[:space:]]*false[[:space:]]*[,}]'
    if [[ "$INPUT" =~ $AUTOFIX && ! "$INPUT" =~ $AUTOFIX_OFF ]]; then
      REASON="Blocked by a hook: autofix would change the file. This folder only checks."
    fi
    ;;
esac

if [[ -n "$REASON" ]]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"%s"}}\n' "$REASON"
fi
exit 0
