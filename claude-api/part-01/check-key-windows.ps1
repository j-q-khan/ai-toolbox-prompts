# check-key-windows.ps1: check your Claude API key is set, without showing it (type the line in a NEW PowerShell window)
# Set the key first in the Environment Variables window (Control Panel, System, Advanced system settings,
# Environment Variables, New under User variables, name ANTHROPIC_API_KEY, value your key), then open a new window.
# This prints the key's length, never the key. 0 means it isn't set in this window.
"$env:ANTHROPIC_API_KEY".Length
