# Full code: Official Blender MCP vs MCP for Blender vs Headless: Which to Use?



### 1. Official server: .claude/settings.json in your test folder (Part 2's four ask rules)
```
{
  "permissions": {
    "ask": [
      "mcp__blender__execute_blender_code",
      "mcp__blender__execute_blender_code_for_cli",
      "mcp__blender__render_viewport_to_path",
      "mcp__blender__render_thumbnail_to_path"
    ]
  }
}
```

### 2. Community server, locked to 2.2.8, usage report off, safe mode on (one route at a time)
```
# Switch the official add-on off first: both add-ons listen on port 9876.
# The add-on, from the same package version (never the piped install script):
uvx mcp-for-blender@2.2.8 install-addon
# Then in Blender: Edit, Preferences, Add-ons, enable "Interface: MCP for Blender".
# Its Auto-Start box is on in a new file: untick it in the sidebar if you start it by hand.
# The server, under its own name, from your test folder:
claude mcp add --env DISABLE_TELEMETRY=true --env BLENDER_MCP_SAFE_MODE=1 --transport stdio blender-community -- uvx mcp-for-blender@2.2.8
claude mcp list
# Look for: blender-community. Switch off: disable the add-on; for good: claude mcp remove blender-community
```

### 3a. Community server: .claude/settings.json ask rules (its own test folder)
```
{
  "permissions": {
    "ask": [
      "mcp__blender-community__execute_blender_code",
      "mcp__blender-community__generate_3d",
      "mcp__blender-community__generate_gaussian_world",
      "mcp__blender-community__import_asset"
    ]
  }
}
```

### 3b. Headless: .claude/settings.json ask rules (its own test folder)
```
{
  "permissions": {
    "defaultMode": "default",
    "ask": [
      "Bash(blender *)",
      "PowerShell(blender *)"
    ]
  }
}
```

### 4. Headless: the command (Blender on your PATH, so the command starts with blender)
```
# Options run in the order given: --python-exit-code must come before --python.
# Never add -y: it turns on scripts stored inside .blend files.
# A full path like /usr/bin/blender wouldn't match the ask rule (Claude Code docs).
blender --background --factory-startup --offline-mode --python-exit-code 1 --python phone_stand.py -- phone_stand.blend
```

### 5. Headless: phone_stand.py (bpy, math and sys only; look over it before you say yes)
```
# A simple desk phone stand in millimetres; saves to the path after "--".
import math
import sys
import bpy

MM = 0.001
bpy.ops.wm.read_factory_settings(use_empty=True)


def add_box(name, size_mm, centre_mm, tilt_deg=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=[c * MM for c in centre_mm])
    box = bpy.context.active_object
    box.name = name
    box.scale = [s * MM for s in size_mm]
    box.rotation_euler[0] = math.radians(tilt_deg)
    return box


add_box("Stand_Base", (80, 70, 10), (0, 0, 5))
tilt = 20.0
add_box("Stand_Back", (80, 8, 100),
        (0, 25 + 50 * math.sin(math.radians(tilt)), 10 + 50 * math.cos(math.radians(tilt))),
        -tilt)
add_box("Stand_Lip", (80, 8, 20), (0, -31, 20))

out = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "phone_stand.blend"
bpy.ops.wm.save_as_mainfile(filepath=bpy.path.abspath(out))
print("Saved", out)
```

### Safety checklist
```
[ ] One route at a time: never both add-ons on (both use port 9876)
[ ] Official: v1.0.3 from disk, Auto Start off, Allow Online Access only while working, block 1 saved
[ ] Community: 2.2.8 only, DISABLE_TELEMETRY=true, BLENDER_MCP_SAFE_MODE=1, its own name, block 3a saved
[ ] Community: service boxes unticked unless you need one; recheck the ask rules after an update
[ ] Headless: Manual mode, block 3b saved, Blender called as blender, never -y
[ ] A new Blender file with nothing private open; test models only, never a client's files
[ ] I look over every script before saying yes: no os, subprocess, socket or web calls
[ ] Done? Stop the server or disable the add-on; claude mcp remove <name> for good
```
