# Full code: Claude Code Skills Tutorial: Make Your First Skill

A first skill written for this video from Anthropic's Claude Code skills docs (checked 2026-11-11), in the portable format: only name and description in the frontmatter, a name without "claude", a description under 1,024 characters, so it works in Claude Code and also uploads to the Claude app. Instructions only, no scripts. The frontmatter was parsed with a YAML parser; nothing was installed or run.

### 1. Make the folder (type it in your terminal before you start Claude Code)
```
# Windows: PowerShell. Mac and Linux: Terminal. (It doesn't work in the old Command Prompt.)
# It makes ~/.claude, then skills inside it, then email-reply inside that.
mkdir -p ~/.claude/skills/email-reply
# On Windows, ~/.claude is the .claude folder in your user folder, C:\Users\you\.claude
# Claude Code already open when you made the skills folder? Type /reload-skills in it.
# Saving SKILL.md in Notepad: set Save as type to All files, and type this in File name:
#   %USERPROFILE%\.claude\skills\email-reply\SKILL.md
# Saving in TextEdit on a Mac: choose Format, then Make Plain Text, before you paste.
#   In the save box, press Shift-Command-G and type ~/.claude/skills/email-reply
#   If it asks which ending to use, click Use .md
```

### 2. email-reply/SKILL.md (the file name in capitals, exactly SKILL.md; the first --- on line 1)
```
---
name: email-reply
description: Drafts a short, clear reply to an email the user pastes in, answering every question and ending with one next step. Use when the user pastes an email or message and asks for a reply, a response, or help writing back.
---

# Email reply

1. Find every question and request in the email.
2. Answer each one in plain words, in the order they were asked.
3. If an answer needs something you don't know, ask the user. Don't guess.
4. End with one clear next step, like a time to talk or what happens next.
5. Never make up a date, a price, a name or a promise that isn't in the user's message.
```

### 3. The step to add at the end of SKILL.md in chapter 5 (it points to the supporting file)
```
6. Before you show the draft, go through reply-checklist.md and fix anything that fails.
```

### 4. email-reply/reply-checklist.md (the supporting file step 6 points to)
```
# Reply checklist

Check the draft against every line, and fix it if a line fails.

- Every question and request in the email has an answer, or a question back to the user.
- It's under 150 words.
- It ends with one clear next step.
- No date, price, name or promise appears that the user didn't give you.
- No placeholder like [your name] is left in.
- It doesn't open with "I hope this email finds you well".
```

### 5. A made-up email to test with, and the request with your facts
```
Hi,

Thanks for sending the quote. Two quick questions: does the price include delivery, and could the work start before the end of the month?

Also, who should we contact if something goes wrong after installation?

Thanks

Can you write a reply to this? Delivery's included, we can start on the 20th, and they should email our support address.
```

### 6. Where the files go
```
~/.claude/
└── skills/
    └── email-reply/              # personal: works in every folder on this computer
        ├── SKILL.md              # section 2, plus the step from section 3
        └── reply-checklist.md    # section 4: opened only when step 6 says so

your-repo/
└── .claude/
    └── skills/
        └── a-team-skill/         # for one folder only: share it through Git
            └── SKILL.md
```
