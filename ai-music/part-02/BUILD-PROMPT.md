# Claude build prompt: AI Music Part 2, a lyric-sheet builder

Paste this into Claude Code in an empty folder on your computer. It builds one local web page that lays out your own lyrics as a clean lyric sheet with section labels and checks your style prompt for artist names before you paste it into Suno. It downloads nothing, signs in nowhere, runs no third-party code and makes no audio. Written from Suno's help pages, checked 2026-11-25. Nothing here was run for the video.

Goal: build a single file called lyric-sheet.html that turns my lyrics and style prompt into a tidy lyric sheet I can copy into Suno's Custom mode, and warns me if the style prompt names an artist.
Steps, in order:
1. Create lyric-sheet.html in this folder, plain HTML, CSS and JavaScript in that one file, with no external scripts, fonts or images, and nothing fetched from the internet.
2. Add four boxes: Title, Style prompt, Lyrics, and "Names to block" (one name per line, which I fill in myself with any singers or bands I don't want to mention).
3. Add a "Build sheet" button. When I press it, lay out the lyrics with each label line ([Verse], [Chorus], [Bridge], [Outro] and any other line that starts with "[" and ends with "]") shown as a bold heading, the lyric lines under it, and a blank line between parts.
4. Count the lyric lines (not the labels) and show the count, and show a gentle note if any part has no label above it.
5. Check the style prompt and show a warning if it contains any name from "Names to block" (ignoring capital letters), or the whole phrases "in the style of", "sounds like", "cover of", "feat." or "featuring" (match whole words only, so "feature" or "feather" never trigger it). Also warn if it doesn't mention at least one of these kinds of words: a genre, an instrument, a mood, a voice. Explain each warning in one plain sentence.
6. Add a "Copy lyrics" button and a "Copy style prompt" button that copy exactly what goes into Suno's lyrics box and Styles box.
7. Fill the boxes with this example the first time the page opens, so I can see it working: Title "Bench at Nine"; Style prompt "upbeat indie pop, bright electric guitar, handclaps, steady drums, warm male vocal, hopeful late-night mood"; Lyrics: the ten lines and three labels from lyric-template.txt in this folder if it exists, otherwise leave the Lyrics box empty with a hint to paste my own.
8. Save what I type only in my browser's local storage, and add a "Clear" button. Don't send anything anywhere.
9. Open nothing automatically. When you're done, tell me the file's full path and how to open it by double-clicking it.
Safety: don't download, install or run anything, and don't fetch any web page. Don't add any artist names, song titles or lyrics other than the ones I give you. Don't claim the page can find every artist name: it only checks the names I list and the phrases above.
Output: the path of lyric-sheet.html and a two-line summary of what it does.
