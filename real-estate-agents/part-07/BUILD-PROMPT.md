# Claude build prompt: AI Tools for Real Estate Photography (Part 7 of 10)

**What you need:** Claude Code on a paid Claude plan (Pro or higher, at the time of checking), a test folder, and made-up test data. Never use real client details. Claude should ask you before it changes anything.

From the AI for Real Estate Agents series. Use test data only, never real client data. Claude should ask before it changes anything.

Goal: blend bracketed listing photos with OpenCV exposure fusion, then have Claude audit each edited photo into a CSV I check by hand.
Inputs: a new test folder with brackets/ (camera JPEGs, three or five frames per shot) and edited/ (final photos named like their originals).
Steps, in order:
1. Set up a Python virtual environment with opencv-python, Pillow and anthropic.
2. Group the frames in brackets/ into sets by EXIF capture time and exposure value. Show me the sets and wait for my yes.
3. Per set: cv2.createAlignMTB, then cv2.createMergeMertens, multiply by 255, clip to 0 to 255, save an 8-bit JPEG to blended/ plus a side-by-side preview.
4. Per pair in edited/, send original and edit to claude-haiku-5-5 and ask for JSON only: file, changes, property_changed (true or false), reason. Validate it.
5. Write edit_audit.csv, one row per photo, property_changed true rows first. Add a Message Batches API option at half price.
Safety rails: dummy photos or a home I own, with no faces, mail or house numbers. Never overwrite or delete originals; write only to blended/ and edit_audit.csv. Show the cost first. Stop and ask me before running anything that changes data.
Output: blended JPEGs, previews, edit_audit.csv and a README.
