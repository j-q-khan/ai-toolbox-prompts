Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder where you have saved this video's prompt library as photo-edit-prompts.md (from the GitHub folder in the description). It builds one web page from the library: the consent rule at the top, every prompt for editing your own photos grouped by job, a Copy button beside each one and a search box. The page works offline in your browser, loads nothing from the internet and uploads nothing. Written for this video, checked 2026-11-25. Nothing here was run for the video.

Goal: build one self-contained page, photo-edit-prompts.html, that turns photo-edit-prompts.md into a prompt library you can search, copy from and print.
Input: photo-edit-prompts.md in this folder. Read only that file.
Steps, in order:
1. Tell me in two sentences what you will build and which file you will create, then wait for me to say go.
2. Write a single file, photo-edit-prompts.html, with its styling and script inside it. Plain HTML, CSS and JavaScript only: no libraries, no CDN links, no fonts or images from the internet, no build step, nothing to install.
3. Put the library's consent rule at the very top in a box that always stays visible, word for word as written in the file.
4. Copy every heading and every prompt into the page exactly as written. Don't add prompts, steps, limits or claims of your own, and don't reword anything in quotation marks.
5. Show each section of the file (Remove something, Change one part, Light and colour, Ask again, How to use it in ChatGPT, How to use it in Gemini, Not for, Hidden marks on what you make, Sources) under its own heading, in the file's order, and each prompt in its own box.
6. The prompts are the bullet lines under the first four headings (Remove something, Change one part, Light and colour, Ask again). Show every other section as plain text, with no Copy button. Add a Copy button beside every prompt that copies only that prompt's text to the clipboard. If the browser blocks the clipboard, select the prompt's text instead and show the words: Press Ctrl+C, or Cmd+C on a Mac.
7. Add a search box above the prompts that hides every prompt box not containing the typed words (the other sections stay shown), ignoring capitals, and shows them all again when the box is empty. Keep the last search in the browser's local storage only.
8. Add a print style: black text on white, every prompt shown, no buttons and no search box, and the consent rule at the top of the first printed page.
9. Add one line under the consent rule: From the makers' help pages, checked 2026-11-25. Apps change: check the source links before you rely on a step.
10. Add no analytics, tracking or network calls of any kind, and never send or upload anything.
11. Never overwrite a file that already exists: if photo-edit-prompts.html is there, stop and tell me.
12. Then tell me how to open the page by double-clicking it, and how to check it worked: clicking Copy beside the first prompt, pasting into Notepad or TextEdit and seeing that prompt, typing sky in the search box and seeing only the prompts with sky in them.
Safety: read only photo-edit-prompts.md. Don't change, move, rename or delete it or anything else. Don't upload anything or call any website or API.
Output: photo-edit-prompts.html and a three-line note saying what you created.
