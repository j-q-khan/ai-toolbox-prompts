# Claude build prompt: Playwright MCP, Part 3

Use this in Claude Code (Pro or higher, or a Console account), in an empty folder you've made for testing, such as playground. Start in plan mode.

Goal: set up a safe first test of Playwright MCP v0.0.85 in this folder. You write files and show me commands; I run the commands myself. Don't install or start anything.
Steps, in order:
1. Write serve.js here: a Node.js script that uses only the built-in http module, binds to 127.0.0.1 on port 8080, serves one fixed HTML page (a heading "My test to-do list", a labelled text box "New task", an "Add" button, and a list the button adds the box's text to with textContent), reads no files, and prints "Test page ready: http://localhost:8080 (press Ctrl+C to stop)". If port 8080 is busy, print a plain message and exit.
2. Write .claude/settings.json here with exactly this permissions block: deny mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload; ask mcp__playwright__browser_evaluate. Show it to me.
3. Show me, without running them: node --version (it must say 20 or higher); node serve.js, for a second window; and claude mcp add playwright -- npx -y @playwright/mcp@0.0.85 --isolated, to run from this folder. Explain each part of the add command in one line, and why it's @0.0.85 and not @latest, and why --isolated.
4. Tell me what I should see: the "Added stdio MCP server playwright … to local config" line, then playwright marked connected in /mcp.
5. Give me the first prompt to try, which only looks at http://localhost:8080 and clicks or types nothing, and remind me that the Playwright MCP README says it "is not a security boundary".
6. Tell me how to switch it off (Disable in /mcp) and remove it (claude mcp remove playwright).
Safety: write only serve.js and .claude/settings.json in this folder. Don't run any command, don't install anything, and don't start the server or a browser.
Output: the two files, the commands to run in order, and what each should show.
