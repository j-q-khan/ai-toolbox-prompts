# Full code: Gemini CLI Install on Windows and Mac (2026): Who Can Still Use It

The install lines, the key file, the first task and the checklist from this video, written from Google's Gemini CLI docs and README (checked 2026-11-25). They were written from the docs, not run for this video.

### 1. install-gemini-cli.txt
```
# Gemini CLI install lines, from Google's Gemini CLI README and installation page (checked 2026-11-25).
# Written from the docs, not run for this video. Read every line before you use it.
# Before you install: since June 18, 2026, Gemini CLI doesn't serve free accounts or Google AI Pro and Ultra.
# You need a company Gemini Code Assist licence, or a paid Gemini API key (Google's blog says paid keys still work;
# the README calls them "legacy"). Free accounts: Google points you to Antigravity CLI instead.
#
# Windows: open PowerShell from the Start menu. Mac: open Terminal from Spotlight (Command + Space).
# Node.js first: Google asks for Node.js 20 or later. Download the LTS version from https://nodejs.org/en/download
# (it was v26.13.1 when checked), run the installer, and keep its default choices.
# The lines starting with # are notes for you: don't type them.

# 1. Check Node.js is installed (you should see a version number starting with v):
node --version

# 2. Install Gemini CLI (Windows PowerShell or Mac Terminal). -g means global: you can start it from any folder.
npm install -g @google/gemini-cli

# 2a. Windows only: if PowerShell says "running scripts is disabled on this system", Windows is blocking
# small program files called scripts, which npm and Gemini CLI use there. This line, from Microsoft's PowerShell docs
# (about_Execution_Policies), lets scripts made on this computer run, for your account only; downloaded scripts
# still need a signature. If it asks whether to change the execution policy, type Y and press Enter, then try again.
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2b. Mac alternative, only if you already use Homebrew. Use this OR the npm line, never both:
brew install gemini-cli

# 3. Check it worked (it was 0.71.1, the newest stable version, on 2026-11-25).
# If your terminal can't find gemini, open a new terminal window and try again.
gemini --version

# Later: update to the newest stable version (Google publishes one every Tuesday):
npm install -g @google/gemini-cli@latest
```

### 2. gemini-env-file.txt
```
# Keep your key in Gemini CLI's .env file instead of typing it into the terminal.
# Written from Gemini CLI's authentication docs ("Persisting environment variables"), checked 2026-11-25.
# Gemini CLI loads the first .env file it finds, searching up from the folder you start it in,
# then the .env inside the .gemini folder in your home folder. Only one file is loaded, never merged.
# If you already keep a file called .env in a folder above your work, that one may be loaded instead.
#
# Windows (PowerShell): these two lines make the folder and open the file in Notepad.
# If Notepad asks whether to create the file, click Yes.
New-Item -ItemType Directory -Force -Path "$HOME\.gemini" | Out-Null
notepad "$HOME\.gemini\.env"

# Mac (Terminal): these three lines make the folder and the file, and open it in TextEdit.
mkdir -p ~/.gemini
touch ~/.gemini/.env
open -e ~/.gemini/.env

# In the file, type ONE of these lines, with no spaces and no quotes, then save (Ctrl+S on Windows, Command+S on a Mac).
# No quotes, because TextEdit can turn straight quotes into curly ones, which would break the line.
# With a paid key from Google AI Studio (https://aistudio.google.com/apikey): replace paste-your-key-here with your own key.
# A new key starts on the Free Tier: click Set up billing in AI Studio and prepay credit (at least $5 when checked,
# https://ai.google.dev/gemini-api/docs/billing) to make it a paid key.
GEMINI_API_KEY=paste-your-key-here

# With a company Code Assist licence: your admin gives you your company's Google Cloud project ID.
# Then choose "Sign in with Google" with your work account when Gemini CLI starts.
GOOGLE_CLOUD_PROJECT=your-company-code-from-your-admin

# Never put the company line in the file if you don't have a company licence:
# Google's troubleshooting page says it forces a company subscription check, and you'll see a "named user" error.
# Keep this file private: never share it, sync it to a shared folder, or show it in a screenshot.
# If your key ever leaks, delete it in Google AI Studio and make a new one.
```

### 3. first-task.txt
```
# A first task in a scratch folder (a throwaway test folder), with made-up data only.
# Written from Gemini CLI's quickstart, tools reference and file management docs, checked 2026-11-25. Not run for this video.
#
# Windows (PowerShell): make the folder, move into it, add a made-up notes file, start Gemini CLI.
mkdir "$HOME\gemini-scratch"
cd "$HOME\gemini-scratch"
Set-Content -Path notes.txt -Value "Test Bakery: open 9 to 5, closed on Sundays. Made-up notes for a test."
gemini

# Mac (Terminal): the same four steps.
mkdir -p ~/gemini-scratch
cd ~/gemini-scratch
echo "Test Bakery: open 9 to 5, closed on Sundays. Made-up notes for a test." | tee notes.txt
gemini

# The first time, it asks "Do you trust the files in this folder?": choose "Trust folder (gemini-scratch)".
# Not "Trust parent folder": here the parent is your whole home folder.
# It then says "Gemini CLI is restarting to apply the trust changes..." and starts again: that's normal.
# Then choose how to sign in: "Use Gemini API Key" (already picked if your key is in the .env file),
# or "Sign in with Google" with your work account if your company gave you a licence.
# Then type this request (the @ makes Gemini CLI look at that file first):
@notes.txt Write a one-line summary of this file in a new file called summary.txt.

# Gemini CLI shows the new file and asks "Apply this change?". Choose "Allow once" (yes to this one change only).
# Then leave Gemini CLI:
/quit

# Check it worked: show the new file (Windows first, then Mac).
Get-Content summary.txt
cat summary.txt

# When you're done, you can delete the whole gemini-scratch folder.
```

### 4. gemini-cli-checklist.md
```
# Gemini CLI install checklist (facts checked 2026-11-25)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you still sign in?
- [ ] A company Gemini Code Assist Standard or Enterprise licence (Google's README: "Designed for Gemini Code Assist Standard / Enterprise licenses"), or
- [ ] A paid Gemini API key (Google's blog, May 19, 2026: "Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys"; the README calls these "legacy").
- [ ] Neither? Free accounts and Google AI Pro / Ultra moved to Antigravity CLI on June 18, 2026. Comparison video: https://youtu.be/YXwUvlRdItg

## Install
- [ ] Node.js 20 or later (Google's install page). Node.js 20 reached end of life on April 30, 2026, so take the LTS version from https://nodejs.org/en/download (v26.13.1 when checked).
- [ ] Windows: PowerShell. Mac: Terminal.
- [ ] node --version shows a version number.
- [ ] npm install -g @google/gemini-cli (or, on a Mac with Homebrew, brew install gemini-cli: one or the other).
- [ ] Windows says "running scripts is disabled"? Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser (Microsoft's docs; your account only), answer Y, try again.
- [ ] gemini --version shows a number (0.71.1 was the newest stable version on 2026-11-25). Can't find gemini? Open a new terminal window.

## Sign in
- [ ] Key: make it at https://aistudio.google.com/apikey, then click Set up billing and prepay credit (at least $5 when checked), because a new key starts on the Free Tier. Put GEMINI_API_KEY=your-key (no spaces, no quotes) in the .env file inside the .gemini folder in your home folder.
- [ ] Company licence: put GOOGLE_CLOUD_PROJECT=the-ID-from-your-admin in that file, then choose Sign in with Google with your work account.
- [ ] One or the other. Using a key without a company licence? Leave the company line out: Google's troubleshooting page says it forces a company subscription check and a "named user" error.
- [ ] Keep the .env file private: no shared folders, no screenshots, no chats.

## First task
- [ ] Use a scratch folder with made-up files only.
- [ ] Asked "Do you trust the files in this folder?" Choose Trust folder for the scratch folder, not Trust parent folder. It restarts itself once: that's normal.
- [ ] When Gemini CLI asks "Apply this change?", read the change, then choose Allow once.
- [ ] /quit leaves Gemini CLI.

## Old guides
- [ ] A guide says "Sign in with Google" on a free account, or "1,000 free requests a day"? It's out of date: Google says those accounts "can no longer use the Login with Google option".

## Company licence dates (Google's Code Assist deprecations page)
- [ ] After October 9, 2026: no new Standard or Enterprise subscriptions.
- [ ] After January 31, 2027: no annual renewals and no extra licences.
- [ ] After December 31, 2027: no monthly renewals.

## Stay current
- [ ] New stable version every Tuesday: npm install -g @google/gemini-cli@latest

Sources: github.com/google-gemini/gemini-cli (README, docs/get-started/installation.mdx, docs/get-started/authentication.mdx, docs/resources/troubleshooting.md) ; developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli ; developers.google.com/gemini-code-assist/docs/deprecations ; nodejs.org/en/download
```
