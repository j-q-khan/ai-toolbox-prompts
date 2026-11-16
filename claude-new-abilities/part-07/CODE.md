# Full code: Godot MCP with Claude: Can Claude Make a Godot Game?

A checklist and commands written for this video from the repo's files at tag v4.4.1 (read as text), its release page, Godot's docs, uv's docs, Microsoft's docs and Anthropic's Claude Code docs, checked 2026-11-15. Not run by us: try it in a new, empty Godot test game first.

### 1. godot-ai-checklist.md
```
# Godot MCP with Claude: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/hi-godot/godot-ai ("Godot AI"). Original; not made by
  the Godot Foundation.
- Licence: MIT
- Latest release: 4.4.1, 2026-11-03 (last commit 2026-11-03)
- Real use: about 3,500 stars, almost 200 forks; issues 406 closed, 5 open;
  7 closed issues sampled: the same core contributor closed 6, 2 with a fix
- Needs: Godot 4.7 or newer (newest: 4.7.2, godotengine.org/download)
  and uv (docs.astral.sh/uv). Godot is free under the MIT licence.
- Reaches, in the open Godot editor: scenes, scripts, materials, animation,
  screenshots, playing the game, running code inside the running game.
  Its own file tools stay inside the game folder (project.godot,
  override.cfg and .godot/ are off-limits), but code running in your game
  is not fenced in: test game and manual mode only. Editor connection:
  your computer only, with a rotating secret.
- Telemetry: ON by default (install ID, event, outcome, duration, platform,
  version; never code or scene contents). Sent in batches about every
  15 minutes. After Apply and Restart Server with it off, the restarted
  server sends no usage data. (Not telemetry: on each start the add-on
  asks GitHub for its newest release, and uv fetches the server from PyPI.)
- Costs: free.
- Don't install from Godot's AssetLib tab: it lists an older version
  (3.2.5 in the Asset Library, 4.3.1 in the Asset Store, 2026-11-15).

## Setup (one new, empty test game)
1. Install uv (sections 2 and 3 below), then open a new window and check:
   uv --version. Start Godot only after uv is installed.
2. Godot: unzip it and open the program inside (Windows: the .exe
   without "console" in its name). In the first window
   (Project Manager): Create, Project Name godot-test, Browse to your user
   folder (C:\Users\you or /Users/you), Create Folder ticked, Create.
3. Download godot-ai-v4-plugin.zip from the 4.4.1 release into your
   Downloads folder: github.com/hi-godot/godot-ai/releases/tag/v4.4.1
   (Mac with Safari: it may unzip downloads for you and drop the zip; turn
   off Safari > Settings > General > "Open safe files after downloading",
   or use a browser that keeps the zip, then download it again)
4. Check its fingerprint (section 4). The code on the release page is:
   aa101a3e8991e95fb2a358cae1aeb06f3550622daea10b366aeda81335a91f7f
   PowerShell prints True, Terminal prints OK, when the zip matches.
   False, FAILED or "No such file"? Stop.
5. Unzip it into the game folder, so you get godot-test/addons/godot_ai/
   (section 5). Never unzip over an existing addons/godot_ai folder.
6. Godot: Project > Project Settings > Plugins, tick Enable beside
   Godot AI. The dock says Starting server..., then Server connected.
7. Telemetry off, straight away and before Configure:
   dock > Clients & Tools > Tools tab > Telemetry switch at the bottom,
   below the tool list, off (leave the tool boxes as they are) >
   Apply and Restart Server.
   Stricter, before the server ever starts (optional): quit Godot, then
     Windows (PowerShell): setx GODOT_AI_DISABLE_TELEMETRY true
       (then start Godot again; setx reaches programs started afterwards)
     Mac (Terminal), if Godot is in Applications:
       GODOT_AI_DISABLE_TELEMETRY=true /Applications/Godot.app/Contents/MacOS/Godot
     Once the add-on sees it, the opt-out is saved in Godot's editor settings.
8. Clients tab: Configure next to Claude Code ONLY (dot green, button
   reads Reconfigure). NOT Configure all.
   The entry goes into Claude Code's user settings (works from any folder),
   pinned to godot-ai 4.4.1. Keep only the test game open in Godot.
   Configure fails (red dot, Retry)? Use the dock's "Run this manually"
   command instead: /exit any Claude Code session first, then run it.

## Claude builds a scene
1. Claude Code already open anywhere? /exit first, so it sees the new server.
   PowerShell or Mac Terminal: cd "$HOME/godot-test"
2. claude. Say yes to trusting the folder.
   If it says auto mode, press Shift+Tab once: manual mode on.
3. /mcp: check godot-ai is connected.
4. Ask: Create a new 3D scene with a camera, a light and a red cube,
   and save it as main.tscn.
5. Approve each Godot tool after checking what it does. The file lands at
   godot-test/main.tscn.

## The common mistake
- Clicking Configure while Claude Code is already open: it only picks up
  new servers when it starts. /exit, start claude again, check /mcp.

## Updates
- Click Update in the dock and confirm ("Update Godot AI?"): it checks the
  signature and every file first. Never unzip a new version over the old.

## Remove it
- In Claude Code: /exit
- Godot: Clients & Tools > Clients tab > Remove next to Claude Code
  (or, in a terminal: claude mcp remove --scope user godot-ai)
- Project > Project Settings > Plugins: untick Enable.
- Quit Godot (it asks about saving? Don't Save), then delete the
  godot-test folder and the zip in Downloads.
- Done for good? Delete the add-on's data folder if it exists:
  Windows: %APPDATA%\godot-ai     Mac: ~/Library/Application Support/godot-ai
  Set the telemetry variable with setx? Windows:
  [Environment]::SetEnvironmentVariable("GODOT_AI_DISABLE_TELEMETRY", $null, "User")
- uv stays until you uninstall it.
```

### 2. Before Godot opens (Windows PowerShell)
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# open a new PowerShell window, then:
uv --version
```

### 3. Before Godot opens (Mac Terminal)
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# open a new Terminal window, then:
uv --version
```

### 4. Check the zip's fingerprint (compare with the release page)
```
# Windows PowerShell (prints True when it matches):
$want = "aa101a3e8991e95fb2a358cae1aeb06f3550622daea10b366aeda81335a91f7f"
(Get-FileHash "$HOME\Downloads\godot-ai-v4-plugin.zip").Hash -eq $want
# Mac Terminal (prints ".../godot-ai-v4-plugin.zip: OK" when it matches):
want=aa101a3e8991e95fb2a358cae1aeb06f3550622daea10b366aeda81335a91f7f
echo "$want  $HOME/Downloads/godot-ai-v4-plugin.zip" | shasum -a 256 -c
# The code is the one on the 4.4.1 release page (2026-11-15).
```

### 5. Only if it matches: unzip it into the game folder (made by Godot first)
```
# Windows PowerShell:
Expand-Archive "$HOME\Downloads\godot-ai-v4-plugin.zip" -DestinationPath "$HOME\godot-test"
# Mac Terminal:
unzip ~/Downloads/godot-ai-v4-plugin.zip -d ~/godot-test
```

### 6. Only after Configure: start Claude Code in the game folder (PowerShell or Mac Terminal; /exit first if you're inside Claude Code)
```
cd "$HOME/godot-test"
claude
```

### 7. Inside Claude Code (manual mode on: Shift+Tab once if it says auto mode), check the connection first
```
/mcp
```

### 8. Then type this inside Claude Code
```
Create a new 3D scene with a camera, a light and a red cube, and save it as main.tscn.
```

### 9. Only when you're done, leave Claude Code
```
/exit
```

### 10. Then, if you didn't click Remove in Godot, remove the entry in the same window
```
claude mcp remove --scope user godot-ai
```
