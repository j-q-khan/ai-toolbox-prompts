# Full code: Meshy AI for 3D Printing: From Image to an STL That Actually Prints



### preprint-checklist.txt
```
PRE-PRINT CHECKLIST for a Meshy model (Meshy docs and help centre, checked 2026-11-07)
Tick every line before you spend filament. Plans and credit costs change:
check meshy.ai/pricing before you rely on a number.

IN MESHY (click Print in the left sidebar, then Print Check: free)
[ ] Print size: will it fit on your printer?
[ ] Printer set to FDM (a filament printer) so the check matches your machine
[ ] Thin walls: a small share, or none (click show to see where)
[ ] Watertight: Yes
[ ] Holes: 0
[ ] Non-manifold edges: 0
[ ] Problems? Make Printable: 10 credits; Meshy's docs say a paid plan for a model
    Meshy made. It removes colour from a textured model. Free plan: use the
    slicer's Fix model or Blender's 3D Print Toolbox instead.

DOWNLOAD
[ ] Free plan: only untextured Meshy 6 Lite models download (10 a month)
[ ] Format: STL for a one-colour print (3MF for colour, from Multi-Color Print)
[ ] Paid plan: Resize on, real height typed in (the unit starts as cm)
[ ] Free plan: remember an STL has no units; slicers read its numbers as mm

IN THE SLICER
[ ] Mesh warning? Right-click the model, Fix model (Bambu Studio on Windows
    only; on a Mac, use Blender's 3D Print Toolbox below)
[ ] Scale tool: Size Z = the real height in mm, uniform scale ticked
    (80 mm for an 8 cm figurine)
[ ] Thin parts (tail, ears, legs) about 1.2 mm or thicker on a filament printer
    (Meshy's docs; one help page says 0.8 mm); too thin? print it bigger
[ ] Flat on the plate: Lay on face, pick the plane under the feet; a base 3 mm
    or thicker helps (Add Base in Meshy's Print panel shows any cost first)
[ ] Support tab: Enable support ticked, for anything leaning out more than 45 degrees
[ ] Sliced, then Preview: dragged the layer slider through every thin part,
    no gaps or missing layers

OPTIONAL: BLENDER'S 3D PRINT TOOLBOX (free, Blender 4.2 or newer)
[ ] Installed from Edit, Preferences, Get Extensions
[ ] N, 3D Print tab, Check All
[ ] Solid: 0 non-manifold edges (if not: Clean Up, Make Manifold, Check All again)
[ ] Dimensions in the Item tab match your real size before you trust Thickness

FIRST TEST PRINT
[ ] Same size as the real print (shrinking thins the legs and tail)
[ ] A draft process setting (thicker layers), infill about 10% (Strength tab)
[ ] After: legs whole, tail printed, stands without wobbling, supports off cleanly

SELLING PRINTS
[ ] Free-plan model: Meshy's CC BY 4.0 credit line in your listing (Part 2)
```

### stl_check.py
```
#!/usr/bin/env python3
# STL checker: the size your slicer will see, the triangle count and an
# open-edge count, for an ASCII or binary STL. Standard library only:
# no installs, no network, no API key. It only reads the file.
#
# Run:  python stl_check.py dog.stl
#       python stl_check.py dog.stl --height 80    scale needed for an 80 mm print
#
# An STL has no units. Slicers read its numbers as millimetres, so that's how
# the size is shown. Big files (a million triangles or more) take a while and
# need a lot of memory. Checked against Meshy's docs on 2026-11-07.
import argparse
import os
import re
import struct
import sys

FLOAT3 = struct.Struct("=3f")


def binary_count(data):
    # A binary STL is an 80-byte header, a 4-byte triangle count, then 50 bytes
    # a triangle. Test this first: some binary files start with "solid" too.
    if len(data) in range(84):
        return None
    n = int.from_bytes(data[80:84], "little")
    return n if len(data) == 84 + 50 * n else None


def floats_le(chunk):
    x, y, z = FLOAT3.unpack(chunk)
    if sys.byteorder == "big":
        x, y, z = (struct.unpack("=f", struct.pack("=f", v)[::-1])[0] for v in (x, y, z))
    return (x, y, z)


def read_triangles(path):
    with open(path, "rb") as f:
        data = f.read()
    if not data:
        sys.exit(f"{path}: the file is empty")
    n = binary_count(data)
    if n is not None:
        tris = []
        for i in range(n):
            base = 84 + 50 * i + 12          # skip the 12-byte normal
            tris.append(tuple(floats_le(data[base + 12 * k: base + 12 * k + 12]) for k in range(3)))
        return "binary", tris
    text = data.decode("ascii", errors="replace")
    if not text.lstrip().lower().startswith("solid"):
        sys.exit(f"{path}: this doesn't look like an STL file")
    nums = re.findall(r"vertex\s+(\S+)\s+(\S+)\s+(\S+)", text)
    if len(nums) % 3 or not nums:
        sys.exit(f"{path}: couldn't find whole triangles in this ASCII STL")
    try:
        pts = [tuple(float(v) for v in xyz) for xyz in nums]
    except ValueError:
        sys.exit(f"{path}: a vertex has a number that isn't valid")
    return "ASCII", [tuple(pts[i:i + 3]) for i in range(0, len(pts), 3)]


def main():
    ap = argparse.ArgumentParser(description="STL size and open-edge checker (offline)")
    ap.add_argument("stl")
    ap.add_argument("--height", type=float, help="the height you want to print, in mm")
    a = ap.parse_args()
    if a.height is not None and (a.height in (0.0,) or a.height != abs(a.height)):
        sys.exit("--height must be a positive number of mm")
    if not os.path.isfile(a.stl):
        sys.exit(f"{a.stl}: file not found")
    kind, tris = read_triangles(a.stl)
    if not tris:
        sys.exit(f"{a.stl}: no triangles in this file")

    # The size: the box around every corner of every triangle.
    xs = [p[0] for t in tris for p in t]
    ys = [p[1] for t in tris for p in t]
    zs = [p[2] for t in tris for p in t]
    size = (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs))

    # Edges: join corners that match to 5 decimal places, then count how many
    # triangles use each edge. 1 = open (a hole's edge), 3 or more = non-manifold.
    ids, edges, flat = {}, {}, 0
    for t in tris:
        v = [ids.setdefault(tuple(round(c, 5) for c in p), len(ids)) for p in t]
        if len(set(v)) != 3:
            flat += 1                        # a triangle with no area; skip it
            continue
        for a_, b_ in ((v[0], v[1]), (v[1], v[2]), (v[2], v[0])):
            key = (min(a_, b_), max(a_, b_))
            edges[key] = edges.get(key, 0) + 1
    open_edges = sum(1 for c in edges.values() if c == 1)
    nonmanifold = sum(1 for c in edges.values() if c not in (1, 2))

    print(f"File:       {a.stl} ({kind} STL)")
    print(f"Size:       {size[0]:.1f} x {size[1]:.1f} x {size[2]:.1f} mm "
          "(X x Y x Z, as your slicer will see it)")
    print(f"Triangles:  {len(tris):,}" + (f" ({flat:,} with no area)" if flat else ""))
    print(f"Open edges: {open_edges:,}")
    print(f"Non-manifold edges: {nonmanifold:,}")
    if open_edges == 0 and nonmanifold == 0:
        print("Verdict:    no open or non-manifold edges found: looks watertight")
    else:
        print("Verdict:    holes or bad edges: run Meshy's Print Check, the slicer's "
              "Fix model, or Blender's 3D Print Toolbox")
    if a.height is not None:
        if size[2] == 0:
            sys.exit("The model is flat (no height), so it can't be scaled to a height")
        pct = a.height / size[2] * 100
        print(f"Scale:      {pct:.1f}% in your slicer for a print {a.height:g} mm tall "
              f"({size[0] * pct / 100:.1f} x {size[1] * pct / 100:.1f} x {a.height:g} mm)")
    print("Reminder:   thin parts under about 1.2 mm may not print on a filament printer "
          "(Meshy docs, checked 2026-11-07). Check the slicer's layer preview.")


if __name__ == "__main__":
    main()
```
