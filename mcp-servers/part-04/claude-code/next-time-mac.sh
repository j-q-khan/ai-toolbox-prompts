#!/bin/zsh
# Next time, Mac (zsh): make a fresh token from token-links.txt first and delete the old one. The server is already added.
cd "$HOME/github-test"
read -rs "GITHUB_MCP_PAT?Paste your GitHub token: " && export GITHUB_MCP_PAT && echo
claude
