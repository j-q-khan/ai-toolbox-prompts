# Block 4. Exit Claude Code first; only after your DAX questions gave answers you trust. Then start Claude Code and connect to your copy again.
Set-Location "$HOME\model-test"
claude mcp remove powerbi
claude mcp add powerbi -- npx -y @microsoft/powerbi-modeling-mcp@1.0.1 --start
