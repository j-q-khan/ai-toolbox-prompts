Paste this into Claude Code in an empty folder on your computer. It builds one local web page that splits a voiceover script into chunks under a character limit and flags the things ElevenLabs' docs say are hard for a voice to say. It works only on text you paste in, downloads nothing, signs in nowhere, runs no third-party code, uses no A.P.I. key and makes no audio. Written from ElevenLabs' Text to Speech guide, checked 2026-11-26. Nothing here was run for the video.

Goal: build a single file called script-splitter.html that I open by double-clicking. I paste a voiceover script into it, and it splits the script into chunks under a character limit and flags words and marks that a text to speech voice may say badly, so I can fix them before I generate anything.
Steps, in order:
1. Create script-splitter.html in this folder: plain HTML, CSS and JavaScript in that one file, no external scripts, fonts, images or libraries, and nothing fetched from the internet.
2. Add a large text box for the script, a number box called Character limit with 5000 as its default and a note under it: "ElevenLabs' website: up to 100,000 characters per generation with Eleven v4, up to 5,000 with every other model (checked 2026-11-26)". Add a button called Split and check.
3. Splitting: count characters the way the note says (letters, spaces and punctuation all count). Split the script into chunks no longer than the limit, breaking only at the end of a sentence (a full stop, question mark or exclamation mark followed by a space or a line break). If one sentence is longer than the limit on its own, break it at the last comma before the limit, and mark that chunk "split mid-sentence, check it". Show each chunk in its own box with its number, its character count and a Copy button that copies just that chunk.
4. Checking: under the chunks, list every flag with the chunk number and the words around it, for these cases, which come from ElevenLabs' Text to Speech guide:
   - digits (the guide says to avoid writing numbers as digits): suggest writing the number out as words
   - symbols such as the ampersand, percent sign, at sign, hash, slash, plus sign and currency signs: suggest the word instead ("and", "percent", "at", "dollars")
   - emojis (the guide says emojis are particularly difficult for the AI to interpret correctly): suggest removing them
   - words in capitals of two to six letters, which may be abbreviations: suggest spelling them the way they should sound
   - any word in my own list of hard words (see step 5)
5. Add a small box called My hard words, one word per line, for names and words I know the voice gets wrong, and keep that list only in this browser's local storage so it's still there next time. Don't send it anywhere.
6. Add a Clear button that empties the script box and the results, but not My hard words.
7. Keep the page readable: large text, high contrast, and it should work on a laptop screen without sideways scrolling.
8. Open nothing automatically. When you're done, tell me the file's full path and that I open it by double-clicking it.
Safety: use only the text I paste in. Don't download, install or run anything, don't fetch any web page, don't call any A.P.I., don't generate audio, and don't send my script or my word list anywhere.
Output: the path of script-splitter.html and a two-line summary of what it checks.
