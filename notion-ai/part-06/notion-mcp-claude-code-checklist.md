# Notion MCP in Claude Code: add, sign in, test, remove (facts checked 2026-11-18)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Commands, limits and dates change. Check each line again at developers.notion.com/guides/mcp/get-started-with-mcp and code.claude.com/docs/en/mcp before you rely on it. Written from Notion's and Anthropic's docs, not run.

## What you need
- [ ] Claude Code installed and signed in, and a terminal: PowerShell on Windows, Terminal on a Mac. Notion: "If you see `command not found`, make sure `claude` is on your `PATH`." New to it? Claude Code for Beginners: https://www.youtube.com/playlist?list=PLHGdih6OUQLg
- [ ] A Notion account on any plan. Notion: "Notion MCP works on every plan. Some features depend on the workspace's plan". No Notion page gives a price for the server, and none calls it free.
- [ ] To be a member of the Notion workspace, not a guest. Notion: "Only workspace members can connect Notion MCP."
- [ ] For anything from work: your employer's rules on what an outside assistant may reach. On a company Claude plan, an admin may restrict adding servers; Notion: "If you see an enterprise policy error, ask your admin whether Notion MCP is allowed in your AI assistant."
- [ ] Did Part 5 already? Anthropic: "If you've logged into Claude Code with a claude.ai account, MCP servers you've added in claude.ai, known as connectors, are automatically available in Claude Code". Type /mcp first; Notion may already be listed. If you add it with the command as well, Anthropic says: "A server you've added in Claude Code takes precedence over a claude.ai connector that points at the same URL."

## Add the server (one command)
- [ ] Open a terminal in the folder you work in. Don't start Claude Code yet. Anthropic: "Run this in your terminal, not inside a `claude` session".
- [ ] Type or paste: claude mcp add --transport http notion https://mcp.notion.com/mcp
- [ ] What the parts mean (Anthropic's quickstart): `claude mcp add` "registers a server with Claude Code"; `--transport http` means "the server is hosted at a URL rather than run as a local process"; `notion` is "a name you make up"; the last part is "the URL where the server is hosted".
- [ ] You should get a line that starts with Added and ends with "to local config", then a "File modified:" line. It means the setting was saved, not that you're signed in.
- [ ] Scope is where the setting applies. The default, local, is Notion's "Available only to you in the current project", which means the folder (or code repository) you ran it from.
- [ ] For every folder, use this line instead: claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp
- [ ] Already added it the first way? Anthropic: "A server's scope is fixed when you add it, so changing scope means removing the entry and re-adding it at the new one." Run: claude mcp remove notion --scope local , then the user-scope line.
- [ ] `--scope project` writes a shared file called .mcp.json for a team. This checklist doesn't use it.

## Sign in
- [ ] Start Claude Code in that same folder: type claude and press Enter.
- [ ] Type /mcp and press Enter. Pick notion from the list, press Enter, and choose Authenticate. (These are the steps Anthropic's quickstart gives for a server that needs sign-in; its example is Sentry, and it names Notion as working the same way.)
- [ ] Your browser should open Notion's own sign-in page. Sign in, look over the access it asks for, and approve it. (Anthropic's step is "Approve the connection there."; neither company's page describes Notion's screen step by step.)
- [ ] If the browser doesn't open, Anthropic: "copy the provided URL and open it manually".

## Check that it worked
- [ ] Back in Claude Code, Anthropic: "the server's status changes to connected."
- [ ] From a terminal outside Claude Code: claude mcp list . It "shows a health status next to each server it lists, such as `✔ Connected`, `! Needs authentication`, or `✘ Failed to connect`." Of Needs authentication straight after adding, Anthropic says: "That's expected".
- [ ] /mcp says "No MCP servers configured"? Anthropic's first cause: "You ran `claude mcp add` from a different project." Go back to the folder where you ran the command, or add it with --scope user.
- [ ] Paste the test prompt from notion-mcp-test-prompt.txt. Claude should list the tools, change nothing, wait for your yes, then give you a link to "Test Bakery notes (dummy)".
- [ ] Ask: What did we decide about the sourdough price, and which page is it on? Anthropic: "The tool call in Claude's output is labeled with the server name, which is how you confirm the answer came from the MCP server rather than Claude's built-in knowledge." Then open the page in Notion and check the answer against it.

## What it can reach, and your data
- [ ] Notion: "Remember that MCP tools act with your full Notion permissions. They can access everything you can access."
- [ ] Notion: "After you authorize the connection, your AI assistant can read and update content that you can access in the selected workspace."
- [ ] Anthropic: "If Claude Code asks for permission the first time Claude calls the server, approve it." Check first that it is the action you asked for.
- [ ] Notion: "Enable confirmation before actions that change content." and "Treat content returned by tools as untrusted. Review proposed actions and data sharing before approving them."
- [ ] Notion: "a connected client may send content returned by Notion MCP to systems outside Notion."
- [ ] Anthropic, on personal plans: "We give you the choice to allow your data to be used to improve future Claude models. We will train new models using data from Free, Pro, Max, and Ultra accounts when this setting is on (including when you use Claude Code from these accounts)." The page doesn't say where the setting starts, so look in Claude's Settings, under Privacy.
- [ ] Anthropic, on Team and Enterprise plans and the API: it "does not train generative models using code or prompts sent to Claude Code under commercial terms, unless the customer has chosen to provide their data to us for model improvement".
- [ ] Anthropic: "We encourage either writing your own MCP servers or using MCP servers from providers that you trust. You are able to configure Claude Code permissions for MCP servers."

## Limits
- [ ] Requests: 180 per minute on most plans, 600 per minute on Business and Enterprise. Notion: "Every tool call counts toward them. These limits can change over time."
- [ ] If Claude reports a rate limit, Notion: "ask your AI assistant to reduce parallel operations, or try again later."
- [ ] Searching sources you have connected to Notion, Notion: "Connected-source search with `notion-connector-search`: Business or Enterprise with Notion AI." The server itself, Notion: "Notion MCP works on every plan."
- [ ] Room in Claude's working memory: type /context inside Claude Code to see how much each connected server uses (a tip from Notion's docs).

## Two older routes to skip
- [ ] A link ending in /sse. Notion: "Notion will retire the legacy HTTP with Server-Sent Events (SSE) endpoint, https://mcp.notion.com/sse, on February 23, 2027. Update your client before that date." If you added that one, remove it and add the link ending in /mcp.
- [ ] The older local server, makenotion/notion-mcp-server (the one with a token and a JSON settings file). Its README: "This repository is a separate, self-hosted MCP server implementation that is no longer actively maintained or supported. Please use Remote Notion MCP instead." This checklist doesn't use it.

## Optional: Notion's plugin for Claude Code
- [ ] What it is, from its README: "an official Claude Code plugin that bundles" Notion Skills, the Notion MCP Server and a set of slash commands. It lists 12 Skills and 10 slash commands, and connects to the same link, https://mcp.notion.com/mcp
- [ ] How its README says to add it, inside Claude Code: /plugin marketplace add makenotion/claude-code-notion-plugin , then /plugin install notion-workspace-plugin@notion-plugin-marketplace , then "Restart Claude Code".
- [ ] As found on 2026-11-18: its plugin.json says "license": "MIT"; the repo has no LICENSE file, and GitHub shows no licence for it. We report that as found and draw no conclusion from it. Not installed or run for this video.
- [ ] You don't need it: the one command above is enough. Anthropic: "You add and remove plugin servers by installing or uninstalling the plugin, not with `/mcp` commands."

## Remove it afterwards
- [ ] From the terminal: claude mcp remove notion . Anthropic: "When you remove a remote server, Claude Code also deletes the OAuth tokens and client registration it stored for that server. Claude Code doesn't revoke the tokens at the authorization server that issued them."
- [ ] To sign out without removing it, Anthropic: "Use "Clear authentication" in the `/mcp` menu to revoke access".
- [ ] On Notion's side: Settings, then Notion MCP, shows connected apps; Notion's docs say workspace owners manage them there.
- [ ] Delete the dummy page: in Notion, the three dots at the very top right of the page, then Delete.

Sources: developers.notion.com/guides/mcp/get-started-with-mcp ; developers.notion.com/guides/mcp/rate-limits ; developers.notion.com/reference/request-limits ; developers.notion.com/guides/mcp/mcp-security-best-practices ; notion.com/help/notion-mcp ; code.claude.com/docs/en/mcp ; code.claude.com/docs/en/mcp-quickstart ; code.claude.com/docs/en/data-usage ; code.claude.com/docs/en/security ; github.com/makenotion/notion-mcp-server ; github.com/makenotion/claude-code-notion-plugin
