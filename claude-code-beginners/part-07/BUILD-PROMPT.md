# Claude build prompt: Claude Code for Beginners, Part 7

Use this in Claude Code, started inside your claude-test folder, with the status bar showing manual mode on. It adds the one permission rule this video sets up, without losing any setting you already have.

Goal: stop Claude Code opening any file called .env, in every folder I start it in, without losing any setting I already have.
Steps, in order:
1. Look for my user settings file, ~/.claude/settings.json (on Windows, %USERPROFILE%\.claude\settings.json). Don't change anything yet.
2. If the file exists, keep every setting in it exactly as it is, and add "Read(**/.env)" to the "deny" list inside "permissions", creating "permissions" or "deny" if they aren't there. If the rule is already there, tell me and change nothing.
3. If the file doesn't exist, create it containing only this:
{
  "permissions": {
    "deny": ["Read(**/.env)"]
  }
}
4. Make the change with your file editing tool, so I see the whole change and approve it in the permission question, not in chat.
5. After saving, look at the file again, confirm it's valid JSON, and tell me to type /permissions to see the rule.
Safety: change only ~/.claude/settings.json. Don't run commands, don't install anything, don't go online, and don't touch any other file.
Output: the saved settings file and one line saying whether it already existed.
