# Claude build prompt: Playwright MCP, Part 5

Use this in Claude Code (Pro or higher, or a Console account), in the playground folder from Parts 3 and 4, which already has serve.js, .claude/settings.json and .claude/check-site.js. Start in plan mode.

Goal: add Chrome DevTools MCP 1.13.0 to my setup to find why a page is slow, with its data-sharing off and the same locks as my Playwright MCP server. You write files and show me commands; I run the commands myself. Don't install or start anything.
Steps, in order:
1. Show me, without running it, the add command: claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@1.13.0 --isolated --no-usage-statistics --no-performance-crux --javascriptEvaluation=false. Explain each flag in one line, quoting the README for usage statistics and CrUX.
2. Write serve-slow.js in this folder: a copy of serve.js's to-do page (Node.js, built-in http only, listening on 127.0.0.1:8080) with a script tag for /slow.js in the head, which the server answers after a 3 second wait with one console.log line, and an img for /logo.png, which returns 404. Every other path except / returns 404.
3. Update .claude/check-site.js: keep it exactly, and add one rule so that mcp__chrome-devtools__navigate_page passes when tool_input.type is "reload", "back" or "forward" and the call gives no url.
4. Update .claude/settings.json: keep its permissions and hooks exactly, add to deny mcp__chrome-devtools__evaluate_script, mcp__chrome-devtools__set_logpoints, mcp__chrome-devtools__upload_file and the five extension tools (install_extension, uninstall_extension, reload_extension, trigger_extension_action, list_extensions), add to ask mcp__chrome-devtools__get_network_request, and add a second PreToolUse entry with matcher "^mcp__chrome-devtools__(navigate_page|new_page)$" running the same check-site.js with "command": "node", "args": ["${CLAUDE_PROJECT_DIR}/.claude/check-site.js"] and "onFailure": "block". Show it to me.
5. Give me the three prompts: a trace with the LCP and insights; the browser log messages and network requests; the defer fix, shown before saving.
6. Tell me what the hook can't see (a click on a link, a redirect, the page's own scripts), and that the plugin route runs none of these flags and its tools have a longer name, so my rules wouldn't match it.
Safety: write only serve-slow.js, .claude/check-site.js and .claude/settings.json in this folder. Don't run any command, don't install anything, and don't start the server, a browser or the page.
Output: the three files, the commands to run in order, and what each should show.
