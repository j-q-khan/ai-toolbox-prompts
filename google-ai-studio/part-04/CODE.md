# Full code: How to Get a Gemini API Key in Google AI Studio (and Keep It Safe)

Commands and a small script written for this video from Google's docs, with Microsoft's page for the PowerShell line (checked 2026-11-13). key_check.py was checked with Python's py_compile only, and the shell lines by syntax only; nothing was installed or run, and no key was used. The key shown is a fake.

### set-key-windows.ps1 (PowerShell)
```
# set-key-windows.ps1: set your Gemini API key for this PowerShell window only (type the lines one at a time)
# Put your own key between the quotes. EXAMPLE-NOT-A-REAL-KEY is a fake, so this line alone won't work.
# Typed commands can be saved in PowerShell's history file, so to keep the key for good,
# use Google's Windows steps instead: search "Environment Variables", click Environment Variables,
# New... under User variables, name GEMINI_API_KEY, value your key, OK, then open a new PowerShell window.
$env:GEMINI_API_KEY = "EXAMPLE-NOT-A-REAL-KEY"
# Check it: this prints the key's length, never the key (0 means it isn't set in this window)
$env:GEMINI_API_KEY.Length
```

### set-key-mac.sh (Mac Terminal, zsh)
```
# set-key-mac.sh: set your Gemini API key on a Mac (zsh, the default since macOS 10.15); type the lines one at a time, don't run this file
# Put your own key between the quotes. EXAMPLE-NOT-A-REAL-KEY is a fake, so this line alone won't work.
# This window only:
export GEMINI_API_KEY="EXAMPLE-NOT-A-REAL-KEY"
# Check it: this prints the key's length, never the key (0 means it isn't set in this window)
echo ${#GEMINI_API_KEY}
# Keep it for every new window: this creates ~/.zshrc if it's missing and opens it in TextEdit (-e means TextEdit).
# Keep it plain text: if TextEdit shows a formatting bar, choose Format, then Make Plain Text.
# Paste the export line at the bottom, with your key, press Command-S to save, then quit TextEdit.
touch ~/.zshrc && open -e ~/.zshrc
# Or skip TextEdit and add the line from Terminal: type the line below without the leading "# ".
# Use two > signs, because one > would wipe the file.
# echo 'export GEMINI_API_KEY="EXAMPLE-NOT-A-REAL-KEY"' >> ~/.zshrc
# The file is hidden because its name starts with a dot. To find it in Finder: press Shift-Command-G and type ~/.zshrc
# On an older Mac that uses bash, use ~/.bash_profile instead of ~/.zshrc in these lines (Terminal opens bash as a login shell).
# Load it into this window
source ~/.zshrc
```

### key_check.py
```
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
```
