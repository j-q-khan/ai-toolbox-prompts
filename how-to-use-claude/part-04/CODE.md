# Full code: Claude Artifacts Tutorial: Build a Dashboard or Tool From One Prompt

An artifact build checklist and the made-up sales numbers, written for this video from Anthropic's own help pages (checked 2026-11-14). Menu names are as the help pages gave them that day; check the linked page if a menu looks different.

### 1. claude-artifact-checklist.md
```
# Claude artifacts: build checklist (from Anthropic's help pages, checked 2026-11-14)

## Before you start
- [ ] Any Claude account. Every plan, Free included, can make artifacts in a chat.
- [ ] Turn on the setting called Create and edit files (older layout: Cloud code execution and file creation) in Settings, then Capabilities. Team and Enterprise: Organization settings, then Capabilities.

## Build one from one prompt
- [ ] Start a new chat on the web or the desktop app.
- [ ] Ask for it as an artifact and say exactly what to show (the total, the best seller, a weekly chart).
- [ ] Type made-up numbers into the prompt (corner-bakery-sales.csv). Nothing private, no apps connected.
- [ ] It opens in its own window beside your chat. If Claude answers in the chat instead, ask again for an artifact.

## Change it
- [ ] Ask Claude in the same chat ("Make the bars orange and add the average week at the top").
- [ ] An error? Click Try fixing with Claude near the error message, then send. A fix isn't guaranteed: say exactly what still looks wrong.
- [ ] Check the numbers yourself. With the sample data: total 4,860, best seller Sourdough 1,720, average week 810.
- [ ] Want another direction? Edit an earlier message: you get a different version of the chat, with its own artifacts, and keep the first.

## Find it again
- [ ] Everything you make is saved to the Artifacts tab in your sidebar.
- [ ] Phone: view and edit it in the Artifacts tab; change sharing on the web or the desktop app.

## Share it (artifacts start private to you)
- [ ] Free: the sharing page lists no way to share a new artifact. Free can still publish legacy artifacts (made in a chat before Sept 16, 2026).
- [ ] Pro, Max, Ultra: open the artifact, click Share, under Who has access pick Anyone with the link, copy the link and send it.
- [ ] Most link artifacts open without a Claude account; parts that use Claude or connected apps won't work for those viewers.
- [ ] Team and Enterprise: artifacts stay inside your organization unless an owner allows sharing outside it.
- [ ] Stop sharing: Share, then Only you (Pro, Max, Ultra) or Only people invited (Team, Enterprise). On Pro, Max and Ultra, people you invited by email keep their access until you open their access level and select Remove.

## Build on someone else's
- [ ] Works for legacy artifacts published from a chat, on Free, Pro, Max and Ultra.
- [ ] Open it, click Copy, start a new chat, paste the code and say what to change. The original isn't touched.
- [ ] Only from people you trust: treat it like a file from an unknown sender.

Help pages: support.claude.com (What are artifacts and how do I use them?; Publish and share artifacts)
```

### 2. corner-bakery-sales.csv
```
week,sourdough,rye,croissants,cinnamon_buns,week_total
1,260,120,190,150,720
2,280,135,200,165,780
3,290,140,205,170,805
4,270,130,195,165,760
5,300,160,220,180,860
6,320,185,240,190,935
total,1720,870,1250,1020,4860
```
