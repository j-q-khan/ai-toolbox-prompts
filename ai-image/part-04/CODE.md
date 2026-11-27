# Full code: AI Image Detector: How to Tell If a Picture Is AI

The check-an-image checklist for this video, written from each maker's own pages (checked 2026-11-26). It was written from the docs, not run, and nothing was uploaded to any checker for this video.

### 1. ai-image-check-an-image-checklist.md
```
# Is this picture AI? The check-an-image checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as ai-image-check-an-image-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every quote below is the maker's own words, from its own page on 2026-11-26. Nothing was uploaded to any checker, signed up for or run. Pages change: read each one again before you rely on it.

No single check proves it. Check in this order: the label, then a hidden mark or a detector, then the picture and where it came from.

## Words
- Provenance: the history of where a picture came from and how it was made.
- Metadata: extra information stored inside the file.
- Watermark: a hidden pattern mixed into the picture's dots of colour.
- Content Credentials: a label stored inside the file that says how it was made (from the C2PA).
- SynthID: Google's invisible watermark.
- Detector: an app that studies the picture and guesses if it was made with AI.
- Confidence score: a number for how sure a detector is, from 0 to 1. A guess, not proof.

## 1. The label (Content Credentials)
- [ ] I'm checking the original file, not a screenshot, cropped or converted copy. (OpenAI: Content Credentials "can be lost through everyday actions, such as taking a screenshot or converting a file".)
- [ ] OpenAI's verify page: https://openai.com/verify ("checks whether an uploaded file contains provenance signals associated with OpenAI tools"; it looks for "C2PA metadata and SynthID watermarks")
- [ ] Google Photos on a phone: open the picture, tap More, then About, scroll to "How this was made". (Android and iPhone app; not on the web.)
- [ ] Facebook or Instagram: Meta's "AI info" label, or in the post's menu for pictures "only modified or edited by AI tools".
- Who adds it, in their words: OpenAI, "Images generated with ChatGPT or the OpenAI API include both signals."; Adobe's Firefly plans page, Adobe "automatically attaches content credentials for transparency"; Microsoft Copilot, "Provenance metadata can be viewed on the Content Credentials site."
- No label proves nothing: "While C2PA Manifests are typically embedded in the asset, they can be separated." (C2PA FAQ)
- A label doesn't settle it: Content Credentials don't "Tell you if a photo or video is real or fake" (Google Photos help).

## 2. A hidden mark, or a detector
- [ ] Gemini app (Google's SynthID check): on a computer, https://gemini.google.com , Add files, ask "Was this image created or edited by Google AI?" About 10 image checks in a rolling 24 hours. "Gemini can currently only recognize content created by Google AI tools." Not detected: "it could have been created by other AI systems".
- [ ] Google's SynthID Detector: https://synthid.com/ ("made with AI from Google or our partners")
- [ ] A detector, if I use one. Hive's docs: confidence scores from 0 to 1; recommended line for an AI-generated image 0.9; "As an image's metadata can be stripped or falsified, we recommend that customers view the entire API response holistically."; "you should always refine these thresholds to suit your specific use case."
- Accuracy, as the companies state it: Hive's blog, "near-perfect 98.03% accuracy rate" (its description of a University of Chicago study). AI or Not's home page, "98.9% accuracy". AI or Not's pricing page: "$5 in free credits to get you started.", "20 AI image checks"; Pro was $5/month and Business $100/month on 2026-11-26.
- One score is never proof, either way.

## 3. The picture and where it came from
- [ ] Who posted it first?
- [ ] Does the person or shop say how it was made?
- [ ] What does the rest of the page or post say about it?
- OpenAI: "consider the file's source and context before drawing a conclusion".

## If all I have is a screenshot
- Google: "If you're taking a screenshot of an image to verify, make sure to crop tight around the image".

## Sources (checked 2026-11-26)
- https://c2pa.org/faqs/
- https://help.openai.com/en/articles/8912793-c2pa-and-synthid-in-openai-generated-images
- https://openai.com/verify
- https://support.google.com/photos/answer/16496549?hl=en
- https://about.fb.com/news/2024/04/metas-approach-to-labeling-ai-generated-content-and-manipulated-media/
- https://deepmind.google/models/synthid/
- https://support.google.com/gemini/answer/16722517?hl=en
- https://docs.thehive.ai/docs/ai-image-and-video-detection
- https://thehive.ai/blog/clear-winner-study-shows-hives-ai-generated-image-detection-api-is-best-in-class
- https://www.aiornot.com/ and https://www.aiornot.com/pricing
- https://www.adobe.com/products/firefly/plans.html
- https://support.microsoft.com/en-us/privacy/microsoft-copilot/transparency-note
```
