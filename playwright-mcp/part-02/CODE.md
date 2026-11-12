# Full code: Chrome DevTools MCP vs Playwright MCP: Which Should You Use?



### 1. which-browser-server-checklist.md (from the link in the description; to keep a copy, save it in Notepad with the Save as type box set to All files, or on a Mac in TextEdit set to plain text before pasting)
```
# Chrome DevTools MCP or Playwright MCP: which fits your job?
# Facts from each project's own README and docs, checked 2026-11-12. Nothing to install to use this list.

1. Does your site have to work in Safari or Firefox?
   Yes: Playwright MCP. Its --browser flag takes chrome, firefox, webkit or msedge.
   Chrome DevTools MCP "officially supports Google Chrome and Chrome for Testing only".
2. Do you want test code you can keep?
   Yes: Playwright MCP (opt-in test tools with --caps=testing; Part 4 of the series).
3. Is your page working but slow, or throwing errors in Chrome?
   Yes: Chrome DevTools MCP (performance traces first, log messages that point to the line of code; Part 5).
4. Where does each keep your logins?
   Playwright MCP: its profile section says a persistent profile is the default.
   Chrome DevTools MCP: its profile is "not cleared between runs".
   Both: add --isolated so nothing is kept after you finish.
5. What does each send out by default?
   Chrome DevTools MCP: usage statistics to Google ("enabled by default"),
   and performance tools "may send trace URLs to the Google CrUX API".
   Turn both off: --no-usage-statistics --no-performance-crux
   Playwright MCP: its README doesn't mention collecting usage statistics.
6. Which tools can run code?
   Playwright MCP: browser_evaluate and browser_run_code_unsafe ("RCE-equivalent"), no off flag.
   Block or ask with Claude Code permission rules (Part 3 writes them).
   Chrome DevTools MCP: --javascriptEvaluation=false turns its script tools off,
   but "This is not a JavaScript sandbox".
7. Neither one is a wall:
   "Playwright MCP is not a security boundary."
   Chrome DevTools MCP lets the app "inspect, debug, and modify any data in the browser".
8. Fix the version before the first run:
   @playwright/mcp@0.0.85 or chrome-devtools-mcp@1.13.0, never @latest.
9. All five tools in this video are Apache-2.0 and free:
   Playwright MCP, Chrome DevTools MCP, Playwright CLI, agent-browser, Browser MCP.
   Browser MCP uses your own signed-in Chrome: read Part 6 before trying it.
```
