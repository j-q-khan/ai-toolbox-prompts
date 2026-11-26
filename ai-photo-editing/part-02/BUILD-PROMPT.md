Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder where you have saved this video's checklist as photoshop-ai-checklist.md (from the GitHub folder in the description). It builds one printable web page from the checklist: the Generative Fill steps, what each tool costs in credits, the greyed-out fixes as tick boxes, and a short prompt sheet. The page works offline in your browser, loads nothing from the internet and uploads nothing. Written for this video, checked 2026-11-25. Nothing here was run for the video.

Goal: build one self-contained page, photoshop-ai-checklist.html, that turns photoshop-ai-checklist.md into a clean printable checklist with real tick boxes.
Input: photoshop-ai-checklist.md in this folder. Read only that file.
Steps, in order:
1. Tell me in two sentences what you will build and which file you will create, then wait for me to say go.
2. Write a single file, photoshop-ai-checklist.html, with its styling and script inside it. Plain HTML, CSS and JavaScript only: no libraries, no CDN links, no fonts or images from the internet, no build step, nothing to install.
3. Copy the checklist's text into the page exactly as written: keep every heading, every step, every quote mark and every date. Don't add facts, prices or steps of your own, and don't reword Adobe's quoted lines.
4. Turn each line that starts with a box into a real checkbox with its text as the label, at least 18 pixels, and keep the ticks in the browser's local storage only, with a button labelled Clear ticks that clears them.
5. Show the prompt sheet section as a plain table with two columns, Prompt and Use it for, in a monospace font.
6. Add a print style: black text on white, one column, no buttons, page breaks before each main heading, and the date line from the checklist at the top of every printed page.
7. Add one line at the top: Facts from Adobe's own pages, checked 2026-11-25. Menus and credit costs change: check the links before you rely on them.
8. Add no analytics, tracking or network calls of any kind, and never send or upload anything.
9. Never overwrite a file that already exists: if photoshop-ai-checklist.html is there, stop and tell me.
10. Then tell me how to open the page by double-clicking it, and how to check it worked: ticking a box, refreshing the page, and seeing the tick stay.
Safety: read only photoshop-ai-checklist.md. Don't change, move, rename or delete it or anything else. Don't upload anything or call any website or API.
Output: photoshop-ai-checklist.html and a three-line note saying what you created.
