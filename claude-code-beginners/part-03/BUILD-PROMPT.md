# Claude build prompt: Claude Code for Beginners, Part 3

Use this in Claude Code in VS Code, in your claude-test folder, in Manual mode. It only looks at two settings files and changes nothing. Both files are outside your test folder, so it may ask before looking at each one: Yes is fine, because it only reads them.

Goal: tell me which permission mode my new Claude Code conversations in VS Code will start in, and why.
Steps, in order:
1. Look at my VS Code user settings file, without changing it: on Windows %APPDATA%\Code\User\settings.json, on a Mac ~/Library/Application Support/Code/User/settings.json. Note the value of "claudeCode.initialPermissionMode", or that it isn't there.
2. Look at my Claude Code user settings file, ~/.claude/settings.json (on Windows, %USERPROFILE%\.claude\settings.json), without changing it. Note the value of "defaultMode" inside "permissions", or that it isn't there or the file doesn't exist.
3. Apply Anthropic's order for the VS Code extension, first match wins: (1) claudeCode.initialPermissionMode; (2) the mode I last picked from the mode indicator, if it was Manual, Edit automatically or Auto; (3) permissions.defaultMode from ~/.claude/settings.json; (4) the built-in default, Auto. You can't see item 2, so say that it would win over item 3 if I've ever picked a mode there.
4. Tell me in plain English which mode new conversations will start in. If claudeCode.initialPermissionMode isn't "manual" or "default", tell me how to set it: Settings (Ctrl+, or Cmd+,), the User tab, search initial permission mode, choose manual.
Safety: only look at those two files. Don't edit or create any file, don't run commands, don't install anything and don't go online. If a file has a key, token or password in it, don't repeat it.
Output: three to five short lines: what each file says, and the mode new conversations will start in.
