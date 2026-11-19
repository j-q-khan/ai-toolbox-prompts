# Full code: Figma Make Tutorial: Turn a Prompt into a Working Prototype

The copy-paste prompt and a checklist, written from Figma's help pages (checked 2026-11-19). They were written from the docs, not run for this video.

### 1. habit-tracker-prompt.txt
```
# Paste this into Figma Make's chat box, not into Claude:
# open your drafts in Figma's file browser, click Make in the upper-right corner,
# paste everything below the # lines, and send it.
# Every habit and number is made up, so it needs no files, no logins and no websites.
# It uses some of the AI credits on your plan.
# Written from Figma's help pages, checked 2026-11-19, not run. Check every screen before you share it.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste into Figma Make.

Goal: build a clickable three-screen prototype of a made-up habit tracker called Tiny Steps, using only the made-up data at the end of this message, then tell me how to publish it with its own link.
Steps, in order:
1. Before you build anything, ask me two things and wait for my answers: whether it's for a computer screen or a phone screen (Figma's tips say full-screen layouts work best for now), and which colour I want for the buttons.
2. Build three screens with a simple menu to move between them: Today, Add a habit, and This week.
3. Today: list the habits below, each with a tick box. Ticking one marks it done and updates a count at the top, for example 2 of 4 done.
4. Add a habit: a box for the habit's name, a choice of how often (Every day, Weekdays, Weekends), and an Add habit button. Pressing it adds the habit to the Today list for this session only.
5. This week: a simple grid showing how many habits were done on each day, Monday to Sunday, using the sample week below.
6. Keep all data inside the screens. Don't add a backend, a database, logins, sign-up, payments, real names, photos of real people or links to other websites. If you think the app needs a backend, ask me first and don't create one until I say yes.
7. When it's built, describe what each screen does in one short line each, tell me this is a rough prototype, and list three things I should click to check it works.
8. Finally, tell me the steps to publish it with its own link in Figma Make, and remind me that on the free Starter plan, publishing also puts the file on the Figma Community, where, for now, people who remix it can see this chat.
Rules: never ask me for a password, a payment detail, a secret key or any personal data. Don't use any of my files. If anything is unclear, ask me first.
Reminder for me: this uses some of the AI credits on my plan. Check every screen before I share it.

Made-up data for this prototype:
- Habits: Drink a glass of water, Stretch for five minutes, Write one line in a journal, Go to bed by 11 pm
- Sample week, habits done out of 4: Monday 3, Tuesday 4, Wednesday 2, Thursday 3, Friday 1, Saturday 4, Sunday 2
```

### 2. figma-make-checklist.md
```
# Figma Make tutorial: checklist (facts checked 2026-11-19, from Figma's own help pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## What you need
- [ ] A Figma account. Make is on Starter (free), Professional, Education (not K-12), Organization, Government and Enterprise plans. Starter: 150 AI credits a day, up to 500 a month (pricing page, checked 2026-11-19): https://www.figma.com/pricing/
- [ ] On a paid plan, Make comes with a Full seat. Dev, Collab and View seats can try Make in drafts only, and can't share or publish those files.
- [ ] Made-up data only. Figma's tips say not to put API keys, email or street addresses, personal data or ID numbers in the chat.

## Open Make and write the first prompt
- [ ] In the file browser, open your drafts, then click Make in the upper-right corner.
- [ ] Optional: to start from a design, click +, then Add context, and paste the design's link, or paste a frame straight into the chat.
- [ ] Write one clear first prompt: the task, who it's for, and the limits (device, what to leave out). Figma says full-screen layouts work best for now.
- [ ] Try habit-tracker-prompt.txt: paste it into the chat box, answer its two questions, then click Send.
- [ ] While it works, a to-do list may show in the chat; it can take a few minutes. You can type more prompts and they queue.
- [ ] If a card offers to create a backend (the part that saves data and handles logins), you don't have to click Create for a clickable prototype.

## Check it worked
- [ ] When it's done, Make writes a summary and the preview appears. Click every button.
- [ ] To see other screen sizes: in the Browser tab, click Preview options. For a full-screen copy, click Preview in the upper-right corner.

## Fix what it builds
- [ ] Ask in the chat, or: Browser tab, Edit, Select, click the item, change it in the properties panel, then click Apply in the chat.
- [ ] The Edit tool, properties panel and annotations are only available in new Make files (Figma's words).
- [ ] Draw: mark up the preview, Add note, then Apply. Annotate for agent: pin several notes, then Apply them as one request.
- [ ] Nothing is kept until you click Apply, and edits made with the properties panel or annotations use AI credits.
- [ ] Files tab: your app's code. Review tab: what each change did. You don't need either for this prototype.
- [ ] Gone wrong? Click Version history at the top of the chat, More options beside an earlier version, then Restore this version. Restoring deletes nothing; later versions stay in the list.

## Publish it with its own link
- [ ] Click Publish in the upper-right corner, set a title, click Publish. The link looks like three-random-words.figma.site.
- [ ] Anyone with the link can open it. By default, search engines won't index it.
- [ ] Free Starter plan: you can only publish to the web if you also publish to the Figma Community (turn on Feature on Community). Figma says conversation history is currently shown when someone remixes it, so keep anything private out of your prompts.
- [ ] Paid plans: publishing needs a Full seat, and a Full seat can publish to the web without the Community.
- [ ] Changed the app? The link only shows the change after you click Publish, then Update.
- [ ] Just a test? Take it down: Make settings (upper-right corner), then Unpublish.
- [ ] You're responsible for the rights to any fonts, images or code packages Make pulls in. Figma says images from Make come from Unsplash, under Unsplash's terms.

## Bring a screen back into Figma (paid plans)
- [ ] Browser tab, Edit, Copy designs, Whole page, then paste into a Figma Design file you can edit.
- [ ] The layers are a snapshot: not connected to the Make file, not tied to your design system, and not interactive.

## Credits
- [ ] Each prompt uses AI credits. Figma's example: an app from scratch about 100+ credits, change the font about 30+, make an attached design interactive about 75+ (default model as of February 2026; rates as of 19 November 2026). Other models in Make cost more or less.
- [ ] After a prompt finishes, hover over the AI credits icon under it to see what it used. Your balance: Main menu, then AI balance.
- [ ] What each task costs: Part 3 of this series, and https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work

## Afterwards
- [ ] Unpublish anything that was only a test.
- [ ] On a team: ask your admin how the Content training setting is set before you put work files into Make (Part 1 of this series).

Sources: help.figma.com/hc/en-us/articles/31304412302231 ; /31304485164695 ; /42009840449175 ; /31304586129559 ; /33652209702423 ; /31722591905559 ; /35060759685015 ; /33459875669015 ; figma.com/pricing
```
