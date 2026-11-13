# Full code: Claude Code Setup: Permissions, Undo and CLAUDE.md, the Settings to Change First

Every prompt and command from this video, written from Anthropic's docs and Git's own site (checked 2026-11-13). Nothing was installed or run; outputs shown in the video are labelled "Example output". settings-example.json was parsed with Python's json module. It only shows what your settings file looks like after prompt 1, with the Manual setting from the install video: never save it over your own settings file, because the prompt adds the rule and keeps everything else.

### steps.txt
```text
# Claude Code setup: the settings to change first (checked 2026-11-13)
# Open your terminal. Windows: press Win + X, choose Windows PowerShell or Terminal (not Admin).
# Mac: press Cmd + Space, type Terminal, press Enter.
# Start Claude Code in your test folder (made in the install video, in your home folder). Press Enter after each line:
cd claude-test
claude
# Check the status bar under the typing box says: manual mode on. If not, press Shift+Tab until it does.

# 1. A deny rule for .env files: copy the prompt in deny-env-prompt.txt, click in the terminal,
#    paste it (Ctrl+V on Windows, Cmd+V on a Mac) and press Enter.
#    If it first asks only to look at the file, press Enter on the highlighted Yes.
#    When it shows the change (a "deny" list with Read(**/.env)), press Enter on the plain Yes.
#    Check the rule is there: type this and press Enter, press the right arrow key until you see the deny rules, then press Esc:
/permissions
#    The rule covers .env files in the folder you start Claude Code in and the folders inside it,
#    for Claude Code's own file tools and the file commands it recognises. It doesn't cover a script that opens files itself,
#    a .env in a folder above, or names like .env.local. In the desktop app, /permissions says "isn't available in this environment",
#    but the rules in your settings file still apply there.

# 2. Undo (Esc twice with the typing box empty, or /rewind) doesn't put back: files changed only by commands Claude ran,
#    most edits made by subagents, or changes you make yourself. Checkpoints are deleted after about 30 days. Use Git for these.

# 3. Git. Leave Claude Code running and open a second window.
#    Windows: press Win + X, choose Windows PowerShell or Terminal (not Admin). Mac: press Cmd + N in Terminal. Then type this and press Enter:
git --version
#    A version number means Git is installed: click back on the Claude Code window.
#    Windows, "git is not recognized": open https://git-scm.com/downloads/win, click the download link, open the file
#    from your Downloads folder, choose Yes if Windows asks to allow changes, click Next on each screen, then Install and Finish.
#    Then type exit in the Claude Code window, open a fresh PowerShell window (Win + X) and start Claude Code again:
exit
cd claude-test
claude
#    Mac, a box offers to install the command line developer tools: click Install, agree to the licence if it asks,
#    wait for it to finish, then type git --version again.
#    In Claude Code, paste the commit prompt from git-prompts.txt. Before each Git command that changes something,
#    it asks: press Enter on the plain Yes, never "Yes, and don't ask again" (on a command, that saves an allow rule).
#    To go back to your last commit, paste the go-back prompt from git-prompts.txt, check its list, then type yes or no and press Enter.

# 4. CLAUDE.md, a note Claude loads every session. Type this and press Enter:
/init
#    It shows you the file and asks first: press Enter on the plain Yes. Keep it under 200 lines.
#    Check it saved: paste this and press Enter, and Claude prints the file:
Show me what's in CLAUDE.md in this folder.
#    To add the lines from claude-md-example.txt, paste: Add these lines to CLAUDE.md in this folder, keep everything already in it, and show me the change.
#    Then paste the lines after it.

# 5. Never paste a key or password into a prompt. Transcripts of every session are kept in plain text
#    in ~/.claude/projects/ for at least 30 days, including anything a tool opened.
```

### deny-env-prompt.txt
```text
# Paste into Claude Code in your claude-test folder, with the status bar showing manual mode on (Ctrl+V on Windows, Cmd+V on a Mac, then Enter).
# If it first asks only to look at the file, press Enter on the highlighted Yes. When it shows the change, press Enter on the plain Yes.
# Skip any option that says "for this session". Then type /permissions, press the right arrow key until you see the deny rules, and press Esc.
Add a permission rule to my user settings file, ~/.claude/settings.json, that stops you opening any file called .env. If the file exists, keep everything in it exactly as it is and add "Read(**/.env)" to the "deny" list inside "permissions", creating "permissions" or "deny" if they aren't there. If the file doesn't exist, create it with only that rule. Make the change as a file edit, so I approve it in the permission question, and change no other file.
```

### git-prompts.txt
```text
# Paste into Claude Code in your claude-test folder, in Manual mode (Ctrl+V on Windows, Cmd+V on a Mac, then Enter).
# Choose the plain Yes on each Git command. When it lists what will change, type yes or no and press Enter.
# Commit (a save point for the whole folder):
Set up Git in this folder if it isn't set up yet, then commit my changes with a descriptive message. Leave any .env file out of the commit and tell me if you find one. If Git says it needs a name and email, stop and ask me what to use, and set them for this folder only. Don't change my files, any other folder or any global Git settings, and don't send anything online.
# Go back to your last commit (changes since then are thrown away, so check its list first):
Put every file in this folder back the way it was at my last commit. Before you change anything, list the files that will change and what I'll lose, and wait for my yes. Use git restore for this, never git reset, git clean or any force option. Leave any new files I haven't committed where they are and tell me their names, keep all my commits, and don't touch any other folder.
```

### settings-example.json
```json
{
  "permissions": {
    "defaultMode": "default",
    "deny": ["Read(**/.env)"]
  }
}
```

### claude-md-example.txt
```text
# An example CLAUDE.md for the claude-test folder. These are requests Claude tries to follow, not locks:
# a deny rule is what actually blocks something.
# My test folder
- This folder holds small practice websites and apps in plain HTML, CSS and JavaScript, with no libraries.
- Ask me before deleting or renaming any file.
- Explain each change in one or two plain sentences.
- Never open or print .env files, or anything that looks like a key or password.
- When something works, remind me to ask for a commit.
```
