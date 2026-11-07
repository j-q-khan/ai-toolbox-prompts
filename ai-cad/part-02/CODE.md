# Full code: OpenSCAD Tutorial for Beginners: Code Your First 3D Print

Part 1's headphone hook, built by hand in this video, with the same names and sizes, plus rounded top corners on the back plate. Uses only commands that are in both OpenSCAD 2021.01 and the 2026.11 release candidate. Checked for syntax only: not rendered, printed or tested.

### hook.scad
```
// Headphone wall hook. All sizes in millimetres.
// Print it lying on its side (a side face down, so the L shape lies flat), so the arm and the
// back plate are built in the same layers and the weight doesn't pull them apart.
// Fits two 4 mm countersunk wood screws.
// Written from the OpenSCAD manual, tutorial and cheat sheet, checked 2026-11-07.
// Checked by syntax only; not rendered or printed. Test the hook before you
// trust it with anything heavier than headphones.
// Part 2 adds corner_r and the hull() that rounds the back plate's top corners.
// Paste into a new OpenSCAD file. F5 = preview, F6 = render, then File, Export, Export as STL.
// In your slicer the size should be 30 x 45 x 70 mm. Too bendy? Make arm_thick bigger.

width        = 30;    // side to side
plate_height = 70;    // back plate, up the wall
plate_thick  = 5;     // back plate thickness
arm_length   = 45;    // how far the arm sticks out from the wall
arm_thick    = 6;     // arm thickness
lip_height   = 10;    // lip height above the arm, stops the headband sliding off
lip_thick    = 4;     // lip thickness
corner_r     = 5;     // radius of the back plate's rounded top corners

screw_d      = 4;     // screw shank diameter
clearance    = 0.5;   // extra room so the screw slides through
hole_d       = screw_d + clearance;   // 4.5 mm hole
head_d       = 8.5;   // countersink width at the front face
sink_depth   = (head_d - hole_d) / 2; // 2 mm, for a 90 degree countersink
hole_z       = [25, 55];              // hole centres, up from the bottom

$fn = 64;             // round circles

difference() {
    union() {
        // back plate, top corners rounded: the wall is the plane y = 0
        hull() {
            cube([width, plate_thick, 1]);
            translate([corner_r, 0, plate_height - corner_r])
                rotate([-90, 0, 0])
                    cylinder(h = plate_thick, d = 2 * corner_r);
            translate([width - corner_r, 0, plate_height - corner_r])
                rotate([-90, 0, 0])
                    cylinder(h = plate_thick, d = 2 * corner_r);
        }
        // arm, from the wall outwards along the bottom
        cube([width, arm_length, arm_thick]);
        // lip at the end of the arm
        translate([0, arm_length - lip_thick, 0])
            cube([width, lip_thick, arm_thick + lip_height]);
    }
    for (z = hole_z) {
        // screw hole, sticking out 1 mm past both faces
        translate([width / 2, -1, z])
            rotate([-90, 0, 0])
                cylinder(h = plate_thick + 2, d = hole_d);
        // countersink, wide end at the front face, carried 1 mm past it
        translate([width / 2, plate_thick - sink_depth, z])
            rotate([-90, 0, 0])
                cylinder(h = sink_depth + 1, d1 = hole_d, d2 = head_d + 2);
    }
}
```

### Step by step, as built in the video
```
// Build it up one step at a time, pressing F5 after each. The size lines stay at the top.

// Step 1: the back plate
cube([30, 5, 70]);

// Step 2: replace step 1 with the same plate, using named sizes
width        = 30;
plate_height = 70;
plate_thick  = 5;
cube([width, plate_thick, plate_height]);

// Step 3: add these under step 2: the arm (same corner, so no translate)
// and the lip (moved with translate)
arm_length = 45;
arm_thick  = 6;
lip_height = 10;
lip_thick  = 4;
cube([width, arm_length, arm_thick]);
translate([0, arm_length - lip_thick, 0])
    cube([width, lip_thick, arm_thick + lip_height]);

// Step 4: keep all the size lines, and replace the three shape lines
// (the plate cube, the arm cube and the lip) with this: union joins them,
// difference cuts one hole. hook.scad above has both holes, the
// countersinks and the rounded corners.
difference() {
    union() {
        cube([width, plate_thick, plate_height]);
        cube([width, arm_length, arm_thick]);
        translate([0, arm_length - lip_thick, 0])
            cube([width, lip_thick, arm_thick + lip_height]);
    }
    translate([width / 2, -1, 25])
        rotate([-90, 0, 0])
            cylinder(h = plate_thick + 2, d = 4.5);
}
```

### Checklist: fixing AI-written OpenSCAD
```
[ ] Every size is a named variable at the top, with a comment
[ ] The message panel shows no errors or warnings after F5
[ ] Each difference() keeps the right first shape (a union() if it's several)
[ ] Every hole uses d= (diameter), not r= (radius)
[ ] Every cutter pokes out past both faces (put # in front and press F5)
[ ] Shapes with center = true are where you expect them
[ ] Rounding with hull(), or minkowski() with the size growth allowed for
[ ] $fn is set, so holes are round (64 is plenty for small parts)
[ ] F6 finishes, then File, Export, Export as STL
[ ] The slicer shows the size you expected, in millimetres
[ ] Anything that carries weight is printed and tested before you trust it
```
