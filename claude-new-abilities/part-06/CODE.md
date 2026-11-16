# Full code: Unity MCP with Claude Code: Can Claude Make a Unity Game?

A checklist and commands written for this video from the repo's files at tag v10.3.0 (read as text), its docs, Unity's docs, uv's docs, Microsoft's docs and Anthropic's Claude Code docs, checked 2026-11-15. Not run by us: try it in a new, empty Unity test game first.

### 1. unity-mcp-checklist.md
```
# Unity MCP with Claude Code: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/CoplayDev/unity-mcp ("MCP for Unity", by Coplay,
  sponsored by Aura). Not affiliated with Unity Technologies.
- Licence: MIT
- Latest release: v10.3.0, 2026-10-04 (last commit 2026-11-14)
- Real use: about 16,000 stars, 1,600 forks; issues 457 closed, 58 open;
  7 closed issues sampled: the same core contributor closed 5, 4 with a fix
- Unity versions: 2021.3 LTS to 6.x (Unity Personal: free under $200K of
  revenue and funds raised in the last 12 months, unity.com, 2026-11-15).
  Unity Hub needs you signed in with a Unity licence to create a game.
- Reaches (core tools, on by default): scenes, GameObjects, scripts
  (create and delete), assets, packages, menu items, builds.
  execute_code (runs any C# in the editor) is off by default: leave it off.
- Telemetry: ON by default, to https://api-prod.coplay.dev/telemetry/events.
  Off: UNITY_MCP_DISABLE_TELEMETRY=true in Unity's environment, set BEFORE
  Unity Hub opens (Unity starts the server; it inherits Unity's settings).
- Costs: free. Optional AI asset generation uses your own paid keys
  (fal.ai, OpenRouter, Tripo, Sketchfab): leave it off.
- Unity's own route: Unity's official plugin for Claude Code (Unity 6.0+).
  Unity's older in-editor MCP server (AI beta) is deprecated.

## Setup (one new, empty test game)
1. Install Git (git-scm.com), Python 3.10+ (python.org) and uv
   (docs.astral.sh/uv; its install lines are in sections 2 and 3 below).
   Open a new window, then check: git --version, python --version
   (Mac: python3 --version), uv --version
   Mac: the first git command may offer Apple's developer tools: accept.
2. Telemetry off, before Unity Hub opens:
   Windows (PowerShell): setx UNITY_MCP_DISABLE_TELEMETRY true
     It prints SUCCESS. Quit Unity Hub fully (also its icon near the clock),
     then open it again.
   Mac (Terminal): quit Unity Hub, then start it from Terminal:
     UNITY_MCP_DISABLE_TELEMETRY=true \
     "/Applications/Unity Hub.app/Contents/MacOS/Unity Hub"
     (Unity Hub's path, from Unity's Hub docs.) Keep that Terminal window open; do this each time you open Unity Hub.
3. Unity Hub: New project, a 3D template, Project name unity-test,
   Location: leave it on your user folder (C:\Users\you or /Users/you),
   then Create project.
4. Unity: Window > Package Management > Package Manager
   (older Unity: Window > Package Manager), plus menu,
   Install package from git URL, paste:
   https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#v10.3.0
   Unity offers to update scripts? Fine in an empty test game.
5. The setup window opens by itself: Python and uv green, then Next.
   Configure MCP Clients: every detected client starts TICKED.
   Untick all but Claude Code, then Configure Selected (box: 1 configured).
   Mac, Claude Code not listed (Claude not found)? Click Skip; see step 7.
6. Window > MCP for Unity > Toggle MCP Window: Start Server, then Start.
   The button now reads Stop Server. (Local only: http://127.0.0.1:8080)
7. NOT Configure All Detected Clients (writes into every client it finds).
   NOT Install Skills (writes ~/.claude/skills/unity-mcp-skill from main).
   Skipped in step 5 (Mac)? Client: Claude Code, Browse beside Claude CLI
   Path, pick the claude file that which -a claude prints in a new Terminal window,
   then Configure.

## Claude builds a scene
1. PowerShell: cd "$HOME\unity-test"   (Mac: cd "$HOME/unity-test")
2. claude. Say yes to trusting the folder.
   If it says auto mode, press Shift+Tab once: manual mode on.
3. /mcp: check UnityMCP is connected.
4. Ask: Create a red, blue, and yellow cube in the current scene,
   spaced one unit apart on the X axis.
5. Approve each Unity tool after checking what it does.
   Cubes grey? Add: This project uses URP, please use the URP/Lit shader.

## The common mistake
- Claude Code started in another folder sees no Unity tools: Configure
  registers the server at local scope, for the unity-test folder only.

## Remove it
- In Claude Code: /exit
- In the same window, in unity-test: claude mcp remove --scope local UnityMCP
- In Unity: Stop Server, then remove MCP for Unity in Package Manager.
- Quit Unity (it asks about saving the scene: Don't Save), then delete the
  unity-test folder.
- Done for good?
  Windows: [Environment]::SetEnvironmentVariable("UNITY_MCP_DISABLE_TELEMETRY", $null, "User")
           and delete %APPDATA%\UnityMCP
  Mac: delete ~/Library/Application Support/UnityMCP
- Python, uv and Git stay until you uninstall them.
```

### 2. Before Unity Hub opens (Windows PowerShell)
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# open a new PowerShell window, then:
git --version
python --version
uv --version
setx UNITY_MCP_DISABLE_TELEMETRY true
# now quit Unity Hub fully (also its icon near the clock) and open it again
```

### 3. Before Unity Hub opens (Mac Terminal)
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# open a new Terminal window, then:
git --version
python3 --version
uv --version
# quit Unity Hub first; keep this window open while you work, and do this every time
UNITY_MCP_DISABLE_TELEMETRY=true \
"/Applications/Unity Hub.app/Contents/MacOS/Unity Hub"
```

### 4. The package address (Unity: Package Manager, plus menu, Install package from git URL)
```
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#v10.3.0
```

### 5. Only after Configure and Start Server: start Claude Code in the game folder (Windows PowerShell; /exit first if you're inside Claude Code)
```
cd "$HOME\unity-test"
claude
```

### 6. Only after Configure and Start Server: start Claude Code in the game folder (Mac, a new Terminal window; /exit first if you're inside Claude Code)
```
cd "$HOME/unity-test"
claude
```

### 7. Inside Claude Code (manual mode on: Shift+Tab once if it says auto mode), check the connection first
```
/mcp
```

### 8. Then type this inside Claude Code
```
Create a red, blue, and yellow cube in the current scene, spaced one unit apart on the X axis.
```

### 9. Only when you're done, leave Claude Code
```
/exit
```

### 10. Then, in the same window, in the unity-test folder, remove the server
```
claude mcp remove --scope local UnityMCP
```
