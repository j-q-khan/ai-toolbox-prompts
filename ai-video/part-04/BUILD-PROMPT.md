Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only shots.csv from this video's files (or your own file in the same shape). It builds a small Python script that turns each row of your shot list into a Kling text to video prompt, a first-frame prompt and a settings line, using the rules from this video. It reads only the file you name, writes one new file beside it, calls no video service or website, and changes nothing else. Written for this video, checked 2026-11-23. Nothing here was run for the video.

Goal: write one Python script, kling_sheet.py, that reads my shot list and writes a Kling prompt and settings sheet next to it.
Input: one file I name on the command line, for example python kling_sheet.py shots.csv. It is comma-separated with a header row. Skip blank lines and lines starting with #. NAME below means the file's name without .csv.
shots.csv columns: product, setting, what_moves, camera, light, sound, shape, seconds. shape is tall or wide. seconds is a whole number from 3 to 30. sound may be empty.
Steps, in order:
1. Tell me in two sentences what the script will do and which file it will create, then wait for me to say go.
2. Use only Python's standard library. No installs, no internet, no other files read, no calls to any video or AI service or website.
3. Check every row first. If a column is missing, shape isn't tall or wide, or seconds isn't a whole number from 3 to 30, stop and list each bad row with its line number, and write nothing.
4. For each row, write a text to video prompt in this order: the product and the setting, what moves, the camera, the light, the sound if there is one, then end with: one continuous shot, no cuts, no subtitles, no background music. If sound is filled in, leave out "no background music" only when sound names music.
5. For each row, write a first-frame prompt: Use @Image1 as the first frame. Then what moves, the camera and the sound if there is one, ending with: one continuous shot, no cuts, no subtitles, no background music. Never describe the product or the setting again in this prompt.
6. For each row, write a settings line: Duration: the seconds, and if it is over 5, add "test at 5 first". Aspect ratio: 9:16 if shape is tall, 16:9 if wide. Resolution: test at 720p. Sound: on by default, no toggle.
7. Flag any prompt that uses one of these vague words: premium, cinematic feel, vintage feel, beautiful, stunning, high quality. Write the flag under that row as: vague word found, describe what the camera should see instead.
8. Write all of it to NAME-kling-sheet.txt: one block per row (the product, the text to video prompt, the first-frame prompt, the settings line, any flag), then one line saying the sheet uses only what is in the file, and that Kling's screen and settings can change, so check them on the day.
9. Never overwrite a file that already exists: if NAME-kling-sheet.txt is there, stop and tell me.
10. Then run it once on the file I named and show me the sheet.
Safety: read only the file I name. Don't change, move or delete it or anything else. Don't call any website or API.
Output: kling_sheet.py, the new sheet file, and a three-line note saying what you created.
