# Full code: AI Image Upscaler and Enhancer: Make Small Images Sharp

The upscale checklist for this video, written from each maker's own pages (checked 2026-11-26). It was written from the docs, not run, and nothing was upscaled or generated for this video.

### 1. ai-image-upscale-checklist.md
```
# Make a small picture sharp: the upscale checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as ai-image-upscale-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every quote below is the maker's own words, from its own page on 2026-11-26. Nothing was signed up for, installed, run, upscaled or generated. Pages change: read each one again before you rely on it.

## Words
- Pixel: a tiny square of colour. Resolution: how many pixels across and down.
- Upscale: add pixels to make a picture bigger; the AI guesses what goes in the new ones.
- 100% zoom: one pixel of the picture fills one pixel of your screen.

## Pick a tool
| Tool | Cost, in the maker's words | Steps or setup | Limits | Source |
|---|---|---|---|---|
| Adobe Firefly (web) | "Yes, you can use the Adobe Firefly image upscaler for free with an Adobe account." | Edit an Image, then Quick Actions, then Generative Upscale, then choose a model and 2x or 4x, then Upscale. "A separate upscaled image will be generated in a new document with an updated name." | JPEG, PNG or WEBP, up to 100MB; at least 512 x 512 pixels | https://www.adobe.com/products/firefly/features/image-upscaler.html |
| Upscayl (Windows 10+, macOS 12+, Linux) | "Free and Open Source AI Image Upscaler"; AGPL-3.0; latest release v2.15.0, 2024-12-25 | Download from https://github.com/upscayl/upscayl/releases/latest. Windows: upscayl-x.x.x-win.exe, "Double click exe file to launch." macOS: upscayl-x.x.x-mac.dmg, "Double click dmg, drag Upscayl icon into Applications folder." Linux: upscayl-x.x.x-linux.AppImage, allow it to run as a program in its Permissions, then double-click it. In the app: Step 1 Select Image, Step 2 Select AI Model (Upscayl Standard: "Suitable for most images."), Step 3 Set Output Folder, Step 4 the Upscayl button. | "You'll need a Vulkan compatible GPU (Graphics Card) to upscale images." Check https://github.com/upscayl/upscayl/wiki/Compatibility-List. "all the default models only support x4" | https://github.com/upscayl/upscayl |
| Ideogram Upscale (web) | "The Upscale app needs a paid plan or bought credits." "The button shows the cost before you click." | Your own picture: Apps, search for Upscale, then under Source image click + Add (or click Upscale on an image page); Scale 2x, 4x or 8x (default 2x) | Output no bigger than the equivalent of 8192 x 8192 pixels | https://docs.ideogram.ai/using-ideogram/features-and-tools/upscale |
| Topaz Gigapixel | Paid. Personal was $29 a month billed monthly on 2026-11-26, during a Black Friday sale. No free trial mentioned on the page. | "Upscale almost any image 6x." | | https://www.topazlabs.com/gigapixel |

## What an upscaler can't do, in the makers' words
- "This process may have introduced inaccurate, speculative details not present in the original picture." (Wikimedia Commons, on a photo upscaled with Upscayl)
- "it cannot de-blur or do focus adjustment on your image" (Upscayl's GitHub page)
- "No upscaler is guaranteed to leave every detail unchanged." (Ideogram's docs)

## Before you upscale
- [ ] The picture is sharp, not blurry. (Upscayl's GitHub page says it cannot de-blur or do focus adjustment.)
- [ ] It's a picture of a thing, not a real person's face.
- [ ] I cropped it to the shape I need first. ("Upscaling does not turn a portrait image into a square or add space around the subject." Ideogram's docs)
- [ ] For Firefly: it's at least 512 x 512 pixels.
- [ ] I kept the original.

## After you upscale
- [ ] I looked at it at 100% zoom.
- [ ] I compared the edges, any lettering and fine texture with the original.
- [ ] Nothing is smeared or made up, like an extra letter. If it is, I tried a smaller scale.
- [ ] The new width really is bigger, in pixels (example: 436 px to 1,744 px at 4x).
- [ ] When to stop: if a smaller scale still looks made up, I use the original.
```
