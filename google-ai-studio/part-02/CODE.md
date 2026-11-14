# Full code: Is Google AI Studio Free? Limits, Costs and What Google Does With Your Prompts

A small script written for this video from Google's docs (checked 2026-11-13). It was checked with Python's py_compile only; nothing was installed or run, and no key was used.

### token_cost.py
```
# token_cost.py: one test question to the Gemini API, then its token usage and its cost at paid prices (test folder only)
# Install first, in a new test folder:  pip install -U google-genai
# (Google's tokens page: interaction.usage "will only work for SDK newer than 2.0.0", and -U installs the newest)
# Set GEMINI_API_KEY to a throwaway key first (Part 4). Never paste a key into this file.
# The key is passed in explicitly, because if GOOGLE_API_KEY is also set, Google's SDK would use that one instead.
# Free tier: Google may use what you send to improve its products, and human reviewers may see it,
# so send dummy questions only, never personal or confidential information.
# Prices: gemini-4-hydrogen paid tier, per 1M tokens, from https://aistudio.google.com/docs/pricing (checked 2026-11-13).
# Thinking tokens are counted at the output price ("Output price (including thinking tokens)"). Check the page before you trust the number.
# Google's tokens page lists thinking tokens as their own field, so this adds them to the output count; it's an estimate, not your bill.
import os
import sys

from google import genai

INPUT_PRICE = 1.50
OUTPUT_PRICE = 7.50

if not os.environ.get("GEMINI_API_KEY"):
    sys.exit("GEMINI_API_KEY is not set. Set it in your terminal first (Part 4), then try again.")

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

interaction = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Name three primary colours.",
)
print(interaction.output_text)

usage = interaction.usage
thinking = usage.total_thought_tokens or 0
print(f"Input tokens: {usage.total_input_tokens}")
print(f"Output tokens: {usage.total_output_tokens}")
print(f"Thinking tokens: {thinking}")
paid_in = usage.total_input_tokens * INPUT_PRICE
paid_out = (usage.total_output_tokens + thinking) * OUTPUT_PRICE
cost = (paid_in + paid_out) / 1_000_000
print(f"Cost at paid prices checked 2026-11-13: ${cost:.6f} (free tier: $0)")
```
