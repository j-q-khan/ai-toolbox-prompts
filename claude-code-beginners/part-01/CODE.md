# Full code: How to Use Claude Code: What It Is, What It Costs, and Where to Start (2026)

A dated plans table and a before-you-install checklist written for this video from Anthropic's own pricing page, docs and help centre (checked 2026-11-13). Prices are what they were when checked; re-check the source link in each row before you pay for anything. The CSV was parsed with Python's csv module; nothing was installed or run.

### 1. claude-code-plans-2026-11-13.csv
```
plan,includes_claude_code,price_when_checked,usage_wording,limits,training_on_your_data,checked,source
Free,No,$0,Limited usage,Every 5 hours and every week,"Used for training when the setting is on (personal plan)",2026-11-13,https://claude.com/pricing
Pro,Yes,"$20 a month, or $17 a month billed yearly ($200 up front)",More usage than Free,"5-hour and weekly, shared with Claude chat","Used for training when the setting is on (personal plan)",2026-11-13,https://claude.com/pricing
Max,Yes,$100 a month,5x Pro usage,"5-hour and weekly, shared with Claude chat","Used for training when the setting is on (personal plan)",2026-11-13,https://claude.com/pricing
Ultra,Yes,$200 a month,10x Pro usage every week,"Weekly; no 5-hour limit for verified accounts; shared with Claude chat","Used for training when the setting is on (personal plan)",2026-11-13,https://claude.com/pricing
Team,Yes,Priced per seat (see the source),More usage than Pro (standard seat),Per seat,"Not used for training unless the company opts in (commercial terms)",2026-11-13,https://claude.com/pricing
Enterprise,Yes,Per seat plus usage (see the source),Usage cost scales with model and task,Per seat,"Not used for training unless the company opts in (commercial terms)",2026-11-13,https://claude.com/pricing
Pay as you go (Claude Console),Yes,Pre-paid credits,Billed for what you use,None stated as 5-hour or weekly,"Not used for training unless the customer opts in (commercial terms)",2026-11-13,https://code.claude.com/docs/en/setup
```

### 2. before-you-install-checklist.md
```
# Claude Code: before you install (facts checked 2026-11-13)

## 1. A plan that includes Claude Code
- [ ] Pro or higher (the free plan doesn't include Claude Code). Pro was $20 a month, or $17 a month billed yearly, when checked.
- [ ] I know the limits (every 5 hours and every week) are shared with Claude chat.

## 2. A computer that meets the requirements
- [ ] Mac: macOS 13 or newer. Check: Apple menu, About This Mac.
- [ ] Windows: Windows 10 version 1809 or newer (Windows 11 counts). Check: right-click Start, Settings, System, About.
- [ ] 4 GB of memory or more, and an internet connection.
- [ ] Claude Code is offered in my country: https://www.anthropic.com/supported-countries

## 3. Privacy, decided before the first session
- [ ] I've chosen my training setting: https://claude.ai/settings/data-privacy-controls
- [ ] I'll never paste a password or a key into a prompt (sessions are saved as plain text on my computer for 30 days or more).

## 4. Ready for Part 2
- [ ] I'll use a new, empty test folder, never my Desktop or my home folder.
- [ ] I'll switch on Manual mode before the first task (Part 2 shows how).
```
