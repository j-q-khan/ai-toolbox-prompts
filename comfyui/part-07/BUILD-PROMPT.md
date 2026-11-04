# Claude build prompt: ComfyUI ControlNet and Inpainting Tutorial

A mask maker for Claude Code: it turns boxes and ovals you describe into feathered inpainting masks in both formats ComfyUI loads (a black and white mask for Load Image (as Mask), and a copy with a transparent hole for Load Image), plus a preview, without touching your originals. Mask conventions checked against ComfyUI v0.44.0's LoadImage and LoadImageMask source on 2026-11-04. Not run by us.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a mask maker that turns boxes and ovals I describe into clean inpainting masks for ComfyUI, in both formats ComfyUI loads, without ever changing my original images.
Inputs: a folder test-images with one or two test pictures, for example upscale-input.jpg from Comfy's docs (github.com/Comfy-Org/docs, images/tutorial/basic/upscale folder, GPL-3.0), and a regions.json file you create with me, listing for each image one or more shapes: type box or oval, left, top, right, bottom in pixels, plus grow and feather in pixels.
Steps, in order:
1. Show me your plan and every command, and wait for my yes. Ask before installing Pillow, the Python image library, into a virtual environment inside this folder (never the system Python), or downloading any test image.
2. Write a small Python script, make_masks.py. Open each image read-only and read its size. Refuse any shape that falls outside the image, and tell me which one.
3. For each image, draw the shapes in white on a black image of the same size. Grow the white area by the grow value, then blur its edge by the feather value, so the seam blends.
4. Save it as masks/NAME_mask.png. This black and white mask loads in ComfyUI with Load Image (as Mask), channel red, where white means repaint.
5. Also save masks/NAME_rgba.png: a copy of the image with the masked area made transparent, using the mask, so it can go straight into Load Image, which turns transparent pixels into the mask. Write the copy only into the masks folder.
6. Save masks/NAME_preview.png with the mask shown as a red tint over the image, so I can check the region by eye.
7. Write masks-report.md listing each image, its size, each shape, and the three files made.
Safety: never edit, move or overwrite the original images, write only inside the masks folder in this test folder, use only test images I choose, make no network calls except an approved install or test download, and never run ComfyUI. Stop and ask me before running anything that changes data.
Output: make_masks.py, regions.json, the masks folder, masks-report.md, and a short note on which ComfyUI node to load each file with, reminding me to copy NAME_mask.png into ComfyUI's input folder or upload it through the node first.
