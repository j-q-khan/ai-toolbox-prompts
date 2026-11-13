# Claude build prompt: Claude Code for Beginners, Part 4

Use this in the Code tab of the Claude desktop app, in your claude-test folder, with the mode control on Manual. It only looks, and changes nothing. The settings file is outside your test folder, so it may ask before looking at it: approving is fine, because it only looks.

Goal: check that this session is set up safely for a beginner, and tell me in plain English.
Steps, in order:
1. Tell me the full path of the folder you're working in. If it is my home folder, my Desktop folder, or a drive's top folder such as C:\ or /, say so first and tell me to pick a new, empty folder instead, with Open folder in the row under the prompt box.
2. List the files in this folder, without opening them. Say whether it's empty, or how many files it holds.
3. Look at my Claude Code user settings file, ~/.claude/settings.json (on Windows, %USERPROFILE%\.claude\settings.json), without changing it. Note the value of "defaultMode" inside "permissions", or that it isn't there or the file doesn't exist.
4. Tell me what that means for new sessions in this app: if it's "default" or "manual", new local sessions can start in Manual from it; if not, say that I should check the mode control in the row under the prompt box before my first message and choose Manual.
Safety: don't edit, create or delete any file, don't run commands, don't install anything and don't go online. If the settings file has a key, token or password in it, don't repeat it.
Output: three to five short lines: the folder and whether it's safe, what the settings file says, and what to check in the mode control.
