Paste this into Claude Code, Anthropic's coding assistant, opened in a new folder that holds only a copy of a small test vault (Markdown notes, no private notes). It opens only the Markdown notes in that folder, makes one new page beside them, and asks before every change. Written from Anthropic's and Obsidian's help pages, not run.

Goal: make me a "vault map" page that lists every note in this test vault and the links between them, so I can check nothing is broken before and after I let Claude Cowork work in my vault.
Rules:
1. Open only the Markdown notes (files ending in .md) in this folder and its subfolders. Don't open the .obsidian folder or any other file, don't change, rename, move or delete anything, don't install anything, and don't go online.
2. Before you write anything, show me your plan in three lines and wait for my OK.
3. Make one new file beside the notes, vault-map.html: a single HTML page with no scripts and no links to other sites.
4. List every note by its name, in alphabetical order. Under each one, list the notes it links to. An internal link is a note's name inside two square brackets, like [[Note name]]; ignore anything after a vertical bar or a hash sign inside the brackets, and match on the part after the last slash, when you match names.
5. Mark any link whose note doesn't exist in this folder as "Missing note", in bold, and put a count of missing notes at the top of the page.
6. Keep the line "Facts checked 2026-11-22 from Anthropic's and Obsidian's help pages" at the top, and add a footer: "Run this again after Claude works in your vault, and compare the counts."
7. Use large, high-contrast text, no images and no logos.
8. Ask me before every file change, and change nothing else.
9. When it's done, tell me how to open the page in my browser.
Output: vault-map.html, and a one-line summary of what you made.
