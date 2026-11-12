# Claude build prompt: Playwright MCP, Part 1

Use this in Claude Code (Pro or higher, or a Console account), in the folder of the web app you'd like Claude to check. Start in plan mode.

Goal: help me decide whether my work needs the Playwright MCP server, the Playwright CLI, or neither, before I install anything. You run nothing and install nothing.
Steps, in order:
1. Look through this folder's files (package.json, any test folders, any existing Playwright config) and tell me in plain words what kind of web app it is and whether it already has browser tests. Don't run any command.
2. Ask me which of these I do most: copying error messages from the browser into chat, clicking through the same form by hand after each change, or describing a page you can't see. Wait for my answer.
3. Ask me these checklist questions one at a time: Do I mostly want you to explore a page step by step, keeping the browser open? Do I mostly want quick checks while you write code in a big codebase? Would long page outlines fill up your working space on my pages? Is the page one I control, on my own computer? Then tell me which one fits my answers: the MCP server (Claude explores the page step by step and keeps the browser open), the CLI with skills (short commands that cost fewer tokens, for quick checks while coding), or neither. Give one reason from my answers for each choice.
4. Quote Microsoft's own two lines from the Playwright MCP README: "If you are using a coding agent, you might benefit from using the CLI+SKILLS instead." and "MCP remains relevant for… exploratory automation, self-healing tests, or long-running autonomous workflows".
5. Remind me that the README says "Playwright MCP is not a security boundary", and list what I'd set before the first run: a fixed version (@playwright/mcp@0.0.85, not @latest), the --isolated flag, no --port, and deny rules for mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload with an ask rule for mcp__playwright__browser_evaluate. Don't write any settings file.
Safety: read files only. Don't create, edit or delete any file, don't run any command, and don't install anything.
Output: the recommendation, the reasons, and the short list of settings to make before installing.
