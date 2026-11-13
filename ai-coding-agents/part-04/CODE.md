# Full code: OpenCode Tutorial: Install OpenCode 2 and Make It Ask First

Written for this video from OpenCode's v2.2.7 docs and source (checked 2026-11-12). The JSONC file was parsed with comments stripped; nothing was installed or run. Use a new, empty test folder, never your home folder.

### 1. setup-checklist.md
```
# OpenCode 2 setup checklist (facts checked 2026-11-12, OpenCode 2.2.7)

## 1. What it costs
- [ ] OpenCode itself is free (MIT, by Anomaly). You bring the model.
- [ ] Either OpenCode Console's pay-as-you-go models (some free for a limited time; OpenCode Go was $10 a month when checked), or your own provider's key.

## 2. Install (version 2 only)
- [ ] Windows: install Node.js (https://nodejs.org), open PowerShell and paste: npm install -g @opencode/cli
- [ ] Red error in PowerShell saying running scripts is disabled? Type npm.cmd install -g @opencode/cli instead, and later type opencode.cmd wherever this checklist says opencode.
- [ ] Windows without Node.js: download the standalone zip (https://opencode.ai/update/api/latest/cli/opencode/opencode-windows-x64.zip), extract it, and start opencode.exe by its full path (see install-lines.txt).
- [ ] Mac: open Terminal and paste: curl -fsSL https://opencode.ai/v2/install | bash  (or, with Homebrew: brew install anomalyco/tap/opencode-v2)
- [ ] Open a new window and check: opencode --version (2.2.7 or later). Starts with 1? That's version 1: follow https://opencode.ai/docs/migrate-v1

## 3. Make it ask first, before the first start
- [ ] Windows: paste the Notepad line from install-lines.txt into PowerShell. Notepad asks to create the file: Yes.
- [ ] Mac: paste the TextEdit line from install-lines.txt into Terminal.
- [ ] The file: ~/.config/opencode/opencode.jsonc (Windows: %USERPROFILE%\.config\opencode\opencode.jsonc). Already has text in it? Merge the rules into it; never paste a second { }.
- [ ] Paste opencode.jsonc from this folder, then save (Ctrl+S or Command+S).
- [ ] Every agent: shell, external_directory and subagent set to ask. The build agent: edit set to ask.
- [ ] Mac, to find the file in Finder: Shift-Command-G, then ~/.config/opencode

## 4. A test folder and a model
- [ ] mkdir opencode-test, then cd opencode-test, then opencode. Never your home folder.
- [ ] /connect, then either: OpenCode's pay-as-you-go provider (sign in at https://opencode.ai/console, add billing details and credits, copy your key, paste it), or your own provider with a fresh key made only for this.
- [ ] /models, then pick one. Some say Free; a few free models' providers may keep what you send to improve the model (Console docs, Privacy).
- [ ] Spend limit: Console, Controls, Add policy, Entire workspace, a Budget rule with a monthly amount, Save. Own key: that provider's own spend limit. Running requests finish, so spend can end slightly above a budget.

## 5. First task, the plan agent and house rules
- [ ] First task: make a page called index.html with a button that counts clicks, then tell me what you did.
- [ ] Expect "Permission required" and "Edit index.html": pick Allow once (or Reject). Avoid Always allow for now: it saves a lasting allow rule for this folder.
- [ ] No box, and the file was made anyway? The settings file isn't where it should be, or has the wrong name (opencode.jsonc, in the folder above).
- [ ] Shift+Tab switches Build to Plan (explores and plans without editing your files). Shift+Tab again for Build.
- [ ] Save AGENTS.md in opencode-test: Notepad, Save as type All files; TextEdit, Make Plain Text first. Then Ctrl+X, then N, for a new session.

## 6. Re-check before you rely on it
- [ ] Versions, prices, menu names and permission names change. Check the links in SOURCES.md.
```

### 2. Install and start lines (PowerShell on Windows, Terminal on Mac)
```
# Windows: install Node.js from https://nodejs.org first, then open PowerShell, paste this line, press Enter (OpenCode docs, checked 2026-11-12):
npm install -g @opencode/cli
# If PowerShell says running scripts is disabled, use this instead, and type opencode.cmd wherever these lines say opencode:
npm.cmd install -g @opencode/cli
# Windows without Node.js: download and extract https://opencode.ai/update/api/latest/cli/opencode/opencode-windows-x64.zip
# then start it by its full path, for example from inside opencode-test (change the path to where you extracted it):
#   & "$env:USERPROFILE\Downloads\opencode-windows-x64\opencode.exe"
# Mac: open Terminal, paste this line, press Enter:
curl -fsSL https://opencode.ai/v2/install | bash
# Mac with Homebrew, instead:
brew install anomalyco/tap/opencode-v2
# Then open a new window. Same on Windows and Mac (2.2.7 or later; 1.x means version 1):
opencode --version
# Before the first start: make the settings folder and open the settings file.
# Windows PowerShell (Notepad asks to create the file: choose Yes):
New-Item -ItemType Directory -Force "$env:USERPROFILE\.config\opencode" | Out-Null; notepad "$env:USERPROFILE\.config\opencode\opencode.jsonc"
# Mac Terminal (opens it in TextEdit as plain text):
mkdir -p ~/.config/opencode && touch ~/.config/opencode/opencode.jsonc && open -e ~/.config/opencode/opencode.jsonc
# Paste opencode.jsonc, save (Ctrl+S or Command+S). Then the test folder (if it already exists, skip mkdir):
mkdir opencode-test
cd opencode-test
opencode
# Inside OpenCode: /connect adds a provider, /models picks a model, Shift+Tab switches Build and Plan,
# Ctrl+X then N starts a new session, Ctrl+C quits.
```

### 3. ~/.config/opencode/opencode.jsonc (Windows: %USERPROFILE%\.config\opencode\opencode.jsonc)
```
// Make OpenCode 2 ask first (OpenCode docs: Permissions and Agents, checked 2026-11-12).
// Every agent asks before shell commands, folders outside this one, and starting a helper (subagent).
// The build agent also asks before editing files. Last matching rule wins.
// The subagent rule also turns the shipped general and explore helpers' block on starting helpers into ask.
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "external_directory", "resource": "*", "effect": "ask" },
    { "action": "subagent", "resource": "*", "effect": "ask" }
  ],
  "agents": {
    "build": {
      "permissions": [
        { "action": "edit", "resource": "*", "effect": "ask" }
      ]
    }
  }
}
```

### 4. AGENTS.md (save in your test folder)
```
# AGENTS.md
## House rules for this folder
- Work only inside this folder.
- Ask me before deleting or renaming any file.
- Keep each change small.
- When you finish, explain each change in plain words.
```

### 5. Saving the files
```
# opencode.jsonc goes in the hidden .config\opencode folder in your home folder (Mac: ~/.config/opencode).
# Open it with the line for your system in install-lines.txt: it makes the folder first, then opens the file.
# If the file already has text, merge our rules into it: one pair of { } for the whole file, no second copy.
# Save with Ctrl+S (Windows) or Command+S (Mac).
# AGENTS.md and setup-checklist.md are new files in your test folder (opencode-test, inside your home folder):
#   Windows, Notepad: paste, then File, Save as. Set the box called Save as type to All files, and name it AGENTS.md.
#   Mac, TextEdit: Format, then Make Plain Text, then paste. Save it in opencode-test as AGENTS.md; if TextEdit asks, choose Use .md.
#   (Shift-Command-G in a Finder window or the save box reaches any folder by its path, such as ~/opencode-test or ~/.config/opencode.)
# After saving AGENTS.md, press Ctrl+X, then N, in OpenCode for a new session.
```
