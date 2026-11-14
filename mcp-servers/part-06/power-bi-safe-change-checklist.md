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
