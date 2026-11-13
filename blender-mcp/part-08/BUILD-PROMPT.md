# Claude build prompt: Blender MCP with Claude, Part 8

Helps you choose between the official Blender Lab MCP (v1.0.3), the community MCP for Blender (package 2.2.8) and headless Blender scripts, then writes the config and locks for your pick. Claude writes text files only: it uses no Blender tool, installs nothing and runs nothing. Written from each route's own docs and code, checked 2026-11-12. Not run by us.

Use this in Claude Code (Pro or higher), in a new, empty test folder. Start in plan mode. It writes text files only: it installs nothing, runs nothing and uses no Blender tool.

Goal: help me choose between the official Blender Lab MCP (v1.0.3), the community MCP for Blender (package 2.2.8) and headless Blender scripts, then write the config and locks for the one I pick. You install nothing and run nothing.
Inputs: ask me, one at a time: do I want Claude in my open Blender window; do I want online model libraries or outside AI model services; do I want nothing listening on my computer; my operating system; my home folder path.
Steps, in order:
1. Tell me which files you'll create and wait for my yes. Only create files in this folder. Don't install, download or run anything, make no web requests, and don't use any mcp__ tool.
2. Write choice.md: the seven checks (features, usage data, network reach, latest release, licence, how it asks, stars) for all three, from the video's table, each dated 2026-11-12, and which one fits my answers, with the reason. No "best".
3. For the official server: .claude/settings.json with ask rules for mcp__blender__execute_blender_code, mcp__blender__execute_blender_code_for_cli, mcp__blender__render_viewport_to_path and mcp__blender__render_thumbnail_to_path, and the Part 2 steps (v1.0.3 from disk, Auto Start off, Allow Online Access only while working).
4. For the community server: the line claude mcp add --env DISABLE_TELEMETRY=true --env BLENDER_MCP_SAFE_MODE=1 --transport stdio blender-community -- uvx mcp-for-blender@2.2.8, the add-on line uvx mcp-for-blender@2.2.8 install-addon (never the piped install script), and .claude/settings.json with ask rules for mcp__blender-community__execute_blender_code, mcp__blender-community__generate_3d, mcp__blender-community__generate_gaussian_world and mcp__blender-community__import_asset. Warn me: never have the official add-on switched on at the same time, because both use port 9876.
5. For headless: .claude/settings.json with "defaultMode": "default" and ask rules Bash(blender *) and PowerShell(blender *); phone_stand.py (bpy, math and sys only) that builds a base 80 x 70 x 10 mm, a back 80 x 8 x 100 mm tipped back 20 degrees and a lip 80 x 8 x 20 mm, and saves to the path after "--"; and the command blender --background --factory-startup --offline-mode --python-exit-code 1 --python phone_stand.py -- phone_stand.blend, with --python-exit-code before --python, and never -y.
6. Write safety-checklist.md: one route at a time; a new Blender file with nothing private open; test models only, never a client's files; I look over every script before saying yes; switched off afterwards.
7. Check every JSON file parses by reading it back, show me the files, then give me a three-line summary.
Safety: this folder only, test models only. You write text files and nothing else; I copy them into place and run every command myself after reading it.
Output: choice.md, the config file(s) for my pick, safety-checklist.md and a three-line summary.
