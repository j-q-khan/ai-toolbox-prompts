# Figma to code: route-picker checklist (facts checked 2026-11-19, from Figma's own pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Pick your route
- [ ] I don't write code and want something clickable to share today: Figma Make.
- [ ] A developer builds from my designs: Dev Mode.
- [ ] I already have a codebase and Claude Code or Codex: the Figma MCP server.

## Route 1: Figma Make (a prompt-to-app tool)
- [ ] Plans: Starter, Professional, Education (not K-12), Organization, Government, Enterprise.
- [ ] See and edit the code: the Files tab. Download it: File actions, then Download code (a zip). Needs a Full or Dev seat.
- [ ] Publish with its own link: on paid plans, a Full seat. On Starter, you also publish the file to the Figma Community.
- [ ] Credits: an app from scratch was about 100+ credits (rates as of 19 November 2026).
- [ ] GitHub, option A: push to a repository Make creates (one way, default branch only).
- [ ] GitHub, option B: once a Figma admin connects GitHub, clone a team web app (Clone from GitHub), work on branches, open pull requests.
- [ ] Make in your local codebase: closed beta, limited users, the Figma Beta desktop app for Mac; free during the beta.

## Route 2: Dev Mode (a developer-focused workspace)
- [ ] Plans: Professional, Education, Organization, Government, Enterprise. Not Starter.
- [ ] Open a design file, click the Dev Mode toggle in the toolbar, or press Shift + D.
- [ ] Code snippets in the Inspect panel need a Full or Dev seat: CSS (web), SwiftUI or UIKit (iOS), Compose or XML (Android).
- [ ] Mark frames, components or sections as ready for dev so developers know what's finished.
- [ ] Code Connect links your design components to your code components (Full or Dev seat; Professional: one active library and one framework).
- [ ] Developers in Visual Studio Code: install Figma for VS Code; in Dev Mode, set CSS as the language, click a top-level frame, Options next to its name, then Open in VS Code.

## Route 3: Figma MCP server with a coding agent
- [ ] A coding agent already set up (Claude Code or Codex). Setup: https://youtu.be/ah5iCrbRZcE and https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/
- [ ] Remote server (recommended): paste a link to one frame in your prompt. The desktop server needs a Dev or Full seat on a paid plan.
- [ ] Tool calls that pull data from Figma: View and Collab seats up to 20 a month (every plan), and the Starter plan up to 20 a month; Full and Dev seats: Professional and Education 200 a day (10 a minute), Organization 200 a day (15 a minute), Enterprise 600 a day (20 a minute). Figma may change them.
- [ ] Output is React and Tailwind unless you name another framework in your prompt.
- [ ] Code Connect helps the agent reuse your real components.
- [ ] Use prompt 1 (route picker), then prompt 2 (look at one frame) before asking for code.

## Check it worked
- [ ] Put the result next to the frame in Figma and compare spacing, fonts and colours.
- [ ] Look for raw colour values where your variables should be.
- [ ] Every route still needs a person to check the code: none hands you finished code.

## Afterwards
- [ ] Work in a test copy of your file, and delete it if you don't need it.
- [ ] Ask your admin how the Content training setting is set before you use work files.

Prices as of 19 November 2026 (Professional, billed yearly): Full seat 16 USD a month, Dev seat 12 USD a month. https://www.figma.com/pricing/

Sources: help.figma.com/hc/en-us/articles/33649966245783 ; /31304586129559 ; /44220165255063 ; /40775535020695 ; /35463818346647 ; /15023124644247 ; /15023202277399 ; /23920389749655 ; /15023121296151 ; /33459875669015 ; developers.figma.com/docs/figma-mcp-server/rate-limits-access/ ; /tools-and-prompts/ ; /mcp-vs-agent/ ; /remote-server-installation/
