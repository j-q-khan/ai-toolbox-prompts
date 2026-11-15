# Full code: Claude Memory: Give Claude Long-Term Memory with the Official MCP Server

A checklist, config blocks and an instruction written for this video from the memory server's README and code (npm version 2.1.1, read as text), the M.C.P. docs and Anthropic's docs, checked 2026-11-15. Not run by us: start with a test fact, never a password or anything private.

### 1. claude-memory-checklist.md
```
# Claude memory with the official memory server: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/modelcontextprotocol/servers, folder src/memory
  (npm: @modelcontextprotocol/server-memory)
- Made by: the Model Context Protocol team. The repo calls its servers
  reference implementations: educational examples, not production-ready.
- Licence: the memory README says MIT; the repo LICENSE says the project is
  moving from MIT to Apache-2.0 for new code
- Latest version: 2.1.1, published 2026-11-11 (last memory commit the same day)
- Real use: about 92,000 stars and 12,000 forks, for the whole repo of servers;
  10 closed memory issues sampled: 7 closed with a fix
- Reaches: one file (MEMORY_FILE_PATH). No network calls in its code,
  no telemetry, free. What Claude pulls from the file goes into your chat.
- Needs: Node.js 24 or later

## Setup (Claude desktop app)
1. Install Node.js (long-term support version) from nodejs.org.
   Check in PowerShell or Terminal: node --version (24 or higher).
2. Make the folder: mkdir ~/claude-memory
   (the server makes the file, not the folder)
3. Open the config file: Settings, Developer, Edit Config. If your menus differ:
   Windows: %APPDATA%\Claude\claude_desktop_config.json
   Mac: ~/Library/Application Support/Claude/claude_desktop_config.json
   (Windows: Windows key + R, paste %APPDATA%\Claude, Enter.
    Mac: Finder, Shift-Command-G, paste ~/Library/Application Support/Claude.
    In Terminal, put the Mac path in double quotes, because of the space.)
   No claude_desktop_config.json there yet? Make it: Notepad, Save as type
   set to All files; or TextEdit, Format, Make Plain Text; save it with that
   exact name in that folder (Mac save window: Shift-Command-G reaches the
   hidden folder).
4. Paste section 3 (Windows) or section 4 (Mac). Notepad or TextEdit in
   plain text mode. Paste, don't type: one missing comma or bracket breaks it.
   If the file already has anything in it, don't replace it:
   - it has "mcpServers": put the "memory": { ... } entry inside that list,
     with a comma after the entry before it;
   - it has other settings only: put the "mcpServers": { ... } part inside the
     outer curly brackets, with a comma after the setting before it.
5. Save. Quit the app completely (menu bar or system tray), then open it again.
6. Check: plus button in the message box, Connectors, Manage connectors,
   memory. Keep both tool groups on Needs approval.
   Not listed? Look for a missing comma or bracket, check node --version
   shows 24 or higher, check the folder exists, and quit the app fully again.
7. Test in a new chat with a harmless fact. Click Allow Once.
8. Optional: paste the instruction in section 5 at the start of a chat
   (or into the instructions of a Claude Project).
9. The app has its own memory too (Settings, Your Claude, Generate memory
   from chats). To keep memories only in your file, pause it there.

## Never
- Never tell it a password, key, or private details about health, money or
  other people. The memory file is plain text.
- Never use the README's sample prompt as it is: it tells Claude to gather your
  age, gender, location, job and relationships.

## Claude Code too (shares the same file)
- Start Claude Code in a test folder in Manual mode (.claude/settings.json with
  "defaultMode": "default"; Claude Code starts in auto mode otherwise).
- Mac (Terminal):
  claude mcp add memory --env MEMORY_FILE_PATH=~/claude-memory/memory.jsonl -- npx -y @modelcontextprotocol/server-memory@2.1.1
- Windows: the same line with cmd /c before npx.
- Check: claude mcp list. Remove: claude mcp remove memory

## Switch it off
- Delete the "memory": { ... } entry from claude_desktop_config.json, then
  quit and reopen the app.
- To forget everything: delete the folder ~/claude-memory.
```

### 2. Make the folder (PowerShell on Windows or Terminal on a Mac)
```
mkdir ~/claude-memory
```

### 3. Windows: claude_desktop_config.json
```
{
  "mcpServers": {
    "memory": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-memory@2.1.1"],
      "env": {
        "MEMORY_FILE_PATH": "~/claude-memory/memory.jsonl"
      }
    }
  }
}
```

### 4. Mac: claude_desktop_config.json
```
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory@2.1.1"],
      "env": {
        "MEMORY_FILE_PATH": "~/claude-memory/memory.jsonl"
      }
    }
  }
}
```

### 5. The instruction (paste at the start of a chat)
```
At the start of each chat, search the memory server for anything that helps with my question.
Save something to the memory server only when I say "remember".
Never save passwords, keys or private details about health, money or other people.
```
