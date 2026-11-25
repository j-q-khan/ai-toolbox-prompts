Paste this into Claude Code, Anthropic's coding agent that works with the files in a folder on your computer, started in a new, empty folder (the video calls it arcade). It builds Comet Dodge, a small browser game in one file, in three small steps, and waits for you to test each step in your browser before the next one. It creates one file, game.html, downloads nothing, installs nothing and changes nothing else. Written for this video from Anthropic's docs, checked 2026-11-25. Nothing here was run for the video.

Goal: build a small browser game in one file, game.html, one change at a time.
Rules for every step: one HTML file with a canvas element and plain JavaScript, nothing loaded or downloaded from the internet, and no other files. Change only what the step asks for. After each step, tell me in two lines what changed and how to test it in my browser, then wait until I say next.
Steps, in order:
1. Tell me in two sentences what you'll build and the one file you'll create, then wait for me to say go. If game.html already exists in this folder, stop and tell me instead.
2. Create game.html, a game called Comet Dodge. A ship at the bottom moves left and right with the arrow keys and stops at the edges. Comets fall from the top, and touching one ends the game. The score goes up every second you survive and shows in the top left corner. When you lose, show Game over and Press R to play again, and R starts a new game.
3. Add yellow stars that fall more slowly than the comets. Catching a star adds 10 points. Change nothing else.
4. Make the comets fall 15% faster every 10 seconds. Change nothing else.
5. Tell me how to open game.html in my browser: on Windows, start arcade\game.html in a new PowerShell window; on a Mac, open arcade/game.html in a new Terminal window.
Safety: don't run any program, install anything, upload anything or call any website or service. Don't change, move or delete any file except the game.html you create. Don't sign up for or sign in to anything.
Output: game.html, and after each step a two-line note on what to test in the browser.
