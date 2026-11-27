# Full code: Claude Opus vs Sonnet: Which Claude Model to Use (and When Fable Is Worth It)

The checklist, the Claude Code lines and the example prompt from this video, written from Anthropic's models docs, pricing pages, Fable page and Claude Code docs (checked 2026-11-26). They were written from the docs, not run for this video.

### 1. claude-opus-vs-sonnet-checklist.md
```markdown
# Claude Opus vs Sonnet vs Haiku vs Fable checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What each one is for (Anthropic's words)
- [ ] Sonnet 5.5: "The best combination of speed and intelligence"; "a faster, lower-cost complement to Opus 5.5" for "well-scoped everyday tasks".
- [ ] Opus 5.5: "For long-running agentic coding and knowledge work". "If you're unsure which model to use, start with Claude Opus 5.5 for most workloads."
- [ ] Fable 5.2: "Anthropic's most capable model open to all customers", "For demanding reasoning and long-horizon agentic work".
- [ ] Haiku 5.5: "For high-volume, latency-sensitive tasks such as classification, extraction, and routing".

## The differences that decide it
- [ ] Speed: Sonnet "Fast", Haiku "Fastest"; Opus and Fable a step slower. Real speed depends on prompt length, answer length and effort.
- [ ] Effort: low, medium, high, xhigh (extra high), max. Opus 5.5 starts at medium. Higher effort: "more thorough responses, but they take longer and use more tokens, so you'll reach your usage limits faster."
- [ ] "Tuning effort is often a better lever than switching models."
- [ ] Plans (when checked, November 26, 2026): Opus is not on Free; Sonnet and Haiku are. Fable is not on Free; paid plans count it in different ways: check https://claude.com/pricing
- [ ] Limits: "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are."

## API prices per million tokens (when checked, November 26, 2026: https://platform.claude.com/docs/en/about-claude/pricing)
- [ ] Sonnet 5.5: $2 in / $10 out
- [ ] Opus 5.5: $4 in / $20 out (2x Sonnet)
- [ ] Fable 5.2: $8 in / $40 out (2x Opus)
- [ ] Haiku 5.5: from $0.10 in / $0.50 out ($0.50 / $2.50 for prompts over 100,000 tokens)

## Claude Code (Pro and up, not Free)
- [ ] /model opusplan: Opus in plan mode, Sonnet to carry the plan out. Typed with /model, it also becomes your default for new sessions.
- [ ] Plan mode: press Shift+Tab until the bar at the bottom says "plan mode on" (each press moves to the next mode), or start one message with /plan. At the approval question, Shift+Tab approves the plan: press Esc first to stop.
- [ ] Fable can bill to usage credits on some plans and seats; the /model picker then shows "Requires usage credits".

## Fable's catches (anthropic.com/claude/fable)
- [ ] "Using Fable models requires 30-day data retention for safety monitoring by default."
- [ ] "Many queries on topics including biology and cybersecurity will instead receive a response from Opus models."
- [ ] Move up only "If your evals at xhigh or max effort still fall short on demanding reasoning or long-horizon agentic work".

## Who picks which
- [ ] On Free, or quick questions and everyday writing: Sonnet 5.5.
- [ ] Paying, with long documents, research or coding with many steps: Opus 5.5 (opusplan in Claude Code).
- [ ] Opus at its highest effort still not enough, and the catches are fine for you: Fable 5.2.

Sources: platform.claude.com/docs/en/about-claude/models/overview ; platform.claude.com/docs/en/about-claude/models/choosing-a-model ; platform.claude.com/docs/en/about-claude/pricing ; claude.com/pricing ; anthropic.com/claude/sonnet ; anthropic.com/claude/fable ; code.claude.com/docs/en/model-config ; code.claude.com/docs/en/permission-modes ; support.claude.com/en/articles/8664678
```

### 2. claude-code-opusplan-lines.txt
```text
# Claude Code lines for opusplan, from Anthropic's Claude Code docs (model-config and permission-modes), checked 2026-11-26.
# Written from the docs, not run for this video. Read every line before you use it.
# Claude Code is on Pro, Max, Ultra, Team and Enterprise, not Free (claude.com/pricing, checked 2026-11-26).
# Not installed yet? See the Claude Code for Beginners playlist linked in the description.
# Windows: PowerShell. Mac: Terminal. The lines starting with # are notes for you: don't type them.

# 1. Inside Claude Code, where you type a message: plan with Opus, carry out with Sonnet (this also becomes your default for new sessions):
/model opusplan

# 2. Go into plan mode with the keyboard: press these two keys together (it's a key press, not something you type).
#    Each press moves to the next mode, so keep pressing until the bar at the bottom says "plan mode on":
Shift+Tab

# 3. Or put plan mode on one message only, by starting the message with this:
/plan

# 4. At the plan approval question, Shift+Tab approves the plan. To stop instead, press Esc first.

# 5. Back to Opus for everything (also your default for new sessions):
/model opus

# 6. Or Sonnet for everything:
/model sonnet
```

### 3. example-prompt.txt
```text
# The example from this video, with made-up data only. Swap in your own jobs (nothing private).
# Written for this video, not run. Works on any model, Free plan included.
I use Claude for these jobs (made up for Test Bakery): answering quick customer emails, writing a weekly menu, and turning 40 pages of supplier notes into a one-page plan. For each job, tell me whether Sonnet 5.5, Opus 5.5 or Haiku 5.5 fits best and what effort level to start at, in one line each, and say which jobs might need Fable 5.2.
```
