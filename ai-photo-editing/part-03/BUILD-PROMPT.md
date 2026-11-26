Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder where you have saved this video's table as free-ai-photo-editors.md (from the GitHub folder in the description). It builds one web page from the table: each AI photo editor, what its maker says you get without paying, in the maker's own words, the limits, the date it was checked and the source link, with a filter by device. The page works offline in your browser, loads nothing from the internet and uploads nothing. Written for this video, checked 2026-11-25. Nothing here was run for the video.

Goal: build one self-contained page, free-ai-photo-editors.html, that turns free-ai-photo-editors.md into a clean, dated comparison table you can filter and print.
Input: free-ai-photo-editors.md in this folder. Read only that file.
Steps, in order:
1. Tell me in two sentences what you will build and which file you will create, then wait for me to say go.
2. Write a single file, free-ai-photo-editors.html, with its styling and script inside it. Plain HTML, CSS and JavaScript only: no libraries, no CDN links, no fonts or images from the internet, no build step, nothing to install.
3. Copy every row of the table into the page exactly as written: keep every quote mark, every date and every link. Don't add tools, prices, limits or claims of your own, and don't reword any maker's quoted words.
4. Show the table with these columns, in this order: Tool, Device, What the maker says you get without paying, Limits and needs, Checked, Source. Make each source a link that opens in a new tab.
5. Add four buttons above the table, Phone, Web, Computer and All. Phone, Web and Computer each show only the rows whose Device cell contains that word (so a row marked Phone and web shows under both), and All shows every row. Keep the choice in the browser's local storage only.
6. Add a print style: black text on white, the full table, no buttons, and the line from step 7 at the top of every printed page.
7. Add one line at the top: Makers' own words, checked 2026-11-25. Plans, limits and prices change: check each source link before you rely on it.
8. Add no analytics, tracking or network calls of any kind, and never send or upload anything.
9. Never overwrite a file that already exists: if free-ai-photo-editors.html is there, stop and tell me.
10. Then tell me how to open the page by double-clicking it, and how to check it worked: clicking Phone, seeing the ChatGPT and Gemini rows still there, refreshing the page, and seeing the same rows still shown.
Safety: read only free-ai-photo-editors.md. Don't change, move, rename or delete it or anything else. Don't upload anything or call any website or API.
Output: free-ai-photo-editors.html and a three-line note saying what you created.
