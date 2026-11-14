# Full code: GitHub MCP Server with Claude Code and VS Code: Read-Only First

Written for this video from GitHub's MCP Server README and docs, GitHub Docs and the Claude Code and VS Code docs (checked 2026-11-14). Use a private test repository with a made-up issue, never your real work. Every token is a placeholder: never paste a real one into a file. The JSON was parsed and the shell lines checked for syntax only; nothing was installed or run.

### 1. Token links: open one while signed in to GitHub, then under Repository access pick Only select repositories and choose your test repository by hand (the link can't do that part)
```
# Look-only token, 7 days, view-only Contents, Issues and Pull requests (Metadata comes with it):
https://github.com/settings/personal-access-tokens/new?name=MCP+look-only+test&description=GitHub+MCP+server+test,+one+repo&expires_in=7&contents=read&issues=read&pull_requests=read

# Later, for chapter 5 only: Issues raised to read and write, everything else unchanged:
https://github.com/settings/personal-access-tokens/new?name=MCP+issues+test&description=GitHub+MCP+server+test,+issues+only&expires_in=7&contents=read&issues=write&pull_requests=read

# Click Generate token and leave that page open: copy the token only when the line in block 2 or 3 asks for it, because copying these lines first would replace it on your clipboard.
```

### 2. Claude Code on Windows, in a new PowerShell window: make the test folder, keep the token in memory only, add the look-only server, then start Claude Code in the same window; paste the first three lines, paste your token when it asks, then paste the rest (VS Code only? run only the first line, to make the folder)
```
New-Item -ItemType Directory -Force "$HOME\github-test\.claude" | Out-Null
Set-Location "$HOME\github-test"
$env:GITHUB_MCP_PAT = [System.Net.NetworkCredential]::new('', (Read-Host 'Paste your GitHub token' -AsSecureString)).Password
claude mcp add --transport http github https://api.githubcopilot.com/mcp/readonly --header 'Authorization: Bearer ${GITHUB_MCP_PAT}'
# Not tested: Claude Code's docs say it expands ${VAR} in a server's headers and shows it by name, so the list below should show ${GITHUB_MCP_PAT}, never your token.
# If github shows a cross and 401 with a correct token, Claude Code may treat that name as a credential it reads as empty: use another name in every line.
claude mcp list
claude
```

### 3. The same on a Mac, in the Terminal app; paste the first two lines, paste your token when it asks, then paste the rest (zsh, the default shell; in bash, use: read -rsp 'Paste your GitHub token: ' GITHUB_MCP_PAT; VS Code only? run only the first line, to make the folder; the two notes in block 2 apply here too)
```
mkdir -p "$HOME/github-test/.claude" && cd "$HOME/github-test"
read -rs "GITHUB_MCP_PAT?Paste your GitHub token: " && export GITHUB_MCP_PAT && echo
claude mcp add --transport http github https://api.githubcopilot.com/mcp/readonly --header 'Authorization: Bearer ${GITHUB_MCP_PAT}'
claude mcp list
claude
```

### 4. github-test/.claude/settings.json (block 2 or 3 made the .claude folder; Notepad: the box called Save as type set to All files; Mac: TextEdit, Format, Make Plain Text, then Shift-Command-G to reach github-test/.claude)
```
{
  "permissions": {
    "ask": ["mcp__github__*"]
  }
}
```

### 5. VS Code: .mcp.json at the top of the github-test folder (first switch off the built-in github-mcp-server: Chat: Open Customizations, MCP Servers, its ... menu, Disable (Workspace); Copilot asks you to Authenticate the first time; if Claude Code asks whether to use this file, say no, because it already uses the server from your add line)
```
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/readonly",
      "tools": ["*"]
    }
  }
}
```

### 6. VS Code with your one-repository token instead of the sign-in (use this .mcp.json in place of block 5; quit every VS Code window first, set GITHUB_MCP_PAT as in block 2 or 3, then start VS Code from that same window with: code . ; on a Mac, the code command needs Shell Command: Install 'code' command in PATH first; edit this file directly, because the workspace form rejects ${...})
```
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/readonly",
      "headers": {
        "Authorization": "Bearer ${GITHUB_MCP_PAT}"
      },
      "tools": ["*"]
    }
  }
}
```

### 7. One exact version on your own computer: the local server in Docker, version 2.1.0, look-only (Docker must be installed and running; remove the hosted one first; set GITHUB_MCP_PAT as in block 2 or 3, then run this in the same window)
```
claude mcp remove github
claude mcp add github -e 'GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_MCP_PAT}' -- docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN -e GITHUB_READ_ONLY=1 ghcr.io/github/github-mcp-server:v2.1.0
claude mcp list
```

### 8. Chapter 5, changes on purpose, in Claude Code: after making the issues token from block 1 and setting GITHUB_MCP_PAT to it, swap the look-only address for the full one
```
claude mcp remove github
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header 'Authorization: Bearer ${GITHUB_MCP_PAT}'
# VS Code: don't drop /readonly from block 5 (its sign-in reaches every repository your account can).
# Use block 6 instead, with "url": "https://api.githubcopilot.com/mcp/", so changes stay on your one test repository.
```

### 9. Chapter 5: github-test/.claude/settings.json with changes switched on (replaces block 4; every tool still asks, and the five that change code or can't be undone are blocked)
```
{
  "permissions": {
    "ask": ["mcp__github__*"],
    "deny": [
      "mcp__github__merge_pull_request",
      "mcp__github__push_files",
      "mcp__github__create_or_update_file",
      "mcp__github__delete_file",
      "mcp__github__delete_repository"
    ]
  }
}
```

### 10. Optional: load fewer toolsets (add this header to the add line in block 2 or 3, after the Authorization header; the hosted server ignores names it doesn't know)
```
--header 'X-MCP-Toolsets: repos,issues'
```

### 11. Switch it off when you're done
```
# Claude Code, in the github-test folder:
claude mcp remove github
# VS Code: Chat: Open Customizations, MCP Servers, github's ... menu, Disable, or delete github-test\.mcp.json
# VS Code, optional: turn the built-in github-mcp-server back on from the same menu
# GitHub: profile picture, Settings, Developer settings, Fine-grained tokens, your token, Delete
# Deleting the token ends the token's access. Disabling the server stops VS Code using your sign-in; to end that sign-in itself, see
# https://docs.github.com/en/apps/using-github-apps/reviewing-and-revoking-authorization-of-github-apps (revoking an app there may sign it out elsewhere too)
# Close the terminal window: the GITHUB_MCP_PAT variable goes with it
```

### 12. Next time, on Windows, in a new PowerShell window (make a fresh token from block 1's link first, and delete the old one; the server is already added, so there's no add line; paste the first two lines, paste your token when it asks, then type claude)
```
Set-Location "$HOME\github-test"
$env:GITHUB_MCP_PAT = [System.Net.NetworkCredential]::new('', (Read-Host 'Paste your GitHub token' -AsSecureString)).Password
claude
```

### 13. Next time, on a Mac, in a new Terminal window (zsh; make a fresh token from block 1's link first, and delete the old one; the server is already added, so there's no add line; paste the first two lines, paste your token when it asks, then type claude)
```
cd "$HOME/github-test"
read -rs "GITHUB_MCP_PAT?Paste your GitHub token: " && export GITHUB_MCP_PAT && echo
claude
```
