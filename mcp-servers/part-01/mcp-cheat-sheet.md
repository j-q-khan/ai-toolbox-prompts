# MCP cheat sheet (facts checked 2026-11-13)
# Save it: copy this text from the link in the description.
# Windows: paste into Notepad, Save as, set the box called Save as type to All files, name it mcp-cheat-sheet.md
# Mac: paste into TextEdit, choose Format, Make Plain Text, then save it as mcp-cheat-sheet.md

## What MCP is
- MCP (Model Context Protocol): one shared set of rules that lets an assistant plug into your files, apps and tools.
- Open source: the rules are published for anyone to use. Docs: modelcontextprotocol.io
- Specification: the protocol's official rulebook. Current version: 2026-07-28.

## The three pieces (plug and socket)
- Host: the app you talk to (Claude Desktop, Claude Code, a code editor). The house.
- Client: a connector the host makes for each server. One socket for each plug.
- Server: a small program that gives the assistant access to one thing (a folder, a notes app, a calendar). The plug.

## What a server offers
- Tools: actions the assistant asks the server to run. The assistant calls them.
- Resources: things the assistant can look at, each with its own link. You or the assistant pick them.
- Prompts (in MCP): ready-made templates the server offers. You pick them.

## Where a server runs
- Local: on your computer, started by the app (spec name: stdio). It can reach what your account can reach.
- Remote: on someone else's computer, over the internet (spec name: Streamable HTTP). You usually sign in.

## Who runs MCP
- Created by Anthropic. Since 2025-12-09: the Agentic AI Foundation, under the Linux Foundation.
- The MCP Steering Group (its maintainers) decides technical direction.

## Safety: the idea behind this series
- A local server runs with your permissions.
- Prompt injection: text a server hands back (a web page, an email, a file) can carry someone else's instructions.
- Anthropic: "Verify you trust each server before connecting it."
- The protocol can't enforce safety on its own, so keep the app asking before tools run.
- Claude Code (v2.1.283 or later) starts in auto mode: a second model checks most actions instead of you. Part 3 shows how to make it ask first.
- Habits: one exact version of each server, a test folder instead of your real files, switch it off when done.

## Next in the series
- Part 2: Best MCP Servers for Claude Code, and How to Check One Is Safe
