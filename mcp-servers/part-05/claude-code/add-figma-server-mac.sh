#!/usr/bin/env bash
set -euo pipefail
mkdir -p "$HOME/figma-test/.claude" && cd "$HOME/figma-test"
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp list
