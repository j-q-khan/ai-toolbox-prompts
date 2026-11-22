Paste this into Claude Code, Anthropic's coding assistant, opened in a new, empty test folder. It makes two small files there and asks before every change. Written from Anthropic's docs, not run.

Goal: make me a small Python script that checks my Claude API key is set up safely, and a .gitignore that keeps my .env file out of Git.
Rules:
1. Work only in this folder. Don't open, change or delete any file outside it, don't install anything, and don't go online.
2. Before you write anything, show me your plan in three lines and wait for my OK.
3. Make check_key.py, using only Python's standard library (Python 3.10 or later). It looks up the environment variable ANTHROPIC_API_KEY and prints one of three plain messages: "Not set: add ANTHROPIC_API_KEY as an environment variable, then open a new terminal window", "Set, but it doesn't start with sk-ant-: check you copied the whole key", or "Set, and it starts with sk-ant-".
4. Never print, log or save the key itself, or any part of it beyond the words sk-ant-.
5. The script makes no network calls and sends the key nowhere. It exits with code 0 only when the key is set and starts with sk-ant-, and 1 otherwise.
6. Make .gitignore with these lines, one per line: .env, .env.*, and a comment line at the top that says "Keep secrets out of Git".
7. If a .gitignore already exists here, don't overwrite it: show me the lines you'd add and ask first.
8. Ask me before every file change, and change nothing else.
9. When it's done, tell me how to run the script on Windows (PowerShell) and on a Mac (Terminal), and remind me to open a new terminal window after setting the variable.
Output: check_key.py and .gitignore, and a one-line summary of what you made.
