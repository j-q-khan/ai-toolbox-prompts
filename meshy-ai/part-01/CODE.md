# Full code: Meshy AI Tutorial for Beginners: Photo to 3D Model with Meshy 7.1

Copy these into text files. Checked against Meshy's docs, help centre and pricing page on 2026-11-07. Plans and credit costs change, so check meshy.ai/pricing before you rely on a number.

### photo-checklist.txt
```
PHOTO CHECKLIST for Meshy Image to 3D (from Meshy's docs and help, checked 2026-11-07)
Tick every line before you spend credits.

[ ] One subject only, the whole of it in the frame (a busy scene merges into one shape)
[ ] Plain background: a plain floor and a plain wall, or use Remove Background
[ ] Soft, even light, no harsh shadows (dark areas can become black patches)
[ ] Taken from a step back and zoomed in a little, not with the phone right up to it
    (held too near, the nearest parts look stretched, and Meshy copies that)
[ ] Every part you care about is visible: for a dog, all four legs, both ears, the tail
[ ] Sharp, not blurry
[ ] File type PNG, JPG, JPEG or WEBP (an iPhone HEIC photo: export a JPG copy first)
[ ] 20 MB or smaller
[ ] 512 x 512 pixels or larger works best (any phone photo is)
```

### model-check.txt
```
MODEL CHECK before you download (Meshy web app, checked 2026-11-07)

[ ] Turned all the way round in the viewer: front, back, sides, underneath
[ ] The back looks like your subject, not a guess (one photo has no back view)
[ ] Legs, ears, tail: all there, joined to the body, thick enough to hold together
[ ] No extra or missing toes, fingers or small parts
[ ] Small text (a name tag) is readable, or you plan to leave it off
[ ] Texture off if it's for a one-colour print (texture adds 10 credits)
[ ] Format: STL for 3D printing, GLB for websites, FBX for game engines
[ ] Free plan: only untextured Meshy 6 Lite models download, 10 a month.
    Meshy's help centre says any other model, Meshy 7.1 included, asks you to upgrade.
[ ] Real size: set it in your slicer (the Resize option at download needs a paid plan)

Costs as checked on 2026-11-07 (Image to 3D, per try):
  Meshy 6 Lite ............. 10 credits
  Meshy 7.1, Standard ...... 20 credits
  Meshy 7.1, Ultra 2K/4K ... 25 credits (paid plans; Ultra 2K is the paid default)
  Texture at generation .... +10 credits
  A failed generation ...... no credits charged
Free plan: 100 credits a month, reset on the 1st at 00:00 UTC. Unused credits don't carry over.
```

### text-to-3d-prompts.txt
```
TEXT TO 3D PROMPT TEMPLATES, for when you have no photo
(Meshy's formula: Subject + Material/Texture + Art Style + Technical Constraints.
In the web app, Text to 3D uses Meshy 6, 20 credits, or Meshy 6 Lite, 10 credits;
Meshy 7.1 isn't in it. Free plan: only an untextured Meshy 6 Lite model downloads.
Checked 2026-11-07. Up to 800 characters; the first words count most.)

For a 3D print:
A small standing dog figurine, short-haired terrier, smooth matte surface,
friendly cartoon style, solid and watertight, thick legs and tail,
no floating parts, printable proportions, 8 cm tall

Your own subject, for a print:
[what it is], [material or surface], [style], solid, watertight,
no thin parts, no floating parts, printable proportions, [height] cm tall

For a game prop:
[what it is], [material], [style], game-ready, clean edges, minimal geometry

Leave things out with a short negative phrase:
no background elements / no text or labels / without floating particles
```
