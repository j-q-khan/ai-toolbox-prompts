# Full code: Home Assistant MCP with Claude: Control Your Smart Home Safely

A checklist and commands written for this video from the repo's files at tag v9.2.0 (read as text), its release and issue pages, Home Assistant's docs, uv's docs, Microsoft's docs and Anthropic's Claude Code docs, checked 2026-11-15. Not run by us: try it with a test account and one harmless device first.

### 1. home-assistant-mcp-checklist.md
```
# Home Assistant MCP with Claude: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/homeassistant-ai/ha-mcp. Unofficial: its GitHub group is
  "The Unofficial Home Assistant AI Toolkit". Not made by Home Assistant
  or the Open Home Foundation.
- Licence: MIT
- Latest release: 9.2.0, 2026-11-11 (daily "Dev Build" entries are not
  releases). Known 9.2.0 bug: automation tools (issue #3077), so test with
  a light, not an automation.
- Real use: almost 7,900 stars, 480 forks; issues 889 closed, 10 open;
  7 closed issues sampled: core maintainers closed all 7 and replied on each
- Reaches: everything the token's account can, through 87 tools: switching
  devices (ha_call_service, ha_bulk_control), running automations, and with
  an administrator account also editing automations, dashboards and
  settings, backups, updates and restarting Home Assistant.
- Telemetry: none in 9.2.0. Planned stats would follow Home Assistant's
  analytics setting (Settings > System > Analytics). A release fixed at
  9.2.0 can't gain them without an update.
- Costs: free.
- Home Assistant's own built-in MCP server (it has a Read-only option):
  Claude connects to it from the cloud, so Home Assistant must be
  reachable from the internet, and
  Claude Code needs an HTTPS link.
- The repo calls local stdio (this route) "not recommended" and
  "recommended only for demo/testing tinkering". For a real setup it points
  to its HA-MCP integration inside Home Assistant, which needs an
  administrator's token. So treat this route as a test.
- Configure exactly ONE install method per client (two cause hangs).

## Want to practise first? The public demo home
- Its makers run a demo Home Assistant that resets weekly. Use
  HOMEASSISTANT_URL https://ha-mcp-demo-server.qc-h.net and
  HOMEASSISTANT_TOKEN demo instead of your own (whatever you type there goes
  to their server; never real details).

## Test account (Home Assistant, signed in as you)
1. Settings > People > Users tab > add a user: claude-test.
   Local access only: ON (works only on your home network).
   Administrator: OFF (can't change your setup; the server's FAQ says
   non-administrator tokens work, with administrator-only calls refused,
   though they're not officially supported; the server logs a warning
   about the non-administrator token, which is expected).
   It can still switch EVERY device: Claude's approval prompt is the gate.
2. Private browser window, sign in as claude-test > your name at the bottom
   of the sidebar > Security > Long-lived access tokens > Create token >
   name: claude > OK. It's shown only once: leave this box open until the
   hidden token prompt (Connect it, step 3), then copy it from there.
   Afterwards copy something else, so it leaves your clipboard (and if
   Windows clipboard history is on, Windows key + V, delete it there).
   Never paste it into a chat, a file or a screenshot.

## Connect it (one terminal window; sections 2 to 4)
1. Install uv, then open a NEW window.
2. Make home-test in your user folder, go into it, run:
   uvx ha-mcp@9.2.0 --version     (prints: ha-mcp 9.2.0)
3. Set HOMEASSISTANT_URL (the link your browser shows for Home Assistant
   at home, like http://homeassistant.local:8123; never a Home Assistant
   Cloud or other outside link, which claude-test can't use) and
   HOMEASSISTANT_TOKEN (copied from the open token box, pasted hidden;
   PowerShell: the Read-Host line, paste, Enter, then the line after it).
   They exist only in this window.
4. Run the add line (section 4). It writes home-test/.mcp.json. Open it:
   it must show ${HOMEASSISTANT_TOKEN}, never your token.
5. claude --permission-mode manual   (status bar: manual mode on)
   Trust the folder: Yes. The new server in .mcp.json: use this server.
6. /mcp: home-assistant connected.
   Mac and not connecting? System Settings > Privacy & Security >
   Local Network: allow your terminal app, then /exit and start again.

## First switch
- Ask: Turn on the desk lamp.   (a harmless light; never a lock, alarm or
  garage door)
- Claude asks before each Home Assistant tool: at least 2 prompts (find the
  lamp, switch it), maybe one more to check it. Yes each time. Never the
  "don't ask again" option.
- The lamp's card on your Home Assistant dashboard shows it on.

## The common mistake
- Starting Claude from a new window: the token isn't set, /mcp warns about
  a missing variable. /exit, set both variables again in that window, then
  claude --permission-mode manual.
- Lost the token? It's shown only once. Private window as claude-test:
  Security > delete the claude token > Create token again, then set the
  variables with the new one.

## Look first (bonus)
- Put  -e READ_ONLY_MODE=true  in the add line BEFORE --transport (after
  the -- it would go to uvx and do nothing). Every tool that changes things
  is hidden. The whole add line with it:
  claude mcp add -e 'HOMEASSISTANT_URL=${HOMEASSISTANT_URL}' -e 'HOMEASSISTANT_TOKEN=${HOMEASSISTANT_TOKEN}' -e HA_MCP_DISABLE_SETTINGS_UI=1 -e READ_ONLY_MODE=true --transport stdio --scope project home-assistant -- uvx ha-mcp@9.2.0
- Already added? /exit, run the remove line, then the add line above.

## Remove it
- In Claude Code: /exit
- In home-test: claude mcp remove --scope project home-assistant
- Shut the window (it forgets both variables).
- Private window as claude-test: Security > delete the claude token.
- Your own account: Settings > People > Users tab > claude-test >
  Delete user > OK.
- Delete the home-test folder and .ha-mcp (the server's settings) from your
  user folder. A Mac hides .ha-mcp in Finder, so use these lines:
  Windows PowerShell:
    cd $HOME
    Remove-Item -Recurse "$HOME\home-test"
    Remove-Item -Recurse "$HOME\.ha-mcp"
  Mac Terminal:
    cd ~ && rm -rf ~/home-test ~/.ha-mcp
  (If .ha-mcp isn't there, PowerShell says it can't find it; that's fine.)
  uv stays until you uninstall it.
```

### 2. Windows PowerShell: uv, the folder, the variables
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# open a NEW PowerShell window, then run these lines one at a time:
mkdir "$HOME\home-test"
cd "$HOME\home-test"
uvx ha-mcp@9.2.0 --version
# your Home Assistant link at home, never an outside one
$env:HOMEASSISTANT_URL = "http://homeassistant.local:8123"
$s = Read-Host "Token" -AsSecureString
# copy the token from the open box, paste it at the prompt (it shows stars),
# press Enter, then run the next line on its own
$env:HOMEASSISTANT_TOKEN = [Net.NetworkCredential]::new("", $s).Password
```

### 3. Mac Terminal: uv, the folder, the variables
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# open a NEW Terminal window, then:
mkdir ~/home-test && cd ~/home-test
uvx ha-mcp@9.2.0 --version
# your Home Assistant link at home, never an outside one
export HOMEASSISTANT_URL="http://homeassistant.local:8123"
read -rs HOMEASSISTANT_TOKEN && export HOMEASSISTANT_TOKEN
# copy the token from the open box, paste it (nothing shows), then Return
```

### 4. Same window, in home-test (PowerShell or Terminal): add the server to this folder only
```
claude mcp add -e 'HOMEASSISTANT_URL=${HOMEASSISTANT_URL}' -e 'HOMEASSISTANT_TOKEN=${HOMEASSISTANT_TOKEN}' -e HA_MCP_DISABLE_SETTINGS_UI=1 --transport stdio --scope project home-assistant -- uvx ha-mcp@9.2.0
```

### 5. Same window: start Claude Code in manual mode
```
claude --permission-mode manual
```

### 6. Inside Claude Code: check the connection, then ask
```
/mcp
Turn on the desk lamp.
```

### 7. Only when you're done: leave Claude Code, then remove the server (same folder)
```
/exit
claude mcp remove --scope project home-assistant
```
