# Claude build prompt: Claude Code for Beginners, Part 2

Use this in Claude Code, started inside your new claude-test folder, after pressing Shift+Tab until the status bar shows manual mode on.

Goal: make every new Claude Code session on this computer start in Manual mode, without losing any setting I already have.
Steps, in order:
1. Look for my user settings file, ~/.claude/settings.json (on Windows, %USERPROFILE%\.claude\settings.json). Don't change anything yet.
2. If the file exists, keep every setting already in it exactly as it is, and add "defaultMode": "default" inside "permissions", creating "permissions" if it isn't there. If "defaultMode" is already set to something other than "default" or "manual", tell me what it is and ask before changing it.
3. If the file doesn't exist, create it containing only this:
{
  "permissions": {
    "defaultMode": "default"
  }
}
4. Apart from the question in step 2, make the change with your file editing tool, so I see the whole change and approve it in the permission question, not in chat.
5. After saving, look at the file again, confirm it's valid JSON, and tell me to type exit, then claude, and check that the status bar says manual mode on.
Safety: change only ~/.claude/settings.json. Don't run commands, don't install anything, don't go online, and don't touch any other file.
Output: the saved settings file and one line saying whether it already existed.
