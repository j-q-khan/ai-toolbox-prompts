# Full code: How to Add an MCP Server to Claude Code, Claude Desktop and VS Code

Written for this video from the Claude Code, MCP and VS Code docs and the Filesystem server's README (checked 2026-11-13). Use a test folder with a made-up note, never your real files. The JSON was parsed and the shell lines checked for syntax only; nothing was installed or run.

### 1. Make the test folder (with the .claude folder that chapter 3 saves into) and add the server to Claude Code, Windows PowerShell (in a new PowerShell window; using only Claude Desktop or VS Code? run the first three lines to make the folder and the note, and skip the two claude lines)
```
New-Item -ItemType Directory -Force "$HOME\server-test\.claude" | Out-Null
Set-Location "$HOME\server-test"
Set-Content -Path note.txt -Value "A made-up note for testing. Nothing private here."
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem@2.3.0 --read-only "$HOME\server-test"
claude mcp list
```

### 2. The same on a Mac (in the Terminal app; using only Claude Desktop or VS Code? run the first two lines to make the folder and the note, and skip the two claude lines)
```
mkdir -p "$HOME/server-test/.claude" && cd "$HOME/server-test"
printf 'A made-up note for testing. Nothing private here.\n' > note.txt
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem@2.3.0 --read-only "$HOME/server-test"
claude mcp list
```

### 3. .claude/settings.json in the test folder (block 1 or 2 already made the .claude folder; Notepad: Save as, the box called Save as type set to All files, name server-test\.claude\settings.json; Mac: TextEdit, Format, Make Plain Text, then Shift-Command-G to reach server-test/.claude)
```
{
  "permissions": {
    "ask": ["mcp__filesystem__*"],
    "deny": [
      "mcp__filesystem__write_file",
      "mcp__filesystem__edit_file",
      "mcp__filesystem__append_file",
      "mcp__filesystem__create_directory",
      "mcp__filesystem__move_file",
      "mcp__filesystem__copy_file"
    ]
  }
}
```

### 4. Claude Desktop on Windows: %APPDATA%\Claude\claude_desktop_config.json (change yourname; if the file already has "mcpServers", add only the "filesystem" entry inside it; then quit Claude Desktop from the tray and open it again)
```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "C:\\Users\\yourname\\server-test"
      ]
    }
  }
}
```

### 5. Claude Desktop on a Mac: ~/Library/Application Support/Claude/claude_desktop_config.json (change yourname; add only the "filesystem" entry if the file already has "mcpServers"; then quit Claude Desktop from the menu bar and open it again)
```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "/Users/yourname/server-test"
      ]
    }
  }
}
```

### 6. VS Code on Windows: .mcp.json at the top of the server-test folder (change yourname; pick Copilot in the Session Target menu; trust the folder only because it's your own test folder; Claude Code also reads a .mcp.json here and may ask whether to use it: say no, because the server you added with the add line has the same name, and Claude Code uses that one first)
```
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "C:\\Users\\yourname\\server-test"
      ],
      "tools": ["*"]
    }
  }
}
```

### 7. VS Code on a Mac: .mcp.json at the top of the server-test folder (change yourname; as in block 6, if Claude Code asks whether to use this file, say no, because it already uses the server from your add line)
```
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "/Users/yourname/server-test"
      ],
      "tools": ["*"]
    }
  }
}
```

### 8. Claude Desktop on Windows still won't start it? The Filesystem README's own fallback: start npx through cmd /c (use this "filesystem" entry in place of the one in block 4)
```
{
  "mcpServers": {
    "filesystem": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "C:\\Users\\yourname\\server-test"
      ]
    }
  }
}
```

### 9. Claude Code through a file instead of the add line in block 1: .mcp.json in the test folder (use this only if PowerShell drops the two dashes; shared scope, so Claude Code asks you to approve it the first time; it is the same file name VS Code uses, so don't keep VS Code's file in this folder too; change yourname, or use /Users/yourname/server-test on a Mac)
```
{
  "mcpServers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem@2.3.0",
        "--read-only",
        "C:\\Users\\yourname\\server-test"
      ]
    }
  }
}
```

### 10. Switch it off when you're done
```
# Claude Code, in the test folder:
claude mcp remove filesystem
# Claude Desktop: delete the "filesystem" entry from claude_desktop_config.json, then quit Claude Desktop and open it again
# VS Code: Chat: Open Customizations > MCP Servers > the server's ... menu > Disable, or delete server-test\.mcp.json
```

### 11. Not showing up in Claude Desktop? Where its logs are (mcp.log, and mcp-server-filesystem.log for this server)
```
# Windows: %APPDATA%\Claude\logs
# Mac:     ~/Library/Logs/Claude
```
