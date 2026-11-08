# Sources: FreeCAD with AI: Fix "Wire Is Not Closed", Tolerances and Threads

Part 7 of the AI CAD with Claude series.

- FreeCAD releases (GitHub API, 2026-11-08): https://github.com/FreeCAD/FreeCAD/releases
- The error text, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Part/App/FaceMakerBullseye.cpp
- Validate Sketch, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/Gui/Command.cpp
- Part Design's Sketch menu, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/PartDesign/Gui/Workbench.cpp
- FreeCAD wiki, Sketcher ValidateSketch (2026-11-08): https://wiki.freecad.org/Sketcher_ValidateSketch
- Coincident constraint, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/Gui/CommandConstraints.cpp
- Toggle Construction Geometry, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/Gui/CommandAlterGeometry.cpp
- External geometry colours, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/Gui/EditModeCoinManagerParameters.cpp
- FreeCAD 1.1 release notes (wiki API, 2026-11-08): https://wiki.freecad.org/Release_notes_1.1
- The preference, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/Gui/SketcherSettings.ui
- Sketch Python attributes, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/Sketcher/App/SketchObject.pyi
- FreeCAD wiki, Part ToleranceSet (2026-11-08): https://wiki.freecad.org/Part_ToleranceSet
- PartDesign Hole, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Mod/PartDesign/Gui/TaskHoleParameters.ui
- FreeCAD wiki, PartDesign Hole (2026-11-08): https://wiki.freecad.org/PartDesign_Hole
- FreeCAD wiki, Expressions (2026-11-08): https://wiki.freecad.org/Expressions
- FreeCAD wiki licence (API siteinfo, 2026-11-08): https://wiki.freecad.org/api.php?action=query&meta=siteinfo&siprop=rightsinfo
- FreeCAD wiki image records (API imageinfo, 2026-11-08): https://wiki.freecad.org/File:Sketcher_defining_external_relnotes_1.1.gif
- freecad-mcp, Part 6's server (as checked for Part 6, 2026-11-07): https://github.com/neka-nat/freecad-mcp/blob/main/docs/tools.md
- Macro and view menus, FreeCAD 1.1.4 source: https://github.com/FreeCAD/FreeCAD/blob/1.1.4/src/Gui/CommandMacro.cpp

## Images

- Sketcher_defining_external_relnotes_1.1.gif: https://wiki.freecad.org/images/b/b4/Sketcher_defining_external_relnotes_1.1.gif (CC BY 3.0, FreeCAD wiki by NewJoker)
- Part_Design_hole_tool_relnotes_1.1.gif: https://wiki.freecad.org/images/d/dc/Part_Design_hole_tool_relnotes_1.1.gif (CC BY 3.0, FreeCAD wiki by Alfrix)
- Part_Design_thread_profiles_relnotes_1.1.gif: https://wiki.freecad.org/images/6/61/Part_Design_thread_profiles_relnotes_1.1.gif (CC BY 3.0, FreeCAD wiki by Alfrix)
- FreeCAD_Tree_view_error.png: https://wiki.freecad.org/images/e/e1/FreeCAD_Tree_view_error.png (CC BY 3.0, FreeCAD wiki by Roy 043)
