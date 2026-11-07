# Full code: OpenSCAD with Claude Code: Design 3D Prints by Describing Them



### CLAUDE.md (save it in your empty parts folder before you start claude, named exactly CLAUDE.md; in Notepad, set Save as type to All files so it doesn't become CLAUDE.md.txt)
```
# OpenSCAD parts in this folder

- Write OpenSCAD code. Save each part as its own .scad file in this folder.
- All sizes are in millimetres. Say so in a comment at the top of the file.
- Put every size at the top of the file as a named variable, with a comment saying what it measures. No unexplained numbers further down.
- Use d= (diameter) for every cylinder and hole, never r=.
- Give every screw hole and every fit its own clearance variable, and say how much extra room it adds.
- Set $fn = 64 at the top of the file so circles come out round.
- When difference() cuts one shape out of another, make the cutting shape stick out 1 mm past both faces, so no face is left exactly touching.
- Add a comment at the top saying which way up to print the part, and why.
- When you finish, show a table of every size you used next to the size I asked for, and list anything you guessed.
- Don't install anything, download libraries or run commands. I preview, render and export in OpenSCAD myself.
- Only create or change files in this folder.
```

### The description to paste into Claude Code
```
Make hook.scad: a wall hook for headphones. It screws to the wall with two 4 mm countersunk wood screws, so give the holes 0.5 mm clearance (4.5 mm holes) and a countersink 8.5 mm across at the front face. Back plate: 30 mm wide, 70 mm tall, 5 mm thick, flat against the wall. Hole centres 25 mm and 55 mm up from the bottom, in the middle of the width. Arm: sticks out 45 mm from the wall along the bottom, 6 mm thick, the full width. Lip: at the end of the arm, 4 mm thick, rising 10 mm above the arm, so the headband can't slide off. I'll print it lying on its side.
```

### hook.scad (what a correct answer looks like; compare Claude's file with it)
```
// Headphone wall hook. All sizes in millimetres.
// Print it lying on its side (a side face down, so the L shape lies flat), so the arm and the
// back plate are built in the same layers and the weight doesn't pull them apart.
// Fits two 4 mm countersunk wood screws.
// Written from the OpenSCAD manual, tutorial and cheat sheet, checked 2026-11-07.
// Checked by syntax only; not rendered or printed. Test the hook before you
// trust it with anything heavier than headphones.

width        = 30;    // side to side
plate_height = 70;    // back plate, up the wall
plate_thick  = 5;     // back plate thickness
arm_length   = 45;    // how far the arm sticks out from the wall
arm_thick    = 6;     // arm thickness
lip_height   = 10;    // lip height above the arm, stops the headband sliding off
lip_thick    = 4;     // lip thickness

screw_d      = 4;     // screw shank diameter
clearance    = 0.5;   // extra room so the screw slides through
hole_d       = screw_d + clearance;   // 4.5 mm hole
head_d       = 8.5;   // countersink width at the front face
sink_depth   = (head_d - hole_d) / 2; // 2 mm, for a 90 degree countersink
hole_z       = [25, 55];              // hole centres, up from the bottom

$fn = 64;             // round circles

difference() {
    union() {
        // back plate: the wall is the plane y = 0
        cube([width, plate_thick, plate_height]);
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

### Asking for fixes (one sentence each)
```
The mistake looks like this (r = radius, so this hole is 9 mm wide):
    cylinder(h = 7, r = 4.5);

Holes wrong size:   Check every cylinder uses d= and not r=, then tell me each hole's diameter in mm.
Flat-sided holes:   Set $fn = 64 at the top of the file.
Flickering faces:   Make every cutting shape stick out 1 mm past both faces.
Wrong way round:    In the preview, [what you see, with numbers]. It should [what you want]. Fix only that, and tell me which lines you changed.
An error:           OpenSCAD shows this message: [paste the line exactly]. Explain it in one sentence, then fix it.
```

### Check before you print
```
[ ] CLAUDE.md saved in the folder (not CLAUDE.md.txt) before starting claude
[ ] Design, Automatic Reload and Preview ticked; hook.scad opened with File, Open
[ ] Every size at the top of the file matches what you asked for
[ ] Every cylinder uses d= (diameter), not r= (radius)
[ ] Holes have clearance: 4 mm screw, 4.5 mm hole
[ ] The arm and the countersinks are on the front face
[ ] F6 render finished with no error or warning in the Console pane
[ ] Exported as STL; the .scad file kept next to it
[ ] Printed one, screwed it up, and gave it a day before trusting it
```
