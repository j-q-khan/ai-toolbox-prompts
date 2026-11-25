# Claude build prompt: AI Music Part 1, a free-plan comparison page

Paste this into Claude Code in an empty folder on your computer. It builds one local web page, a dated comparison table of free A.I. music plans in each maker's own words, with a link to every source. It uses only the facts written below, downloads nothing, signs in nowhere, runs no third-party code and makes no audio. Written from the makers' pages, checked 2026-11-25. Nothing here was run for the video.

Goal: build a single file called free-music-plans.html that shows a comparison table of free A.I. music plans, so I can check them again later.
Steps, in order:
1. Create free-music-plans.html in this folder, plain HTML and CSS only, no external scripts, fonts or images, and nothing fetched from the internet.
2. Add a table with these columns: Tool, What it is, Free credits or limits, Downloads on the free plan, Commercial use on the free plan, Who owns the song, Source link, Checked on.
3. Fill one row per tool with exactly these facts, quoted where they are in quotation marks, all checked on 2026-11-25:
   - Suno: an app that writes and sings a whole song from your words. "50 song credits per day". "No monthly song downloads"; trial downloads "are not eligible for commercial use". "No commercial rights". "If you make music with the Basic (free) plan, Suno is the owner of the songs." Sources: https://suno.com/pricing and https://help.suno.com/en/articles/2746945
   - Udio: another app that makes songs from a prompt. Free credits: not quoted (pricing page did not load). "downloading of audio, video, and stems has been disabled". Commercial use: not stated on a page we could read. Ownership: not stated on a page we could read. Source: https://help.udio.com/articles/12683565-changes-associated-with-the-universal-music-group-umg-partnership
   - Gemini with Lyria: Google's chat app and its music model. "There are limits for how many tracks you can create with Lyria." Download as MP4 with cover art or MP3. Commercial use: no clause found, check Google's terms. "Google won't claim ownership over that content." Sources: https://support.google.com/gemini/answer/16901237 and https://policies.google.com/terms
   - ACE-Step 1.5: an open-source music model you run on your own computer. Limits: your own hardware, "less than 4GB of VRAM" (the README's headline figure; its XL models need 12GB or more). Downloads: the files are made on your computer. Commercial use: code is MIT; the model files' licence is not stated on the README, so check it. Ownership: not stated. Source: https://github.com/ace-step/ACE-Step-1.5
4. Under the table, add a note in plain words: prices and plans change, so open each source link before relying on a row, and this is not legal advice.
5. Add a small form at the bottom that lets me add a new row in the page (tool, fact, source link, date) and keeps it only in my browser's local storage. Don't send anything anywhere.
6. Open nothing automatically. When you're done, tell me the file's full path and how to open it by double-clicking it.
Safety: use only the facts above; don't invent prices, limits or rights for any tool. Don't download, install or run anything, and don't fetch any web page. Don't add any artist names, song titles or lyrics other than the ones I give you.
Output: the path of free-music-plans.html and a two-line summary of what's in it.
