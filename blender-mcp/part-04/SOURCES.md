# Sources: Blender MCP for 3D Printing: From a Prompt to a Printable STL

Part 4 of the Blender MCP with Claude series.

- Blender 5.2 manual, Scene Properties, Units (2026-11-10): https://docs.blender.org/manual/en/5.2/scene_layout/scene/properties.html
- Blender 5.2 Python API, UnitSettings (2026-11-10): https://docs.blender.org/api/5.2/bpy.types.UnitSettings.html
- Blender 5.2 manual, STL (2026-11-10): https://docs.blender.org/manual/en/5.2/files/import_export/stl.html
- Blender 5.2 Python API, bpy.ops.wm (2026-11-10): https://docs.blender.org/api/5.2/bpy.ops.wm.html
- Blender 4.1 release notes, import and export (2026-11-10): https://developer.blender.org/docs/release_notes/4.1/pipeline_assets_io/
- Blender's STL exporter at v5.2.3 (2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/io/stl/exporter/stl_export.cc
- Blender's STL export operator at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/editors/io/io_stl_ops.cc
- The file window's button at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/editors/space_file/filesel.cc
- Blender 5.2 manual, File Browser (critic, 2026-11-10): https://docs.blender.org/manual/en/5.2/editors/file_browser.html
- Blender's menus at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/scripts/startup/bl_ui/space_topbar.py
- Hidden pieces at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/blenkernel/intern/layer.cc
- Join at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/editors/mesh/mesh_join.cc
- Blender's units at v5.2.3 (critic, 2026-11-10): https://projects.blender.org/blender/blender/src/tag/v5.2.3/source/blender/blenkernel/intern/unit.cc
- The StL Format, fabbers.com (2026-11-10): http://www.fabbers.com/tech/STL_Format
- Blender 5.2 manual, Apply (2026-11-10): https://docs.blender.org/manual/en/5.2/scene_layout/object/editing/apply.html
- Blender 5.2 manual, Selecting (2026-11-10): https://docs.blender.org/manual/en/5.2/scene_layout/object/selecting.html
- Blender 5.2 manual, Join (2026-11-10): https://docs.blender.org/manual/en/5.2/scene_layout/object/editing/join.html
- Blender 5.2 manual, Boolean modifier (2026-11-10): https://docs.blender.org/manual/en/5.2/modeling/modifiers/generate/booleans.html
- Blender 5.2 Python API, BooleanModifier (2026-11-10): https://docs.blender.org/api/5.2/bpy.types.BooleanModifier.html
- Blender 5.2 Python API, Object (2026-11-10): https://docs.blender.org/api/5.2/bpy.types.Object.html
- Blender 5.2 manual, Solidify modifier (2026-11-10): https://docs.blender.org/manual/en/5.2/modeling/modifiers/generate/solidify.html
- Blender 5.2 manual, Properties editor (2026-11-10): https://docs.blender.org/manual/en/5.2/editors/properties_editor.html
- Blender 5.2 manual, Topbar (2026-11-10): https://docs.blender.org/manual/en/5.2/interface/window_system/topbar.html
- readme_tools.rst at v1.0.3 (2026-11-10): https://projects.blender.org/lab/blender_mcp/src/tag/v1.0.3/readme_tools.rst
- The piece-detail tool at v1.0.3 (2026-11-10): https://projects.blender.org/lab/blender_mcp/src/tag/v1.0.3/mcp/blmcp/tools/get_object_detail_summary_toolcode.py
- Licence and attribution (2026-11-10): every manual page above carries "This page is licensed under a CC-BY-SA 4.0 Int. License";: https://docs.blender.org/manual/en/5.2/copyright.html

## Images

- editors_preferences_section_system.webp: https://docs.blender.org/manual/en/5.2/_images/editors_preferences_section_system.webp (CC-BY-SA-4.0, docs.blender.org by Blender Documentation Team)
