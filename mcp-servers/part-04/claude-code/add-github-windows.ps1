# GitHub MCP Server, look-only, for Claude Code on Windows PowerShell. Test repository only; the token stays in memory.
New-Item -ItemType Directory -Force "$HOME\github-test\.claude" | Out-Null
Set-Location "$HOME\github-test"
$env:GITHUB_MCP_PAT = [System.Net.NetworkCredential]::new('', (Read-Host 'Paste your GitHub token' -AsSecureString)).Password
claude mcp add --transport http github https://api.githubcopilot.com/mcp/readonly --header 'Authorization: Bearer ${GITHUB_MCP_PAT}'
# Not tested: Claude Code's docs say it expands ${VAR} in a server's headers and shows it by name, so the list below should show ${GITHUB_MCP_PAT}, never your token.
# If github shows a cross and 401 with a correct token, Claude Code may treat that name as a credential it reads as empty: use another name in every line.
claude mcp list
claude
