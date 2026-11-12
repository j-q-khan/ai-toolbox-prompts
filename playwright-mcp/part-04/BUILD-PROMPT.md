# Claude build prompt: Playwright MCP, Part 4

Use this in Claude Code (Pro or higher, or a Console account), in the playground folder from Part 3, which already has serve.js and .claude/settings.json. Start in plan mode.

Goal: add browser testing and a navigation hook to my Playwright MCP v0.0.85 setup. You write files and show me commands; I run the commands myself. Don't install or start anything.
Steps, in order:
1. Show me, without running them, the two lines to re-add the server with its test tools: claude mcp remove playwright, then claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --isolated --caps=testing. Explain what --caps=testing adds (browser_generate_locator and the four browser_verify tools).
2. Write .claude/check-site.js: a Node.js script, built-in modules only, that reads the hook's JSON from stdin, takes tool_input.url, and exits 0 when its origin is exactly http://localhost:8080 or http://127.0.0.1:8080, or when the tool is mcp__playwright__browser_tabs with no url. For anything else, including JSON or an address that doesn't parse, it writes a short reason to stderr and exits 2. Compare origins with new URL(), never with startsWith.
3. Update .claude/settings.json: keep its permissions block exactly (deny mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload; ask mcp__playwright__browser_evaluate) and add a hooks block: PreToolUse, matcher "^mcp__playwright__browser_(navigate|tabs)$", one command hook with "command": "node", "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"] and "onFailure": "block". Show it to me.
4. Write todo.spec.js in this folder: a Playwright test in JavaScript with require("@playwright/test") and test.use({ channel: "chrome" }) that opens http://localhost:8080, fills the New task box with "Buy milk", clicks Add, and expects the list to have the text "Buy milk" and the box to be empty.
5. Show me, without running them, how to run it: npm install --save-dev @playwright/test@1.65.0, then npx playwright test todo.spec.js, with node serve.js running in a second window.
6. Tell me what the hook can't see (a click on a link, a redirect, the page's own scripts), and remind me that the Playwright MCP README says it "is not a security boundary".
Safety: write only .claude/check-site.js, .claude/settings.json and todo.spec.js in this folder. Don't run any command, don't install anything, and don't start the server, a browser or the tests.
Output: the three files, the commands to run in order, and what each should show.
