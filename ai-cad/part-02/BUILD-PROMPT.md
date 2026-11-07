# Claude build prompt: OpenSCAD Tutorial for Beginners: Code Your First 3D Print

A read-only OpenSCAD checker for Claude Code: it explains a .scad file line by line for a beginner and lists the common mistakes, without running OpenSCAD. Checked against the OpenSCAD manual on 2026-11-07. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a read-only checker that explains an OpenSCAD .scad file line by line for a beginner and lists the mistakes beginners and AI code make, without running OpenSCAD.
Inputs: every .scad file in this folder. If there are none, first write hook.scad from the Full code of this video, plus a deliberately broken copy, hook-broken.scad, with: a difference() whose first shapes are the plate, the arm and the lip with no union() around them, a hole cylinder exactly as long as the plate is thick and starting on its face, a hole written with r = 4.5 instead of d = 4.5, a size typed as a bare number in three places, a missing semicolon, and no $fn line. Use both.
Steps, in order:
1. Tell me which files you'll open and what you'll write, and wait for my yes. Never run openscad or any other program on these files, install nothing, and make no network calls.
2. Check brackets: count (), [] and {} per file and report the first line where they stop balancing. Report statements that should end in a semicolon and don't, with the line number.
3. Explain: write explain.md with one short plain-English sentence per line of code, in order, saying what the line makes, moves, joins or cuts, and naming X, Y and Z as across, out and up.
4. Sizes: list every bare number inside cube(), cylinder(), sphere(), translate() or rotate() that isn't a named variable, and suggest a variable name for each. List every cylinder used as a hole with its diameter in mm, and flag any that uses r= where d= was meant.
5. difference(): for each one, say which shape is kept (the first child) and which are cutters. If the first child is not a union() or a single shape, warn that the other shapes will be cut away. For each cutter, work out from the numbers whether it extends past both faces of the shape it cuts; if a face lines up exactly, mark it "flush: likely a thin skin" and suggest extending it by 1 mm each side.
6. Rounding and smoothness: flag minkowski() (it grows the shape by the rounding radius on every side and can be slow) and suggest hull() for flat parts; flag a missing $fn, or a $fn under 24, for parts with holes.
7. center = true: list every shape using it and say where its middle sits, because it changes where translate moves it.
8. Write check.md: a table with each finding, the file, the line, why it matters for a 3D print and the fix. Then ask me before changing anything. Only if I say yes, write fixed copies with -fixed added to the name, and never overwrite the originals.
Safety: this folder and test files only. No programs run, no installs, no network calls. Stop and ask me before doing anything not listed here.
Output: explain.md, check.md and a three-line summary.
