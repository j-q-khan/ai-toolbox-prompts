# Claude build prompt: Meshy AI for 3D Printing: From Image to an STL That Actually Prints

An offline pre-print helper for Claude Code: it reads an STL and tells you the size your slicer will see, the scale for the height you want, whether it fits your printer, and whether the mesh has holes, non-manifold edges or loose pieces. Checked against Meshy's docs and help centre on 2026-11-07. Not run by us. It never calls Meshy or uses a key.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small, offline pre-print helper that reads an STL file and tells me, before I open my slicer, how big it will print, how much to scale it for the height I want, whether it fits my printer, and whether the mesh has holes, non-manifold edges or loose pieces.
Inputs: an STL file path, my target height in millimetres, and my printer's build volume in millimetres (default 256 x 256 x 256). If I give no file, create two test files in a folder called test-stl with Python's standard library only: a closed triangular pyramid (a tetrahedron, four triangles) and the same shape with one face removed, each saved once as ASCII STL and once as binary STL, and make one binary file's 80-byte header start with the word solid.
Rules, from Meshy's docs and help centre (checked 2026-11-07; re-check https://docs.meshy.ai/en/webapp/guides/use-cases/3d-printing before you trust them):
- an STL has no units; report sizes as millimetres, because slicers read the numbers that way
- a watertight mesh has no holes or open edges; an edge used by only one triangle is open, and an edge used by three or more is non-manifold
- a filament (FDM) printer's minimum wall is about 1.2 mm; just print this as a reminder, don't try to measure walls
Steps, in order:
1. Tell me which files you'll create and wait for my yes. Use Python 3 and the standard library only. Install nothing, make no network calls, and never call Meshy's API or use any key.
2. Write preprint.py. Detect binary STL first (the file size equals 84 plus 50 times the triangle count in bytes 80 to 84), and only then ASCII, because some binary files start with the word solid.
3. Print: the size in X, Y and Z in mm, the triangle count, open edges, non-manifold edges, and the number of loose pieces (groups of triangles that share no edge with the rest), joining vertices that match to 5 decimal places.
4. Print the scale percentage that turns the current Z height into my target height, the new X, Y and Z after scaling, and FITS or TOO BIG against my build volume.
5. End with a plain verdict: LOOKS PRINTABLE, or a list of what to fix and where (Meshy's Print Check, the slicer's Fix model, or Blender's 3D Print Toolbox), and the reminder about 1.2 mm walls.
6. Run it on the test files and show me the output. Then explain how to run it on my own file.
Safety: this folder only. Never change or overwrite the STL I give you; the script only looks at it. Print a clear error for a missing, empty or non-STL file instead of crashing. Stop and ask me before doing anything not listed here.
Output: preprint.py, the test-stl folder, and a three-line summary.
