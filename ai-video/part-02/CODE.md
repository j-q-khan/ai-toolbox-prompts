# Full code: AI Video Generator from Image: Image to Video AI, Step by Step

The prompt sheet, the settings checklist and the test photo list for this video, written from Google's Flow help pages (checked 2026-11-23). They were written from the docs, not run, and nothing was generated for this video.

### 1. image-to-video-prompt-sheet.txt
```
# Image to video motion prompts, written for this video (2026-11-23). Not run: nothing was generated.
# To keep a copy: paste this into Notepad and save it as image-to-video-prompt-sheet.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Your photo already shows what's in the shot, so the prompt says what moves, how the camera moves and the light.
# Pick ONE movement and ONE camera move. Name the thing in your photo once. Never ask for something your photo doesn't show.
# Products, places and scenes only: keep people, faces and characters out of the photo.

The [thing in your photo], [one movement]. [Slow push in / Slow pan from left to right]. [Light], calm.

# Product examples:
The candle on the wooden shelf, its flame flickering gently. Slow push in. Warm evening light, calm.
The mug of coffee on the kitchen table, steam rising slowly. Slow push in. Soft morning light, calm.
The bunch of flowers in the glass vase, petals moving in a light breeze. Slow push in. Bright daylight, calm.

# Place examples:
The beach at sunset, small waves rolling onto the sand. Slow pan from left to right. Golden light, calm.
The quiet market street, light shifting across the stalls. Slow pan from left to right. Late afternoon light, calm.
The garden after rain, leaves moving in a light breeze. Slow push in. Soft grey light, calm.

# If the clip warps (edges bend, label letters melt): cut back to one movement and one camera move, and retest at 360p.
```

### 2. flow-image-to-video-checklist.md
```
# Image to video in Google Flow: settings checklist (facts checked 2026-11-23)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as flow-image-to-video-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from Google's Flow help pages on 2026-11-23. Nothing was signed up for, uploaded, run or generated. Menus, models and credit costs change: check the help pages and Settings before you generate.

## Before you start
- [ ] A computer with a Chromium browser, such as Chrome or Edge. Frames to Video is "Currently only available at Google Flow on web". https://support.google.com/flow/answer/16352836
- [ ] A Google account; age 18 or over; a supported country. https://support.google.com/flow/answer/16353544
- [ ] A sharp photo of a product or a place, the moving part clearly in view, nothing cut off, a plain background for products.
- [ ] No people in the photo: Flow has "precautions to protect minors and uploaded photos of people", and "Generating videos of prominent people." is not supported in any region.

## The path
- [ ] Google Flow, sign in, + New project.
- [ ] In the prompt box: click the model name (it starts on an image model, for still pictures), then Video, then Frames.
- [ ] Drag your photo onto "+ Add start frame". Leave "+ Add end frame" empty for your first clip.
- [ ] Prompt: one movement, one camera move, one line about the light; name the thing in your photo once; "complement, not contradict" the photo. https://support.google.com/flow/answer/16353334

## The four settings
- [ ] Model: Omni Flash 1.2 (Google recommends it; 3 to 10 s without a subscription).
- [ ] Outputs: 1 (credits are "per generation, not per request").
- [ ] Aspect ratio: the shape that matches where you'll post. Length: 5 seconds for a test.
- [ ] Resolution: Settings, at the top right of the prompt box. 360p for tests, 720p for the version you'll post.

## The cost (when checked, 2026-11-23)
- [ ] No subscription: "only 50 Google Flow credits per day"; unused credits don't roll over. https://support.google.com/flow/answer/16526234
- [ ] Omni Flash 1.2 up to 10 s: 1 credit a second at 360p, 3 at 720p. A 5-second test: 5 credits at 360p (10 tests a day), 15 at 720p (3 tests a day).
- [ ] Credits are taken when a generation begins; a failed or filtered generation gets them back "within one hour".
- [ ] Peak hours, "roughly 2 PM to 5 PM UTC": without a subscription, video may be unavailable. Try again later.

## Check, then download
- [ ] The first moment matches your photo. The product keeps its shape. Only what you asked for moves.
- [ ] Warping at the edges or on a label? Cut back to one movement and one camera move; retest at 360p.
- [ ] Download: hover over the clip, More, Download, pick a file type. https://support.google.com/flow/answer/16935308
- [ ] Every Flow clip carries an invisible SynthID watermark, which "should not be tampered with or removed".
- [ ] Next try: project Settings, top right, turn on Show tile details to see the prompt under each clip.
```

### 3. photos.txt
```
# Test photo descriptions for the Claude build prompt: what's in the photo | product or place | light or mood.
# To keep a copy: paste this into Notepad and save it as photos.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you, and the script skips them. Describe the photo; the script never opens it.
candle on a wooden shelf | product | warm evening light
mug of coffee on a kitchen table | product
beach at sunset | place | golden light
quiet market street | place
```
