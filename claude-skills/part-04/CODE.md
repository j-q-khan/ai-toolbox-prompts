# Full code: Claude Skills for Marketing: Build a Brand Voice Skill

Two skills written for this video from Anthropic's Claude Code skills docs (checked 2026-11-12), for a made-up candle shop. brand-voice is portable (only name and description in the frontmatter, a name without "claude"), so it works in Claude Code and also uploads to the Claude app. campaign-check sets disable-model-invocation, a Claude Code key, so it's Claude-Code-only and won't upload to the Claude app. Instructions only, no scripts. Both frontmatter blocks were parsed with a YAML parser; nothing was installed or run.

### 1. Make the two folders (type each line in your terminal before you start Claude Code)
```
# Windows: PowerShell. Mac and Linux: Terminal. (Not the old Command Prompt.)
mkdir -p ~/.claude/skills/brand-voice
mkdir -p ~/.claude/skills/campaign-check
# One folder per line: PowerShell's mkdir gives an error if you put both on one line.
# Claude Code already open when you made the skills folder? Type /reload-skills in it.
# Saving in Notepad: set Save as type to All files, and type the full path in File name, e.g.
#   %USERPROFILE%\.claude\skills\brand-voice\SKILL.md
#   %USERPROFILE%\.claude\skills\brand-voice\voice.md   (and the same for the other files)
# Saving in TextEdit on a Mac: Format, then Make Plain Text, before you paste.
#   In the save box, press Shift-Command-G and type ~/.claude/skills/brand-voice
#   If it asks which ending to use, click Use .md
```

### 2. brand-voice/SKILL.md (portable: only name and description; the first --- on line 1)
```
---
name: brand-voice
description: Writes marketing posts in the Hollowfern Candles brand voice, following its tone, banned words and post formats. Use when the user asks for an Instagram caption, a newsletter email, a product description or any other marketing post for Hollowfern Candles, or asks to make copy sound like the brand.
---

# Hollowfern brand voice

1. Work out which kind of post the user wants, then open formats.md and follow that format's length and layout. If it isn't listed there, ask.
2. Write in the voice described in voice.md. Match the feel of its example lines; don't reuse the lines themselves.
3. Never invent a price, date, discount, scent note or claim the user didn't give you. Ask instead.
4. Before you show the draft, check every word against banned-words.md and use the swap it gives.
5. Show the draft, then one line saying which format from formats.md you followed.
```

### 3. brand-voice/voice.md
```
# Hollowfern voice

## Who we're talking to
People who buy a candle as a small treat for themselves or a gift for a friend.
We talk like a friend at a market stall: plain, warm and a little dry. Short sentences.

## We say
- Poured by hand in small batches, so every jar's a little different.
- Smells like a walk in the woods after rain. Burns for about 40 hours.
- Back in stock on Friday. We made 200, and that's the lot.

## We don't say
- Indulge in our luxurious artisan creations!
- Elevate your space with this must-have scent experience.
- Hurry, don't miss out!!!

## Habits
- At most one exclamation mark in a post.
- No emoji in the first line. At most one emoji in a post.
- Say what the candle smells like, not how it will change your life.
```

### 4. brand-voice/banned-words.md
```
# Banned words

Never use these. Use the swap instead.

- hurry, don't miss out: give the real end date, if the user gave one. If not, leave it out.
- luxurious, luxury: say what it's made of (soy wax, cotton wick).
- indulge: say what they'll do with it (light it, give it).
- elevate, transform: say what it smells like.
- artisan, artisanal: say "poured by hand".
- must-have, game-changer: leave it out.
- best ever, perfect: say one plain thing you like about it.
```

### 5. brand-voice/formats.md
```
# Post formats

## Instagram caption
- Under 60 words.
- First line: the candle's name and one plain thing about it.
- One call to action, like "Find it on the shop page."
- 3 hashtags at the end: #hollowfern, plus two that fit.

## Newsletter intro
- Under 90 words.
- First line names the candle.
- One link, written out in full, only if the user gave it.

## Product description
- Under 120 words.
- Scent notes and burn time only if the user gives them.
- End with the size and the price, if the user gave them.
```

### 6. campaign-check/SKILL.md (Claude Code only: disable-model-invocation won't upload to the Claude app)
```
---
name: campaign-check
description: Final check of a finished Hollowfern Candles marketing campaign before the user posts or sends it. Checks every draft against the brand-voice skill and lists what to fix.
disable-model-invocation: true
---

# Campaign check

Never post, send, schedule or upload anything yourself.

1. Load the brand-voice skill, and use its banned-words.md and formats.md for this check.
2. List every draft in the user's message.
3. For each draft, check:
   - No word from banned-words.md.
   - It matches its format in formats.md: length, layout and one call to action.
   - Every price, date, discount and link was given by the user.
   - The same offer has the same price and end date in every draft.
4. Show each draft's result: "Pass", or a numbered list of fixes.
5. If every draft passes, end with "Ready for you to post." If not, end with the fixes, and nothing else.
```

### 7. Prompts to test with
```
What skills are available?

Write an Instagram caption for our new autumn candle, Rainy Bracken. It's $18 and out on October 3.

/brand-voice Write an Instagram caption for our new autumn candle, Rainy Bracken. It's $18 and out on October 3.

Check my campaign.

/campaign-check
```

### 8. Where the files go
```
~/.claude/
└── skills/
    ├── brand-voice/            # portable: name and description only
    │   ├── SKILL.md            # section 2: the steps, most pointing to a file
    │   ├── voice.md            # section 3: who we talk to, and example lines
    │   ├── banned-words.md     # section 4: each word with its swap
    │   └── formats.md          # section 5: one section per kind of post
    └── campaign-check/         # Claude Code only: disable-model-invocation
        └── SKILL.md            # section 6: run it by typing /campaign-check
```
