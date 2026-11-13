# Full code: Claude Code Tutorial: Build Your First Website, No Coding Needed

Everything from this video, written from Anthropic's docs (checked 2026-11-13). Nothing was installed or run, and nobody has run the prompt; files shown in the video are labelled "Example output". The example index.html and style.css are separate files in the GitHub folder, under example-output/.

### website-prompt.txt
```text
# Paste into Claude Code inside your claude-test folder, with the status bar showing manual mode on.
# It asks before each file: choose the plain Yes (not the option that stops it asking). If it asks to run a command, choose No.
Make a one-page website for an invented bakery called Crumb and Co. Use exactly two plain files in this folder, index.html and style.css, with index.html linking to style.css, and nothing else: HTML and CSS only, with no JavaScript, no images, and no fonts, links or files from the internet. On the page, put the bakery's name as the main heading, a one-line welcome, a short About us paragraph, a menu of four made-up items with prices, and the opening hours, all dummy text. Use warm, friendly colours and keep each file under 80 lines. Leave any other files in this folder as they are. Don't run any commands, install any packages, start a server, use any accounts or open the page for me. Ask me before creating or changing any file outside this folder. When you've finished, tell me in two short sentences what each file does, and the full path of index.html so I can find it and double-click it.
```

### change-and-undo.txt
```text
# After the page is built and open in your browser, go back to the terminal window by clicking its button on the taskbar along the bottom of the screen on Windows, or its icon in the Dock on a Mac.
# Then paste this and press Enter to send it. Check the change is only the colour, then choose Yes:
In style.css, change the page's background colour to pale blue, and change nothing else.
# See it: click the page's browser tab and refresh (F5 on Windows, Cmd + R on a Mac).
# Undo it: in the terminal, with the typing box empty, press Esc twice to open the rewind menu (or type /rewind and press Enter).
# Pick the colour prompt with the arrow keys and press Enter, choose "Restore code and conversation" and press Enter, then refresh the browser again.
# The colour prompt comes back into the typing box: don't press Enter, or it makes the change again.
# Esc once stops Claude Code in the middle of a task.
```

### open-your-page.txt
```text
# Start Claude Code in your test folder (made in the install video, in your home folder):
# Windows: press Win + X, choose Windows PowerShell or Terminal (not the one marked Admin). Mac: press Cmd + Space, type Terminal, press Enter.
cd claude-test
# Says it cannot find the path, or no such file or directory? Open a fresh terminal window (it starts in your home folder) and try again.
claude
# The status bar should say manual mode on. If it says auto mode on, press Shift+Tab once.

# Open the page Claude wrote (you don't need Claude Code for this):
# Windows: File Explorer (Win + E), click This PC, then double-click Local Disk (C:), Users, your name (the folder in the path Claude gave you), claude-test.
# Mac: click Finder (left end of the Dock), then Go (menu bar), Home, and double-click claude-test.
# Windows may hide extensions: if you see "index" and "style", index is the page.
# Double-click index.html (or index). It opens in your web browser.
# Opened as code in Notepad, TextEdit or VS Code, or asked which app to use? Right-click index (Mac: Control-click), choose Open with, pick your web browser.
# The bar at the top of the browser shows a path to the file: only you can see this page.
```
