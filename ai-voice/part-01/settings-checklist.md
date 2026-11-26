# ElevenLabs Text to Speech: settings checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.
Plans and models change. Before you rely on a line, open its source and check the date. This is not legal advice.

## Before you start
- [ ] Decide what the voiceover is for: a video that earns money (ads, a sponsor, a product), or one that doesn't.
- [ ] If it might earn money, pick a paid plan before you make it. ElevenLabs: "Content created outside of a paid subscription (before or after) cannot be used commercially and always requires attribution when shared non-commercially." Source: elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform
- [ ] Write the script for the voice: numbers as words, no symbols or emojis (see voiceover-script-template.txt).

## The steps (ElevenLabs' Text to Speech page)
- [ ] Sidebar: Text to Speech.
- [ ] Paste the script into the text box. Eleven v4: up to 100,000 characters in one generation on the website; every other model: up to 5,000.
- [ ] Voice: the menu called Voice at the top of the settings panel on the right (the docs' screenshots; the guide's text still says "at the bottom left"). The Voice Library has "over 10,000 voices shared by the ElevenLabs community". The docs say the voice matters most, then the model, then the settings.
- [ ] Model: the menu called Model, under Voice. Pick Eleven v4 ("Our most emotionally rich, expressive speech synthesis model"). Others: Multilingual v2 ("Most stable on long-form generations"), Flash v2.5 ("Our fast, affordable speech synthesis model").
- [ ] Settings on Eleven v4: two sliders, Stability and Similarity ("Style and Speed sliders are not available in Eleven v4"). Start where the docs' general guidance starts: "stability around 50, similarity around 75", then nudge. Source: elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4
- [ ] Press Generate speech. The button shows the credits it will use.
- [ ] Not right? Change a slider and press Regenerate speech. Two free regenerations apply when the text, voice and model stay the same, the first generation was less than two hours ago, and you haven't refreshed the page.
- [ ] Download: the download button at the bottom right after generating. From the History tab on the right: MP3 (128kbps) or WAV; Advanced gives more formats. "Higher quality audio options are only available on paid tiers."
- [ ] Put the file on your video editor's timeline, under your clips.

## What the sliders do (ElevenLabs' docs, in short)
- [ ] Stability (Eleven v4 page): "Lower values allow more expressive, varied delivery; higher values keep the performance closer to a fixed baseline."
- [ ] Similarity (Eleven v4 page): "Higher values enforce closer adherence to the reference, which can come at the cost of some naturalness."
- [ ] Style exaggeration: older models only (for example Multilingual v2); the Text to Speech guide recommends keeping it at 0.
- [ ] Speed: older models only; 1.0 is normal, 0.7 slowest, 1.2 fastest (not on Eleven v3 either).
- [ ] The sliders work as a range, not an exact setting: the same values won't give the same take every time.

## Plans and commercial use (checked 2026-11-26, regular prices; sale prices on the page end December 1)
- [ ] Free: $0, 10k credits a month. Terms (last updated 09 October 2026): a free user "may only use the Services for non-commercial purposes".
- [ ] Free: if you publish it, ElevenLabs says you "must attribute it to ElevenLabs by including "elevenlabs.io" or "11.ai" in the title".
- [ ] Starter: was $6 a month when checked, 30k credits, "Commercial License", Instant Voice Cloning.
- [ ] Creator: was $22 a month when checked, 121k credits, Professional Voice Cloning.
- [ ] Sources: elevenlabs.io/pricing ; elevenlabs.io/terms-of-use

## YouTube (checked 2026-11-26)
- [ ] YouTube's disclosure page lists realistic content creators must disclose, such as making "a real person appear to say or do something they didn't do". It doesn't mention a narrator voice that isn't a real person, and it says "the above list is not exhaustive". Check it for your own video: support.google.com/youtube/answer/14328491

## Free options (checked 2026-11-26; read, not run, for this video)
- [ ] Kokoro: open-weight voice model, Apache-2.0 code and "Apache-licensed weights". Runs on your own computer; needs Python. Source: huggingface.co/hexgrad/Kokoro-82M
- [ ] Piper: engine GPL-3.0-or-later (OHF-Voice/piper1-gpl, v1.8.0). Each voice has its own licence: the lessac voice's recordings exclude commercial use; docs/COMMERCIAL_USE.md lists voices that allow it (for example en_US-joe-medium, CC0).
- [ ] Gemini text to speech (Gemini 3.8 Flash TTS): Free Tier "Free of charge"; Free Tier "Used to improve our products: Yes". Source: aistudio.google.com/docs/pricing
- [ ] CapCut text to speech: "free of charge"; "can be used for commercial purposes such as advertisements, YouTube videos, and brand promotions" if you "comply with CapCut's terms of use". Source: capcut.com/tools/text-to-speech
