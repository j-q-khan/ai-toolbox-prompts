# Full code: Figma AI Credits and Pricing Explained: What Each Task Costs

The copy-paste prompt, a budget worksheet and a checklist, written from Figma's pricing and help pages (checked 2026-11-19). They were written from the docs, not run for this video.

### 1. credit-planner-prompt.txt
```
# Paste this into Figma Make's chat box, not into Claude:
# open your drafts in Figma's file browser, click Make in the upper-right corner,
# paste everything below the # lines, and send it.
# It holds no prices or credit rates: you type today's numbers from Figma's credits page, because rates change.
# Building it counts as an app from scratch: about 100+ credits on Figma's credits page (checked 2026-11-19).
# The worksheet in the same folder costs no credits.
# Written from Figma's help pages, checked 2026-11-19, not run. Check every total against Figma's page.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste into Figma Make.

Goal: build a simple one-screen credit planner that adds up how many Figma AI credits I plan to use in a month and compares the total with my seat's allowance. Use only the numbers I type in; don't fill in any credit rates or prices of your own.
Steps, in order:
1. Before you build anything, ask me three things and wait for my answers: my Figma plan (Starter, Professional, Organization or Enterprise), my seat type (Full, Dev, Collab or View), and my monthly credit allowance, which I'll copy from Figma's credits page: https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work
2. If I say Starter or View, also ask for the daily limit from that page, and show it next to the monthly allowance.
3. Build a table with one row per task and these columns: Task, Credits each (I type it from Figma's page), Times this month, and Row total (Credits each times Times this month).
4. Start the table with these made-up example rows, with the Credits each boxes empty and labelled [type from Figma's page]: Change the font in Make; App from scratch in Make; Five-screen flow with the agent; Remove a background; Make an image.
5. Add an Add task button for my own rows, and a Remove button on each row.
6. Under the table, show the month's total, my allowance, and what's left. If the total is more than the allowance, show a plain warning that says seat credits don't roll over and only a paid team's admin can buy more.
7. Show a line at the top that says: Rates change. Copy today's numbers from Figma's credits page and check the date on that page.
8. Keep everything on this one screen. Don't add a backend, a database, logins, payments, or links to other websites except the credits page above. Don't save my numbers anywhere.
9. When it's built, tell me in one short line what each part of the screen does, and list three things I should try to check the totals add up.
Rules: never ask me for a password, a payment detail, a secret key or any personal data. Don't use any of my files. If anything is unclear, ask me first.
Reminder for me: this uses some of the AI credits on my plan. Check every total against Figma's page before I rely on it.
```

### 2. credit-budget-worksheet.md
```
# Figma AI credit budget worksheet (fill in by hand; no rates included)

Rates change, so copy today's numbers from Figma's credits page and write the date you checked:
https://help.figma.com/hc/en-us/articles/33459875669015-How-Figma-AI-credits-work

Date I checked Figma's page: [date]

## My allowance
- My plan: [Starter / Professional / Organization / Enterprise]
- My seat: [Full / Dev / Collab / View]
- Monthly seat credits (from Figma's page): [number]
- Daily limit, Starter or View seat only (from Figma's page): [number, or none]

## My month
| Task | Credits each (from Figma's page) | Times this month | Row total |
|---|---|---|---|
| Change the font in Make | [ ] | [ ] | [ ] |
| App from scratch in Make | [ ] | [ ] | [ ] |
| Five-screen flow with the agent | [ ] | [ ] | [ ] |
| Remove a background | [ ] | [ ] | [ ] |
| Make an image (model: [ ]) | [ ] | [ ] | [ ] |
| [my own task] | [ ] | [ ] | [ ] |

Row total = Credits each x Times this month.

## The check
- Month's total (add up the Row totals): [ ]
- Monthly seat credits: [ ]
- Left over (seat credits minus total): [ ]
- Figma's costs are approximate and end in a plus sign (for example 30+), so leave some room.
- If any one task costs more than your daily limit, it won't fit in one day's credits on Starter or a View seat.
- Seat credits reset monthly, don't roll over and can't be shared. If the total is bigger than your allowance, only a Professional, Organization or Enterprise admin can buy more.
```

### 3. figma-ai-credits-checklist.md
```
# Figma AI credits and pricing: checklist (facts checked 2026-11-19, from Figma's own pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Know your seat and allowance (pricing page, checked 2026-11-19, prices in USD)
- [ ] Starter: Free. 150 AI credits a day, up to 500 a month.
- [ ] Professional, with the page's Annual billing selected: Full seat $16 a month with 3,000 credits; Dev $12 and Collab $3, each 500. The monthly-billing price is behind the page's Monthly switch.
- [ ] Organization (billed annually): Full $55 with 3,500 credits; Dev $25 and Collab $5, each 500.
- [ ] Enterprise (billed annually): Full $90 with 4,250 credits; Dev $35 and Collab $5, each 500.
- [ ] View seats get 500 a month with a daily limit of 150. On paid plans, people can view and comment without a paid seat.
- [ ] Seat credits belong to one person, reset monthly, don't roll over, and can't be shared or transferred.
- [ ] Education and Government plans have their own credit rules: see Figma's credits page.

## Know what tasks cost (credits page, rates as of 19 November 2026, approximate)
- [ ] Figma Make (default model as of February 2026): change the font about 30+, make an attached design interactive about 75+, an app from scratch about 100+. Other Make models cost more or less. Plan mode's planning step costs credits on top of the build.
- [ ] Figma agent in Figma Design: change the fonts 30+, summarize the canvas 100+, a five-screen mobile checkout flow 300+. The agent also uses credits in FigJam, Slides and Specs (see the page).
- [ ] Code layers from frames about 250+; Figma lists a limited-time launch promotion where eligible users use them without credits.
- [ ] Remove background 1 to 5 per image; make or edit an image 2, 6 or 16 per image, by model; add interactions 20 per use; Weave tools have their own fixed costs.
- [ ] Free: AI search, rename layers, summarize stickies, cluster stickies, update visual (FigJam).
- [ ] The agent in Figma Design left open beta on 6 October 2026 and now uses credits from the same allowance as Make.
- [ ] Bigger files, attached files, libraries, connectors and long chats cost more per prompt.

## Check your balance
- [ ] Open a file where you have edit access (View seat: a file in your drafts), open the Main menu, choose AI balance: used, remaining, and the reset date.
- [ ] After a prompt finishes, hover the AI credits icon under it to see what that prompt used.

## When you run out
- [ ] Paid AI features stop until your credits reset or an admin adds more. A Starter or View daily limit lifts the following day.
- [ ] If you see the option to request more, your admin gets an email and a notice in Figma.

## Buying more (admins on Professional, Organization or Enterprise)
- [ ] File browser, Admin tab, AI credits, View usage, + Add credits: a monthly subscription (pooled for the plan; the price per credit falls as you buy more) or pay as you go up to a monthly spending limit.
- [ ] Order used: seat credits first, then subscription credits, then pay as you go.
- [ ] The current rates show in the Add credits flow in the admin dashboard; Figma's public pages don't list a price per credit.
- [ ] Professional's credits subscription is month to month; on Organization and Enterprise it follows the annual contract.
- [ ] Admins can set credit limits for individual people.

## Save credits
- [ ] With the agent, start a new chat for each task: the whole chat history goes into every new request.
- [ ] In Make, start fresh (duplicate the file, save a template, or clear chat context) when old context isn't needed.
- [ ] Attach only the files the task needs.

## Figma's MCP server and credits
- [ ] Most MCP tools use no credits. generate_image, generate_vector_illustration and send_prompt do. Credit actions don't count toward MCP rate limits.
- [ ] Writing to the canvas through MCP is "free to use during the beta period" and "will eventually become a usage-based paid feature".

Sources: figma.com/pricing ; help.figma.com/hc/en-us/articles/33459875669015 ; /35865276858647 ; /42614902212887 ; /43707097479575 ; /40097793879191 ; /42495251338775 ; developers.figma.com/docs/figma-mcp-server/rate-limits-access/
```
