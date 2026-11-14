# Full code: Power BI MCP Server with Claude: Connect Your Model Safely

Written for this video from Microsoft's Power BI Authoring MCP docs and README and Anthropic's Claude Code docs (checked 2026-11-14). These steps are for Windows and Power BI Desktop (Microsoft: "The local server doesn't support macOS"). Use a copy of a Microsoft sample file in a test folder, never a work file. The JSON was parsed and the PowerShell lines checked for syntax only; nothing was installed or run.

### 1. Make the test folder and the working copy (Windows PowerShell; run the first line, download a Microsoft sample .pbix such as Store Sales into the model-test folder from the link in the description, then run the other two; open only the copy in Power BI Desktop)
```
New-Item -ItemType Directory -Force "$HOME\model-test\.claude" | Out-Null
Set-Location "$HOME\model-test"
Copy-Item -Path "Store Sales.pbix" -Destination "Store Sales - copy.pbix"
```

### 2. Add the server to Claude Code in safe mode (Windows PowerShell, after block 1)
```
Set-Location "$HOME\model-test"
claude mcp add powerbi -- npx -y @microsoft/powerbi-modeling-mcp@1.0.1 --start --readonly
claude mcp list
```

### 3. .claude/settings.json in the test folder (block 1 made the .claude folder; Notepad: Save as, the box called Save as type set to All files, name model-test\.claude\settings.json)
```
{
  "permissions": {
    "ask": ["mcp__powerbi__*"],
    "deny": [
      "mcp__powerbi__security_role_operations"
    ]
  }
}
```

### 4. Allow changes, still on your copy: exit Claude Code, then in PowerShell add the server again without safe mode (only after your DAX questions gave answers you trust; then start Claude Code and connect to your copy again)
```
Set-Location "$HOME\model-test"
claude mcp remove powerbi
claude mcp add powerbi -- npx -y @microsoft/powerbi-modeling-mcp@1.0.1 --start
```

### 5. Claude Desktop instead: %APPDATA%\Claude\claude_desktop_config.json (if the file already has "mcpServers", add only the "powerbi" entry inside it; quit Claude Desktop from the tray and open it again; then set the server's tools to Needs approval; remove "--readonly" only when you're ready to allow changes)
```
{
  "mcpServers": {
    "powerbi": {
      "command": "npx",
      "args": [
        "-y",
        "@microsoft/powerbi-modeling-mcp@1.0.1",
        "--start",
        "--readonly"
      ]
    }
  }
}
```

### 6. Claude Code through a file instead of the add line in block 2, if PowerShell drops the two dashes: .mcp.json in the model-test folder (shared scope, so Claude Code asks you to approve it the first time; block 3's settings still apply)
```
{
  "mcpServers": {
    "powerbi": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@microsoft/powerbi-modeling-mcp@1.0.1",
        "--start",
        "--readonly"
      ]
    }
  }
}
```

### 7. Check what it did, then switch it off
```
# Audit logs, a daily file for each running server (operation type and success; no DAX text, no model contents):
#   %LOCALAPPDATA%\Microsoft\powerbi-authoring-mcp\Logs
# Save the copy in Power BI Desktop only when you're happy with the change.
# Switch it off: exit Claude Code, then in PowerShell, in the model-test folder:
claude mcp remove powerbi
# Claude Desktop: delete the "powerbi" entry from claude_desktop_config.json, then quit and open it again
```

### 8. power-bi-safe-change-checklist.md
```
# Power BI MCP server: safe-change checklist (facts checked 2026-11-14)
# Save it: copy this text from the link in the description.
# Windows: paste into Notepad, Save as, set the box called Save as type to All files, name it power-bi-safe-change-checklist.md

## Before you connect
- [ ] Microsoft's own server: github.com/microsoft/powerbi-modeling-mcp (now called Power BI Authoring MCP). One exact version: 1.0.1 (November 6, 2026).
- [ ] Windows: "The local server doesn't support macOS."
- [ ] I looked through the licence terms (EULA.txt). The software "may collect information about you and your use of the software and send it to Microsoft."
- [ ] The repo holds docs and screenshots, not the server's code, so I limit what it can do and check what it did.

## Back up
- [ ] Microsoft: "An agent writes to your model, and its changes might be irreversible."
- [ ] A Microsoft sample .pbix, never a work file, in a test folder: an untouched original plus a working copy.
- [ ] Only the copy is open in Power BI Desktop.
- [ ] My own models later: File, Save as, type Power BI Project (*.pbip), kept in Git, so I see every changed line and have a way back.
- [ ] Table names, measures and query results go to my chat model's provider: sample data only.

## Connect in safe mode
- [ ] Added with --readonly ("Safe mode, prevents any write operations").
- [ ] .claude/settings.json: "ask": ["mcp__powerbi__*"], plus a deny rule for mcp__powerbi__security_role_operations (who sees what data).
- [ ] Every tool can take a list of items in one call, so I check each call names only the item I asked about before I approve.
- [ ] Never "mcp__*" in "allow".
- [ ] No key or token needed. A service principal's secret (AZURE_CLIENT_SECRET) goes in an environment variable, never in a file I share.
- [ ] Microsoft's powerbi-authoring plugin registers @latest with changes on; I add the server by hand with one exact version and --readonly instead.
- [ ] Plugin already installed? Uninstall it first: its copy of the server has its own tool names (mcp__plugin_powerbi-authoring_powerbi-modeling-mcp__...), so my mcp__powerbi__* ask rule doesn't cover it, and two copies of the server would give Claude overlapping tools.

## Ask before any change
- [ ] Connect: Connect to '[my copy's file name]' in Power BI Desktop
- [ ] First question only looks: List the tables and measures in this model.
- [ ] A DAX question I can check against a report page I trust, with the DAX shown.
- [ ] Prompt injection: text in someone else's model (a description) could try to give Claude orders. Claude asking first is the safety net.
- [ ] DAX queries return at most 100,000 rows.

## One change at a time
- [ ] Exited Claude Code, added the server again without --readonly in PowerShell, still on the copy, then connected again.
- [ ] The server's own prompt asks "once per database"; my ask rule asks at every call.
- [ ] One small change, shown to me before I approve, checked in Power BI Desktop, then the next.
- [ ] Something wrong? The original is untouched: throw the copy away and start again.

## Check and switch off
- [ ] Audit log: %LOCALAPPDATA%\Microsoft\powerbi-authoring-mcp\Logs, a daily file for each running server (operation type and success; no DAX text, no model contents).
- [ ] Save the copy only when I'm happy.
- [ ] Exited Claude Code, then ran: claude mcp remove powerbi
```
