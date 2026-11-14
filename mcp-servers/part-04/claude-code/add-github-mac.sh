#!/bin/zsh
# GitHub MCP Server, look-only, for Claude Code on a Mac (zsh). Test repository and placeholder token only.
mkdir -p "$HOME/github-test/.claude" && cd "$HOME/github-test"
read -rs "GITHUB_MCP_PAT?Paste your GitHub token: " && export GITHUB_MCP_PAT && echo
claude mcp add --transport http github https://api.githubcopilot.com/mcp/readonly --header 'Authorization: Bearer ${GITHUB_MCP_PAT}'
claude mcp list
claude
