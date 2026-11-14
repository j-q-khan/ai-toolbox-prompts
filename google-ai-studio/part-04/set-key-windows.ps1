# set-key-windows.ps1: set your Gemini API key for this PowerShell window only (type the lines one at a time)
# Put your own key between the quotes. EXAMPLE-NOT-A-REAL-KEY is a fake, so this line alone won't work.
# Typed commands can be saved in PowerShell's history file, so to keep the key for good,
# use Google's Windows steps instead: search "Environment Variables", click Environment Variables,
# New... under User variables, name GEMINI_API_KEY, value your key, OK, then open a new PowerShell window.
$env:GEMINI_API_KEY = "EXAMPLE-NOT-A-REAL-KEY"
# Check it: this prints the key's length, never the key (0 means it isn't set in this window)
$env:GEMINI_API_KEY.Length
