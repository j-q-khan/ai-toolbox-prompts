# Claude build prompt: MCP Servers, Part 1

Use this in Claude Code, in a new empty test folder. Start in plan mode, so nothing is changed until you say yes. It opens your MCP settings files as text only.

Goal: make me a plain-words inventory of the MCP servers I already have connected, so I know what each one is and what it can reach. You install nothing, run nothing and change no settings.
Steps, in order:
1. Look for these files and open each one that exists, as text only: .mcp.json in this folder; the file .claude.json in my home folder (on Windows, C:\Users\MyName\.claude.json); and Claude Desktop's config, claude_desktop_config.json (Windows: %APPDATA%\Claude\; Mac: ~/Library/Application Support/Claude/). If none exists, tell me I have no servers set up and stop.
2. Don't run claude mcp list, any server command, npx, uvx or anything else, because starting a server runs its code.
3. For each server under mcpServers, write down: its name; which file it's in; local (it has a command) or remote (it has a url); the command and its arguments, or the url; whether one exact version is set (a version number in the package name or image), or not; which folders, accounts or websites it can reach, going only by what the file shows; and the names of any environment variables or headers it uses.
4. Never show the value of an environment variable, header, token, password or key. Write only its name, followed by "(value hidden)". Do the same inside commands, arguments and urls: replace anything that looks like a key, token or password (for example after --api-key, --token, key= or token=) with "(value hidden)".
5. For each server, add one plain sentence on what it's likely for, and mark any server you can't identify as "unknown: check who publishes it".
6. Show me mcp-inventory.md and wait for my yes. I'll switch you out of plan mode so you can save it in this folder.
Safety: create only mcp-inventory.md in this test folder. Don't edit any settings file, don't remove any server, don't install anything, don't run commands and don't go online.
Output: mcp-inventory.md, and a three-line summary of how many servers I have, how many are local and remote, and how many have no exact version set.
