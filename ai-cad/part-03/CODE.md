# Full code: OpenSCAD MCP Server: Let Claude Render and Check Your Model

Written from the openscad-mcp README and source (v0.6.1), Claude Code's MCP and permissions docs and the OpenSCAD manual, checked 2026-11-07. Use an empty test folder with made-up parts. The JSON was parsed, the shell lines checked with `bash -n` and PowerShell's parser, and the .scad file checked for balanced brackets only; nothing was installed, rendered or run.

### Add the server, macOS or Linux (in a new terminal)
```
mkdir -p "$HOME/cad-test" && cd "$HOME/cad-test"
claude mcp add --env MCP_ALLOWED_PATHS="$HOME/cad-test" --transport stdio openscad -- uvx openscad-mcp@0.6.1
```

### Add the server, Windows PowerShell
```
New-Item -ItemType Directory -Force "$HOME\cad-test" | Out-Null
Set-Location "$HOME\cad-test"
claude mcp add --env "MCP_ALLOWED_PATHS=$HOME\cad-test" --transport stdio openscad -- uvx openscad-mcp@0.6.1
```

### Then check it (in the same folder)
```
claude mcp list
# then look for: openscad  ✔ Connected, and start Claude Code with:
claude
```

### Failed? Tell the server where OpenSCAD is installed (remove it, then add it again with the path)
```
claude mcp remove openscad --scope local
claude mcp add --env MCP_ALLOWED_PATHS="$HOME/cad-test" OPENSCAD_PATH=/path/to/openscad --transport stdio openscad -- uvx openscad-mcp@0.6.1
# On Windows the path is usually C:\Program Files\OpenSCAD\openscad.exe; put each --env value in double quotes
```

### Or, instead of the command: .mcp.json in the test folder (Claude Code asks you to approve it the first time; change the path to your folder's full path, and on Windows write it like "C:\\Users\\you\\cad-test")
```
{
  "mcpServers": {
    "openscad": {
      "type": "stdio",
      "command": "uvx",
      "args": ["openscad-mcp@0.6.1"],
      "env": {
        "MCP_ALLOWED_PATHS": "/home/you/cad-test"
      }
    }
  }
}
```

### .claude/settings.json in the test folder (the second lock: Claude Code asks before every file change or export)
```
{
  "permissions": {
    "ask": [
      "mcp__openscad__model",
      "mcp__openscad__export_model"
    ]
  }
}
```

### hook.scad (Part 1's headphone hook, to test the loop with)
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

### No server: Claude Code runs OpenSCAD itself (in the test folder)
```
openscad -o hook.png --imgsize=800,600 --autocenter --viewall hook.scad
openscad -o hook.stl hook.scad
# If either prints a WARNING or ERROR line, treat it as failed, even if the command said it finished
```

### Remove the server when you're done
```
claude mcp remove openscad --scope local
```

### Safety checklist
```
[ ] Installed only from the official package: pypi.org/project/openscad-mcp links to github.com/robertcoop/openscad-mcp
[ ] Version pinned: openscad-mcp@0.6.1
[ ] Added from an empty test folder, local scope (no --scope user)
[ ] MCP_ALLOWED_PATHS set to that test folder
[ ] .claude/settings.json asks before model (create, change, delete) and export_model
[ ] I look at every model's code before it renders: no include, import or surface outside the folder
[ ] Measured and watertight before I trust the picture or export
[ ] Windows: no memory cap in this server, so stop a render that hangs (timeout 300 s)
[ ] Plugin install skipped: it isn't pinned and has no folder lock
[ ] Made-up parts only, never a client's files
[ ] Done? claude mcp remove openscad --scope local
```
