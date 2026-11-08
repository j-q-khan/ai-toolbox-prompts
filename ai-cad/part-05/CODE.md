# Full code: FreeCAD 1.1 Tutorial for Beginners: Your First Part for 3D Printing

Written from the FreeCAD 1.1.4 source and the FreeCAD wiki, checked 2026-11-07. Not run by us: the steps were checked against FreeCAD 1.1.4's labels and the macro by syntax only (`py_compile`). The hook is not printed or tested.

### hook-steps.txt (every size, step by step, in FreeCAD 1.1.4)
```
Headphone wall hook in FreeCAD 1.1.4. All sizes in millimetres.

1  Start page > New File > Parametric Body  (opens Part Design, with one Body)
2  New Sketch > YZ-plane > OK
   Polyline from the origin, around the side outline:
   (0,0) > (45,0) > (45,16) > (41,16) > (41,6) > (5,6) > (5,70) > (0,70) > back to (0,0)
   Dimension (D): bottom 45, end of the lip 16, lip top 4, inside of the lip 10,
   plate top 5, back 70  ->  "Fully constrained", lines green  ->  Leave Sketch
3  Pick the sketch > Pad: Mode Symmetric, Type Dimension, Length 30 > OK
4  Click empty space > New Sketch > XZ-plane > OK
   Circle From Center: two circles, centres on the green vertical axis
   Dimension (D): each circle 4.5 (diameter sign, not R: press M to switch)
   Each centre to the red horizontal axis: 25 and 55  ->  green  ->  Leave Sketch
5  Pick that sketch > Pocket: Mode Symmetric, Type Through all > OK
6  Click one short top-corner edge of the plate (through its 5 mm thickness),
   Ctrl+click the other > Fillet: Use all edges unticked, Radius 5 > OK
7  Ctrl+S (Cmd+S on a Mac) to save hook.FCStd
8  Optional (small holes are already round at the default 0.1 mm):
   Workbench list > Mesh (once) > Edit > Preferences > Import-Export > Mesh Formats >
   Maximum mesh deviation 0.01 mm > OK
9  Click Body in the Model tree > File > Export > STL Mesh (*.stl *.ast) > hook.stl > Save
10 In the slicer: 30 x 45 x 70 mm. Print one and test it before trusting it.
```

### Countersinks (optional: the same as Part 1's hook, done after step 5)
```
Countersinks for 4 mm countersunk wood screws, 8.5 mm across at the front face.

1  Turn the view to the front of the plate (the side the arm sticks out from).
2  Click the round edge of the top hole on that face, Ctrl+click the bottom one.
3  Part Design > Chamfer: Type Equal distance, Size 2 mm > OK
   (4.5 mm hole + 2 mm each side = 8.5 mm across, a 90 degree countersink)
4  Check the chamfer is on the front face, not the wall side.
```

### hook_check.py (a FreeCAD macro that builds the same hook, so you can compare it with yours)
```
# hook_check.py: builds the series' headphone wall hook in FreeCAD 1.1, in a new file,
# so you can compare it with the one you built by hand. All sizes in millimetres.
# To run it: Macro > Macros... > Create, name it hook_check, paste this in, save,
# then Macro > Execute macro, and press V then F to fit the view.
# It only builds shapes in a new document.
# A macro is Python and can do anything a program can on your computer, so read every
# line of any macro before you run it. This one imports only FreeCAD, Part and Sketcher, and
# opens, saves and downloads nothing.
# It also adds the optional countersinks (a Chamfer step), so its Model tree has one
# more step than a hand build without them.
# Written from the FreeCAD 1.1.4 source and wiki, checked 2026-11-07.
# Checked by syntax only; not run by us. Test any print before you trust it.

import FreeCAD as App
import Part
import Sketcher

width = 30          # side to side: the Pad's length, symmetric about the middle
plate_height = 70   # back plate, up the wall
plate_thick = 5     # back plate thickness
arm_length = 45     # how far the arm sticks out from the wall
arm_thick = 6       # arm thickness
lip_height = 10     # lip height above the arm
lip_thick = 4       # lip thickness
hole_d = 4.5        # screw hole diameter: 4 mm screw + 0.5 mm clearance
hole_z = [25, 55]   # hole centres, up from the bottom
corner_r = 5        # rounded top corners
sink = 2            # countersink chamfer: 4.5 + 2 x 2 = 8.5 mm across the face

V = App.Vector
EPS = 1e-4


def near(a, b):
    return abs(a - b) < EPS


def edges(shape, test):
    # edge names like "Edge7", found by their geometry, not by a fixed number
    return ["Edge%d" % (i + 1) for i, e in enumerate(shape.Edges) if test(e)]


doc = App.newDocument("HookCheck")
body = doc.addObject("PartDesign::Body", "Body")
planes = {f.Role: f for f in body.Origin.OriginFeatures}

# 1. The side outline on the YZ plane: sketch x is out from the wall, sketch y is up
side = body.newObject("Sketcher::SketchObject", "SideSketch")
side.AttachmentSupport = [(planes["YZ_Plane"], "")]
side.MapMode = "FlatFace"
end_h = arm_thick + lip_height
pts = [(0, 0), (arm_length, 0), (arm_length, end_h), (arm_length - lip_thick, end_h),
       (arm_length - lip_thick, arm_thick), (plate_thick, arm_thick),
       (plate_thick, plate_height), (0, plate_height)]
for i in range(8):
    a, b = pts[i], pts[(i + 1) % 8]
    side.addGeometry(Part.LineSegment(V(a[0], a[1], 0), V(b[0], b[1], 0)))
for i in range(8):
    side.addConstraint(Sketcher.Constraint("Coincident", i, 2, (i + 1) % 8, 1))
    side.addConstraint(Sketcher.Constraint("Horizontal" if i % 2 == 0 else "Vertical", i))
side.addConstraint(Sketcher.Constraint("Coincident", 0, 1, -1, 1))  # start on the origin
for line, length in [(0, arm_length), (1, end_h), (2, lip_thick), (3, lip_height),
                     (6, plate_thick), (7, plate_height)]:
    side.addConstraint(Sketcher.Constraint("Distance", line, length))

# 2. Pad it, symmetric, so the middle of the hook sits on the vertical axis
pad = body.newObject("PartDesign::Pad", "Pad")
pad.Profile = side
pad.SideType = "Symmetric"
pad.Length = width

# 3. Two holes on the XZ plane (the wall side), centres on the vertical axis
holes = body.newObject("Sketcher::SketchObject", "HoleSketch")
holes.AttachmentSupport = [(planes["XZ_Plane"], "")]
holes.MapMode = "FlatFace"
for i, z in enumerate(hole_z):
    holes.addGeometry(Part.Circle(V(0, z, 0), V(0, 0, 1), hole_d / 2))
    holes.addConstraint(Sketcher.Constraint("Diameter", i, hole_d))
    holes.addConstraint(Sketcher.Constraint("PointOnObject", i, 3, -2))   # centre on the vertical axis
    holes.addConstraint(Sketcher.Constraint("DistanceY", -1, 1, i, 3, z))  # height above the origin
pocket = body.newObject("PartDesign::Pocket", "Pocket")
pocket.Profile = holes
pocket.Type = "ThroughAll"
pocket.SideType = "Symmetric"
doc.recompute()

# 4. Countersinks: a 2 mm chamfer on each hole's edge at the front face (y = plate_thick)
sink_edges = edges(pocket.Shape, lambda e: hasattr(e.Curve, "Radius")
                   and near(e.Curve.Radius, hole_d / 2) and near(e.Curve.Center.y, plate_thick))
chamfer = body.newObject("PartDesign::Chamfer", "Chamfer")
chamfer.Base = (pocket, sink_edges)
chamfer.Size = sink
doc.recompute()


# 5. Round the plate's two top corners: the short edges through its thickness
def top_corner(e):
    a, b = e.Vertexes[0].Point, e.Vertexes[-1].Point
    return (len(e.Vertexes) == 2 and near(a.z, plate_height) and near(b.z, plate_height)
            and near(a.x, b.x) and near(abs(a.x), width / 2))


fillet = body.newObject("PartDesign::Fillet", "Fillet")
fillet.Base = (chamfer, edges(chamfer.Shape, top_corner))
fillet.Radius = corner_r
side.Visibility = False
holes.Visibility = False
doc.recompute()

print("Hook built: %d countersink edges, %d corner edges. Compare it with yours."
      % (len(sink_edges), len(fillet.Base[1])))
```

### Check before you print
```
[ ] FreeCAD 1.1.4 from freecad.org (Help > About FreeCAD shows the version)
[ ] Unit System: Standard (mm, kg, s, degree)
[ ] Both sketches say "Fully constrained" (double-click each to check, then Leave Sketch)
[ ] Pad: Mode Symmetric, Length 30 (or your width)
[ ] Holes: diameter 4.5 (not R 4.5), centres at 25 and 55, on the middle line
[ ] Pocket: Type Through all; both holes go right through the plate
[ ] Rounded top corners, radius 5; no red marks in the Model tree
[ ] Saved as hook.FCStd, so you can change it later
[ ] Maximum mesh deviation 0.01 mm (optional: the default 0.1 already keeps small holes round); the Body selected for File > Export
[ ] Slicer shows 30 x 45 x 70 mm (or your sizes)
[ ] Printed one, screwed it to the wall, and gave it a day before trusting it
```
