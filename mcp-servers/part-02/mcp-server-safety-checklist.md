# MCP server safety checklist (facts checked 2026-11-13)
# Save it: copy this text from the link in the description.
# Windows: paste into Notepad, Save as, set the box called Save as type to All files, name it mcp-server-safety-checklist.md
# Mac: paste into TextEdit, choose Format, Make Plain Text, then save it as mcp-server-safety-checklist.md

## Before you start
- A listing is not a safety check. The MCP Registry says to "assume minimal-to-no moderation".
- Anthropic reviews Directory connectors but "does not security-audit or manage any MCP server".
- The official reference servers are "educational examples", not "production-ready solutions".

## Check 1: who publishes it
- [ ] I opened the GitHub page from the app maker's own docs, not from a search result.
- [ ] The account that owns it is the app maker or the protocol's maintainers (modelcontextprotocol), or I know who it is.
- [ ] The package name matches the docs letter for letter (typosquatting = a name one letter off).

## Check 2: licence
- [ ] The About box on the right of the GitHub page names a licence (for example MIT or Apache-2.0).
- [ ] The code is public, so I (or the free prompt) can look through it.

## Check 3: last release and open issues
- [ ] Releases (right-hand column, under the About box): the latest release is recent, and it is not marked Pre-release.
- [ ] Issues tab: the maintainers reply. Busy is normal for a popular server; silent with a year-old release is a warning sign.

## Check 4: what it can reach
- [ ] README: I know which folders, accounts, websites and network locations it can touch.
- [ ] I found the setting that limits it (an allowed folder list, a single-repository setting, a read-only flag) and I will use it.
- [ ] I know whether its tools that change things are on by default.
- [ ] I noted any caution box in the README.

## Check 5: its tool list and code (the step up)
- [ ] I looked through every tool's description. Nothing in one tells Claude to do something unrelated to the tool's job.
- [ ] I know which tools only look and which change, delete or send things.
- [ ] In the code: it sends nothing to a website the README doesn't mention.
- [ ] In the code: it opens no files outside the folders I give it.
- [ ] In the code: it starts no other programs, or I know why it does.
- [ ] If I used the MCP Inspector, I did it only after checks 1 to 4, inside a container, because the Inspector starts the server.

## After you add it
- [ ] One exact version, not "latest".
- [ ] A test folder or test account, not my real files.
- [ ] Claude asks before tools that change things run (Part 3 sets this up).
- [ ] Only a handful of servers. I look through tool descriptions again now and then, not only on day one (a server can change them after I approve it, even on the same version: a rug pull).
- [ ] Switched off when I'm done.

## Remember
- "No check proves what a server will do." Treat a server "as untrusted code with exactly the privileges you hand it — and hand it as few as possible." (MCP local server security guide)
- Next in the series: Part 3, How to Add an MCP Server to Claude Code, Claude Desktop and VS Code
