Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder. It builds one local web page, upscale-checklist.html, a printable checklist for making a small picture bigger with an AI image upscaler: it works out the size before and after, warns about what an upscaler invents, and says when to stop. It uses only the facts written below, needs no internet to work, opens no image, calls no image service and upscales nothing. Written for this video, checked 2026-11-26. Nothing here was run for the video.

Goal: write one file, upscale-checklist.html, a plain HTML page with a little JavaScript and no outside libraries, that I can print, with a size calculator and a checklist to tick before and after I upscale a picture.
Steps, in order:
1. Tell me in two sentences what the page will do and which file you will create, then wait for me to say go.
2. Use only plain HTML, CSS and JavaScript in one file. No installs, no downloads, no fonts or scripts from the internet, no calls to any website or AI service, and no file picker: I type the numbers myself. Links in the page are for me to click; the page never fetches them.
3. At the top, a size calculator: two number boxes, width and height in pixels, and a choice of scale: 2x, 4x, 8x. Show the size after (width times scale, height times scale) and the total pixels. Then show these notes, worked out from the numbers:
   If the width or the height is under 512: Adobe Firefly's web upscaler will turn this picture away. Adobe's message: "Image is smaller than the minimum dimensions (512 x 512 pixels)."
   If the scale is 8x: Adobe Firefly's web upscaler offers 2x or 4x only.
   If the total pixels after are more than 8192 times 8192: Ideogram's docs say the output can't go over the equivalent of 8192 x 8192 pixels.
   Always: Upscayl's default models only support x4 (its guide, GitHub wiki).
4. Under it, a section headed Pick a tool, as a plain table with these rows exactly:
   Adobe Firefly (web) / "Yes, you can use the Adobe Firefly image upscaler for free with an Adobe account." / Edit an Image, then Quick Actions, then Generative Upscale, choose a model and 2x or 4x, click Upscale / JPEG, PNG or WEBP, up to 100MB, at least 512 x 512 pixels / https://www.adobe.com/products/firefly/features/image-upscaler.html
   Upscayl (Windows, Mac, Linux) / "Free and Open Source AI Image Upscaler", AGPL-3.0, latest release v2.15.0 from 2024-12-25 / "You'll need a Vulkan compatible GPU (Graphics Card) to upscale images." In the app: Step 1 Select Image, Step 2 Select AI Model, Step 3 Set Output Folder, Step 4 the Upscayl button / it "cannot de-blur or do focus adjustment on your image" / https://github.com/upscayl/upscayl and https://github.com/upscayl/upscayl/wiki/Compatibility-List
   Ideogram Upscale (web) / your own picture: Apps, search for Upscale, then under Source image click + Add; 2x, 4x or 8x / "The Upscale app needs a paid plan or bought credits." / "The button shows the cost before you click." / https://docs.ideogram.ai/using-ideogram/features-and-tools/upscale
   Topaz Gigapixel / "Upscale almost any image 6x." / Personal was $29 a month billed monthly when checked on 2026-11-26, during a Black Friday sale / no free trial mentioned on the page / https://www.topazlabs.com/gigapixel
5. Then a section headed What an upscaler invents, with these three quotes, each with its source:
   "This process may have introduced inaccurate, speculative details not present in the original picture." (Wikimedia Commons, on an upscaled photo)
   "it cannot de-blur or do focus adjustment on your image" (Upscayl's GitHub page)
   "No upscaler is guaranteed to leave every detail unchanged." (Ideogram's docs)
6. Then a checklist headed Before you upscale, with these tick boxes: Is the picture sharp, not blurry? (Upscayl's GitHub page says it cannot de-blur or do focus adjustment.) / Is it a picture of a thing, not a real person's face? / Did I crop it to the shape I need first? (Ideogram's docs: upscaling won't turn a tall picture into a square or add space around it.) / Is it at least 512 x 512 pixels, if I'm using Firefly? / Did I keep the original?
7. Then a checklist headed After you upscale, with these tick boxes: Did I look at it at 100% zoom? / Did I compare edges, any lettering and fine texture with the original? / Is anything smeared or made up, like an extra letter? If so, try a smaller scale. / Is the new width really bigger, in pixels? / When to stop: if a smaller scale still looks made up, use the original.
8. Keep the ticks and numbers in the page while it is open; don't save them anywhere. Add a print style so the page prints on one or two plain white pages without the calculator's input boxes looking broken.
9. Add a footer: Facts checked 2026-11-26 from each maker's own page. Not affiliated with any of these companies. Prices and plans change: read each page again before you rely on it.
10. Never overwrite a file that already exists: if upscale-checklist.html is there, stop and tell me.
11. Then tell me how to open the page by double-clicking upscale-checklist.html, and show me the first 20 lines of the file.
Safety: create only upscale-checklist.html in this folder. Don't change, move or delete anything else. Don't upload anything or call any website or API.
Output: upscale-checklist.html and a three-line note saying what you created.
