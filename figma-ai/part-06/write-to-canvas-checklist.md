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
