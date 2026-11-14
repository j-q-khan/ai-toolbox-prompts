# Block 2. Windows PowerShell, after block 1.
Set-Location "$HOME\model-test"
claude mcp add powerbi -- npx -y @microsoft/powerbi-modeling-mcp@1.0.1 --start --readonly
claude mcp list
