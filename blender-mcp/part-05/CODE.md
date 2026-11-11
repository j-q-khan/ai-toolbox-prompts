# Full code: Blender 3D Print Toolbox with Claude: Fix Non-Manifold Edges and Thin Walls

Written from the 3D Print Toolbox 1.5.0 source, the Blender 5.2 manual and the Blender Lab MCP v1.0.3 source, checked 2026-11-11. Use your blender-test folder, a file with nothing private open, and made-up models only. Nothing here was installed or run, and Blender wasn't opened; the shell lines were checked with `bash -n` and the Python with `py_compile`.

### 1. Back on, and the 3D Print Toolbox (Blender 5.2, then a terminal)
```
# Blender: Edit, Preferences, System, Network: tick Allow Online Access (Part 4 unticked it).
# Add-ons, the arrow beside MCP: click Start MCP Bridge Server, and look for: Server is running
# Get Extensions: search "3D print", click Install beside 3D Print Toolbox (1.5.0 when checked).
# One version only? Download it from extensions.blender.org, then Install from Disk.
# File, Open Recent: your latest phone-stand-0N.blend. Viewport: N, tab "3D Print".
# Terminal, Windows PowerShell:   Set-Location "$HOME\blender-test"
# Terminal, macOS or Linux:
cd "$HOME/blender-test"
claude
```

### 2. Example of prompt 1's code (not run; Claude's may differ)
```
# File, Save Incremental first. By hand instead: Modifiers tab, each one's arrow, Apply (top first).
import bpy

base = bpy.data.objects["Stand_Base"]
for ob in bpy.context.view_layer.objects:
    ob.select_set(False)
base.select_set(True)
bpy.context.view_layer.objects.active = base
apply = bpy.ops.object.modifier_apply
for name in ("Union_Back", "Union_Lip"):
    apply(modifier=name)
result = {"modifiers": [m.name for m in base.modifiers]}
```

### 3. Example of prompt 2's code (not run)
```
import bpy

base = bpy.data.objects["Stand_Base"]
for ob in bpy.context.view_layer.objects:
    ob.select_set(False)
base.select_set(True)
bpy.context.view_layer.objects.active = base
mesh_ops = bpy.ops.mesh
toolbox = bpy.context.scene.print3d_toolbox
mesh_ops.print3d_check_all()
report = toolbox.get_report()
result = {"report": [[i.name, i.value] for i in report]}
```

### 4. Example of prompt 3's code, in a new file (not run)
```
import bpy

mesh_ops = bpy.ops.mesh
toolbox = bpy.context.scene.print3d_toolbox
s = 0.01  # half of 20 mm, in metres
verts = [(x, y, z) for z in (-s, s) for y in (-s, s) for x in (-s, s)]
# five faces: the top is left off
faces = [(0, 2, 3, 1), (0, 1, 5, 4), (1, 3, 7, 5), (3, 2, 6, 7), (2, 0, 4, 6)]
me = bpy.data.meshes.new("Test_Hole")
me.from_pydata(verts, [], faces)
cube = bpy.data.objects.new("Test_Hole", me)
bpy.context.scene.collection.objects.link(cube)
for ob in bpy.context.view_layer.objects:
    ob.select_set(False)
cube.select_set(True)
bpy.context.view_layer.objects.active = cube

def solid():
    mesh_ops.print3d_check_solid()
    report = toolbox.get_report()
    return [[i.name, i.value] for i in report]

before = solid()
mesh_ops.print3d_clean_non_manifold()
result = {"before": before, "after": solid()}
```

### 5. Example of prompt 4's code, only if the stand has non-manifold edges (not run)
```
# File, Save Incremental first.
import bpy

base = bpy.data.objects["Stand_Base"]
for ob in bpy.context.view_layer.objects:
    ob.select_set(False)
base.select_set(True)
bpy.context.view_layer.objects.active = base
mesh_ops = bpy.ops.mesh
toolbox = bpy.context.scene.print3d_toolbox
mesh_ops.print3d_clean_non_manifold()
mesh_ops.print3d_check_all()
report = toolbox.get_report()
result = {"report": [[i.name, i.value] for i in report]}
```

### 6. What each line means (want: 0, and Shells 1)
```
Non-manifold Edges    edges with 1 face (a hole) or 3+ (faces inside)
Bad Contiguous Edges  two neighbouring faces pointing opposite ways
Intersect Faces       faces cutting through faces of the same piece
Shells                unconnected chunks: one closed solid = 1
Thin Faces            thinner than Minimum Thickness (default 1 mm)
Overhang Faces        facing down past 45 degrees; a flat underside on the bed is fine
Make Manifold         Clean Up panel; changes the mesh: save first
```

### 7. Switch it off when you're done
```
# Add-ons, MCP: Stop MCP Server. Untick Allow Online Access if nothing else needs it.
```
