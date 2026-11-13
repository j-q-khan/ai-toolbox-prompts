# Full code: Claude Code Desktop App: Use Claude Code Without the Terminal

Everything from this video, written from Anthropic's docs and help centre and Apple's and Microsoft's help pages (checked 2026-11-13). Nothing was installed or run; outputs shown in the video are labelled "Example output".

### 1. practice-prompts.txt
```text
# Paste into the Code tab of the Claude desktop app, in your claude-test folder, with the mode control on Manual.
# Prompt 1: look over the diff, then approve it.
Make a file called packing-list.txt with three things to bring on a day trip, one per line.
# Prompt 2: this time, decline it. Then click the file's name in the chat, or open packing-list.txt from Documents, claude-test: it still has three things.
Add sunscreen to packing-list.txt.
# The app's docs describe no undo button: declining before a change is applied is the undo here.
# Stop it mid-task: the stop button, or Esc.
```

### 2. desktop-app-setup-steps.txt
```text
# Claude Code in the desktop app: the safe setup (Anthropic's docs and help centre, checked 2026-11-13)
# You need a paid Claude plan: Pro, Max, Ultra, Team or Enterprise. The free plan doesn't include Claude Code.
# The app includes Claude Code, so you don't install anything else.
# 1. Download Claude from https://claude.com/download
#    macOS: one download for every Mac (Intel and Apple Silicon).
#    Windows: the Windows download. Windows (arm 64) only if Settings, System, About says ARM-based processor.
# 2. Windows: open the downloaded file from your Downloads folder. If Windows asks to allow the app to make changes, choose Yes.
#    Once it's installed, open Claude from the Start menu if it isn't open already.
#    Mac: open the downloaded file from Downloads, drag Claude to the Applications folder,
#    then in Finder, click Applications and double-click Claude. If your Mac asks if you're sure you want to open it, click Open.
# 3. Sign in with the account your paid plan is on.
# 4. Click Code at the top of the sidebar. Only icons? Hover over each to see its name.
#    Asked to upgrade: subscribe at https://claude.com/pricing. Asked to sign in online: finish it, then restart the app.
#    Where-it-runs control above the prompt box instead of under it? Update the app:
#    Help > Check for Updates... (Windows) or Claude > Check for Updates... (Mac).
# 5. In the row under the prompt box, click the first control and choose the top entry under Local.
#    This course stays on Local. Cloud sessions make file edits without asking first.
# 6. Click the folder control beside it, choose Open folder..., go to Documents,
#    click New Folder, name it claude-test, select it, then Select Folder (Windows) or Open (Mac).
#    Never your Desktop folder or your home folder. Asked to trust the folder? Yes: you made it, and it's empty.
# 7. Click the mode control in the same row (or Ctrl+Shift+M on Windows, Cmd+Shift+M on a Mac) and choose Manual.
#    The app remembers it for this folder. Check it before each first message.
#    Shift+Tab doesn't switch modes in the app.
#    Leave Allow bypass permissions mode off in Settings.
# 8. Try practice-prompts.txt. Approve the first change, decline the second.
# 9. After you approve a change, the file is saved in claude-test, and the Changes card beside the chat
#    shows line counts such as +12 -1 (yours will differ). Click them to see each change, file by file.
#    No card? Make the window wider, or click Changes in the bar along the top of the session.
# 10. The small ring in the row under the prompt box shows your plan usage, shared with your Claude chats.
# Never paste a password or a key into a prompt.
```
