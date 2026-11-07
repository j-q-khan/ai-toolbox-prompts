# Claude build prompt: AI CAD with Claude, Part 1

Use this in Claude Code (Pro or higher), in a new, empty folder. Start in plan mode.

Goal: set up this folder for designing 3D-printable parts in OpenSCAD by description, write my first part, and give me a size check I can go through before I print it.
Steps, in order:
1. Tell me what you plan to create, and wait for my yes. Only create or change files inside this folder. Don't install anything, download libraries or run commands; I preview, render and export in OpenSCAD myself.
2. Create CLAUDE.md with exactly these rules: every size in millimetres, stated in a comment at the top of each file; every size at the top of the file as a named variable with a comment; d= (diameter) for every cylinder and hole, never r=; a named clearance variable for every screw hole and fit; $fn = 64 at the top; every cutting shape in difference() sticks out 1 mm past both faces; a comment saying which way up to print and why; after each part, a table of every size used beside the size I asked for, plus anything guessed; no installs, downloads or commands; only files in this folder.
3. Ask me to describe my part: what it is, what it attaches to and how, every size in mm, where it needs extra room, and which way up I'll print it. If I don't have one yet, use this test part: a headphone wall hook with a back plate 30 x 70 x 5 mm, two 4 mm countersunk wood screws in 4.5 mm holes at 25 mm and 55 mm up, an 8.5 mm countersink at the front face, an arm 45 mm out and 6 mm thick along the bottom, and a 4 mm thick lip rising 10 mm at its end, printed lying on its side.
4. Write the part as one .scad file that follows CLAUDE.md, using only cube, cylinder, translate, rotate, for, union and difference.
5. Write size-check.md: a table with each size I gave, the variable that holds it, its value, and "match" or "check this"; every cylinder with its d value in mm; which face sits on the print bed; and anything you guessed.
6. Finish with the steps for me to do by hand in OpenSCAD: open the file, turn on Design, then Automatic Reload and Preview, check each size, press F6 to render, then use the export as STL button.
Safety: test parts only. Nothing printed from this is checked for strength; tell me to test any part that carries weight before trusting it.
Output: CLAUDE.md, the .scad file, size-check.md and a three-line summary.
