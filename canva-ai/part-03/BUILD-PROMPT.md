Paste this into Claude Code, started in an empty scratch folder, after /mcp shows the Canva connector. It makes Claude list the Canva tools it can see and find one design, and it resizes nothing and changes nothing until you agree. Written from Anthropic's docs and Canva's developer docs, checked 2026-11-17. Nothing here was run for the video.

Goal: show me what the Canva connector can do from this Claude Code session, without changing anything in my Canva account.
Steps, in order:
1. Tell me in one sentence whether you can see a Canva server in this session. If you can't, stop and tell me to type /mcp to see the list, then /status to see which login is active, and to add the Canva connector on claude.ai under Customize, then Connectors, if it isn't there. Don't add a server yourself and don't suggest a claude mcp add command.
2. List every Canva tool you can see, in a table: the tool's name, one line on what it does, and whether it only looks things up or can create or change something.
3. Mark the tools that can create, change, resize, move, comment on or delete something. Don't call any of them.
4. Ask me for a word from the title of one design. When I answer, search my designs for it and show me only the title and the link of the first match. Don't open other designs.
5. Stop and ask me what I'd like to do next. Offer three choices: nothing, a list of the formats that design can be downloaded in, or a resized copy. Do nothing until I pick one.
6. If I pick the resized copy, first tell me the size you'll use and that Canva's docs say resizing makes a copy and leaves the original unchanged, and that it's marked Pro and above with a limited trial on the Free plan. Wait for me to type yes.
Safety: don't create, change, resize, move, comment on, export or delete anything until I agree to that exact step. Don't use autofill or Brand Templates. Don't write any file in this folder. If Canva returns an error, show me the error's name and stop. Don't retry in a loop: Canva's docs set a rate limit for each tool, and a default cap counted across all of my apps.
Output: the one-sentence answer, the table of tools, the one design's title and link, then your question.
