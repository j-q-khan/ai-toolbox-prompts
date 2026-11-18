# Full code: Claude Notion Connector: Connect Claude to Your Notion Workspace

The test prompt from this video, Notion's own setup line and the steps as a checklist, written from Anthropic's and Notion's help pages (checked 2026-11-18). They were written from the docs, not run for this video.

### 1. claude-notion-test-prompt.txt
```
# Paste the first block into a new chat in Claude (not into Notion), after you have connected Notion:
# in Claude, go to Customize, then Connectors, select Discover, find Notion, select Connect to Claude,
# and sign in on Notion's own page. In the chat, select + in the message box, choose Connectors,
# and check that Notion's switch is on.
# It makes one new private page in your Notion workspace with made-up notes for a made-up shop called
# Test Bakery, then waits while you try three asks on it. It asks before it writes, and it changes nothing else.
# An example, written from Anthropic's and Notion's help pages, checked 2026-11-18, and not run or tested:
# check the page it makes yourself. If Claude asks for approval before a step, choose Allow once.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste.

Use my Notion connector for this. Everything here is dummy data for a made-up shop called Test Bakery.
Before you write anything, tell me in two lines what you are about to create and where, and wait for my yes.
Then create one new private page called "Test Bakery notes (dummy)". Do not put it in a shared or team space, and do not change, move or delete any other page or database.
Put this on the page, as written:
- Heading: Weekly sync, dummy notes
- Decision: hold the sourdough price until March (dummy).
- Decision: bake on Saturdays from 6:00 (dummy).
- To do: Order flour (dummy). Not done.
- To do: Print the price list (dummy). Not done.
When the page exists, give me its link and say in one line that nothing else was changed.
Then wait. I will try these three asks, one at a time:
1. What did we decide about the sourdough price, and which page is it on?
2. Create a new private page called "Saturday prep list (dummy)" with three dummy lines.
3. On "Test Bakery notes (dummy)", mark "Order flour (dummy)" as done.
For asks 2 and 3, say what you will change and wait for my yes first.
Rules: use only what is on these dummy pages, and name the page each answer came from. If you can't reach Notion, say so and stop; don't answer from memory. No real names, emails or phone numbers. Don't change sharing, settings or any page I didn't name.

# ---------------------------------------------------------------------------------------------
# Optional, for after the test: Notion's own setup prompt. This one line is Notion's, quoted from
# notion.com/help/notion-mcp on 2026-11-18 (Notion prints the address inside angle brackets; they are
# left out here). Paste it into a new chat in Claude. Notion says the guide it points to "asks before
# changing anything"; it also has Claude make a private guide page in your Notion and offer to save
# your preferences as memories, so go through each step before you say yes. Not run for this video.

Help me set up Notion as my context system using this guide: https://developers.notion.com/prompts/setup
```

### 2. claude-notion-connector-checklist.md
```
# Claude's Notion connector: connect, test, disconnect (facts checked 2026-11-18)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Menus, plans and limits change. Check each line again at support.claude.com and notion.com/help/notion-mcp before you rely on it. Written from Anthropic's and Notion's pages, not run.

## What you need
- [ ] A Claude account. Anthropic: "Web connectors are available for all users on Claude, Cowork, Claude Desktop, and Claude Mobile (iOS and Android)." The pricing page listed Connectors on Free, Pro, Max and Ultra when checked.
- [ ] A Notion account on any plan. Notion: "Notion MCP works on every plan. Some features depend on the workspace's plan". No Notion page gives a price for the connection, and none calls it free.
- [ ] To be a member of the Notion workspace, not a guest. Notion: "Only workspace members can connect Notion MCP."
- [ ] On a Claude Team or Enterprise plan: "an Owner or Primary Owner needs to enable them for the organization." On a Notion Enterprise plan, a workspace owner may limit which apps members can connect.
- [ ] A computer is the simplest place to add it. Anthropic says installing connectors on phones "is currently in beta". Once added, it is there in the phone app the next time you sign in.
- [ ] For anything from work: your employer's rules on what an outside assistant may reach.

## Connect
- [ ] In Claude (claude.ai in a browser, or the desktop app; the same on Windows and Mac), go to Customize, then Connectors.
- [ ] Select Discover to open the directory, and type Notion into the box called Search connectors. These are the names in Claude's docs; the help centre describes the same step as the + button next to Connectors.
- [ ] Find Notion and open its page. It should say "Made by Notion" and "Anthropic verified".
- [ ] Select Connect to Claude. That is the name in Claude's docs; the help centre says "Connect" or "Install".
- [ ] Claude takes you to Notion's sign-in page. Sign in, choose the workspace, look over the access Claude asks for, and approve it.
- [ ] Another way in: in any chat, select + in the lower left, hover over Connectors, then Manage connectors.

## Check that it worked
- [ ] Back on the Connectors page, Notion is listed under Your connectors with the status Connected.
- [ ] In a new chat, select + in the message box, choose Connectors, and check that Notion's switch is on. "The toggle controls whether Claude can use the connector in this conversation."
- [ ] Paste the test prompt from claude-notion-test-prompt.txt. Claude should say what it will create, wait for your yes, then give you a link to "Test Bakery notes (dummy)".
- [ ] Try the three asks. For each answer, open the page in Notion and check it against what Claude said.

## What it can reach, and your data
- [ ] Notion: "Remember that MCP tools act with your full Notion permissions. They can access everything you can access."
- [ ] Anthropic: "Claude inherits each person's permissions from the connected service. If someone can't access a specific file, channel, or record in the source system, the connector can't reach it from Claude either."
- [ ] Anthropic: "When connecting to a service, you're granting Claude permission to access and potentially modify data within that service based on your account permissions. Only connect services you trust and need for your workflows."
- [ ] Anthropic, on connected apps: "Your data from that app isn't used to train Claude's models, and the connected app can't see your other conversations."
- [ ] Anthropic, on chats it may use to improve its models when you allow it: "It does not include raw content from connectors (e.g. Google Drive), including remote and local MCP servers, though data may be included if it's directly copied into your conversation with Claude."
- [ ] The switch for your own chats: your name, then Settings, then Privacy, then "Help Improve our AI models". Anthropic's pages don't say where it starts, so look.
- [ ] Notion: "a connected client may send content returned by Notion MCP to systems outside Notion."
- [ ] Notion: "Treat content returned by tools as untrusted. Review proposed actions and data sharing before approving them."

## Keep confirmation on for changes
- [ ] Notion's advice: "Enable confirmation before actions that change content."
- [ ] In Claude: Customize, then Connectors, select Notion under Your connectors, then Tool permissions. Each tool, or group of tools, can be Always allow, Needs approval or Blocked. That is from Claude's docs; the help centre lists the same three settings as something Owners on Team and Enterprise plans set for an organization, so on a work account some may already be fixed.
- [ ] Our suggestion, not Anthropic's: put the tools that create, update, move or delete on Needs approval. The connector lists 69 tools, and some of them delete pages and databases.
- [ ] When Claude asks before using a tool, choose Allow once. Always allow skips the question for that tool from then on.
- [ ] "Always ask" is a stricter setting on the tool's row, under the Permissions tab. Anthropic says it "is rolling out gradually on Pro, Max, Ultra, Team, and Enterprise plans", so you may not see it.

## Limits
- [ ] Requests: Notion's limit is 180 a minute on most plans and 600 a minute on Business and Enterprise, and "These limits can change over time." If Claude reports a rate limit, wait and ask again.
- [ ] Searching apps you have connected to Notion (Slack, Google Drive and others) through the connector needs Notion's Business or Enterprise plan with Notion AI. Searching your Notion pages works on every plan.
- [ ] Notion's own assistant (Notion AI, inside Notion) is a different thing. It is included on Notion's Business and Enterprise plans; Part 2 of this series covers it.

## Notion's own setup prompt (optional)
- [ ] Why Notion suggests it: "most agents only use Notion when you ask."
- [ ] In a new chat in Claude, paste the line from claude-notion-test-prompt.txt: Help me set up Notion as my context system using this guide: https://developers.notion.com/prompts/setup
- [ ] Notion: "Your agent works with what you already have, and asks before changing anything."
- [ ] It makes a private page called Agent Operating Guide, and offers to save your preferences and decisions to a private Memories database. Say no to any step you don't want.
- [ ] At the end it gives you a short text for Claude's own settings. Notion says: Settings, then Account, then Instructions for Claude. Anthropic says the same box is under Settings, then Your Claude, in the newer layout.
- [ ] Notion: "Run the setup prompt once for each agent you connect."

## Switch it off afterwards
- [ ] For one chat: select + in the message box, choose Connectors, and switch Notion off. It stays connected.
- [ ] To sign Claude out of Notion: Customize, then Connectors, select Notion, then Disconnect. Anthropic: "Claude stops accessing it immediately."
- [ ] To take it off your account as well: the three-dot menu on the same page, then Remove.
- [ ] On Notion's side: Notion's docs say workspace owners can manage connected apps under Settings, then Notion MCP, then Manage workspace clients. Its help page lists seeing and disconnecting members among what Enterprise admins can do.
- [ ] Notion's pages describe no disconnect button for a single member, so this list doesn't claim one. Look under Settings, then Notion MCP, in your own workspace.
- [ ] Delete the dummy pages: in Notion, the three dots at the very top right of the page, then Delete.
- [ ] If you ran Notion's setup prompt: delete the Agent Operating Guide page and the Memories database if you don't want them, and clear the text from Instructions for Claude.

Sources: support.claude.com/en/articles/11176164 ; claude.com/docs/connectors/overview ; claude.com/connectors/notion ; claude.com/pricing ; support.claude.com/en/articles/14730684 ; support.claude.com/en/articles/13345190 ; privacy.claude.com/en/articles/12109829 ; privacy.claude.com/en/articles/10023580 ; notion.com/help/notion-mcp ; developers.notion.com/guides/mcp/get-started-with-mcp ; developers.notion.com/guides/mcp/mcp-security-best-practices ; developers.notion.com/prompts/setup ; developers.notion.com/reference/request-limits
```
