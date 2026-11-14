# key_check.py: test your Gemini API key with one question (test folder only)
# Install first, in a new test folder:  pip install -U google-genai
# The key comes only from the GEMINI_API_KEY environment variable. Never paste a key into this file.
# The key is passed in explicitly, because if GOOGLE_API_KEY is also set, Google's SDK would use that one instead.
# Free tier: Google may use what you send to improve its products, and human reviewers may see it,
# so send test questions only, never personal or confidential information.
# The model and question are from Google's quickstart, https://aistudio.google.com/docs/quickstart (checked 2026-11-13).
import os
import sys

from google import genai

key = os.environ.get("GEMINI_API_KEY")
if not key:
    sys.exit("GEMINI_API_KEY is not set. Set it first.")

client = genai.Client(api_key=key)

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)
