# Full code: How to Use Claude API: Your First Call in Python

Anthropic's quickstart, the same call with the errors handled, the setup lines for Windows and Mac, and a .env example, written from Anthropic's quickstart, Python SDK page and errors page and Python's venv docs (checked 2026-11-22), not run. Every key below is a fake.

### 1. quickstart.py (Anthropic's quickstart, unchanged)
```
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What should I search for to find the latest developments in renewable energy?",
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
```

### 2. first_call.py (the same call, with the common errors explained)
```
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
```

### 3. setup-windows.txt (PowerShell: type these one at a time)
```
# setup-windows.txt: the Windows (PowerShell) lines from Claude API, Part 3. Type them one at a time; don't run this file.
# From Python's venv docs and Anthropic's quickstart, checked 2026-11-22. Windows PowerShell 5.1 has no &&, so one line each.
# 1. Check Python (3.10 or later). If "python" isn't found, try "py --version", or install it from python.org/downloads
python --version
# 2. Check your key is set, without showing it (any number above 0 means it's set; 0 means see Part 1)
"$env:ANTHROPIC_API_KEY".Length
# 3. Make the folder and the virtual environment, then switch it on ((.venv) appears at the start of the line)
mkdir claude-quickstart
cd claude-quickstart
python -m venv .venv
.venv\Scripts\Activate.ps1
# If PowerShell won't run that line, type this once (from Python's venv docs), then the line above again:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# 4. Install Anthropic's package
pip install anthropic
# 5. Make the file and open it in Notepad (click Yes if it asks to create it), paste quickstart.py's code, save
notepad quickstart.py
# 6. Run it
python quickstart.py
```

### 4. setup-mac.txt (Terminal: type these one at a time)
```
# setup-mac.txt: the Mac (Terminal) lines from Claude API, Part 3. Type them one at a time; don't run this file.
# From Anthropic's quickstart, checked 2026-11-22.
# 1. Check Python (3.10 or later). If it's missing or older, install it from python.org/downloads
python3 --version
# 2. Check your key is set, without showing it (any number above 0 means it's set; 0 means see Part 1)
echo ${#ANTHROPIC_API_KEY}
# 3. Make the folder and the virtual environment, then switch it on ((.venv) appears at the start of the line)
mkdir claude-quickstart && cd claude-quickstart
python3 -m venv .venv && source .venv/bin/activate
# 4. Install Anthropic's package
pip install anthropic
# 5. Make the file and open it in TextEdit, paste quickstart.py's code (paste, don't retype), save with Command-S
touch quickstart.py && open -e quickstart.py
# 6. Run it
python quickstart.py
```

### 5. .env.example (only if you'd rather use a .env file)
```
# .env.example: only if a tool asks for a .env file, or you'd rather not use the environment variable from Part 1.
# 1. pip install python-dotenv   2. copy this file to a new file named .env in the same folder
# 3. put your own key after the = sign   4. add .env to your .gitignore so it never goes up to GitHub (Part 1)
# Never share or commit the .env file. The key below is a fake.
ANTHROPIC_API_KEY=sk-ant-EXAMPLE-not-a-real-key
```
