# Full code: Claude vs Claude Code vs Cowork: Which One Do You Actually Need?

A plan picker and a checklist written for this video from Anthropic's own pages (checked 2026-11-13). Prices are what they were when checked; re-check the source link in each row before you pay for anything. The CSV was parsed with Python's csv module; nothing was installed or run.

### 1. claude-plans-2026-11-13.csv
```
app,what_anthropic_says_it_is,where_it_works,what_it_can_touch,default_approval,asks_before_deleting,free_plan,cheapest_paid_plan,price_when_checked,usage_pool,checked,source
Claude chat,"Chat on web, desktop, and mobile; search the web, create files, and run code; Artifacts","Web, desktop app, phone","What you put in the conversation, plus apps you connect",Not an agent: answers in the conversation,Not stated in the docs,"Yes, limited usage every 5 hours and every week",Pro for more usage,"$0 on Free; Pro $20 a month, or $17 a month billed yearly",Same pool as Claude Code,2026-11-13,https://claude.com/pricing
Cowork,"Built for non-coding knowledge work: research, analysis, document creation, and other multi-step tasks","Desktop app, web, phone; new tasks on Pro, Max and Ultra run on Anthropic's servers since 2026-10-06","Only folders you connect, with the desktop app open; commands run on Anthropic's servers","Auto on Pro, Max, Ultra and Team; Manual on Enterprise",Yes in every mode,No,Pro,"$20 a month, or $17 a month billed yearly",Not stated in the docs,2026-11-13,https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork ; https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
Claude Code,"Built for software engineering: writing, debugging, and shipping code","Terminal, code editors, desktop app, web","The folder you start it in; commands run on your machine in the terminal","auto mode in the terminal from v2.1.283 (a second model, the classifier, reviews actions); Manual asks before edits, commands and network",Not stated as a separate rule,No,Pro,"$20 a month, or $17 a month billed yearly",Same pool as Claude chat,2026-11-13,https://code.claude.com/docs/en/setup ; https://code.claude.com/docs/en/permission-modes ; https://claude.com/pricing
```

### 2. which-claude.md
```
# Which Claude? A checklist (facts checked 2026-11-13)

## 1. What's the job?
- [ ] Answers, writing help, a quick file or an Artifact: Claude chat (Free works).
- [ ] A multi-step job with documents, spreadsheets or research: Cowork (Pro and up).
- [ ] Code written and run in a folder on your computer: Claude Code (Pro and up).

## 2. Which plan are you on?
- [ ] Free ($0): chat only. No Cowork, no Claude Code.
- [ ] Pro ($20 a month, or $17 a month billed yearly, when checked): all three, one usage pool.
- [ ] Max ($100) or Ultra ($200), when checked: all three, more usage.
- [ ] Team or Enterprise: all three; Cowork starts in Manual on Enterprise.

## 3. Before you hand an agent a job
- [ ] Make a new test folder, never your home folder, and connect or start in only that.
- [ ] Keep a backup of anything you give it.
- [ ] Sensitive files, accounts or sites: switch to Manual first.
- [ ] Check your training setting at claude.ai/settings/data-privacy-controls (the docs don't say whether it starts on or off).
- [ ] Re-check prices at claude.com/pricing: they change.
```
