# Full code: Claude Code for Beginners: Build Your First App From Scratch

Everything from this video, written from Anthropic's docs (checked 2026-11-13). Nothing was installed or run, and nobody has run the prompt; files shown in the video are labelled "Example output". The example index.html, style.css, app.js and the bug-fix change are separate files in the GitHub folder, under example-output/.

### app-prompt.txt
```text
# Paste into Claude Code inside your claude-test folder, once the status bar says plan mode on (press Shift+Tab until it does; never send it at accept edits on).
# When the plan appears: don't press Shift+Tab (it approves the plan). Skip any choice that says auto; choose "Yes, manually approve edits".
# Then it asks before each file: choose the plain Yes. If it asks to run a command, choose No.
Build a small to-do list app that works in my web browser. Use exactly three plain files in this folder, index.html for the page, style.css for the look and app.js for what happens when I click, with index.html linking to the other two, and nothing else: plain HTML, CSS and JavaScript only, with no libraries, frameworks, fonts, images, or links or files from the internet. The app needs a box to type a task, an Add button that also works when I press Enter, a list where each task has a tick box to mark it done and a Delete button, and a short line saying how many tasks are left. Save the tasks in this browser's local storage so they're still there when I reload the page, keep them only in this browser, and if the browser won't allow local storage, let the app still work without saving. Keep index.html under 40 lines, style.css under 80 lines and app.js under 100 lines. Leave any other files in this folder as they are. Don't run any commands, install any packages, start a server, use any accounts or open the app for me. Ask me before creating or changing any file outside this folder. Show me your plan first, and wait for my yes before writing any file. When you've finished, tell me in one short sentence what each file does, and the full path of index.html so I can find it and double-click it.
```

### bug-fix-prompt.txt
```text
# After the app is open in your browser. Click the terminal, paste this, and press Enter:
If pressing Enter or clicking Add with nothing typed adds an empty task to the list, stop that from happening and change nothing else. If the app already ignores empty tasks, tell me so and change nothing.
# If there's a change, look it over and choose the plain Yes. Then click the app's browser tab and reload (F5 on Windows, Cmd + R on a Mac).
# Press Enter with nothing typed: nothing should be added. Click Delete on any empty task saved before the fix.
# A change went wrong? In the terminal, with Claude's typing box empty, press Esc twice to open the rewind menu, pick the prompt, choose "Restore code and conversation".
```

### open-and-test.txt
```text
# Start Claude Code in your test folder (made in the install video, in your home folder):
# Windows: press Win + X, choose Windows PowerShell or Terminal (not the one marked Admin). Mac: press Cmd + Space, type Terminal, press Enter.
cd claude-test
# Says it cannot find the path, or no such file or directory? Open a fresh terminal window (it starts in your home folder) and try again.
claude
# Plan mode: press Shift+Tab until the status bar says plan mode on (you pass accept edits on along the way; don't send the prompt there).
# Or, instead of Shift+Tab: type /plan and a space, then paste the app prompt after it, and press Enter.
# A plan not right? Choose "No, keep planning" and say what to change, in plain words.
# Pressed Shift+Tab at the plan by accident? That approves the plan. Press Esc to stop Claude, press Shift+Tab until the status bar says manual mode on, then type: Carry on with the plan, and ask me before each file.

# Open the app Claude wrote (you don't need Claude Code for this):
# Windows: File Explorer (Win + E), click This PC, then double-click Local Disk (C:), Users, your name (the folder in the path Claude gave you), claude-test.
# Mac: click Finder (left end of the Dock), then Go (menu bar), Home, and double-click claude-test.
# Windows may hide extensions: if you see "index", "style" and "app", index is the page.
# Double-click index.html (or index). It opens in your web browser.
# Opened as code in Notepad, TextEdit or VS Code, or asked which app to use? Right-click index (Mac: Control-click), choose Open with, pick your web browser.

# Test it:
# Type a task and press Enter (or click Add). Add two more. Tick one. Click Delete on another. The count of tasks left changes.
# Reload the page (F5 on Windows, Cmd + R on a Mac): the tasks are still there, kept in this browser's local storage.
# A different browser, or a private window, starts with an empty list: that's normal.
# For a file opened from your computer, browsers don't promise to keep local storage: some may not save at all, or may forget the list later, and moving the folder can start a fresh, empty list. The app still works; it just won't remember.

# In VS Code or the desktop app: the same prompt works; pick Plan from the mode menu instead of pressing Shift+Tab.
```
