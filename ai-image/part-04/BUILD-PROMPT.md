Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder. It builds one local web page, check-an-image.html, a printable checklist for telling whether a picture is AI: the three checks in order, with links to the makers' own checkers and their own words about what each check can and can't tell you. The page checks nothing itself: it opens no image, uploads nothing and calls no service. It uses only the facts written below and needs no internet to work. Written for this video, checked 2026-11-26. Nothing here was run for the video.

Goal: write one file, check-an-image.html, a plain HTML page with a little JavaScript and no outside libraries, that I can print, with three sections of checks to tick and the makers' links, so I can work through a picture I'm unsure about.
Steps, in order:
1. Tell me in two sentences what the page will do and which file you will create, then wait for me to say go.
2. Use only plain HTML, CSS and JavaScript in one file. No installs, no downloads, no fonts or scripts from the internet, no calls to any website or AI service, no file picker and no image upload. Links in the page are for me to click; the page never fetches them.
3. At the top, a heading, Is this picture AI? Check in this order, and one line: No single check proves it. A label can be lost, a hidden mark only shows who adds it, and a detector only guesses.
4. Then a section headed 1. Look for the label (Content Credentials), with these tick boxes and notes:
   I checked the original file, not a screenshot, cropped or converted copy. (OpenAI: Content Credentials "can be lost through everyday actions, such as taking a screenshot or converting a file".)
   I checked it with OpenAI's verify page: https://openai.com/verify ("checks whether an uploaded file contains provenance signals associated with OpenAI tools")
   On my phone, Google Photos: open the picture, tap More, then About, and scroll to How this was made. (Android and iPhone app; not on the web.)
   On Facebook or Instagram, I looked for Meta's AI info label, and in the post's menu for pictures only edited with AI.
   Remember: no label proves nothing, and a label doesn't say real or fake. (Google Photos help: Content Credentials don't "Tell you if a photo or video is real or fake".)
5. Then a section headed 2. Look for a hidden mark, or try a detector, with these tick boxes and notes:
   SynthID in the Gemini app: on a computer, go to https://gemini.google.com , click Add files, and ask: Was this image created or edited by Google AI? About 10 image checks in a rolling 24 hours. Google: "Gemini can currently only recognize content created by Google AI tools." Not detected means not made or edited by Google AI, but "it could have been created by other AI systems".
   Google's SynthID Detector: https://synthid.com/ (Google: "made with AI from Google or our partners").
   A detector's confidence score is a guess, not proof. Hive's docs: "As an image's metadata can be stripped or falsified, we recommend that customers view the entire API response holistically." and "you should always refine these thresholds to suit your specific use case."
   Accuracy numbers are the companies' own claims: Hive's blog, "98.03%" (its description of a University of Chicago study); AI or Not's home page, "98.9% accuracy".
6. Then a section headed 3. Look at the picture and where it came from, with these tick boxes:
   Who posted it first?
   Does the person or shop say how it was made?
   What does the rest of the page or post say about it?
   (OpenAI: "consider the file's source and context before drawing a conclusion".)
7. Then a short section headed If all you have is a screenshot, with one line: Google says "If you're taking a screenshot of an image to verify, make sure to crop tight around the image".
8. Under each section, a small notes box I can type in. Keep the ticks and notes in the page while it is open; don't save them anywhere. Add a print style so the page prints on one or two plain white pages with the notes boxes as blank lines.
9. Add a footer: Facts checked 2026-11-26 from each maker's own page. This page checks nothing itself. Not affiliated with any of these companies. Pages change: read each one again before you rely on it.
10. Never overwrite a file that already exists: if check-an-image.html is there, stop and tell me.
11. Then tell me how to open the page by double-clicking check-an-image.html, and show me the first 20 lines of the file.
Safety: create only check-an-image.html in this folder. Don't change, move or delete anything else. Don't upload anything or call any website or API.
Output: check-an-image.html and a three-line note saying what you created.
