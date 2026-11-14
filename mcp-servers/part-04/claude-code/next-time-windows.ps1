# Next time, Windows PowerShell: make a fresh token from token-links.txt first and delete the old one. The server is already added.
Set-Location "$HOME\github-test"
$env:GITHUB_MCP_PAT = [System.Net.NetworkCredential]::new('', (Read-Host 'Paste your GitHub token' -AsSecureString)).Password
claude
