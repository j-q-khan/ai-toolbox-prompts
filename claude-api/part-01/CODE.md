# Full code: Claude API Key: How to Get One, Set a Spend Limit and Keep It Safe

The key-safety checklist, the Windows and Mac lines and the .gitignore line, written from Anthropic's, Microsoft's and Apple's official docs (checked 2026-11-22), not run. Every key below is a fake.

### 1. claude-api-key-checklist.txt
```
# Claude API key: safety checklist
# From Claude API, Part 1. Facts checked 2026-11-22 from Anthropic's docs and help pages. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it claude-api-key-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as claude-api-key-checklist.txt
# Page and button names are as Anthropic's docs gave them on 2026-11-22. If a page looks different, check platform.claude.com/docs.

PLAN
[ ] 1. A paid Claude plan does not pay for the API: it is billed on its own.
[ ] 2. Max, Ultra and Team include monthly API credits: claim them by linking a Claude Console organization to your plan.
       Free, Pro and Enterprise aren't eligible. The credits don't roll over.

SIGN IN AND LIMIT
[ ] 3. Sign in (or create an account) at platform.claude.com. The old console.anthropic.com link forwards there.
[ ] 4. Spend limits page (platform.claude.com/settings/spend-limits): next to Monthly spend limit, click Set limit
       (or Adjust limit) and enter a small amount while you learn.
[ ] 5. Usage is paid from prepaid credits, bought on the Billing page.

CREATE THE KEY
[ ] 6. Keys page (platform.claude.com/settings/keys): click Create key.
[ ] 7. Name it for where it will be used (for example: Test Bakery laptop).
[ ] 8. Expiration: 3 hours, 1 day, 7 days, 30 days, custom or Never. It can't be changed later.
       A key made to last 14 days or more gets a warning email 7 days before it expires.
[ ] 9. Linked account: yourself (a personal key, for your own development).
[ ] 10. Workspace: pick one (the Default Workspace is fine), so calls don't need a workspace header.
[ ] 11. Copy the key now: it starts with sk-ant- and is shown only once. Lost it? Create a new key and delete the old one.

STORE IT
[ ] 12. Keep it in the environment variable ANTHROPIC_API_KEY, never in code, config files, public forums, emails or support tickets.
[ ] 13. Windows: Control Panel, System, Advanced system settings, Environment Variables, New under User variables.
        Then open a new PowerShell window. (Anthropic's one-line alternative, setx ANTHROPIC_API_KEY "your key",
        works too, but anything you type in PowerShell can be saved in its history file.)
[ ] 14. Mac: add the export line to ~/.zshrc in TextEdit, save, then run: source ~/.zshrc
[ ] 15. Check it without printing it: Windows "$env:ANTHROPIC_API_KEY".Length / Mac echo ${#ANTHROPIC_API_KEY}
        Any number above 0 means it's set.

KEEP IT SAFE
[ ] 16. If a tool uses a .env file, add .env to your .gitignore before you push anything to GitHub.
[ ] 17. Never put the key in a web page's code: call the API from your own server.
[ ] 18. GitHub scans public code for Claude keys; Anthropic deactivates any it finds and emails you.
[ ] 19. Think a key has leaked? Keys page: Disable (you can undo it) or Delete (permanent), then make a new key.
[ ] 20. Swap in a fresh key on a schedule (Anthropic's help page gives every 90 days as an example).
```

### 2. check-key-windows.ps1 (PowerShell)
```
# check-key-windows.ps1: check your Claude API key is set, without showing it (type the line in a NEW PowerShell window)
# Set the key first in the Environment Variables window (Control Panel, System, Advanced system settings,
# Environment Variables, New under User variables, name ANTHROPIC_API_KEY, value your key), then open a new window.
# This prints the key's length, never the key. 0 means it isn't set in this window.
"$env:ANTHROPIC_API_KEY".Length
```

### 3. set-key-mac.sh (Terminal)
```
# set-key-mac.sh: keep your Claude API key on a Mac (zsh, the default shell); type the lines one at a time, don't run this file
# 1. Open the settings file Terminal loads every time it starts (this creates it if it's missing, and opens it in TextEdit):
touch ~/.zshrc && open -e ~/.zshrc
# 2. In TextEdit, add this line at the bottom, without the leading "# ", with your own key right after the = sign,
#    no spaces and no quotes (the key below is a fake), as in Anthropic's own zsh line.
#    Then press Command-S to save and quit TextEdit. Don't type this line in Terminal, so the key stays out of its history.
# export ANTHROPIC_API_KEY=sk-ant-EXAMPLE-not-a-real-key
# 3. Load the change into this window:
source ~/.zshrc
# 4. Check it: this prints the key's length, never the key (0 means it isn't set):
echo ${#ANTHROPIC_API_KEY}
# The file is hidden because its name starts with a dot. To find it in Finder: press Shift-Command-G and type ~/.zshrc
```

### 4. .gitignore (one line)
```
# Keep secrets out of Git: add this line to the .gitignore file in your code folder
.env
```
