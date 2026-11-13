# Full code: Google AI Studio Tutorial for Beginners (2026): Your First Prompt

Google's own quickstart example, unchanged, and a safer version written for this video, from Google's docs (checked 2026-11-13). Both were checked with Python's py_compile only; nothing was installed or run, and no key was used.

### 1. quickstart.py
```
# quickstart.py: Google's own example from the Gemini API quickstart, unchanged (checked 2026-11-13)
# Source: https://aistudio.google.com/docs/quickstart
# Install first, in a new test folder:  pip install -U google-genai
# The client finds your key in the GEMINI_API_KEY environment variable (Part 4 shows how to set it).
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
```

### 2. first_prompt.py
```
# first_prompt.py: one question to the Gemini API, with a key check (test folder only)
# Install first, in a new test folder:  pip install -U google-genai
# Set GEMINI_API_KEY to a throwaway key first (Part 4). Never paste a key into this file.
# The key is passed in explicitly, because if GOOGLE_API_KEY is also set, Google's SDK would use that one instead.
# Free tier: Google may use what you send to improve its products, and human reviewers may see it,
# so send dummy questions only, never personal or confidential information.
import os
import sys

from google import genai

if not os.environ.get("GEMINI_API_KEY"):
    sys.exit("GEMINI_API_KEY is not set. Set it in your terminal first (Part 4), then try again.")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain how a rainbow forms, in two sentences, for a ten-year-old.",
)
print(interaction.output_text)
```
