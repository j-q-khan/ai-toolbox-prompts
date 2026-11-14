New-Item -ItemType Directory -Force "$HOME\server-test\.claude" | Out-Null
Set-Location "$HOME\server-test"
Set-Content -Path note.txt -Value "A made-up note for testing. Nothing private here."
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem@2.3.0 --read-only "$HOME\server-test"
claude mcp list
