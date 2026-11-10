# Claude build prompt: Blender MCP with Claude, Part 1

A desk phone stand block-out with no MCP server: Claude writes phone_stand.py, a short Blender 5.2 script, explains every line, and gives you steps to run it yourself in a new, empty Blender file. Written from the Blender 5.2 manual and Python API, checked 2026-11-10. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode. This uses no MCP server: Claude writes a Blender script, and you look over it and run it yourself.

Goal: write phone_stand.py, a short Blender 5.2 Python script that blocks out a small desk phone stand from three boxes, explain every line in plain words, and give me steps to run it myself in a new, empty Blender file.
Inputs: Blender 5.2 installed. Sizes in millimetres: a base 80 x 70 x 10, a back 80 x 8 x 100 tilted back 20 degrees, and a lip 80 x 8 x 20 at the front edge. Blender's default unit is the metre, so 80 mm is 0.08.
Steps, in order:
1. Show me the folder you'll work in and wait for my yes. Work only inside this folder. Don't install anything, don't run Blender and don't run the script; I'll run it myself.
2. Write phone_stand.py using only Blender's built-in bpy and Python's math module. It must only add three shapes to the open file, named Stand_Base, Stand_Back and Stand_Lip. No file reading or writing, no network, no other programs, nothing that deletes or changes anything already in the file. Put every size in a comment in millimetres.
3. Check it with `python -m py_compile phone_stand.py` (ask me first) and fix any syntax error.
4. Explain each line in one plain sentence, so I can check it does only what you say before I run it.
5. Write run-it-yourself.md: open Blender 5.2, start a new General file, click the default Cube and press the Delete key, switch to the Scripting tab, open phone_stand.py in the Text Editor, look over every line, then press Run Script, then select Stand_Base, Stand_Back and Stand_Lip in the Outliner and use Frame Selected in the View menu, because the stand is only 8 cm wide, and what I should see in the 3D viewport (three boxes: a base, a back leaning away from the lip, and a lip). Add what to do if nothing appears (check the Info editor for an error, and paste it to you).
6. Write safety-checklist.md with these lines: run scripts only in a new, empty Blender file; look over every line before running; a script that opens, writes or deletes files, or reaches the internet, is a stop sign; if I later add Blender MCP, follow Part 2's locks (stick to one version, Claude asks before any code runs, look over the code before I say yes, a test file with nothing private open, switch it all off afterwards). Then give me a three-line summary.
Safety: this folder only. No installs, no MCP servers, no web requests, and never run Blender or the script. Ask me before every command.
Output: phone_stand.py, run-it-yourself.md, safety-checklist.md and a three-line summary.
