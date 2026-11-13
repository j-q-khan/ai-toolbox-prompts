# Full code: How to Install Claude Code on Windows and Mac (Safe Setup for Beginners)

Every command and file from this video, written from Anthropic's docs (checked 2026-11-13). Nothing was installed or run; outputs shown in the video are labelled "Example output". The JSON file was parsed with Python's json module. manual-mode-settings.json only shows what the setting looks like: never save it over a settings file you already have, because the prompt in manual-mode-prompt.txt asks Claude Code to add the line and keep everything else, and you see the change before it's saved.

### 1. install-claude-code.txt
```
# Install Claude Code: one path per system (Anthropic's terminal guide, checked 2026-11-13)

# WINDOWS
# 1. Optional, but this course uses it later: install Git for Windows from
#    https://git-scm.com/downloads/win
#    Click Next on each screen. Keep the default editor. On "Adjusting your PATH environment",
#    keep the recommended option.
# 2. Open PowerShell: press Win + X and choose Windows PowerShell (or Terminal).
#    Each line should start with PS. No PS means you're in CMD: open PowerShell instead.
#    You don't need the Admin entry.
# 3. Paste this line and press Enter. It shows no progress; wait for "Claude Code successfully installed!"
irm https://claude.ai/install.ps1 | iex

# MAC
# 1. Open Terminal: press Cmd + Space, type Terminal, press Enter.
# 2. Paste this line and press Enter. It shows no progress; wait for "Claude Code successfully installed!"
curl -fsSL https://claude.ai/install.sh | bash

# BOTH: open a fresh terminal window, then check it worked (prints a version number):
claude --version

# BOTH: make a new, empty test folder, move into it, and start Claude Code there:
mkdir claude-test
cd claude-test
claude
# The first time, a browser window opens to sign in. If it doesn't, press c to copy the link.
# Then press Shift+Tab until the status bar says "manual mode on" (one press from auto mode).
# Check Manual mode stuck: type exit to leave, then start it again; the status bar says manual mode on.
exit
claude
```

### 2. fix-install-errors.txt
```
# Fixes from Anthropic's terminal guide (checked 2026-11-13). Run only the one for the error you see.

# WINDOWS: 'claude' is not recognized
# The install folder isn't on your PATH. Paste these two lines into PowerShell, then open a new
# PowerShell window and type claude again:
$currentPath = [Environment]::GetEnvironmentVariable('PATH', 'User')
[Environment]::SetEnvironmentVariable('PATH', "$currentPath;$env:USERPROFILE\.local\bin", 'User')

# WINDOWS: 'irm' is not recognized
# You're in CMD, not PowerShell. Open PowerShell (Win + X, Windows PowerShell) and paste the install line again.

# WINDOWS: 'Claude Code does not support 32-bit Windows'
# You opened "Windows PowerShell (x86)". Open the entry without (x86) in its name and paste the install line again.

# MAC: command not found: claude
# The installer prints the exact fix under "Setup notes"; run that, or these two lines (Zsh, the Mac default),
# then open a new Terminal window and type claude again:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# MAC: a page of web code, or "App unavailable in region"
# Claude Code isn't offered in your country: https://www.anthropic.com/supported-countries
# Otherwise, run the install line again.
```

### 3. manual-mode-prompt.txt
```
# Paste into Claude Code after pressing Shift+Tab until the status bar says manual mode on.
# If it first asks only to look at the file, choose Yes. When it shows the change, Yes is highlighted: press Enter.
# Skip "for this session" and "switch to auto mode". Don't press Shift+Tab on a question: there it picks the for-this-session option.
Make every new Claude Code session on this computer start in Manual mode. If ~/.claude/settings.json exists, keep everything in it and add "defaultMode": "default" inside "permissions". If it doesn't exist, create it with only that setting. Make the change as a file edit, so I approve it in the permission question, and change no other file.
```

### 4. manual-mode-settings.json
```
{
  "permissions": {
    "defaultMode": "default"
  }
}
```

### 5. undo-practice.txt
```
# Inside your claude-test folder, in Manual mode. Choose Yes each time it asks.
Make a text file called hello.txt with one line that says hello.
Change the line in hello.txt to goodbye.
# Then, with the prompt box empty, press Esc twice, pick the goodbye prompt,
# and choose "Restore code and conversation". hello.txt says hello again.
# Esc once stops Claude Code in the middle of whatever it's doing.
```
