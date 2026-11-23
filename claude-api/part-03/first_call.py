# first_call.py: your first call to the Claude API, with the common errors explained in plain words
# From Claude API, Part 3. Written from Anthropic's quickstart, Python SDK page and errors page (checked 2026-11-22), not run.
# Needs Python 3.10 or later, the anthropic package (pip install anthropic) and your key in the ANTHROPIC_API_KEY
# environment variable (Part 1). Run it from its folder, with the virtual environment switched on: python first_call.py
# How to save it: in the terminal, in your claude-quickstart folder, type  notepad first_call.py  (Windows)
# or  touch first_call.py && open -e first_call.py  (Mac), paste this text in, and save. On a Mac, paste rather than
# retype, so TextEdit doesn't swap the straight quotes for curly ones.
import os
import sys

import anthropic

QUESTION = "In two sentences, what is an API?"  # change this to ask something else
MODEL = "claude-opus-5-5"  # current model IDs: platform.claude.com/docs/en/about-claude/models/overview

# Optional: if you keep your key in a .env file instead (see .env.example), install python-dotenv and it's loaded here.
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

if not os.environ.get("ANTHROPIC_API_KEY"):
    sys.exit("ANTHROPIC_API_KEY isn't set in this window. Set it (Part 1), then open a new terminal window.")

client = anthropic.Anthropic()  # finds the key in ANTHROPIC_API_KEY by itself

try:
    message = client.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": QUESTION}],
        # Don't add temperature, top_p or top_k: API version 2026-10-21 returns a 400 error for any of them.
    )
except anthropic.AuthenticationError:
    sys.exit("401 authentication_error: there's an issue with your API key. Check ANTHROPIC_API_KEY, or make a new key.")
except anthropic.RateLimitError:
    sys.exit("429 rate_limit_error: a rate limit or the monthly spend cap. The package already retried twice: wait, then try again. If it keeps failing, check platform.claude.com/usage/limits")
except anthropic.BadRequestError:
    sys.exit("400 invalid_request_error: look for temperature, top_p or top_k, check the spend limit you set, or use a key tied to a workspace.")
except anthropic.APIStatusError as error:
    if error.status_code == 402:
        sys.exit("402 billing_error: an issue with your billing or payment information. See platform.claude.com/settings/billing")
    sys.exit(f"Error {error.status_code}: see platform.claude.com/docs/en/api/errors")
except anthropic.APIConnectionError:
    sys.exit("The API couldn't be reached. Check your internet connection, then try again.")

for block in message.content:
    if block.type == "text":
        print(block.text)

print(f"\nTokens used: {message.usage.input_tokens} in, {message.usage.output_tokens} out")
