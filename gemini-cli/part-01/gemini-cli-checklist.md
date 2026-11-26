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
