# Claude build prompt: AI CAD with Claude, Part 7

Gives you a fit-and-screw plan for a 3D-printed part in FreeCAD 1.1: a test card macro sized for your pegs, the Hole tool settings for your screws, and a checklist for the "Wire is not closed" error. Claude runs nothing; you run the macro yourself after looking through it. Written from the FreeCAD 1.1.4 source and the FreeCAD wiki, checked 2026-11-08. Not run or printed by us.

Use this in Claude Code (Pro or higher), in a new, empty test folder. Start in plan mode.

Goal: give me a fit-and-screw plan for my 3D-printed part in FreeCAD 1.1, a test card macro sized for my parts, and a checklist for the "Wire is not closed" error, without running FreeCAD or anything else.
Inputs: my part's description, the pegs or holes that must fit (their sizes in mm), and the screws I'll use (for example M3 or M4). If I don't give them, use this test case: a 10 mm peg into a hole, and two M4 screws through a 5 mm plate.
Steps, in order:
1. Tell me which files you'll create and wait for my yes. Only create files in this folder. Don't install anything, download anything, run FreeCAD, Python or any other program, or make web requests.
2. Write fit_test.py, a FreeCAD macro that imports only FreeCAD and Part and builds, in a new document, a plate with five holes for my peg size: the peg diameter plus twice a gap of 0.10, 0.15, 0.20, 0.25 and 0.30 mm, smallest next to a small dimple, plus a separate peg. Every size goes at the top as a named variable with a comment. It opens, saves and exports nothing, and has a comment saying it is checked by syntax only.
3. Write hole-plan.md: for each screw, the FreeCAD 1.1 Hole tool settings (Standard ISO metric regular, Size, Hole type) for three choices: Clearance / Passthrough at Medium, with the ISO 273 diameter; Tap drill (to be threaded), with the tap drill size; and Modeled thread with Customize thread clearance, explaining that Custom Clearance is added across the diameter, so my measured gap per side is doubled. Say which choice suits a printed part and why, and that small printed threads often strip.
4. Write wire-check.md: the four usual causes of "Wire is not closed" (a gap, a doubled line, a leftover stub, external geometry added as a real line in 1.1), and the FreeCAD 1.1 steps for each: Leave Sketch, select the sketch, Sketch, Validate Sketch, Highlight Troublesome Vertices, Missing Coincidences Find and Fix, the coincident constraint (C), Delete, Toggle Construction Geometry (G, N), and the preference Always add external geometry as construction.
5. Write fit-notes.md: how to use the test card (print both pieces flat, push the peg into each hole from the smallest, the first that slides in by hand is my sliding fit), and the rule hole = peg + 2 x gap, with my numbers worked out.
Safety: this folder only, test parts only. You run nothing; I run the macro myself in a new, empty FreeCAD file, after reading it, because a macro is Python and can do anything a program can on my computer. Nothing here is printed or tested: tell me to print and test any part before trusting it.
Output: fit_test.py, hole-plan.md, wire-check.md, fit-notes.md and a three-line summary.
