# Full code: Blender MCP for 3D Printing: From a Prompt to a Printable STL

Written from the Blender 5.2 manual and Python API, Blender's STL exporter source (v5.2.3) and the Blender Lab MCP source (v1.0.3), checked 2026-11-10. Use your blender-test folder, a file with nothing private open, and made-up models only. Nothing here was installed or run, and Blender wasn't opened; the shell lines were checked with `bash -n` and the Python with `py_compile`.

### 1. Back where we left off (Blender 5.2, then a terminal)
```
# Blender: Edit, Preferences, System, Network: tick Allow Online Access (Part 3 unticked it).
# Add-ons, the arrow beside MCP: click Start MCP Bridge Server, and look for: Server is running
# File, Open Recent: your latest phone-stand-0N.blend
# Terminal, Windows PowerShell:   Set-Location "$HOME\blender-test"
# Terminal, macOS or Linux:
cd "$HOME/blender-test"
claude
```

### 2. Millimetres, scale and walls (by hand, then prompt 1)
```
[ ] Properties editor, Scene tab, Units: Unit System Metric, Length Millimeters
[ ] Unit Scale stays 1.000000 (it only changes the numbers shown; 0.001 would show 80 mm as 0.08 mm)
[ ] Send prompt 1: every piece's scale and size in mm, and is the back sunk into the base?
[ ] Any scale not 1? Hover over the viewport, press A, then Ctrl+A, Scale (Object, Apply, Scale)
[ ] Walls = each slab's smallest size: back 8 mm, lip 8 mm, base 10 mm
[ ] Solidify only gives thickness to a surface with none: not for solid slabs
```

### 3. Example of the union code to expect from prompt 2 (not run; Claude's may differ)
```
# Look for: two Boolean modifiers, Union, Exact, the two pieces hidden. Nothing about files.
import bpy

base = bpy.data.objects["Stand_Base"]
for piece_name, mod_name in (("Stand_Back", "Union_Back"), ("Stand_Lip", "Union_Lip")):
    piece = bpy.data.objects[piece_name]
    mod = base.modifiers.new(name=mod_name, type='BOOLEAN')
    mod.operation = 'UNION'
    mod.operand_type = 'OBJECT'
    mod.object = piece
    mod.solver = 'EXACT'
    piece.hide_set(True)
```

### 4. The export settings, by hand (File, Export, STL (.stl))
```
Before:           File, Save Incremental; click the stand (selects Stand_Base, the only piece showing)
Selection Only    ticked     only the joined base, not the hidden back and lip again
Scale             1000       Blender stores 80 mm as 0.08; an STL file has no unit
Scene Unit        unticked   it multiplies by Unit Scale, which is 1 here
Apply Modifiers   ticked     the default: the union goes into the file
Format, Batch     unticked   leave Forward Y and Up Z as they are
Save as           blender-test/phone-stand.stl
```

### 5. Check the size, then switch off
```
[ ] Open phone-stand.stl in your slicer: about 80 x 76 x 103 mm with Part 1's numbers (yours: within a few mm)
[ ] Tiny (0.08 mm)? Export again with Scale 1000; don't resize it in the slicer
[ ] File, Save Incremental
[ ] Add-ons, MCP: Stop MCP Server; untick Allow Online Access if nothing else needs it
```
