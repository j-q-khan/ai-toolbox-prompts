# Full code: Hunyuan 3D and Tripo AI Models in Blender: Clean Them Up with Claude

Written from the Blender 5.2 manual, the 3D Print Toolbox 1.5.0 source and the Blender Lab MCP v1.0.3 source, checked 2026-11-12. Use your blender-test folder, a file with nothing private open, and a model you generated yourself. Nothing here was installed or run, and Blender wasn't opened; the shell lines were checked with `bash -n` and the Python with `py_compile`.

### 1. Back on, a new file, the import (Blender 5.2, then a terminal)
```
# Blender: Edit, Preferences, System, Network: tick Allow Online Access (Part 5 unticked it).
# Add-ons, the arrow beside MCP: click Start MCP Bridge Server, and look for: Server is running
# File, New, General. Click the default cube, press Delete.
# Properties, Scene, Units: Length = Millimeters. File, Save As: blender-test/gen-stand-01.blend
# File, Import, glTF 2.0 (.glb/.gltf): your downloaded file.
# Terminal, Windows PowerShell:   Set-Location "$HOME\blender-test"
# Terminal, macOS or Linux:
cd "$HOME/blender-test"
claude
```

### 2. Example of prompt 2's code (not run; Claude's may differ)
```
# Click the model first. File, Save Incremental first.
import bpy

ob = bpy.context.view_layer.objects.active
assert ob is not None and ob.type == "MESH", "Click the model first"
for o in bpy.context.view_layer.objects:
    o.select_set(False)
ob.select_set(True)
if ob.parent is not None:
    bpy.ops.object.parent_clear(type="CLEAR_KEEP_TRANSFORM")
ob.name = "Gen_Stand"
k = 0.1 / max(ob.dimensions)  # longest side 100 mm, in metres
ob.scale = [s * k for s in ob.scale]
bpy.context.view_layer.update()
apply_scale = bpy.ops.object.transform_apply
apply_scale(location=False, rotation=False, scale=True)
bpy.context.view_layer.update()
size = [round(d * 1000, 1) for d in ob.dimensions]
result = {"scale": list(ob.scale), "size_mm": size}
```

### 3. Example of prompt 3's code (not run)
```
# File, Save Incremental first.
import bpy

ob = bpy.data.objects["Gen_Stand"]
for o in bpy.context.view_layer.objects:
    o.select_set(False)
ob.select_set(True)
bpy.context.view_layer.objects.active = ob
before = len(ob.data.vertices)
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
merge = bpy.ops.mesh.remove_doubles
merge(threshold=0.0001)  # 0.1 mm
bpy.ops.object.mode_set(mode="OBJECT")
after = len(ob.data.vertices)
dec = ob.modifiers.new(name="Decimate", type="DECIMATE")
dec.decimate_type = "COLLAPSE"
dec.ratio = 0.2
deps = bpy.context.evaluated_depsgraph_get()
faces = len(ob.evaluated_get(deps).data.polygons)
result = {"points": [before, after],
          "faces": [len(ob.data.polygons), faces]}
```

### 4. Example of prompt 4's code (not run)
```
# File, Save Incremental first.
import bpy

ob = bpy.data.objects["Gen_Stand"]
for o in bpy.context.view_layer.objects:
    o.select_set(False)
ob.select_set(True)
bpy.context.view_layer.objects.active = ob
apply_mod = bpy.ops.object.modifier_apply
apply_mod(modifier="Decimate")
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
outward = bpy.ops.mesh.normals_make_consistent
outward(inside=False)
bpy.ops.object.mode_set(mode="OBJECT")
result = {"faces": len(ob.data.polygons)}
```

### 5. Example of prompt 6's code, only if Shells is above 1 (not run)
```
# File, Save Incremental first. Delete tiny pieces yourself: click, Delete.
import bpy

ob = bpy.data.objects["Gen_Stand"]
for o in bpy.context.view_layer.objects:
    o.select_set(False)
ob.select_set(True)
bpy.context.view_layer.objects.active = ob
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.select_all(action="SELECT")
split = bpy.ops.mesh.separate
split(type="LOOSE")
bpy.ops.object.mode_set(mode="OBJECT")
pieces = [o for o in bpy.context.selected_objects if o.type == "MESH"]
pieces.sort(key=lambda o: len(o.data.polygons), reverse=True)
result = [[o.name, len(o.data.polygons),
           [round(d * 1000, 1) for d in o.dimensions]] for o in pieces]
```

### 6. The clean-up checklist
```
Download    the GLB from the generator's own site; check its terms
Hunyuan 3D  2.0/2.1 licence: not the EU, the UK or South Korea
Import      new file, Length = Millimeters, File, Import, glTF 2.0
Size        prompt 2: longest side 100 mm, scale applied (scale 1)
Merge       prompt 3: by distance, 0.1 mm; Decimate Collapse 0.2
Ratio       tune it by hand; stop where it still looks right
Apply       prompt 4: apply Decimate (checks skip modifiers)
Normals     prompt 4: outside; Face Orientation, no red outside
Check All   prompt 5; non-manifold: Part 5's Make Manifold
Shells 2+   prompt 6, then delete tiny pieces by hand
Thin faces  make it bigger, or generate a chunkier model
Export      STL, Selection Only, Scale 1000, Apply Modifiers
```

### 7. Switch it off when you're done
```
# Add-ons, MCP: Stop MCP Server. Untick Allow Online Access if nothing else needs it.
```
