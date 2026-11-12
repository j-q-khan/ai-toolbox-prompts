# Claude build prompt: Claude Skills for Marketing: Build a Brand Voice Skill

Use this in Claude Code (Pro or higher, or a Console account). Start it in any folder, in plan mode.

Goal: help me build a brand voice skill for my own brand, plus a final check I run by hand, and test both. You ask and suggest; you write nothing until I say yes, and you install, post or send nothing.
Steps, in order:
1. Ask me for my brand's name, who it talks to, and two or three posts I liked and one I didn't, with anything private taken out. Wait for my answers.
2. Draft voice.md: two lines on who we talk to, then pairs of example lines under "We say" and "We don't say". No list of adjectives on its own. Show it and wait for my yes.
3. Ask which words I never want, and draft banned-words.md with a swap beside each one. Show it and wait.
4. Ask which kinds of post I write, and draft formats.md with one short section each: length, layout, hashtags, the call to action. Show it and wait.
5. Write SKILL.md for a skill called brand-voice: only name and description in the frontmatter, the first three dashes on line 1, a name without the words claude or anthropic, and a description under 1,024 characters that names my brand and the kinds of post, in words I'd type. The steps point to each file by name: formats.md first, then voice.md, never invent a price, date or claim, then banned-words.md before showing the draft.
6. Write a second skill called campaign-check with disable-model-invocation: true, which checks every draft against brand-voice's banned words, formats, prices and dates, and ends with "Ready for you to post" or a list of fixes. Tell me it's Claude-Code-only and won't upload to the Claude app.
7. Show me every file in full and wait for my yes. Then create ~/.claude/skills/brand-voice/ and ~/.claude/skills/campaign-check/ and write the files there, and nowhere else.
8. Tell me how to test: "What skills are available?", a plain request for one post, /brand-voice, then "check my campaign" (which shouldn't start it) and /campaign-check. If the skills folder didn't exist when this session started, remind me to type /reload-skills first.
Safety: don't open, print or edit any file with passwords or keys, or any .env file. Don't install, download or run anything, and never post, send or schedule anything. Write only the files I approved, only in those two folders.
Output: the files, the test prompts, and one line on what the brand-voice description matches.
