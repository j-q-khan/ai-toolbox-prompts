# Full code: Claude Agents in Cowork: Sub-agents and Scheduled Tasks for Business Work

The two scheduled-task prompts and the setup checklist, written from Anthropic's Cowork help pages, checked 2026-11-24. They were not run for this video.

### 1. weekly-rivals-brief.txt (the research job)
```
# Weekly research brief: a scheduled task for Claude Cowork (written from Anthropic's help pages, checked 2026-11-24; not run for this video)
# Replace everything in square brackets first. Test Bakery and the rival names are made-up examples.
# Then paste everything below the dashed line into Claude, and add how often it should run, for example:
# Run this every Monday at 9 in the morning.
# Don't pick a folder for this task, so it can run with your computer asleep.
# ------------------------------------------------------------
Every week, research what changed for my business and write me a one-page brief.

My business: [Test Bakery, a small bakery in your town].
Rivals to track: [Rival 1], [Rival 2], [Rival 3]. Their public websites and public social pages only.
Topics to track: [local food news], [flour and butter prices], [one trend you care about].

How to do it:
1. Research each rival as its own piece of work, and each topic as its own piece, then combine the findings.
2. Only cover the last 7 days. If you find nothing new for a rival or topic, write "Nothing new found" instead of guessing.
3. For every finding, give the link you used.

The brief:
- Title: Week of [date]: rivals and news
- For each rival and topic: what changed, in one or two sentences, and why it might matter to my business.
- Three ideas I could act on this week.
- A short list of anything you couldn't check.

Rules:
- Use public web pages only. Don't sign in to anything, fill in forms, buy anything or contact anyone.
- Don't send, post or share the brief. Leave it in this task for me to review.
- Keep it to one page.
```

### 2. weekly-marketing-drafts.txt (the marketing job, drafts only)
```
# Weekly marketing drafts: a scheduled task for Claude Cowork (written from Anthropic's help pages, checked 2026-11-24; not run for this video)
# Replace everything in square brackets first, and update the menu line whenever your menu changes.
# Then paste everything below the dashed line into Claude, and add how often it should run, for example:
# Run this every Monday at 10 in the morning.
# Anthropic's safety page: don't schedule tasks that send messages on your behalf. This one only drafts.
# ------------------------------------------------------------
Every week, draft next week's posts for my business. Drafts only: I'll check them and post them myself.

My business: [Test Bakery, a small bakery in your town].
Who we sell to: [local families and office workers].
Our tone: [friendly, short, no jargon].
This season's menu and offers: [list them here].

How to do it:
1. Split the work into three pieces: one drafts the social posts, one drafts the newsletter paragraph, and one checks the dates coming up in the next 14 days (public holidays and local events in [your town]).
2. Combine them into one draft document.

The draft:
- Five short social posts, under 50 words each, each with the day to post it and one idea for a photo.
- One newsletter paragraph, under 120 words.
- The dates you used, each with its link.

Rules:
- Draft only. Never post, send, schedule posts or email anyone.
- Don't make up prices, offers or opening hours. Use only what's in this prompt, and mark anything else [CHECK].
- Don't sign in to anything or buy anything.
```

### 3. scheduled-tasks-checklist.md
```
# Cowork scheduled tasks: setup checklist (facts checked 2026-11-24 from Anthropic's help pages)
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before you start
- [ ] A paid plan: Pro, Max, Ultra, Team or Enterprise. Free shows No for "Hand off and schedule tasks".
- [ ] Pro was $20 a month billed monthly ($17 a month billed yearly) when checked 2026-11-24. https://claude.com/pricing
- [ ] "Claude Cowork is now just Claude": no Chat and Cowork options in your message box means the new Claude experience.

## Make each task
- [ ] New experience: paste the prompt into any conversation, say how often it should run, answer Claude's questions, check the name, schedule and instructions, then click Schedule.
- [ ] Older layout: type /schedule in a Cowork task, or click Scheduled in the left sidebar, then New task, then Create with Claude.
- [ ] How often: weekly is the gentle start. Every run is a whole Cowork task, and agentic tasks "consume more capacity than regular chat".
- [ ] No folder: "If you pick a folder, Require this computer turns on, and the task runs only while your computer is awake and Claude Desktop is open."

## Keep it safe
- [ ] Approval mode: start on Manual ("Claude pauses and asks for approval"). Auto "can miss risky actions". Never use Skip.
- [ ] Low-risk jobs only: "Start simple." Don't schedule tasks that "send messages on your behalf, make purchases, or take other actions that are difficult to undo".
- [ ] The marketing job drafts only. You post by hand.
- [ ] Public web pages only. No passwords, card numbers or customer details in any prompt.

## Check each run
- [ ] Open Scheduled in the left sidebar: upcoming and past runs.
- [ ] Manual means Claude stops to ask, and the help pages don't say what a scheduled run does when nobody answers. The first time, run each task on demand from the Scheduled page while you're there.
- [ ] "Review outputs after each run": click two links in the brief and check they back it up.
- [ ] Pause, edit or delete a task from the Scheduled page.

Sources: claude.com/product/cowork ; support.claude.com/en/articles/13345190 ; support.claude.com/en/articles/13854387 ; support.claude.com/en/articles/13364135 ; support.claude.com/en/articles/13837440 ; claude.com/pricing
```
