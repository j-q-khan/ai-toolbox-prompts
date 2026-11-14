mkdir -p "$HOME/server-test/.claude" && cd "$HOME/server-test"
printf 'A made-up note for testing. Nothing private here.\n' > note.txt
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem@2.3.0 --read-only "$HOME/server-test"
claude mcp list
