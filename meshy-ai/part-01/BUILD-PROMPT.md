# Claude build prompt: Meshy AI Tutorial for Beginners: Photo to 3D Model with Meshy 7.1

An offline photo checker for Claude Code: it tells you, before you spend Meshy credits, whether each photo in a folder meets Meshy's Image to 3D upload rules (type, size, pixels, HEIC; a small photo gets a warning). Checked against Meshy's docs on 2026-11-07. Not run by us. It never calls Meshy or uses a key.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small, offline photo checker that tells me, before I spend Meshy credits, whether each photo in a folder meets Meshy's Image to 3D upload rules, and what to fix.
Inputs: every file in a folder called photos next to the script. If the folder is empty or missing, create it and make three test files in it with Python's standard library only: a valid 600 x 600 PNG, a 300 x 200 PNG, and an empty file renamed photo.heic.
Rules to check, from Meshy's docs (checked 2026-11-07; re-check https://docs.meshy.ai/en/webapp/image-to-3d before you trust them):
- file type is PNG, JPG, JPEG or WEBP, judged by the file's first bytes, not only its name
- file size is 20 MB or less
- the shorter side is at least 512 pixels, which Meshy's docs say gives the best result; a smaller photo gets WARN, not FIX, because it may still upload (read the size from the PNG, JPEG or WEBP header with the standard library, no Pillow)
- HEIC or HEIF files are flagged with the fix: export a JPG copy first
Steps, in order:
1. Tell me which files you'll create and wait for my yes. Use Python 3 and the standard library only. Install nothing, make no network calls, and never call Meshy's API or use any key.
2. Write check_photos.py. For each file, print one line: the name, PASS, WARN or FIX, and the reason in plain words.
3. Add a written reminder at the end of the output, as plain text, not checks: plain background, soft even light, the whole subject in the frame, only one subject, step back and zoom rather than holding the phone right up to it, and every part you want visible in the photo.
4. Run it on the test files and show me the output. Then explain how to run it on my own folder.
Safety: this folder only. Never move, change or delete my photos; the script only looks at them. Stop and ask me before doing anything not listed here.
Output: check_photos.py, the test folder, and a three-line summary.
