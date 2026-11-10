# Full code: Blender MCP Explained: What Claude Can Do in Blender 5.2

Written from the Blender 5.2 manual and Python API and the Blender Lab MCP server's docs and source (v1.0.3), checked 2026-11-10. Use a new, empty Blender file with made-up models. phone_stand.py was checked with `py_compile` only; nothing was installed or run, and Blender wasn't opened.

### phone_stand.py: a rough desk phone stand from three boxes (Blender 5.2)
```
# phone_stand.py: a rough first block-out of a small desk phone stand, made of three boxes.
# Look over every line before you run it. It only adds three shapes to the open file.
# Run it in a new Blender 5.2 file with the default cube deleted: Scripting tab, open this file, Run Script.
# Written from the Blender 5.2 Python API, checked 2026-11-10. Checked by syntax only; not run.
# Sizes are in metres, Blender's default unit: 0.08 is 80 mm.
import bpy
from math import radians


def box(name, size, location, tilt_deg=0.0):
    """Add a box of the given size (x, y, z in metres), centred at location, tilted around X."""
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    part = bpy.context.active_object
    part.name = name
    part.scale = size
    part.rotation_euler = (radians(tilt_deg), 0.0, 0.0)
    return part


# base 80 x 70 x 10 mm
box("Stand_Base", (0.08, 0.07, 0.01), (0, 0, 0.005))
# back 80 x 8 x 100 mm, tilted 20 degrees
box("Stand_Back", (0.08, 0.008, 0.10), (0, 0.02, 0.055), -20)
# lip 80 x 8 x 20 mm, at the front
box("Stand_Lip", (0.08, 0.008, 0.02), (0, -0.03, 0.02))
```

### Safety checklist, before you connect Claude to Blender
```
[ ] Official Blender Lab add-on and server only, from projects.blender.org/lab/blender_mcp
[ ] One version: 1.0.3, installed from disk (Part 2)
[ ] Blender 5.2 (the add-on needs 5.1 or newer)
[ ] A test .blend file, with nothing private open
[ ] Claude asks before any code runs: execute_blender_code and execute_blender_code_for_cli set to ask
[ ] Claude asks before it writes a render to a path: render_viewport_to_path and render_thumbnail_to_path set to ask
[ ] I look over every script before I say yes
[ ] It listens on this computer only (localhost, port 9876), with no password
[ ] Allow Online Access is on only while I need it; it covers every add-on, not this one alone
[ ] Done? Auto Start off, server stopped, Allow Online Access off if nothing else needs it
[ ] Bundled docs are Blender 5.1's: check docs.blender.org/manual/en/5.2 for anything new
[ ] Made-up models only, never a client's files
```

### Prompts to try after Part 2's setup (in a test file)
```
1. Before you change anything, list what's in this file: every item, its type, its collection and any missing files. Don't run any code that changes the file.
2. Take a screenshot of the 3D viewport and tell me in one line each what you see.
3. Block out a small desk phone stand in millimetres: a base 80 x 70 x 10, a back 80 x 8 x 100 tilted back 20 degrees, and a lip 80 x 8 x 20 at the front. Show me the Python first and wait for my yes.
4. Take another screenshot and check the back leans away from the lip. If it doesn't, show me the fix before you run it.
5. Rename every item in this file to a clear, consistent name. List the old and new names and wait for my yes before renaming.
```
