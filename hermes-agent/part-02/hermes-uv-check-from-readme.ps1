# The Hermes Agent README's own check for a uv.exe antivirus flag on Windows,
# quoted exactly (Troubleshooting, checked 2026-11-14). The README calls the flag "a false positive".
# It installs the GitHub CLI if needed and asks you to log in to GitHub.
# Success: attestation says "Verification succeeded" and the last line prints True.
# This file deliberately leaves out the README's whitelisting lines: check first.
# The README's lines compare against the x86_64 (Intel or AMD) build of uv, and they leave uv.zip and
# the uv_x folder in your TEMP folder; delete both when you're done.
# Source: https://github.com/NousResearch/hermes-agent (README, Troubleshooting)

# Install GitHub CLI if needed
winget install --id GitHub.cli

# Login to GitHub
gh auth login

# Run verification
$uv = "$env:LOCALAPPDATA\hermes\bin\uv.exe"
$ver = (& $uv --version).Split(' ')[1]
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$zip = "$env:TEMP\uv.zip"
Invoke-WebRequest "https://github.com/astral-sh/uv/releases/download/$ver/uv-x86_64-pc-windows-msvc.zip" -OutFile $zip -UseBasicParsing
gh attestation verify $zip --repo astral-sh/uv
Expand-Archive $zip "$env:TEMP\uv_x" -Force
(Get-FileHash "$env:TEMP\uv_x\uv.exe").Hash -eq (Get-FileHash $uv).Hash
