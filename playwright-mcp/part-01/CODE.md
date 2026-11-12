# Full code: Playwright MCP Explained: What It Does and When to Use It



### 1. mcp-or-cli-checklist.md (from the link in the description; to keep a copy, save it in Notepad with the Save as type box set to All files, or on a Mac in TextEdit set to plain text)
```
# Playwright MCP or Playwright CLI: which fits your job?
# Facts from the Playwright MCP README, checked 2026-11-12. Nothing to install to use this list.

1. Do you mostly want Claude to explore a page step by step, keeping the browser open as it goes?
   Yes: the MCP server fits ("exploratory automation, self-healing tests, or long-running autonomous workflows").
2. Do you mostly want quick checks while Claude writes code in a big codebase?
   Yes: the CLI with skills may fit better ("more token-efficient", in Microsoft's words).
3. Are you working inside a coding agent like Claude Code?
   Microsoft's note: "you might benefit from using the CLI+SKILLS instead". Weigh questions 1 and 2.
4. Would long page outlines fill up Claude's working space on your pages?
   Yes: lean to the CLI. No: either works.
5. Is the page one you control, on your own computer?
   Start there. Never point it at sites where you're signed in until you've seen Part 6.
6. Before the first run, whichever you pick:
   - Playwright MCP is "not a security boundary"
   - fix the version: @playwright/mcp@0.0.85, not @latest
   - add --isolated, so the browser profile stays in memory, not on disk
   - no --port, so nothing listens on the network
   - deny mcp__playwright__browser_run_code_unsafe and mcp__playwright__browser_file_upload
   - ask before mcp__playwright__browser_evaluate
   - switch the server off in /mcp when you're done
   Part 3 sets all of this up, step by step.
```
