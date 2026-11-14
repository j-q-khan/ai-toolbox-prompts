# Full code: Google AI Studio vs the Gemini App: Which One Do You Need?

A small script written for this video from Google's docs (checked 2026-11-13). It was checked with Python's py_compile only; nothing was installed or run, and no key was used.

### rules_test.py
```
# rules_test.py: one test question to the Gemini API, with standing rules (system instructions) from rules.txt (test folder only)
# The code version of the System Instructions field in Google AI Studio's Run settings.
# Install first, in a new test folder:  pip install -U google-genai
# Set GEMINI_API_KEY to a throwaway key first (Part 4). Never paste a key into this file.
# The key is passed in explicitly, because if GOOGLE_API_KEY is also set, Google's SDK would use that one instead.
# Free tier: Google may use what you send to improve its products, and human reviewers may see it,
# so send dummy questions only, never personal or confidential information.
# Model: gemini-4-hydrogen, labelled "Default general-purpose" on https://aistudio.google.com/docs/latest-model (checked 2026-11-13).
# Google's docs name no model field on the response, so this prints the model it asked for.
import os
import sys
from pathlib import Path

from google import genai

MODEL = "gemini-4-hydrogen"
RULES_FILE = Path(__file__).with_name("rules.txt")
QUESTION = "Explain how a rainbow forms."

if not os.environ.get("GEMINI_API_KEY"):
    sys.exit("GEMINI_API_KEY is not set. Set it in your terminal first (Part 4), then try again.")
if not RULES_FILE.is_file():
    sys.exit("rules.txt is missing. Put it in the same folder as this script, then try again.")
rules = RULES_FILE.read_text(encoding="utf-8").strip()
if not rules:
    sys.exit("rules.txt is empty. Write one or two rules in it, then try again.")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

interaction = client.interactions.create(
    model=MODEL,
    system_instruction=rules,
    input=QUESTION,
)
print(interaction.output_text)
print(f"Model asked for: {MODEL}")
```

### rules.txt
```
Answer in plain English.
Use three sentences or fewer.
```
