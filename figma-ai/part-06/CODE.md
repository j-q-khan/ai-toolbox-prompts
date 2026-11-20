# Full code: Figma MCP Write to Canvas: Send Code Back into Figma with Claude Code

The copy-paste prompt for Claude Code, two short prompts, the two settings files, the server lines and a safety checklist, written from Figma's help, developer and pricing pages and Anthropic's Claude Code docs (checked 2026-11-19). They were written from the docs, not run for this video.

### 1. code-to-figma-prompts.txt
```
# PROMPT 1 goes into Claude Code (in a terminal, in the folder of a copy of your app or a throwaway branch), not into Figma Make or the Figma agent.
# Copy all of it, swap the words in square brackets, and send it. It checks your setup and asks three questions first.
# It installs nothing, captures one page into a new file in your drafts, then waits for your link before it changes anything.
# Writing to the canvas is free during Figma's beta and will become a usage-based paid feature (checked 2026-11-19).
# The calls that look at your file count toward your seat's limit (View and Collab seats and the Starter plan: 20 a month, checked 2026-11-19).
# Written from Figma's pages, checked 2026-11-19, not run. Check every change in Figma before you keep it.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste.

# PROMPT 1: capture one page, then rebuild it with your library (the one in the video)
Goal: bring one small page of my test app into a new Figma file in my drafts with Figma's code to canvas, then rebuild it with my team's components and variables using write to canvas. Made-up data only.
Before you start, check these and tell me what you found:
1. Figma's remote server is connected in this session and lists the tools generate_figma_design and use_figma. If they're missing, stop and tell me why that may be: the server may have been added only in another folder (claude mcp add adds it to the current folder by default), or a desktop server at http://127.0.0.1:3845/mcp may be hiding the remote-only tools, as Figma says. Point me to https://youtu.be/ah5iCrbRZcE and https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/ . Don't install, add or remove MCP servers or plugins, and don't change settings files, yourself.
2. This folder is a copy of my app or a throwaway git branch, with made-up data only. If it isn't, stop and ask me.
3. Ask me these three questions one at a time, and wait for each answer: (a) which page to capture ([the page, for example the pricing page]); (b) the exact name of my team's library ([your library name]); (c) my Figma plan and seat (Starter, Professional, Education, Organization or Enterprise; Full or Dev). If I'm on Starter, tell me I can capture but can't write to the canvas, then do step 1 only.
Step 1, capture: start a local server for my app and capture only that page in a new Figma file in my drafts, using generate_figma_design. Tell me before you add the capture script to my app, and list every file you change. Then give me the new file's link and stop.
Step 2, wait: I'll right-click the captured frame in Figma, choose Copy link to selection, and paste the link here: [link to the captured frame].
Step 3, refine: using that selection and use_figma, look at the file first, then replace the captured buttons and colours with components and variables from the [your library name] library. Work in small steps, and change nothing else. Don't write to any file outside my drafts without asking me first. Don't generate images, vector illustrations or Figma Make prompts, because they use Figma AI credits.
Step 4, report: list what you changed, any layer you couldn't match to a library component or variable, and any placeholder image or missing font.
Stop and tell me what it said if a rate limit or permission message appears.
Rules: never ask me for a password, a payment detail or any personal data. Don't open client or personal files. Don't remove the capture script from my app unless I ask. If anything is unclear, ask me first.
Reminder for me: writing to the canvas is free during Figma's beta and will become a usage-based paid feature, and the calls that look at my file count toward my seat's limit. Check every change in Figma before I keep it.

# PROMPT 2: one more refinement (Claude Code, same chat, after prompt 1)
Using this selection: [link to a layer in the captured file], also replace the remaining text styles with styles from the [your library name] library. Change nothing else, and tell me what you changed.

# PROMPT 3: the shortcut from the video: capture into a draft file that already has your library (Claude Code, in your test app's folder)
Start a local server for my app and capture [the page, for example the pricing page] in [link to your draft file], so Figma can bind my library's matching variables. Tell me before you add the capture script, and list every file you change.
```

### 2. claude-code/settings.json
```
{
  "permissions": {
    "ask": ["mcp__figma__*"],
    "deny": [
      "mcp__figma__generate_image",
      "mcp__figma__generate_vector_illustration",
      "mcp__figma__send_prompt",
      "mcp__figma__send_code_to_figma",
      "mcp__figma__html_to_figma",
      "mcp__figma__upload_assets",
      "mcp__figma__generate_diagram",
      "mcp__figma__add_code_connect_map",
      "mcp__figma__send_code_connect_mappings",
      "mcp__figma__create_generative_plugin",
      "mcp__figma__update_generative_plugin",
      "mcp__figma__create_shader",
      "mcp__figma__update_shader"
    ]
  }
}
```

### 3. claude-code/settings.plugin.json
```
{
  "permissions": {
    "ask": ["mcp__plugin_figma_figma__*"],
    "deny": [
      "mcp__plugin_figma_figma__generate_image",
      "mcp__plugin_figma_figma__generate_vector_illustration",
      "mcp__plugin_figma_figma__send_prompt",
      "mcp__plugin_figma_figma__send_code_to_figma",
      "mcp__plugin_figma_figma__html_to_figma",
      "mcp__plugin_figma_figma__upload_assets",
      "mcp__plugin_figma_figma__generate_diagram",
      "mcp__plugin_figma_figma__add_code_connect_map",
      "mcp__plugin_figma_figma__send_code_connect_mappings",
      "mcp__plugin_figma_figma__create_generative_plugin",
      "mcp__plugin_figma_figma__update_generative_plugin",
      "mcp__plugin_figma_figma__create_shader",
      "mcp__plugin_figma_figma__update_shader"
    ]
  }
}
```

### 4. figma-server-lines.txt
```
# Type these in your terminal (PowerShell on Windows, Terminal on a Mac), in your test app's folder, not inside Claude Code.
# From Figma's setup and code to canvas pages, checked 2026-11-19.
# 1. Add Figma's remote server here. By default Claude Code adds it to the current folder only,
#    so if you followed our setup video in another folder, add it again here.
#    To use it in every folder, put --scope user after "add".
claude mcp add --transport http figma https://mcp.figma.com/mcp
# Then start Claude Code, type /mcp, pick figma, choose Authenticate and click Allow access in the browser.
# Or instead, Figma's recommended plugin, which includes Figma's skills (then use settings.plugin.json):
#    claude plugin install figma@claude-plugins-official
# 2. If Claude Code can't find generate_figma_design or use_figma, the desktop server is usually answering instead.
#    The first line lists your servers. If one points at http://127.0.0.1:3845/mcp, remove it with the second
#    (use the name the list shows, if it isn't figma-desktop). Then restart Claude Code.
claude mcp list
claude mcp remove figma-desktop
```

### 5. write-to-canvas-checklist.md
```
# Code back into Figma: safety checklist (facts checked 2026-11-19, from Figma's and Anthropic's own pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What you need
- [ ] Claude Code installed (new to it? https://youtu.be/w3s56HTHDUk).
- [ ] Figma's remote server connected in your test app's folder (figma-server-lines.txt; walkthrough: https://youtu.be/ah5iCrbRZcE). claude mcp add adds it to the current folder only; add --scope user for every folder. Figma recommends its Claude Code plugin for writing, because it includes Figma's skills: claude plugin install figma@claude-plugins-official . The manual line doesn't install the skills.
- [ ] To capture (code to canvas): any plan, including Starter.
- [ ] To write (write to canvas): Professional, Education, Organization or Enterprise, and edit access to the file. A Full seat writes outside your drafts; a Dev seat writes only in your drafts.
- [ ] A copy of your app, or a throwaway git branch, with made-up data only.

## Before the first run
- [ ] Followed MCP Servers Part 5? It added the server to that one test folder, and its settings file there blocks generate_figma_design and use_figma. In your test app's folder, add the server again, then save claude-code/settings.json from this folder as .claude/settings.json (if you installed the plugin, save settings.plugin.json there under the name settings.json instead).
- [ ] Your app already has a .claude/settings.json? Don't replace it: add the ask line and the deny lines from ours to its "permissions" section, and keep its other rules.
- [ ] The new file asks before every Figma call, even in auto mode, and blocks the tools that spend Figma AI credits (generate_image, generate_vector_illustration, send_prompt) and writes this flow doesn't need.
- [ ] Never choose "don't ask again" for a Figma write.
- [ ] Ask your admin how the Content training setting is set before you capture work screens (on by default for Starter and Professional teams).
- [ ] On Organization and Enterprise plans, your admin may need to approve Claude Code again when it first asks to write.

## Capture (code to canvas)
- [ ] Paste prompt 1 into Claude Code in your test app's folder.
- [ ] Claude tells you before it adds the capture script and lists the files it changes. It starts your app, a browser window opens, and the first capture happens on its own.
- [ ] Toolbar: Entire screen captures the full view; Select element captures one part; Open file opens the new file (it lands in your drafts).
- [ ] Bonus: add your library to a draft file and capture into it (prompt 3), and Figma binds matching colour, number and string variables for you.

## Refine (write to canvas)
- [ ] In Figma, right-click the captured frame, Copy link to selection, paste it into Claude Code with your library's exact name.
- [ ] Say yes to each use_figma call you expect, no to anything else.
- [ ] Work in small steps; name the library, components and variables to use.

## Check it worked
- [ ] Open the file and compare it with your running app: spacing, fonts, colours.
- [ ] Buttons are instances of your library's components; colours use your variables.
- [ ] Look for gray boxes (use_figma can't add new images on its own) and missing fonts (fonts must be uploaded to your Figma account).
- [ ] Output is beta quality: review and clean up before you share it.

## If something goes wrong
- [ ] Tools missing: check the server was added in this folder, then run the last two lines of figma-server-lines.txt (the desktop server at http://127.0.0.1:3845/mcp can hide them), then restart Claude Code.
- [ ] Rate limit message: tool calls that pull data count. View and Collab seats and the Starter plan: up to 20 a month. Full and Dev seats: Professional and Education 200 a day (10 a minute), Organization 200 a day (15 a minute), Enterprise 600 a day (20 a minute). Tools that write are exempt. Figma may change them.

## Afterwards
- [ ] Remove the capture script Claude added to your app (or delete the throwaway branch).
- [ ] Delete the test file from your drafts if you don't need it.
- [ ] Writing to the canvas is free during the beta and will become a usage-based paid feature: check Figma's page before you rely on it.

Prices as of 19 November 2026 (Professional, billed yearly): Full seat 16 USD a month, Dev seat 12 USD a month. https://www.figma.com/pricing/

Sources: help.figma.com/hc/en-us/articles/42495251338775 ; /42495237955095 ; /39252411778583 ; /17725942479127 ; developers.figma.com/docs/figma-mcp-server/tools-and-prompts/ ; /rate-limits-access/ ; /remote-server-installation/ ; code.claude.com/docs/en/permission-modes ; code.claude.com/docs/en/permissions
```
