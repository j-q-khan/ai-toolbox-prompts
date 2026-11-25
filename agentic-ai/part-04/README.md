# Part 4: Agentic Coding Explained: How AI Coding Agents Plan, Edit and Check Your Code

Part 4 of 4, the last part of the Agentic AI series: how an AI coding agent works in a loop (it looks through your code, plans a change, edits, runs a check and hands the work back for you to review), shown on one tiny bug in Claude Code's plan mode, then the same loop in GitHub Copilot in the cloud, and how to keep it safe (facts checked 2026-11-22).

## What's here
- cake_orders.py: made-up practice code for Test Bakery that adds up the day's cake orders. It has one bug in it, on purpose.
- test_cake_orders.py: a test that checks 42, 35 and 51 cake orders add up to 128. Before the fix it stops with "expected 128, got 86"; after the fix it prints "Test passed: 128 cake orders".
- BUILD-PROMPT.md: a prompt for Claude Code that walks the agentic coding loop with you on these two files: run the test, find the bug, show a plan, wait for your yes, fix one line, run the test again and show you the output as evidence. It changes one line in cake_orders.py and asks before every change and every command.
- CODE.md: the same two files, as shown in the video, plus the one-line fix so you can check your agent's work.
- SOURCES.md: every page the video's facts come from, with the date checked.

## How to use it
1. Save cake_orders.py and test_cake_orders.py into a new, empty folder. In Notepad, set the box called Save as type to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.
2. To see the bug yourself, open a terminal in that folder and run: python test_cake_orders.py (on Windows, if python isn't found, try: py test_cake_orders.py). You need Python 3.
3. Open Claude Code in that folder, switch to plan mode (press Shift+Tab until the line under the box where you type says plan mode on), and paste the prompt from BUILD-PROMPT.md. When it shows its plan, choose "Yes, manually approve edits".
4. Running the test makes Python add a folder called __pycache__ beside the files. That's normal and safe to delete.

Everything in the video (Test Bakery, its code, the error, the plan, the edit and the passing test) is made up and labelled "Example output". Every app screen is drawn from the makers' docs. Nothing was signed up for, installed or run for the video. Features and plans change: they are as Anthropic's and GitHub's pages showed them on 2026-11-22.

That's the end of the Agentic AI series. Watch next: the AI Coding Agents series, whose first video puts four coding agents side by side: https://www.youtube.com/playlist?list=PLC_ZPnKjVJ3k

Not affiliated with Anthropic or GitHub. Prompts and practice code in this folder are free to use (MIT licence).
