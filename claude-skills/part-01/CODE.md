# Full code: Claude Skills Explained: What a Skill Is and When to Use One

An example skill folder written for this video from Anthropic's skills docs (checked 2026-11-11), in the portable format: only name and description in the frontmatter, a name without "claude", a description under 1,024 characters, so it works in Claude Code and uploads to the Claude app. Instructions only, no scripts. The frontmatter was parsed with a YAML parser; nothing was installed or run.

### 1. The folder (Claude Code, personal skill: put it in ~/.claude/skills/)
```
meeting-notes/
├── SKILL.md
└── template.md
# Claude Code: ~/.claude/skills/meeting-notes/SKILL.md, then ask for a meeting summary, or type /meeting-notes
# Claude app: zip the meeting-notes folder, then Customize, Skills, +, Create skill, Upload a skill
```

### 2. meeting-notes/SKILL.md (the file name in capitals, exactly SKILL.md)
```
---
name: meeting-notes
description: Turns rough meeting notes into a short summary with decisions, action items and open questions. Use when the user pastes meeting notes or a call transcript, or asks for a meeting summary.
---

# Meeting notes

1. Find every decision and write each one as a single sentence.
2. Find every action item: the task, who owns it (as written in the notes) and the due date, or "no date" if none is given.
3. List the open questions that nobody answered.
4. Fill in template.md in that order, and keep the whole summary under 200 words.
5. Never invent a name, a date or a decision that isn't in the notes. If something is unclear, put it under open questions.
```

### 3. meeting-notes/template.md (the extra file the steps point to)
```
## Summary
Two or three sentences.

## Decisions
- One sentence each.

## Action items
- Task / owner / due date

## Open questions
- One line each.
```
