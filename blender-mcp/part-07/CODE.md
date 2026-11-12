# Full code: Blender MCP with Codex, Gemini CLI, Cursor or a Local Model

Written from the Blender Lab MCP source and wiki (v1.0.3), the Codex, Gemini CLI and Cursor docs, and llama.cpp's README and Web UI source, checked 2026-11-12. Use your blender-test folder from Part 2, a new Blender file with nothing private open, and test models only. Nothing here was installed or run, and Blender, the apps and the server weren't opened; the TOML and JSON were parsed and the shell lines checked with `bash -n`.

### 1. Codex: add the server (macOS or Linux; on Windows, use block 2 only)
```
# In a terminal. This writes the [mcp_servers.blender] table into ~/.codex/config.toml:
codex mcp add blender -- uv --directory "$HOME/blender_mcp/mcp" run blender-mcp
codex mcp list
# Look for: blender. Then paste block 2 at the end of ~/.codex/config.toml.
# Switch off: enabled = false under [mcp_servers.blender]; for good: codex mcp remove blender
```

### 2. Codex: the four ask tables, at the end of ~/.codex/config.toml
```
# Windows only (no codex mcp add): remove the # from the next three lines and put in your own path.
# [mcp_servers.blender]
# command = "uv"
# args = ["--directory", 'C:\Users\you\blender_mcp\mcp', "run", "blender-mcp"]

# "prompt" = Codex asks before the tool runs. Never "writes" for these: the server marks
# render_viewport_to_path as read-only, but it writes an image wherever it's pointed.
[mcp_servers.blender.tools.execute_blender_code]
approval_mode = "prompt"
[mcp_servers.blender.tools.execute_blender_code_for_cli]
approval_mode = "prompt"
[mcp_servers.blender.tools.render_viewport_to_path]
approval_mode = "prompt"
[mcp_servers.blender.tools.render_thumbnail_to_path]
approval_mode = "prompt"
```

### 3. Gemini CLI: add the server from blender-test (macOS or Linux; on Windows, use block 4)
```
# Writes blender-test/.gemini/settings.json. The two dashes hand everything after them to the server.
cd "$HOME/blender-test"
gemini mcp add blender uv -- --directory "$HOME/blender_mcp/mcp" run blender-mcp
# Never add "trust": true or --trust, and don't start Gemini in yolo mode.
# If you've switched on Trusted Folders, trust blender-test when Gemini asks.
# Switch off for good (from blender-test): gemini mcp remove blender
```

### 4. Gemini CLI on Windows: blender-test\.gemini\settings.json (put in your own path)
```
{
  "mcpServers": {
    "blender": {
      "command": "uv",
      "args": ["--directory", "C:\\Users\\you\\blender_mcp\\mcp", "run", "blender-mcp"]
    }
  }
}
```

### 5. Gemini CLI: ~/.gemini/policies/blender.toml (Windows: %USERPROFILE%\.gemini\policies\blender.toml)
```
# Gemini asks before each of these four tools. User-wide, because
# Gemini's workspace policy files are switched off for now.
[[rule]]
mcpName = "blender"
toolName = "execute_blender_code"
decision = "ask_user"
priority = 500

[[rule]]
mcpName = "blender"
toolName = "execute_blender_code_for_cli"
decision = "ask_user"
priority = 500

[[rule]]
mcpName = "blender"
toolName = "render_viewport_to_path"
decision = "ask_user"
priority = 500

[[rule]]
mcpName = "blender"
toolName = "render_thumbnail_to_path"
decision = "ask_user"
priority = 500
```

### 6. Cursor: blender-test/.cursor/mcp.json (any system: Cursor fills in ${userHome}; ${/} is its separator if you prefer)
```
{
  "mcpServers": {
    "blender": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "${userHome}/blender_mcp/mcp", "run", "blender-mcp"]
    }
  }
}
```

### 7. Cursor: the ask setting, and switching it off
```
Cursor: Settings > Agents > Approvals & Execution > Run Mode: Allowlist
Leave every Blender tool off the allowlist (an empty list asks every time).
Never choose Run Everything.
Switch off: Customize in the sidebar, switch blender off, or delete the block from .cursor/mcp.json.
```

### 8. A local model with llama.cpp (the Blender Lab wiki's proof of concept), two terminals
```
# Needs a recent llama.cpp (build 8218 or newer) and a model file that can call tools.
# The wiki names Gemma 4 26B-A4B (about 17 GB) and Qwen3.6 35B-A3B (about 26 GB), tested on an M3 MacBook.
# Terminal 1: the model runner (its chat page is http://127.0.0.1:8080/)
llama-server -m "$HOME/models/your-model.gguf"
# Terminal 2: the server in its HTTP mode, on this computer only (127.0.0.1 is its default)
uv --directory "$HOME/blender_mcp/mcp" run blender-mcp --transport http --port 9191
# Windows PowerShell, terminal 2: uv --directory "$HOME\blender_mcp\mcp" run blender-mcp --transport http --port 9191
# Chat page: MCP Servers, Add new Server, Server URL http://127.0.0.1:9191/, Add, Save settings.
# When it asks "Allow use of ...?", click Allow once. Never Always allow: the browser remembers it.
# This mode has no password and its code accepts requests from any web page: run it only while you chat.
# Switch off: Ctrl+C in both terminals.
```

### 9. Every app: switch Blender off afterwards
```
Blender: Edit > Preferences > Add-ons > MCP > Stop MCP Server (it then says: Server is stopped)
Auto Start stays unticked. System > Network: untick Allow Online Access if nothing else needs it.
```

### Safety checklist
```
[ ] Add-on and server both at v1.0.3 (Part 2)
[ ] The server named blender, in lower case, in every app
[ ] Ask setting saved before the first chat:
    Codex: approval_mode = "prompt" on all four tools (never "writes" or "approve")
    Gemini CLI: four ask_user rules; never "trust": true, --trust or yolo mode
    Cursor: Run Mode Allowlist, no Blender tools on it; never Run Everything
    llama.cpp: Allow once, never Always allow; server running only while you chat
[ ] Prompt 2 made the app ask before the code-running tool ran
[ ] A new Blender file with nothing private open; test models only
[ ] I look over every script before I say yes
[ ] Finished: Stop MCP Server, untick Allow Online Access, Ctrl+C any terminal I started
[ ] Done for good: the app's remove command or delete its block; remove the add-on; delete blender_mcp
Prices checked 2026-11-12: Codex CLI from Plus $20/month (Free and Go $8: desktop app only, rolling out);
Gemini CLI free with a Google account, 1,000 requests a day; Cursor Free (limited agent requests),
Plus $8 (Grok models only), other companies' models from Premium $30, billed by usage; llama.cpp free (MIT).
```
