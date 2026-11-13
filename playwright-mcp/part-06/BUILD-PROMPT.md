# Claude build prompt: Playwright MCP, Part 6

Use this in Claude Code (Pro or higher, or a Console account), in a new, empty folder called attach-test in your home folder. Start in plan mode.

Goal: let Playwright MCP 0.0.85 drive a Chrome I start myself on its own profile folder, with only a test account signed in, and every lock from this series on. You write files and show me commands; I run the commands myself. Don't install, start or attach anything.
Steps, in order:
1. Show me, without running it, the command to start Chrome on its own profile with a debugging port, for my system: on Windows in PowerShell, & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$HOME\chrome-claude-test"; on a Mac, /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="$HOME/chrome-claude-test". Tell me to shut every Chrome window first, and to sign in to one test account only.
2. Show me, without running it, the add command: claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --cdp-endpoint http://127.0.0.1:9222. Explain why there's no --port, no --extension, no --caps=storage and no @latest.
3. Write .claude/settings.json: deny mcp__playwright__browser_evaluate, mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload; ask mcp__playwright__*; one PreToolUse entry with matcher "^mcp__playwright__browser_(navigate|tabs)$" running "command": "node", "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"] and "onFailure": "block". Show it to me.
4. Tell me to copy check-site.js from my playground/.claude folder (Part 5) into .claude here, and show me the one line to change: ALLOWED, set to my test site only (scheme, host and port, no path).
5. Write attach-checklist.txt: the six locks, what to check before each session, and how to switch everything off (Disable in /mcp, shut the test Chrome window, untick remote debugging at chrome://inspect if I ever turned it on, remove any browser extension I tried).
6. Tell me plainly what the hook can't see (a click on a link, a redirect, the page's own scripts), that any app on my computer can connect to port 9222 while that Chrome is open, and that --autoConnect would pick my default profile, so I shouldn't use it.
Safety: write only .claude/settings.json and attach-checklist.txt in this folder. Don't run any command, don't install anything, and don't start Chrome, a server or a browser.
Output: the two files, the commands to run in order, and what each should show.
