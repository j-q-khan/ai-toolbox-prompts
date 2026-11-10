# Full code: Blender AI Modeling with Claude: Build a Model by Describing It

Written from the Blender Lab MCP source at v1.0.3 (the tools, the add-on and the server's instructions), the Blender 5.2 manual, and Claude Code's MCP and memory docs, checked 2026-11-10. Use your blender-test folder from Part 2, a file with nothing private open, and made-up models only. Nothing here was installed or run, and Blender wasn't opened; the shell lines were checked with `bash -n`.

### 1. Back where we left off (Blender 5.2, then a new terminal)
```
# Blender: Edit, Preferences, System, Network: tick Allow Online Access (Part 2 unticked it).
# Add-ons, the arrow beside MCP: click Start MCP Bridge Server, and look for: Server is running
# Terminal, macOS or Linux:   cd "$HOME/blender-test"
# Terminal, Windows PowerShell:   Set-Location "$HOME\blender-test"
cd "$HOME/blender-test"
claude
# Send prompt 1. No Stand_Base in the answer? File, New, General; click the cube, press Delete; send prompt 2.
# Then File, Save As: blender-test/phone-stand-01.blend
```

### 2. CLAUDE.md, saved in your blender-test folder (Claude Code loads it every time it starts there)
```
# Blender MCP modeling rules (Blender 5.2, Blender Lab MCP 1.0.3)
- Build one piece at a time, and only the piece I asked for.
- Sizes are in millimetres. Blender's unit is the metre, so 80 mm is 0.08. Check the scene's units first.
- Before any code runs, show me the full Python in the chat and wait for my yes.
- Use only Blender's bpy module and Python's math module.
- No os, subprocess, socket, urllib or requests; no file paths; never save, open, export or delete files.
- Name every new piece in the Model_Part style (Stand_Back) and say its name back to me.
- After each change, focus the 3D viewport on the new piece.
- When I ask for a check, take a screenshot of the 3D viewport and give me the location, rotation and size
  in millimetres and degrees, worked out from the tools' numbers, without running code.
- If a piece sits wrong (sinks in, floats or faces the wrong way), say so and show the fix as Python first.
- If I say I changed something by hand, look at the scene again before changing anything.
- Never touch a piece I didn't name. Ask me when a size or a position is missing; don't guess.
# These rules are guidance Claude follows, not a lock: the ask rules in .claude/settings.json are the lock.
```

### 3. The save-and-check loop, for every piece
```
[ ] Blender: File, Save Incremental (Ctrl+Alt+S): a new file with the next number, nothing overwritten
[ ] Send ONE piece's prompt: what it is, size in mm, where it sits, its name, "show me the Python first"
[ ] Claude Code asks (ask rule): look over the code. Shapes, sizes and names only? Yes. Anything else? No.
[ ] View, Viewpoint, Right (number pad 3) for a side view
[ ] Send the check prompt: a screenshot of the viewport, then the sizes in mm and the tilt in degrees
[ ] Wrong? File, Open Recent, the last good number; say no to saving the changes
[ ] Control Z only for your own clicks: it may not take back what Claude did (add-on v1.0.3, from its code)
[ ] Changed something by hand? Tell Claude, and ask it to look at the scene again
```

### 4. Where things are in Blender 5.2
```
File, Save As (Shift+Ctrl+S)            name the first version: phone-stand-01.blend
File, Save Incremental (Ctrl+Alt+S)     a new file with the next number
File, Open Recent                       go back to a saved version
Edit, Undo (Ctrl+Z)                     your own last step
Edit, Undo History                      your recent steps, newest at the top
View, Viewpoint, Right (number pad 3)   a side view (Front: 1, Top: 7)
N                                       the Sidebar; Item tab: Location, Rotation, Scale, Dimensions
In a number box                         type the value and a unit, like 25mm, then Enter
Preferences, Save & Load, Save Versions how many .blend1, .blend2 backups Blender keeps (default 2)
```

### 5. Switch it off when you're done
```
# Blender: Preferences, Add-ons, MCP: click Stop MCP Server (it then says: Server is stopped).
# Auto Start stays unticked. Untick Allow Online Access (System, Network) if nothing else needs it.
```
