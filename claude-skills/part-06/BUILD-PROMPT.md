# Claude build prompt: Claude Skills with MCP: A Skill That Checks Your 3D Model

Use this in Claude Code (Pro or higher), started in plan mode in your cad-test folder from AI CAD Part 3, where the openscad server is already added at local scope.

Goal: set up a model-check skill in this folder that checks an OpenSCAD model through the openscad MCP server and reports, plus the settings and hook that stop it saving or exporting. You only write the files I approve. You never run, install or download anything, and you never call the openscad tools yourself while setting this up.
Steps, in order:
1. Ask me to run claude mcp list in a second terminal in this folder and tell you the server's name. If it isn't openscad, use that name in every mcp__ tool name below and say so.
2. Ask me for the part's wanted sizes: the bounding box in X, Y and Z in millimetres, the tolerance, and the number of pieces. Default to the headphone hook: 30 x 45 x 70 mm, plus or minus 0.2 mm, one piece.
3. Show me .claude/skills/model-check/SKILL.md with frontmatter name model-check, a description that says what it does and when to use it, context: fork, and allowed-tools listing only mcp__openscad__measure, mcp__openscad__validate and mcp__openscad__render. The body: check the file named in $ARGUMENTS; open ${CLAUDE_SKILL_DIR}/sizes.md; measure mode model first; validate mode geometry, never autofix; compare within the tolerance, a zero box or any error is a fail; only then render once and trust the numbers; report a table; end with "Checked, not printed. Nothing was saved or exported." Wait for my yes.
4. Show me .claude/skills/model-check/sizes.md with my sizes. Wait for my yes.
5. Show me .claude/settings.json: ask on mcp__openscad__model and mcp__openscad__scad_eval, deny on mcp__openscad__export_model, and a PreToolUse hook with matcher mcp__openscad__.* that runs .claude/hooks/no-save.sh with onFailure set to block. If a settings.json is already here, show me both and merge only after I say yes.
6. Show me .claude/hooks/no-save.sh: bash only, no jq; it denies a model call unless its action is get or list, and a validate call whose autofix is anything but false, with a short reason. Wait for my yes, then tell me to make it runnable with chmod +x on macOS or Linux, and that Windows needs Git for Windows.
7. Tell me to start a new session here and type /model-check hook.scad, and how to test the lock.
Safety: this folder only. Never write outside .claude in this folder. Don't open any .env file or any file that holds passwords or keys. Never call export_model or any model action other than get or list.
Output: the four files, each approved by me, and the two test steps.
