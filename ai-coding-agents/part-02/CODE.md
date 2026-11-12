# Full code: Gemini CLI vs Antigravity CLI: Which One Can You Still Use for Free?

Written for this video from the Antigravity CLI README, changelog and docs, and the Gemini CLI README and docs (checked 2026-11-12). Both JSON files were parsed with Python's json module; nothing was installed or run. Use a new, empty test folder, never your home folder.

### 1. setup-checklist.md
```
# Gemini CLI or Antigravity CLI? A setup checklist (facts checked 2026-11-12)

## 1. Which one is yours
- [ ] Personal Google account (free, Google AI Pro or Ultra): Antigravity CLI. Gemini CLI stopped serving these accounts on 18 June 2026.
- [ ] Your company gives you Gemini Code Assist Standard or Enterprise: Gemini CLI.
- [ ] A paid Gemini API key works with both, so it doesn't decide it.

## 2. Before you start either one
- [ ] A new, empty test folder, never your home folder: mkdir agent-test, then cd agent-test.
- [ ] Paying as you go with a key? Set a monthly spend cap first: Google AI Studio, Spend page, Monthly spend cap, Edit spend cap. Google calls it experimental, with about 10 minutes of billing delay, and agent sessions can run past it.

## 3. Antigravity CLI (agy), version 1.5.7 or later
- [ ] Install: Windows PowerShell: irm https://antigravity.google/cli/install.ps1 | iex
- [ ] Install: Mac Terminal: curl -fsSL https://antigravity.google/cli/install.sh | bash
- [ ] Open a new terminal window, go into agent-test, type agy, sign in with Google in the browser.
- [ ] First run: colour scheme, how to draw the screen, trust this folder. If there's a box about sharing your data, make sure it's unticked.
- [ ] /config, Agent Mode: default. (From 1.5.7, a session with no saved mode starts in auto wherever auto is available. Choosing default saves "agentMode": "" to ~/.gemini/antigravity-cli/settings.json.)
- [ ] /config, Tool Permission: request-review (it asks before writing files, running commands, going online or using MCP tools).
- [ ] /config, Enable Telemetry: off, if you'd rather not share your Interactions data. It's saved with your Google account, not in settings.json.
- [ ] Check: the mode label at the bottom right is empty, and the first edit asks "Accept this file edit?" (1 yes, 2 no).
- [ ] Free accounts: a weekly quota, no numbers published. /usage shows what's left.
- [ ] Instructions file, if you want one: AGENTS.md or GEMINI.md in the folder you start agy in.

## 4. Gemini CLI (gemini), version 0.68.0 or later
- [ ] Windows: Windows 11 24H2 or later. Node.js 20 or later: https://nodejs.org/en/download
- [ ] Install: npm install -g @google/gemini-cli
- [ ] Start in agent-test: gemini --approval-mode default ('default' prompts for approval).
- [ ] Sign in with your work account the way your company tells you.
- [ ] Instructions file, if you want one: GEMINI.md in the folder you start gemini in.
- [ ] Ignore any page or video promising "1,000 free requests a day": that ended on 18 June 2026.

## 5. Re-check before you rely on it
- [ ] Quotas, model lists, prices and the starting mode change. Check the source links in SOURCES.md.
```

### 2. Install and start lines (PowerShell on Windows, Terminal on Mac)
```
# Antigravity CLI, Windows PowerShell (from its README, checked 2026-11-12):
irm https://antigravity.google/cli/install.ps1 | iex
# Antigravity CLI, Mac Terminal:
curl -fsSL https://antigravity.google/cli/install.sh | bash
# Then open a new terminal window. Same on Windows and Mac:
mkdir agent-test
cd agent-test
agy
# In agy: type /config, set Agent Mode to default, check Tool Permission is request-review,
# set Enable Telemetry to off if you'd rather not share, then press Esc.

# Gemini CLI, only if your company gives you Gemini Code Assist (Node.js 20 or later first):
npm install -g @google/gemini-cli
# If agent-test already exists, skip mkdir and go straight to cd agent-test.
mkdir agent-test
cd agent-test
gemini --approval-mode default
```

### 3. ~/.gemini/antigravity-cli/settings.json (what /config saves)
```
{
  "agentMode": "",
  "toolPermission": "request-review"
}
```

### 4. ~/.gemini/settings.json (Gemini CLI, optional: makes default the saved mode)
```
{
  "general": {
    "defaultApprovalMode": "default"
  }
}
```

### 5. Saving the checklist, and a settings file by hand
```
# Antigravity CLI: /config writes section 3 for you. Edit the file by hand only if it already exists,
# and change only those two lines, keeping the rest of the file as it is.
# Gemini CLI: if ~/.gemini/settings.json doesn't exist yet, save section 4 as that file.
# Windows, Notepad: paste, then File, Save as. Set the box called Save as type to All files.
#   File name: %USERPROFILE%\.gemini\settings.json
# Mac, TextEdit: Format, then Make Plain Text, then paste. In the save box, press Shift-Command-G
#   and type ~/.gemini, then name the file settings.json. If TextEdit asks, choose Use .json.
# If the file already exists, add only the "general" lines to it, so you keep your other settings.
# setup-checklist.md, for the build prompt: save section 1 the same way, into your test folder,
#   named setup-checklist.md (Notepad: Save as type All files; TextEdit: plain text, then Use .md if asked).
```
