# Full code: Unity AI Tutorial: Unity's AI Assistant and Generators in Unity 6

The checklist and the example prompts for this video, written from Unity's docs (checked 2026-11-25). Example output: they were written from the docs and not run for this video.

### 1. unity-assistant-checklist.txt
```
UNITY'S IN-EDITOR ASSISTANT: A CHECKLIST FOR A FIRST TRY
AI Game Development, Part 3. Written from Unity's docs, checked 2026-11-25. Not run for the video.
To keep a copy: paste this into Notepad and save it as unity-assistant-checklist.txt with the box called
Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste.

BEFORE YOU START
[ ] Make a copy of your game folder and try everything on the copy first.
[ ] Version: Unity 6.3 (6000.3) or later, or Unity 6.0 at 6000.0.76f1 or newer. Unity Hub shows it.
[ ] Signed in to Unity Hub.
[ ] Link the copy to Unity Cloud: Edit, then Project Settings, then Services,
    then Create a new cloud project, pick your organization,
    then Create new cloud project and link to Unity project.
[ ] It worked if the window now shows extra settings, including Unlink.

SWITCH IT ON
[ ] In the toolbar, open the AI menu, accept the terms and choose Agree and install Unity AI.
[ ] No AI menu? Right-click an empty part of the toolbar, then Services, then AI.
[ ] Choose Open Assistant. Dock the window beside your scene.

ASK FIRST, THEN AGENT
[ ] Ask mode: looks and answers, changes nothing. Start here.
[ ] Plan mode: writes a step-by-step plan for you to approve.
[ ] Agent mode: makes changes, only once you approve them.
[ ] Model tier: keep Unity Default. Unity Ultra costs significantly more credits.
[ ] Prompt pattern: what you have, then what you want, then the technical details.

MAKE ONE SPRITE
[ ] AI menu, then Generate New, then Sprite.
[ ] Pick the model first (Change): its style decides the look.
[ ] Prompt: describe only what you can see.
[ ] Check the cost on the Generate button before you press it.
[ ] Find it in the Generations panel, the Inspector and the GeneratedAssets folder.

COST (checked 2026-11-25, check again on the day)
[ ] Pro: includes the assistant, 2,000 credits a month. Was $210 a month.
[ ] Personal: free under $200K revenue or funding in the last 12 months.
    Plans page: a 14-day trial, then a paid subscription; 1,000 monthly credits on the card.
    Tools page: the trial converts to a $10/month subscription.
[ ] Your balance: Unity Dashboard, Manage Credits.

OWNERSHIP
[ ] Unity's guiding principles page: "You own your input and output data".
[ ] Training on your work: off by default (the Improve Unity AI setting).
[ ] Every generated asset carries metadata marking it as made with AI.
[ ] You are responsible for app store declarations and usage rights.
[ ] Generators can be turned off in the dashboard settings (owners and managers only).

Pages: unity.com/features/ai  unity.com/products  unity.com/legal/unityai-guiding-principles
```

### 2. prompts.txt
```
# The example prompts from this video. Written from Unity's docs, checked 2026-11-25; not run for the video.
# To keep a copy: paste this into Notepad and save it as prompts.txt with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you, so don't paste them.

# 1. In the assistant, Ask mode first, then Agent mode (what you have, what you want, the technical details):
I have a 2D player sprite called Ship.
I want it to move left and right with the arrow keys.
Keep it inside the screen, with a speed I can change in the Inspector.

# 2. In the Sprite Generator's Prompt field (pick the model first, then check the cost on the Generate button):
a small green spaceship, side view, flat colours

# 3. Or in the assistant's chat, and it picks the Generator for you:
Make a sprite of a small green spaceship, side view, flat colours, for a 2D space game.
```
