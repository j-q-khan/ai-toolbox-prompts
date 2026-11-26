# Full code: Gemini Code Assist vs Gemini CLI in 2026: What Still Works in Visual Studio Code

The connect lines and the checklist from this video, written from Google's Gemini CLI and Code Assist docs (checked 2026-11-25). They were written from the docs, not run for this video.

### 1. connect-gemini-cli-to-vs-code.txt
```
# Connect Gemini CLI to Visual Studio Code, from Google's Gemini CLI docs (docs/ide-integration, checked 2026-11-25).
# Written from the docs, not run for this video. Read every line before you use it.
# Before you start: Gemini CLI installed and signed in (Part 1 of this series), with a company Gemini Code Assist
# licence or a paid Gemini API key (Google's blog says paid keys still work; the README calls them "legacy").
# Free and Google AI Pro / Ultra (Google One) accounts can't use Gemini CLI or the Code Assist extension since
# June 18, 2026: Google points them to Antigravity.
# The companion extension needs VS Code 1.99 or later (its package.json, v0.71.1).
# The lines starting with # are notes for you: don't type them.

# 1. In VS Code: File, Open Folder and pick the gemini-scratch folder from Part 1 (or any scratch folder with made-up files only).
# 2. Terminal, New Terminal. A terminal panel opens along the bottom, in your open folder.
# 3. Start Gemini CLI there:
gemini

# 4. It asks "Do you want to connect VS Code to Gemini CLI?". Choose Yes and press Enter.
#    Google's docs: Yes installs the companion extension and turns on the connection.
# 5. Said no, or it never asked? Type this inside Gemini CLI:
/ide install

# 5a. Only if you installed the "Gemini CLI Companion" extension yourself from the VS Code Marketplace
#     (extension id google.gemini-cli-vscode-ide-companion), turn the connection on:
/ide enable

# 6. Check it worked. You should see "Connected to VS Code" and a list of files you've had open:
/ide status

# 7. "Disconnected" or "Directory mismatch"? The terminal can't reach the companion yet, or Gemini CLI is in a
#    different folder from the one open in VS Code. Google's docs: for "Disconnected", open a new terminal in
#    VS Code; for "Directory mismatch", go to the folder that's open in VS Code and restart Gemini CLI.
#    A new terminal from Terminal, New Terminal starts in your open folder (Microsoft's VS Code docs), so it covers both:
#    leave Gemini CLI (/quit), open a new terminal with Terminal, New Terminal, and start gemini again there.

# 8. Ask for a change (made-up file). The change opens in VS Code's diff view (before and after).
#    Accept: the checkmark at the top of the diff tab, or save the file (Ctrl+S, or Cmd+S on a Mac).
#    Reject: the x at the top of the diff tab, or shut the diff tab.
#    Google's docs: if you choose "Allow for this session" in the terminal, changes are auto-accepted and
#    stop showing up in VS Code. To see each change in the diff view first, don't choose it.

# Shortcut: open the Command Palette (Ctrl+Shift+P on Windows, Cmd+Shift+P on a Mac), type Gemini and pick:
Gemini CLI: Run
# It starts a new Gemini CLI session in VS Code's terminal.

# To switch the connection off later, type this inside Gemini CLI:
/ide disable
```

### 2. which-gemini-tool-checklist.md
```
# Gemini Code Assist or Gemini CLI in VS Code: who can use which (facts checked 2026-11-25)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Which one can you use?
- [ ] Free account, or Google AI Pro / Ultra (Google One): neither. Since June 18, 2026, Google's page says the Code Assist IDE extensions stopped serving these accounts, and "This also applies to usage of Gemini CLI." Google points you to Antigravity. Comparison video: https://youtu.be/YXwUvlRdItg
- [ ] Company Gemini Code Assist Standard or Enterprise licence: both still work. Sign in with Google, then pick your company's Google Cloud project (your admin knows which).
- [ ] Paid Gemini API key, no licence: Gemini CLI (Google's blog, May 19, 2026: "Gemini CLI will remain accessible via paid Gemini and Gemini Enterprise Agent Platform API keys"; the README calls these "legacy"). Google's Code Assist agent mode page mentions a key only as a top-up for licensed users, so plan on Gemini CLI, not the extension. A new key starts on the Free Tier: set up billing in Google AI Studio (Part 1).

## Company licence dates (Google's Code Assist deprecation and sunset pages)
- [ ] Since October 9, 2026: no new Standard or Enterprise subscriptions.
- [ ] Existing subscriptions: supported until the end of your contract.
- [ ] Annual plans: renew until January 31, 2027. Extra licences: until January 31, 2027.
- [ ] Monthly plans: renew until December 31, 2027.
- [ ] Gemini Enterprise subscriptions keep their Code Assist entitlement until March 31, 2027.
- [ ] Ask your admin: annual or monthly?

## The four differences
- [ ] Where you work: Code Assist suggests code in grey as you type (Tab accepts) and has a chat panel; Gemini CLI takes requests in a terminal, inside VS Code's terminal.
- [ ] Agent mode: a Preview switch in Code Assist's chat. Google: "Agent mode in VS Code uses the Gemini CLI, which is not optimized for the latest Gemini models."
- [ ] Diff view: both. Code Assist: click Accept. Gemini CLI with the companion: VS Code's own diff view; accept with the checkmark or by saving, reject with the x.
- [ ] How long each lasts: Code Assist renewals stop in 2027 and support stays with the Gemini 3.x models; the README says Gemini CLI isn't optimized for Gemini 4+.

## Connect Gemini CLI to VS Code
- [ ] VS Code 1.99 or later.
- [ ] File, Open Folder, then Terminal, New Terminal, then gemini.
- [ ] "Do you want to connect VS Code to Gemini CLI?": Yes.
- [ ] Never asked? /ide install. Installed it yourself from the Marketplace? /ide enable.
- [ ] /ide status shows "Connected to VS Code".
- [ ] "Disconnected" or "Directory mismatch"? /quit, then start gemini in a new terminal from Terminal, New Terminal.
- [ ] Want each change in the diff view first? Don't choose "Allow for this session": Google's docs say it auto-accepts changes, and they stop showing up in VS Code.

## Prices (context only: not on sale since October 9, 2026)
- [ ] Code Assist Standard was $19.00 per user per month on a 12-month commitment, $22.80 on a monthly one, when checked on 2026-11-25. Enterprise was $45.00 and $54.00.

## Old guides
- [ ] A guide says to sign in to Code Assist or Gemini CLI with a personal Google account, or promises a free tier? It's out of date: Google says those accounts "can no longer use the Login with Google option to access the IDE extensions or Gemini CLI".

Sources: github.com/google-gemini/gemini-cli (README, docs/ide-integration/index.md) ; developers.google.com/gemini-code-assist/docs/deprecations ; docs.cloud.google.com/gemini/docs/codeassist/sunset ; docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer ; developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli ; cloud.google.com/gemini/pricing
```
