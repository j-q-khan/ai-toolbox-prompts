# Full code: How to Use Nano Banana Pro in Google AI Studio: Make and Edit Images

A small script written for this video from Google's image generation and pricing pages (checked 2026-11-13). It was checked with Python's py_compile only; nothing was installed or run, no key was used and no picture was made. Nano Banana Pro is not on the free tier, so running it costs money.

### image_app.py
```
# image_app.py: make one picture with Nano Banana Pro (test folder only)
# Install first, in a new test folder:  pip install -U google-genai
# The key comes only from the GEMINI_API_KEY environment variable. Never paste a key into this file.
# Nano Banana Pro is "Not available" on the free tier: this needs a key with billing turned on (Part 4).
# Prices when checked 2026-11-13 (https://aistudio.google.com/docs/pricing): $0.134 per 1K or 2K picture,
# $0.24 per 4K picture, plus text and thinking at $12.00 per 1M tokens. Check the page before you run this.
# Calls and settings from https://aistudio.google.com/docs/image-generation (checked 2026-11-13).
# response_format with aspect_ratio and image_size: that page's "Optional configurations" and
# "Generate images up to 4K" sections, which cover all Gemini 3 image models, Pro included.
# Dummy prompts only: no photos of real people, no fake pictures of real people or events.
import base64
import os
import sys

from google import genai

PROMPT = "A studio photo of a matte black ceramic coffee mug on a polished concrete surface, square image."
SIZE = "2K"  # capital K: 1K, 2K or 4K
PRICE = {"1K": 0.134, "2K": 0.134, "4K": 0.24}
OUT = "nano_banana_pro.png"

key = os.environ.get("GEMINI_API_KEY")
if not key:
    sys.exit("GEMINI_API_KEY is not set. Set it first.")
if os.path.exists(OUT):
    sys.exit(f"{OUT} already exists. Move or rename it first.")

print(f"One {SIZE} picture from gemini-3-pro-image.")
print(f"About ${PRICE[SIZE]} for the picture, plus a little for thinking.")
if input("Type yes to send it: ").strip().lower() != "yes":
    sys.exit("Nothing was sent.")

client = genai.Client(api_key=key)
try:
    interaction = client.interactions.create(
        model="gemini-3-pro-image",
        input=PROMPT,
        response_format={"type": "image", "aspect_ratio": "1:1", "image_size": SIZE},
    )
except Exception as error:
    sys.exit(f"The request failed: {error}")

image = interaction.output_image
data = image.data if image and image.data else None
if not data:
    # Fallback, as in Google's gemini-3-pro-image example: look through the steps for an image.
    for step in getattr(interaction, "steps", None) or []:
        if step.type == "model_output":
            for block in step.content:
                if block.type == "image" and block.data:
                    data = block.data
                    break
        if data:
            break
if not data:
    sys.exit("No picture came back. Check the prompt and your billing, then try again.")
with open(OUT, "wb") as f:
    f.write(base64.b64decode(data))
print(f"Saved {OUT}")
```
