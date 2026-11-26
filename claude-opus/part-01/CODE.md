# Full code: Claude Opus 5.5: What's New, What It Costs and Who Should Use It

The checklist, the Claude Code lines and the example prompt from this video, written from Anthropic's pricing page, models docs, Claude Code docs and help pages (checked 2026-11-26). They were written from the docs, not run for this video.

### 1. claude-opus-checklist.md
```
# Claude Opus 5.5 checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What it is
- [ ] Claude Opus 5.5, released September 22, 2026. Anthropic (November 9, 2026): "start with Claude Opus 5.5, our strongest daily driver".
- [ ] Not the most capable any more: Claude Fable 5.2 is "Anthropic's most capable model open to all customers".
- [ ] Built "For long-running agentic coding and knowledge work" (Anthropic's model docs).

## What's new in 5.5 (Anthropic's words)
- [ ] "costs 40% less to run than Opus 5"
- [ ] "generates output more than 30% faster than Opus 5"
- [ ] "writing clearer and easier to follow"
- [ ] Thinking is always on: "no longer available with thinking mode switched off". Effort is the dial: low, medium, high, xhigh, max. Claude Code starts Opus 5.5 at medium.

## Plans (prices when checked, November 26, 2026: https://claude.com/pricing)
- [ ] Free: $0. No Opus. Sonnet and Haiku: yes. No Claude Code.
- [ ] Pro: $20 a month billed monthly, or $17 a month billed yearly ($200 up front). Opus: yes.
- [ ] Max: $100 a month, 5x Pro usage. Opus: yes.
- [ ] Ultra: $200 a month, 10x Pro usage each week. Opus: yes.
- [ ] Team: standard seat $20 a seat a month billed yearly, $25 monthly. Enterprise: seat price plus usage. Opus: yes on both.
- [ ] Limits: no Opus-only number. "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are."
- [ ] API: $4 per million input tokens, $20 per million output tokens (Opus 5.5, when checked).

## Switch to it
- [ ] Claude app (web or desktop, Windows or Mac): click the model name next to the send button, pick Opus 5.5 (or More models). The suggested effort is marked Default.
- [ ] You can change the model or effort at any point; it applies from Claude's next reply.
- [ ] Claude Code (Pro and up): it starts on Opus 5.5. To switch back: /model opus (this also makes it your default for new sessions)
- [ ] Needs Claude Code v2.1.280 or later. Won't switch? In a new terminal window: claude update
- [ ] Effort: /effort opens a slider. Enter saves it as your default; S keeps it for this session only.

## Its limits
- [ ] Slower than Sonnet 5.5 and Haiku 5.5 (Anthropic's latency column).
- [ ] Gives back text and code only: no pictures or video files of its own.
- [ ] Reliable knowledge to June 2026: give it newer pages or files yourself.
- [ ] Hard technical job still falling short at a higher effort? Anthropic says move up to Fable 5.2 (API $8 / $40 per million tokens, when checked).

## Habit
- [ ] Near your limit? Low or medium effort for routine jobs (the help page: they stretch your usage further); high and above for the hard ones.

Sources: claude.com/pricing ; anthropic.com/claude-opus-5-5 ; anthropic.com/claude-fable-and-mythos-5-2 ; platform.claude.com/docs/en/about-claude/models/overview ; code.claude.com/docs/en/model-config ; support.claude.com/en/articles/8664678
```

### 2. claude-code-model-lines.txt
```
# Claude Code lines for Opus 5.5, from Anthropic's Claude Code docs (model-config), checked 2026-11-26.
# Written from the docs, not run for this video. Read every line before you use it.
# Claude Code is on Pro, Max, Ultra, Team and Enterprise, not Free (claude.com/pricing, checked 2026-11-26).
# Not installed yet? See the Claude Code for Beginners playlist linked in the description.
# Windows: PowerShell. Mac: Terminal. The lines starting with # are notes for you: don't type them.

# 1. Opus 5.5 needs Claude Code v2.1.280 or later. Type this in the terminal (not inside Claude Code) to update:
claude update

# 2. Start Claude Code on Opus (the docs' own example):
claude --model opus

# 3. Already inside Claude Code? Switch to Opus now (typed like this, it also becomes your default for new sessions):
/model opus

# 4. Or open the model picker (the left and right arrow keys move its effort slider):
/model

# 5. Set the effort. On its own, this opens a slider: Enter saves the level as your default, S keeps it for this session only.
/effort

# 6. Or set a level by name (low, medium, high, xhigh). This saves it as your default:
/effort medium
```

### 3. example-prompt.txt
```
# The example job from this video, with made-up data only. Paste your own made-up or non-private notes after it.
# Written for this video, not run. Works on any model; Opus 5.5 is built for long jobs like this.
Here are my meeting notes for Test Bakery (made up). Turn them into a one-page plan with a table of tasks, who does each one and by when. Keep it to one page and tell me anything the notes leave unclear.
```
