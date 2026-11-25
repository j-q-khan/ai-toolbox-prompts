Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder where you have put two copies of your own photos: the original and the edited version, named before.jpg and after.jpg (photos of things or places, not of other people). It builds one small web page that shows the two photos on top of each other with a slider, so you can drag to compare before and after. The page works offline in your browser, loads nothing from the internet, uploads nothing, and changes no photo. Written for this video, checked 2026-11-25. Nothing here was run for the video.

Goal: build one self-contained page, compare.html, that shows two of my photos, before and after, stacked in the same frame, with a slider that moves the dividing line between them.
Input: two image files in this folder, before.jpg and after.jpg. Also let me pick any two other image files from my computer with two file pickers on the page, labelled Before and After, read in the browser only.
Steps, in order:
1. Tell me in two sentences what you will build and which file you will create, then wait for me to say go.
2. Write a single file, compare.html, with its styling and script inside it. Plain HTML, CSS and JavaScript only: no libraries, no CDN links, no fonts or images from the internet, no build step, nothing to install.
3. Show the after photo full width, with the before photo on top of it, clipped from the left edge to the slider's position, so dragging the slider to the right shows more of the before photo. Start the slider at the middle.
4. Add a range slider under the photos, from 0 to 100, plus left and right arrow keys to move it, and label the two sides Before and After in large text, at least 24 pixels.
5. Make both photos fit the same frame: use the after photo's width and height, and scale the before photo to match, so a cropped or extended edit still lines up at the top left. If the two sizes differ, show one line under the photos saying the sizes differ, with both sizes.
6. When I pick files with the pickers, show them with a local object URL from the browser only. Never send, upload or store the images anywhere, and add no analytics, tracking or network calls of any kind.
7. Add a small line of text under the slider: Edited photo. Keep the original, and never pass an edit off as the real moment.
8. Never overwrite a file that already exists: if compare.html is there, stop and tell me.
9. Then tell me how to open compare.html in my browser by double-clicking it, and how to check it worked: the slider moves the dividing line.
Safety: read only before.jpg and after.jpg, or the files I pick on the page. Don't change, move, rename or delete them or anything else. Don't upload anything or call any website or API.
Output: compare.html and a three-line note saying what you created.
