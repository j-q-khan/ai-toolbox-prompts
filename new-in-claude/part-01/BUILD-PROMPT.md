Paste this into Claude Code, Anthropic's coding tool, in a new, empty test folder. It builds a small script that turns meeting notes you've copied from a Claude meeting page into a checklist of who does what, tested on made-up notes only, and it changes nothing until you agree. Written from Anthropic's help page "Use Claude Meetings", checked 2026-11-26. Nothing here was run for the video.

Goal: build a small Python script, notes_to_checklist.py, that turns meeting notes saved as a plain text file into a Markdown checklist of action items, one line per job, with who owns it and when it's due.
Context: Claude Meetings puts notes, a summary and action items on each meeting's page. Anthropic's pages don't describe an export, so the input is notes I copy from the meeting page and save as a .txt file. Use made-up notes only.
Steps, in order:
1. Tell me your plan in a few lines and wait for my OK. Don't create, change or delete any file before I say yes.
2. Create sample-notes.txt with made-up notes for a meeting called "Weekly planning (test)": a two-line summary, then a heading "Action items" and four items, such as "Test User A: send the menu draft by Friday", "Test User B: book the room", "Ask the team about the budget", and "Test User A: share the slides by 2026-12-04". Use no real names, companies or emails; test@example.com is fine.
3. Write notes_to_checklist.py with the Python standard library only. It takes the notes file's path and an output path as arguments. It finds the "Action items" section (any heading line containing those words, in any case) and reads each item that starts with a dash, an asterisk or a number.
4. For each item, write one line: "- [ ] the job (owner: name, due: date)". Take the owner from a "Name:" prefix and the due date from "by" plus a day or date. When either is missing, write "owner: not stated" or "due: not stated". Never guess an owner or a date.
5. If there's no "Action items" section, print a clear message and write nothing. Never overwrite an existing output file: stop and tell me.
6. Run it on sample-notes.txt only, writing checklist.md, and show me checklist.md.
7. Add a short README.md: how to run it on Windows and Mac, that it never sends anything anywhere, and a reminder to remove private details from real notes and to follow your organization's rules before using them.
Safety: work only inside this folder. No network access, no installs, no other packages. Don't open or upload real meeting notes. Ask before every file you create.
Output: the three files, checklist.md made from the made-up notes, and a two-line note of what you did.
