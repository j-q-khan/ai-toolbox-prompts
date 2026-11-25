Paste this into Claude Code, Anthropic's coding tool, after you've saved cake_orders.py and test_cake_orders.py into a new, empty folder and opened Claude Code in that folder. Claude Code needs a Claude subscription or an Anthropic Console account (Anthropic's docs, checked 2026-11-22), and the test needs Python 3 on your computer. Before you paste, switch to plan mode: press Shift+Tab until the line under the box where you type says plan mode on. When Claude Code shows its plan and asks how to go on, choose "Yes, manually approve edits" so it asks before the edit. It walks the agentic coding loop with you on made-up practice code: run the test, find the bug, show a plan, wait for your yes, make a one-line fix, run the test again and show you the output as evidence. It looks only at those two files, changes one line in cake_orders.py, and asks before every change and every command. Running the test makes Python add a folder called __pycache__ beside the files; that is normal and safe to delete. Written from Anthropic's docs, checked 2026-11-22. Nothing here was run for the video.

Goal: walk me through the agentic coding loop on the two practice files in this folder, and fix the one bug in cake_orders.py only after I approve your plan.
Steps, in order:
1. Look only at cake_orders.py and test_cake_orders.py in this folder. Don't open any other file, and don't use the internet.
2. Ask me before you run any command. Then run the test with: python test_cake_orders.py (on Windows, if python isn't found, try: py test_cake_orders.py). If Python isn't installed, stop and tell me.
3. Show me the exact output, and explain in plain words what the error means.
4. Find the cause in cake_orders.py, and explain it in one or two sentences a beginner would follow.
5. Write a short plan: the one line you'd change, what it will say afterwards, and how you'll check it. Then stop and wait for my yes.
6. After I say yes, change only that one line in cake_orders.py, show me the old and new versions of the line, and ask before saving.
7. Ask before running the test again, then run it, and show me the command you ran and its full output as evidence.
8. If the test still fails, stop and show me the output instead of trying other changes.
Safety: change nothing else. Never edit test_cake_orders.py, and don't create, rename, move or delete any file yourself (the __pycache__ folder Python makes on its own is fine). Don't install anything, and don't use git. If anything is unclear, ask me first.
Output: the line you changed, the command you ran, and its output.
