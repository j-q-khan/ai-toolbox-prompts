Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only test-transcript.txt from this video's files (or a transcript of your own, exported as plain text). It builds a small Python script that turns a transcript into a chapter list and caption-ready lines. It reads only the file you name, writes two new files beside it, and changes nothing else. Written for this video, checked 2026-11-19. Nothing here was run for the video.

Goal: write one Python script, make_chapters.py, that reads a plain-text transcript and writes a chapter list and caption-ready lines next to it.
Input: a transcript file I name on the command line, for example python make_chapters.py test-transcript.txt. Each line may start with a timestamp in square brackets, like [00:01:05], followed by the words spoken. Lines without a timestamp belong to the line above. Skip blank lines and lines starting with #. NAME below means the input file's name without .txt.
Steps, in order:
1. Tell me in two sentences what the script will do and which two files it will create, then wait for me to say go.
2. Use only Python's standard library. No installs, no internet, no other files read.
3. Chapters: start a new chapter at the first line and then whenever the words after a line's timestamp begin with the word Chapter, or when three minutes have passed since the last chapter started. Title each chapter with its first five words. Write them to NAME-chapters.txt as one line each, timestamp first, like 00:00 Welcome to the test kitchen, so they can be pasted into a video description. The first chapter must start at 00:00.
4. Captions: split the spoken words into lines of at most 32 characters, breaking only between words, never more than two lines per caption, and write them to NAME-captions.txt, one caption per block with a blank line between blocks. Keep each caption's starting timestamp above it.
5. Never overwrite a file that already exists: if either output file is there, stop and tell me.
6. If the input has no timestamps at all, still write the caption file, write the chapter file with a single 00:00 line, and print a warning.
7. Then run it once on test-transcript.txt and show me the first ten lines of each new file.
Safety: read only the file I name. Don't change, move or delete it or anything else. Don't upload anything or call any website or API.
Output: make_chapters.py, the two new files, and a three-line note saying what you created.
