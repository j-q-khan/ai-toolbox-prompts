# Claude build prompt: AI CAD with Claude, Part 3

A render-and-check loop for OpenSCAD with no MCP server: Claude writes or opens hook.scad, renders a PNG and an STL with the openscad command, looks at the PNG, checks OpenSCAD's warnings and fixes the model while you approve every command. Written from the openscad-mcp README, Claude Code's docs and the OpenSCAD manual, checked 2026-11-07. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: set up a render-and-check loop for OpenSCAD in this folder, with no MCP server: you write a .scad file, run the openscad command to make a PNG preview and an STL, look at the PNG, check OpenSCAD's warnings, and fix the model, while I approve every command.
Inputs: OpenSCAD installed (the stable 2021.01 release or a development snapshot). If `openscad` isn't on my PATH, ask me for its full path and use that.
Steps, in order:
1. Run `openscad --version` (ask me first) and tell me which version I have. Show me the folder you'll work in and wait for my yes. Work only inside this folder; never open, include or import a file outside it.
2. If hook.scad isn't in this folder, write it: a headphone wall hook in millimetres, Z up, the wall at y = 0. A back plate 30 wide, 5 thick and 70 high; an arm 45 long and 6 thick along the bottom; a lip 4 thick and 10 above the arm at its end; two 4.5 mm screw holes through the back plate at 25 and 55 mm up, each with a 90 degree countersink 8.5 mm wide at the front face. Put every size in a named variable at the top. Show me the code and wait for my yes before you run anything. Use only built-in OpenSCAD: no include, use, import or surface lines.
3. Render a preview: `openscad -o hook.png --imgsize=800,600 --autocenter --viewall hook.scad`. Open hook.png by its path and look at it. Then check the text OpenSCAD printed: if it has a WARNING or ERROR line, treat the run as failed even if the command reported success, because OpenSCAD can exit with success and draw an empty scene.
4. Tell me what you see, in numbers where you can: from the code, the overall size (it should be 30 x 45 x 70 mm) and where the holes are. If anything is wrong (holes on the wrong face, a missing wall, an empty picture), fix hook.scad, show me the change, and render again. Stop after three rounds and ask me.
5. When I say it's right, export the mesh: `openscad -o hook.stl hook.scad`, again checking for WARNING or ERROR lines.
6. Write safety-checklist.md with these lines: work only in this test folder with made-up parts; look at every model's code before it renders, with no include, use, import or surface line pointing outside the folder; treat any WARNING or ERROR line as a failure even if the command reports success; check the size from the code and the picture before exporting; approve every command yourself; if you later add an MCP server, install it only from its official package, pin the version, set MCP_ALLOWED_PATHS to the test folder and add ask rules for its file-writing tools. Then give me a three-line summary.
Safety: this folder only, made-up parts only. No installs, no MCP servers, no web requests. Ask me before every command. Never run a command other than openscad (and its --version) without asking me first and saying why.
Output: hook.scad, hook.png, hook.stl, safety-checklist.md and a three-line summary.
