# Full code: OpenSCAD BOSL2 and Customizer: Parametric Parts with AI

Written from the BOSL2 wiki and README (v2.0.782) and the OpenSCAD manual and source (2021.01 and the 2026.11 release candidate), checked 2026-11-07. Checked by syntax only (brackets balanced, the JSON parsed): not rendered, printed or tested. Needs BOSL2 in OpenSCAD's library folder, in a folder named exactly BOSL2.

### Test that BOSL2 is installed (a new file in OpenSCAD; press F5 and a box with rounded edges appears)
```
include <BOSL2/std.scad>
cuboid([30,40,50], rounding=10);
```

### hook.scad (the hook with sliders: open it in OpenSCAD, then Window, Customizer)
```
// Headphone wall hook with sliders: open it in OpenSCAD, then Window, Customizer.
// All sizes in millimetres. Needs the BOSL2 library in OpenSCAD's library folder
// (File, Show Library Folder; the folder must be named exactly BOSL2).
// Print it lying on its side (a side face down, so the L shape lies flat), so the arm and the
// back plate are built in the same layers and the weight doesn't pull them apart.
// Fits two countersunk wood screws, 4 mm by default.
// Written from the OpenSCAD manual and the BOSL2 wiki, checked 2026-11-07.
// Checked by syntax only; not rendered or printed. Test the size you print before you
// trust it with anything heavier than headphones.

include <BOSL2/std.scad>

/* [Hook size] */
// Width, side to side
width = 30;          // [20:1:60]
// Back plate height, up the wall
plate_height = 70;   // [55:5:120]
// Back plate thickness
plate_thick = 5;     // [3:0.5:8]
// How far the arm sticks out from the wall
arm_length = 45;     // [30:1:80]
// Arm thickness
arm_thick = 6;       // [4:0.5:10]
// Lip height above the arm, stops the headband sliding off
lip_height = 10;     // [0:1:20]
// Lip thickness
lip_thick = 4;       // [3:0.5:8]
// Radius of the back plate's rounded top corners
corner_r = 5;        // [1:1:10]

/* [Screws] */
// Screw shank diameter
screw_d = 4;         // [3:0.5:5]
// Extra room so the screw slides through
clearance = 0.5;     // [0:0.1:1]
// Countersink width at the front face
head_d = 8.5;        // [7:0.5:12]

/* [Hidden] */
hole_d     = screw_d + clearance;      // 4.5 mm hole by default
sink_depth = (head_d - hole_d) / 2;    // for a 90 degree countersink
hole_z     = [25, plate_height - 15];  // hole centres, up from the bottom
$fn = 64;                              // round circles

assert(sink_depth < plate_thick,
       "The countersink is deeper than the back plate: make plate_thick bigger or head_d smaller.");

difference() {
    union() {
        // back plate, top corners rounded: the wall is the plane y = 0
        cuboid([width, plate_thick, plate_height], rounding = corner_r,
               edges = [TOP+LEFT, TOP+RIGHT], anchor = FRONT+LEFT+BOT);
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

### hook.json (two presets: save it next to hook.scad, then pick one in the Customizer's preset box)
```
{
    "parameterSets": {
        "Big headset": {
            "width": "40",
            "plate_height": "80",
            "plate_thick": "6",
            "arm_length": "60",
            "arm_thick": "8",
            "lip_height": "14",
            "lip_thick": "5",
            "corner_r": "6",
            "screw_d": "4",
            "clearance": "0.5",
            "head_d": "8.5"
        },
        "Cable hook": {
            "width": "20",
            "plate_height": "55",
            "plate_thick": "4",
            "arm_length": "30",
            "arm_thick": "5",
            "lip_height": "6",
            "lip_thick": "3",
            "corner_r": "4",
            "screw_d": "3.5",
            "clearance": "0.5",
            "head_d": "7.5"
        }
    },
    "fileFormatVersion": "1"
}
```

### Lines to add to CLAUDE.md (the rules file from Part 1; keep its other rules)
```
## Customizer and BOSL2 (added in Part 4)

- BOSL2 is installed in OpenSCAD's library folder. Load it with this one line at the top of the file, and add no other include, use, import or surface line: include <BOSL2/std.scad>
- Always include BOSL2, never use it, so its names like TOP and LEFT work.
- Check every BOSL2 module and argument against the BOSL2 wiki (github.com/BelfrySCAD/BOSL2/wiki) and tell me which page each one comes from. Never write BOSL version 1 code.
- Put every size I may change at the top of the file, above the first {, in Customizer format: a // description on the line above, starting at the left edge, and a // [min:step:max] range after the value. Group them with /* [Group name] */ comments.
- Values worked out from other sizes, and $fn, go under /* [Hidden] */.
- Add an assert() with a plain message for any combination of sizes that would make a broken part.
```

### Make an STL for each preset (optional: a terminal in the hook folder, with openscad on your PATH)
```
# Each line renders one preset from hook.json into its own STL. Names with spaces stay in quotes.
openscad -o hook-big-headset.stl -p hook.json -P "Big headset" hook.scad
openscad -o hook-cable.stl -p hook.json -P "Cable hook" hook.scad
# If a line prints WARNING or ERROR, treat it as failed, even if it says it finished.
```

### Check before you print
```
[ ] BOSL2 is in OpenSCAD's library folder, named exactly BOSL2, with its files straight inside
[ ] The include line says include, not use, and it's the only include line
[ ] Every size is above the first { with a label on the line above it
[ ] Every BOSL2 command matches its page on the BOSL2 wiki (no BOSL v1 code)
[ ] cuboid has anchor=FRONT+LEFT+BOT, so the plate starts at the origin like cube()
[ ] Tried each slider at its smallest and biggest value: no warning, no gaps
[ ] Saved the file, so hook.json holds your presets
[ ] The slicer shows the size you picked, in millimetres
[ ] Printed and tested the size you'll use before trusting it with any weight
```
