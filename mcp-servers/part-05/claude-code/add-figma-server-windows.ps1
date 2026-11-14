New-Item -ItemType Directory -Force "$HOME\figma-test\.claude" | Out-Null
Set-Location "$HOME\figma-test"
claude mcp add --transport http figma https://mcp.figma.com/mcp
claude mcp list
