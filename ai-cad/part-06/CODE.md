# Full code: FreeCAD MCP Server: Connect Claude to FreeCAD

Written from the freecad-mcp README and docs (v0.1.30), Claude Code's MCP and permissions docs and uv's docs, checked 2026-11-07. Use an empty test folder and test parts only. The JSON was parsed, the shell lines checked with `bash -n` and the Python with `py_compile`; nothing was installed or run.

### 1. The add-on, version 0.1.30 (download, unzip, copy the FreeCADMCP folder)
```
https://github.com/neka-nat/freecad-mcp/archive/refs/tags/v0.1.30.zip
# Unzip it. Copy this folder only, not the whole zip: freecad-mcp-0.1.30/addon/FreeCADMCP
# (the one with InitGui.py directly inside it). It isn't in FreeCAD's Addon Manager.
```

### 2. Find FreeCAD's add-on folder (FreeCAD: View, Panels, Python console; paste, press Enter)
```
import os; print(os.path.join(FreeCAD.getUserAppDataDir(), "Mod"))
```

### 3. Start the add-on (after copying FreeCADMCP into that Mod folder and restarting FreeCAD)
```
Workbench list: MCP Addon
Toolbar: Start RPC Server
Bottom of the window: RPC Server started at 127.0.0.1:9875 (PID ...)
In the FreeCAD MCP menu, check these are unticked: Remote Connections, Auto-Start Server
(they're saved between sessions, so check even if you tried the add-on before)
When you finish: Stop RPC Server
```

### 4. Add the server, macOS or Linux (in a new terminal)
```
mkdir -p "$HOME/freecad-test" && cd "$HOME/freecad-test"
claude mcp add --transport stdio freecad -- uvx freecad-mcp@0.1.30
```

### 4. Add the server, Windows PowerShell
```
New-Item -ItemType Directory -Force "$HOME\freecad-test" | Out-Null
Set-Location "$HOME\freecad-test"
claude mcp add --transport stdio freecad -- uvx freecad-mcp@0.1.30
# Server fails to start on Windows? The freecad-mcp installation guide lists a workaround
# (Windows client launch troubleshooting, issue 140). Not tested by us.
```

### 5. .claude/settings.json in the test folder (save it before you start Claude)
```
{
  "permissions": {
    "ask": [
      "mcp__freecad__execute_code",
      "mcp__freecad__execute_code_async"
    ],
    "deny": [
      "mcp__freecad__execute_code_headless",
      "mcp__freecad__run_fem_analysis"
    ]
  }
}
```

### 6. Check it (in the same folder)
```
claude mcp list
# look for: freecad  ✔ Connected (this only means the server started), then start Claude Code:
claude
# ask: Which documents are open in FreeCAD? An answer naming your file means it reached FreeCAD.
# "Failed to connect to FreeCAD"? Click Start RPC Server in FreeCAD and ask again.
```

### 7. Optional: a password (auth token) for the add-on
```
# 1. Make a long random value (on Windows, type py instead of python3):
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
# 2. In FreeCAD: FreeCAD MCP menu, Set Auth Token, paste it, then Stop RPC Server and Start RPC Server
# 3. Add the server again with the same value. Claude Code keeps it in plain text in ~/.claude.json, under this folder.
claude mcp remove freecad --scope local
claude mcp add --env FREECAD_MCP_TOKEN=paste-the-same-value-here --transport stdio freecad -- uvx freecad-mcp@0.1.30
```

### 8. Switch it off, and remove both halves when you're done for good
```
# In FreeCAD: Stop RPC Server. Then, in the test folder:
claude mcp remove freecad --scope local
# Last, delete the FreeCADMCP folder from FreeCAD's Mod folder and restart FreeCAD:
# its code loads every time FreeCAD starts, even with the RPC server stopped.
# The add-on's settings (and any auth token, in plain text) stay in freecad_mcp_settings.json,
# one folder above Mod; delete that file too.
```

### Safety checklist
```
[ ] Add-on from the v0.1.30 zip; server pinned: uvx freecad-mcp@0.1.30
[ ] PyPI maintainer and version checked against github.com/neka-nat/freecad-mcp (tag v0.1.30)
[ ] Remote Connections and Auto-Start Server unticked (the defaults)
[ ] Start RPC Server only while working; Stop RPC Server after
[ ] .claude/settings.json saved before starting Claude: ask on execute_code, deny headless and FEM
[ ] claude mcp list says Connected AND Claude can name the open documents
[ ] I look at every execute_code script before saying yes: only FreeCAD, Part, PartDesign, Sketcher
[ ] No os, subprocess, socket, urllib, file paths, save or export in Claude's code
[ ] Numbers before the picture: bounding box, volume, valid shape
[ ] Backup of the real file first; I save and export myself
[ ] Only the test document open in FreeCAD while Claude is connected
[ ] Test parts only, never a client's files
[ ] Done for the day? Stop RPC Server
[ ] Done for good? claude mcp remove freecad --scope local, then delete Mod/FreeCADMCP and freecad_mcp_settings.json
```
