# Full code: Browser MCP and Your Real Chrome: Is It Safe to Let Claude Log In?



### 1. A new folder for the attach route (PowerShell on Windows or Terminal on a Mac, in your home folder: the same three lines as Part 3)
```
mkdir attach-test
cd attach-test
mkdir .claude
```

### 2. Add Playwright MCP 0.0.85, pointed at Chrome on 127.0.0.1:9222 (the same window, inside attach-test, the same line on Windows and Mac; you'll see a line ending "to local config". No --port, no --extension, no --caps=storage)
```
claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --cdp-endpoint http://127.0.0.1:9222
```

### 3. attach-test/.claude/settings.json (from the link in the description. Windows: Notepad, Save as type: All files. Mac: TextEdit set to plain text before pasting, then Shift-Command-G and type ~/attach-test/.claude; keep .json. Deny is checked first, then ask, so the three denied tools stay blocked and every other Playwright tool asks you, even in auto mode. Check the hook with /hooks)
```
{
  "permissions": {
    "deny": [
      "mcp__playwright__browser_evaluate",
      "mcp__playwright__browser_run_code_unsafe",
      "mcp__playwright__browser_file_upload"
    ],
    "ask": [
      "mcp__playwright__*"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^mcp__playwright__browser_(navigate|tabs)$",
        "hooks": [
          {
            "type": "command",
            "command": "node",
            "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"],
            "onFailure": "block"
          }
        ]
      }
    ]
  }
}
```

### 4. Copy Part 5's check-site.js into this folder (PowerShell on Windows or Terminal on a Mac, inside attach-test; playground and attach-test both sit in your home folder)
```
PowerShell:   Copy-Item ..\playground\.claude\check-site.js .claude\
Terminal:     cp ../playground/.claude/check-site.js .claude/
```

### 5. check-site.js: change one line (open attach-test/.claude/check-site.js in Notepad, with the Open box set to All files, or in TextEdit, pressing Shift-Command-G in the Open box and typing ~/attach-test/.claude; change only its ALLOWED line and save it as it was, keeping .js)
```
// Part 5's check-site.js, unchanged except this line. Put ONLY the site of your test account here:
// scheme, host and port, no path. Part 5's value is shown; replace it with your test site.
// It checks only the site named in each browser_navigate or new-tab call. It can't see a click on a link,
// a redirect, or a page's own scripts, so it's a tripwire, not a wall around the browser.
const ALLOWED = ["http://localhost:8080", "http://127.0.0.1:8080"];
```

### 6. Start Chrome on a profile of its own, Windows (shut every Chrome window first, then paste this in the same PowerShell window; a fresh Chrome window opens)
```
# From Google's guide, with the folder moved to your home folder, from the link in the description.
# It starts a fresh Chrome on its own profile folder, chrome-claude-test, listening on port 9222 on this computer only.
# Since Chrome 136, the debugging port is ignored on your everyday profile, so the folder must be a different one.
# Sign in to ONE test account in this window and nothing else. While it's open, any app on this computer can connect.
# If Chrome is installed for your user only, the path starts with $env:LOCALAPPDATA\Google\Chrome\Application instead.
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$HOME\chrome-claude-test"
```

### 7. Start Chrome on a profile of its own, Mac (quit Chrome first with Command-Q, then paste this in the same Terminal window; a fresh Chrome window opens, and this window stays busy until Chrome shuts)
```
# From Google's guide, with the folder moved to your home folder, from the link in the description.
# It starts a fresh Chrome on its own profile folder, chrome-claude-test, listening on port 9222 on this computer only.
# Since Chrome 136, the debugging port is ignored on your everyday profile, so the folder must be a different one.
# Sign in to ONE test account in this window and nothing else. While it's open, any app on this computer can connect.
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="$HOME/chrome-claude-test"
```

### 8. attach-checklist.txt (from the link in the description; keep it next to settings.json in attach-test, and go through it before every session)
```
Letting Claude use a logged-in browser: the six locks (Playwright MCP series, Part 6, checked 2026-11-12)

BEFORE EACH SESSION
[ ] 1. Exact version: /mcp shows playwright, added with @playwright/mcp@0.0.85, never @latest.
[ ] 2. Local connections only: the add command says http://127.0.0.1:9222, and the server has no --port.
       While that Chrome is open, any app on this computer can connect to port 9222, so browse nothing else in it.
[ ] 3. Rules: .claude/settings.json denies browser_evaluate, browser_run_code_unsafe and browser_file_upload,
       and asks for mcp__playwright__*. No --caps=storage on this server (it gets and sets cookies).
[ ] 4. Hook: /hooks shows the PreToolUse matcher, and check-site.js lists ONLY your test site.
       It checks the site named in each call. It can't see a click on a link, a redirect or a page's own scripts.
[ ] 5. A profile of its own: the Chrome window was started with --user-data-dir pointing at chrome-claude-test,
       never your everyday profile. Only ONE test account is signed in there. No email, bank or work accounts.
[ ] 6. You'll switch it off after (below).

MODES TO AVOID WITH YOUR EVERYDAY PROFILE
- Chrome DevTools MCP --autoConnect: with several profiles open, it connects to Chrome's default profile
  and can reach all its open windows. Use --browserUrl http://127.0.0.1:9222 with the Chrome above instead.
- Playwright MCP --extension: install the Playwright Extension only in a test profile, and name it with
  --profile-dir-name. By default it picks the last used profile that has the extension installed.
- Browser MCP: one browser tool (it can also run JavaScript in the page), your real profiles, @latest,
  --scope user, and a self-updating extension. Its own README: treat pages agents browse as able to read
  any file you can read and overwrite any file you can write.
- Claude in Chrome: shares your browser's login state. Choose its sites in the extension's settings,
  and leave "Enabled by default" off in /chrome unless you want it in every session.

SWITCH IT OFF WHEN YOU'RE DONE
[ ] In Claude Code: /mcp, pick playwright, choose Disable.
[ ] Shut the test Chrome window. Its debugging port goes with it.
[ ] If you ever ticked "Allow remote debugging" at chrome://inspect/#remote-debugging, untick it.
[ ] Remove any browser extension you tried (chrome://extensions).
[ ] To wipe the test profile, delete the chrome-claude-test folder in your home folder.
[ ] To delete the server: claude mcp remove playwright (inside attach-test).
```

### 9. Start Claude Code and check it (a second PowerShell or Terminal window; /mcp should say playwright is connected and /hooks should show the PreToolUse matcher. Then paste prompt 1 from the description)
```
cd attach-test
claude
```

### 10. Switch it off (in Claude Code: /mcp, pick playwright, choose Disable. Then shut the test Chrome window. To delete the server instead, type /exit and run this inside attach-test)
```
claude mcp remove playwright
```

### 11. Not our route: the other modes, for comparison (each project's own setup lines, from their READMEs and docs. Each one reaches a browser with your logins in it)
```
claude mcp add --scope user browsermcp -- npx @browsermcp/mcp@latest
npx @playwright/mcp@latest --extension
npx chrome-devtools-mcp@latest --autoConnect
claude --chrome
```
