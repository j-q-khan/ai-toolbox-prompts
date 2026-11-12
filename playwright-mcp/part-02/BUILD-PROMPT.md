# Claude build prompt: Playwright MCP, Part 2

Use this in Claude Code (Pro or higher, or a Console account), in the folder of the web app you'd like Claude to work on. Start in plan mode.

Goal: help me choose between Playwright MCP and Chrome DevTools MCP for my own web app, before I install anything. You run nothing and install nothing.
Steps, in order:
1. Look through this folder's files (package.json, any test folders, any Playwright or Puppeteer config, any browser list such as a browserslist entry) and tell me in plain words what kind of web app it is, whether it already has browser tests, and whether anything says it must work in Safari or Firefox. Don't run any command.
2. Ask me which job I need a browser for most: testing that the page works, in one browser or several, or finding out why a page is slow or throwing errors in Chrome. Wait for my answer.
3. Ask me these checklist questions one at a time: Does the site have to work in Safari or Firefox? Do I want test code I can keep? Is the page on my own computer, or one nobody else should know about? Do I mind usage statistics being sent to Google? Then recommend Playwright MCP, Chrome DevTools MCP, or both, with one reason from my answers for each choice.
4. For whichever I pick, list the flags and settings I'd use before the first run, quoting each project's own words: for Playwright MCP, @playwright/mcp@0.0.85 (not @latest), --isolated, no --port, and Claude Code deny rules for mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload with an ask rule for mcp__playwright__browser_evaluate; for Chrome DevTools MCP, chrome-devtools-mcp@1.13.0 (not @latest), --isolated, --no-usage-statistics, --no-performance-crux, and --javascriptEvaluation=false if I don't need it to run scripts. Remind me that the Playwright MCP README says it "is not a security boundary" and that --javascriptEvaluation=false "is not a JavaScript sandbox". Don't write any settings file.
Safety: read files only. Don't create, edit or delete any file, don't run any command, and don't install anything.
Output: the recommendation, the reasons, and the short list of flags and settings to make before installing.
