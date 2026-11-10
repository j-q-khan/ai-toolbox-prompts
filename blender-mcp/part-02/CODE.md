# Full code: Blender MCP Setup with Claude Code: The Official Add-on, Safely

Written from the Blender Lab MCP source, release and setup wiki (v1.0.3), the Blender 5.2 manual, and Claude Code's MCP, settings and permissions docs, checked 2026-11-10. Use an empty test folder, a new Blender file and test models only. The JSON was parsed and the shell lines checked with `bash -n`; nothing was installed or run, and Blender wasn't opened.

### 1. The add-on, version 1.0.3 (download, keep it zipped, install from disk)
```
https://projects.blender.org/lab/blender_mcp/releases/download/v1.0.3/mcp-1.0.3.zip
# Blender 5.2: Edit, Preferences, Add-ons, the drop-down arrow (top right), Install from Disk, mcp-1.0.3.zip
# Installed from disk, it gets no update notices, so it stays on 1.0.3.
# MCP appears in the Add-ons list: check its box is ticked.
# System, Network: tick Allow Online Access (the add-on won't start without it; it covers every add-on).
# Add-ons, the arrow beside MCP: untick Auto Start, leave Host (localhost) and Port (9876) as they are,
# click Start MCP Bridge Server, and look for: Server is running
```

### 2. Get the server and add it to Claude Code, macOS or Linux (in a new terminal)
```
# Needs Git (git-scm.com) and uv (docs.astral.sh/uv). Gets the server at version 1.0.3 into your home folder:
git clone --depth 1 --branch v1.0.3 https://projects.blender.org/lab/blender_mcp.git "$HOME/blender_mcp"
# A "detached HEAD" note is normal: you're on one fixed version.
# The next line makes the test folder and, inside it, the hidden .claude folder for step 3's settings file:
mkdir -p "$HOME/blender-test/.claude" && cd "$HOME/blender-test"
claude mcp add --transport stdio blender -- uv --directory "$HOME/blender_mcp/mcp" run blender-mcp
# The first start fetches the server's helper libraries (docutils, mcp, pyyaml); they aren't locked to a version.
```

### 2. Get the server and add it to Claude Code, Windows PowerShell (in a new terminal)
```
# Needs Git (git-scm.com) and uv (docs.astral.sh/uv). Gets the server at version 1.0.3 into your home folder:
git clone --depth 1 --branch v1.0.3 https://projects.blender.org/lab/blender_mcp.git "$HOME\blender_mcp"
# A "detached HEAD" note is normal: you're on one fixed version.
# The next line makes the test folder and, inside it, the hidden .claude folder for step 3's settings file:
New-Item -ItemType Directory -Force "$HOME\blender-test\.claude" | Out-Null
Set-Location "$HOME\blender-test"
claude mcp add --transport stdio blender -- uv --directory "$HOME\blender_mcp\mcp" run blender-mcp
```

### 3. .claude/settings.json in the test folder (save it before you start Claude)
```
{
  "permissions": {
    "ask": [
      "mcp__blender__execute_blender_code",
      "mcp__blender__execute_blender_code_for_cli",
      "mcp__blender__render_viewport_to_path",
      "mcp__blender__render_thumbnail_to_path"
    ]
  }
}
```

### 4. Check it (Blender: File, New, General; click the cube, press Delete)
```
claude mcp list
# look for: blender ... Connected (this only means the server started), then start Claude Code:
claude
# ask: Using the blender tools, list what's in the open Blender file. Don't change anything.
# A camera and a light in the answer means it reached Blender.
```

### 5. "Server disconnected": the two places, and the fixes
```
# 1. claude mcp list says: Failed to connect  (the server never started)
#    - uv not found: open a new terminal after installing uv, then try again
#    - wrong folder: the path after --directory must end in blender_mcp/mcp (Windows: blender_mcp\mcp)
#    - the very first start downloads the server's helper libraries and can take longer than Claude Code waits
#      (30 seconds by default): wait, then run claude mcp list again, or run the line below once first
#    - to see the server's own error, run the part after -- in a terminal, then press Ctrl+C:
#      uv --directory "$HOME/blender_mcp/mcp" run blender-mcp
# 2. Connected, but Claude says: Cannot connect to Blender ... Ensure Blender is running with the MCP addon enabled and the server started.
#    - Blender isn't open: open it
#    - the add-on isn't running: Add-ons, MCP, Start MCP Bridge Server, and look for: Server is running
#    - a red line "Online access must be enabled in the system preferences": System, Network, tick Allow Online Access
```

### 6. Switch it off, and remove it when you're done for good
```
# Every time: Blender, Preferences, Add-ons, MCP, Stop MCP Server (it then says: Server is stopped).
# Auto Start stays unticked. Untick Allow Online Access (System, Network) if nothing else needs it.
# If you've turned off auto-save for preferences, save them (the menu at the bottom left of Preferences).
# Done for good, in the test folder:
claude mcp remove blender --scope local
# Then remove the MCP add-on in Blender's Add-ons list (the 5.2 manual's Extensions page: any extension can be removed;
# unticking it only disables it), and delete the blender_mcp folder in your home folder.
```

### Safety checklist
```
[ ] Add-on: mcp-1.0.3.zip, installed from disk (no update notices)
[ ] Server: git clone --branch v1.0.3; its helper libraries are fetched on first start, not locked
[ ] Blender 5.2; Host and Port left as they are (this computer only)
[ ] Auto Start unticked; Start MCP Bridge Server only while working, Stop MCP Server after
[ ] Allow Online Access on only while I need it: it covers every add-on, not this one alone
[ ] .claude/settings.json saved before starting Claude: ask on both execute_blender_code tools and both render_..._to_path tools
[ ] claude mcp list says Connected AND Claude can list what's in the open file
[ ] A new file with nothing private open; a spare computer or a virtual machine is safer still
[ ] I look over every script before saying yes: only bpy and math
[ ] No os, subprocess, socket, urllib, file paths, save or export in Claude's code
[ ] Test models only, never a client's files
[ ] Done for good? claude mcp remove blender --scope local, remove the add-on, delete blender_mcp
```
