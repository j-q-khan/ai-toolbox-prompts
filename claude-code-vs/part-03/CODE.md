# Full code: Claude Code in VS Code vs Terminal vs Desktop App: Which Should You Use?

A one-page picker and a checklist written for this video from Anthropic's own pages (checked 2026-11-13). Versions, starting modes and plans are what they were when checked; re-check the source link in each row before you rely on one. The CSV was parsed with Python's csv module; nothing was installed or run.

### 1. claude-code-places-2026-11-13.csv
```csv
place,what_it_adds_in_anthropics_words,how_to_open_on_windows,how_to_open_on_a_mac,what_you_see_first,starting_mode_in_anthropics_words,what_you_need,checked,source
Terminal,"The full-featured CLI; all commands and skills; scripting with claude -p","Win+X, choose Windows PowerShell (or Terminal), cd into a test folder, type claude","Cmd+Space, type Terminal, press Enter, cd into a test folder, type claude","A browser window to sign in, then the Claude Code welcome screen","Auto mode with v2.1.283 or later; switch with Shift+Tab","A paid Claude plan from Pro, or a Claude Console account; not on Free",2026-11-13,https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/terminal-guide ; https://code.claude.com/docs/en/permission-modes
VS Code extension,"Inline diffs, @-mentions, plan review, and conversation history; a subset of commands","Ctrl+Shift+X, search Claude Code, Install; File, Open Folder (a test folder); Ctrl+Shift+P, Claude Code, Open in New Tab","Cmd+Shift+X, search Claude Code, Install; File, Open Folder (a test folder); Cmd+Shift+P, Claude Code, Open in New Tab","A sign-in screen, then a Learn Claude Code checklist","Auto with v2.1.283 or later, or the mode you last picked; in Auto, Claude edits most files without asking","VS Code 1.94.0 or later; a paid Claude plan or a Claude Console account",2026-11-13,https://code.claude.com/docs/en/vs-code ; https://code.claude.com/docs/en/permission-modes
Desktop app (Code tab),"Review diffs visually, run multiple sessions side by side, schedule recurring tasks, start cloud sessions; review the changes yourself, without using a terminal","Start menu, sign in, Code tab, Local, Open folder","Applications folder, sign in, Code tab, Local, Open folder","A prompt to upgrade if your plan lacks it; otherwise a new session with a mode selector under the prompt box","No built-in default stated: check the selector before your first message","A paid subscription is required",2026-11-13,https://code.claude.com/docs/en/desktop-quickstart ; https://code.claude.com/docs/en/desktop
Web (claude.ai/code),"Runs in the cloud on an Anthropic-managed VM; works from a GitHub repository; repo only, not your local config","A desktop browser at claude.ai/code","A desktop browser at claude.ai/code","A step to connect GitHub","Accept edits, Plan and Auto offered; no built-in default stated","Pro, Max, Ultra or Team (Enterprise with premium or Chat + Claude Code seats)",2026-11-13,https://code.claude.com/docs/en/web-quickstart ; https://code.claude.com/docs/en/permission-modes
JetBrains plugin,"Interactive diff viewing and selection context sharing; requires the Claude Code CLI, installed separately","Install the CLI first, then the plugin from the JetBrains Marketplace","Install the CLI first, then the plugin from the JetBrains Marketplace","Claude Code in the IDE terminal","Works the same as in the CLI: Shift+Tab to cycle","The Claude Code CLI plus the plugin",2026-11-13,https://code.claude.com/docs/en/jetbrains ; https://code.claude.com/docs/en/overview
```

### 2. first-session-checklist.md
```markdown
# Your first Claude Code session: a checklist (facts checked 2026-11-13)

## 1. Before you start
- [ ] Claude Code isn't on the Free plan: it starts with Pro (claude.com/pricing).
- [ ] Make a new, empty test folder, never your home folder, with nothing private in it.

## 2. Pick one place and open it
- [ ] Terminal, Windows: press Win+X, choose Windows PowerShell (or Terminal), type cd and your test folder's path, press Enter, then type claude and press Enter.
- [ ] Terminal, Mac: press Cmd+Space, type Terminal, press Enter, type cd and your test folder's path, press Enter, then type claude and press Enter.
- [ ] Not installed yet? AI CAD with Claude, Parts 1 to 3, walk through it (links in the description).
- [ ] VS Code: Ctrl+Shift+X (Cmd+Shift+X on a Mac), search Claude Code, Install; open your test folder with File, Open Folder; then Ctrl+Shift+P (Cmd+Shift+P), type Claude Code, choose Open in New Tab, and sign in.
- [ ] Desktop app: open Claude, sign in, click the Code tab, choose Local, then Open folder, and pick your test folder.

## 3. Check the mode before your first message
- [ ] Terminal and VS Code start in auto mode (v2.1.283 or later). Auto "does not guarantee safety".
- [ ] Want it to ask first? Terminal: Shift+Tab to Manual. VS Code and the desktop app: click the mode under the prompt box and choose Manual.
- [ ] Desktop app: "check the selector before your first message".

## 4. The same setup everywhere
- [ ] Your folder's CLAUDE.md, settings and MCP servers work across all of them.
- [ ] Re-check versions and modes at code.claude.com/docs/en/permission-modes: they change.
```
