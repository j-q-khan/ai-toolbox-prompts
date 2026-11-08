# Full code: FreeCAD with AI: Fix "Wire Is Not Closed", Tolerances and Threads

Written from the FreeCAD 1.1.4 source and the FreeCAD wiki, checked 2026-11-08. Not run by us: the steps were checked against FreeCAD 1.1.4's labels and the Python by syntax only (`py_compile`). Nothing here has been printed or tested.

### wire-not-closed-steps.txt (find and fix the error in FreeCAD 1.1.4)
```
"Wire is not closed": an outline in your sketch doesn't come back to where it started.
Four usual causes: a gap, a doubled line, a leftover stub, external geometry added as a real line (new in 1.1).

1  Leave Sketch (the tool only works from outside the sketch)
2  Click the sketch in the Model tree → Sketch menu → Validate Sketch
3  Highlight Troublesome Vertices: marks points where an outline stops or too many lines meet
4  Missing Coincidences → Find (yellow crosses) → Fix (joins them)
5  By hand: double-click the sketch, click the two ends, press C (Coincident Constraint)
6  Doubled line or stub: click it, press Delete, check the corner is still joined
7  External geometry (pinkish purple, solid): click it, press G then N (Toggle Construction Geometry)
8  For good: Edit → Preferences → Sketcher → General →
   tick "Always add external geometry as construction"
   (on a Mac: FreeCAD → Preferences)
9  Leave Sketch, then Pad or Pocket again
```

### open_points.py (a read-only check: prints the open points of a sketch, changes nothing)
```
s = App.ActiveDocument.getObject("Sketch")
print("Open points:", s.OpenVertices)
# Paste both lines into View → Panels → Python console, or let Claude run them through Part 6's
# server (execute_code asks first). "Sketch" is the sketch's Name in the Model tree's
# properties, which can differ from its label. An empty list means no open points.
# Checked by syntax only; not run by us.
```

### fit_test.py (a FreeCAD macro: a 10 mm peg and a plate with five holes, to measure your printer's gap)
```
# fit_test.py: a print-fit test card for FreeCAD 1.1, in a new document.
# Holes 10.2 to 10.6 mm across for a 10 mm peg, so the gap per side runs 0.10 to 0.30 mm.
# The smallest hole is next to the small dimple.
# To run it: Macro → Macros → Create, name it fit_test, paste this in, save,
# then Macro → Execute Macro, and press V then F to fit the view.
# A macro is Python and can do anything a program can on your computer, so look through
# every line before you run it. This one imports only FreeCAD and Part, and opens, saves
# and downloads nothing. It only makes shapes in a new document.
# Then select FitPlate and Peg in the Model tree, File → Export, STL Mesh, and print both flat.
# Push the peg into each hole from the smallest: the first it slides into by hand is your
# sliding fit. Size future holes as peg + 2 x that gap.
# Written from the FreeCAD 1.1.4 source and wiki, checked 2026-11-08.
# Checked by syntax only; not run or printed by us.

import FreeCAD as App
import Part

peg_d = 10.0                            # peg diameter, mm
gaps = [0.10, 0.15, 0.20, 0.25, 0.30]   # gap per side for each hole, mm
spacing = 14.0                          # hole centre to hole centre, mm
plate_t = 5.0                           # plate thickness, mm
plate_w = 18.0                          # plate depth, front to back, mm
peg_h = 15.0                            # peg height, mm

V = App.Vector
doc = App.newDocument("FitTest")

plate = Part.makeBox(len(gaps) * spacing + 4, plate_w, plate_t)
sizes = []
for i, g in enumerate(gaps):
    d = peg_d + 2 * g
    sizes.append(d)
    x = 2 + spacing / 2 + i * spacing
    plate = plate.cut(Part.makeCylinder(d / 2, plate_t + 2, V(x, plate_w / 2, -1)))

# the dimple: 2 mm across and 1 mm deep, beside the smallest hole
plate = plate.cut(Part.makeCylinder(1.0, 2.0, V(3, 2.5, plate_t - 1)))

# the peg, standing apart from the plate
peg = Part.makeCylinder(peg_d / 2, peg_h, V(len(gaps) * spacing / 2, plate_w + 15, 0))

Part.show(plate, "FitPlate")
Part.show(peg, "Peg")
doc.recompute()
print("Holes (mm): " + ", ".join("%.2f" % d for d in sizes) + "; peg %.2f mm" % peg_d)
```

### hole-settings.txt (the Hole tool in FreeCAD 1.1.4, for an M4 screw)
```
Sketch: circles where the holes go (only each circle's centre counts) → Hole
Standard: ISO metric regular
Size: M4x0.7
No hole in your part while the panel's open? It's drilling away from it: tick Switch direction

Hole type: Clearance / Passthrough   the screw slides through
  Clearance: Medium = 4.5 mm (Fine 4.3, Coarse 4.8; ISO 273, from FreeCAD 1.1.4's table)
Hole type: Tap drill (to be threaded)   3.3 mm, for cutting a thread with an M4 tap
Hole type: Modeled thread   the real thread, drawn into the hole
  Tick Customize thread clearance; Custom Clearance is added across the diameter:
  a gap of 0.2 mm a side = type 0.4 mm
  Add it as one of your last steps (slow to compute)
  Depth type: Dimension, a number (not Through all, to keep the file smaller)

For printed parts with small screws (M3, M4): a Clearance hole and a nut,
or a Tap drill hole and a tap. Modelled threads suit big threads, like a jar lid.
Print one and drive the screw in by hand before you trust it.
```

### Optional: a gap you can change in one place (an expression in a sketch size)
```
In a sketch, when you set a circle's size, type = to open the expression editor, then:
  10mm + 2 * 0.2mm
FreeCAD works it out (10.4 mm). Units go on every number (FreeCAD wiki, Expressions).
```

### Check before you print
```
[ ] Every sketch pads: no "Wire is not closed" (Validate Sketch: no missing coincidences)
[ ] External geometry you don't want in the outline is construction (dashed)
[ ] Test card printed flat; your sliding-fit gap written down: ____ mm a side
[ ] Holes sized as peg + 2 x gap
[ ] Screw holes from the Hole tool: Clearance, Medium (M4 = 4.5 mm), or Tap drill (M4 = 3.3 mm)
[ ] Modelled threads only for big threads, Custom Clearance = 2 x your gap, depth as a number
[ ] Printed one, drove the screw in by hand, and it held, before trusting it
```
