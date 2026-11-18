# Full code: Notion AI Free vs Paid: What Each Plan Gets You Now

The prompt from this video and the steps as a checklist, written from Notion's pricing page and help centre (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. plan-worksheet-prompt.txt
```
# Paste this into Claude (a new chat) or into Notion AI (click the face in the bottom corner of Notion to open the Notion Agent chat), then send it.
# It asks five questions, then drafts a one-page worksheet from your answers. No prices are baked in, and it doesn't pick a plan for you.
# In Claude it writes in the chat. In Notion AI it asks first, then makes one new page and changes nothing else.
# On Notion's Free and Plus plans each response in Notion AI uses some of your trial of Notion AI.
# Written from Notion's pricing page and help centre, checked 2026-11-17, not run.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste.

Goal: help me fill in a one-page worksheet called "Which Notion plan do I need?", using only my answers and the facts below. Don't recommend a plan, and don't add prices or facts from memory.
Facts, as checked on 2026-11-17 on Notion's own pages (remind me to check them again at notion.com/pricing, because they change):
- Notion has four plans: Free, Plus, Business and Enterprise.
- Free and Plus list a "Trial of Notion AI": a limited number of responses, with no number published.
- "Notion AI is available on Business and Enterprise Plans." Business lists the Notion Agent and AI Meeting Notes.
- Each Business member gets 1,500 Standard credits and 500 Select credits a month. They reset monthly and don't roll over.
- AI Meeting Notes begin using Standard credits on 1 December 2026.
- Custom Agents need the Business or Enterprise plan.
- The Education Plan is for students and teachers at accredited colleges and universities. Its help page does not mention Notion AI.
- Notion's developer docs say Notion MCP, the connection Claude's Notion connector uses, works on every Notion plan.
Steps, in order:
1. Ask me these five questions, one at a time, and wait for each answer: (a) Do you use Notion on your own or with a team, and how many people? (b) Which Notion plan are you on now? (c) In a normal week, how often would you use Notion AI: never, a few times, or every day? (d) Do you want meeting notes written for you, or agents that run on a schedule? (e) Are you a student or teacher with a school email, and are these work notes covered by an employer's rules?
2. Tell me in two sentences what you will write and where, and wait for me to answer yes. Write nothing until I do.
3. Write the worksheet with these six headings: "My answers"; "What each plan lists" (a small table made only from the facts above); "Which lines matter for me" (match my answers to the facts, without choosing for me); "Prices" (an empty table with Plus and Business, paid monthly and paid yearly, for me to fill in from notion.com/pricing, with the date I looked); "To check before I pay" (the trial has no published size; credits and the 1 December 2026 date; my employer's rules; the money-back wording on the pricing page); "My decision" (leave it empty).
4. If you are Notion AI: make one new private page with that title. Don't edit, move, share or delete any other page or database, and don't search my other pages for this. If you are Claude: write the worksheet in the chat for me to copy, and don't use any connected app.
5. Stop there.
Safety: no real names, emails or phone numbers. No web search, no sharing and no changes to permissions. If anything is unclear, ask me before you write.
Output: the worksheet, and one line that says nothing else was changed.
```

### 2. notion-plan-checklist.md
```
# Notion AI, Free vs Paid: checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Plans, prices and dates change. Check each line again at notion.com/pricing before you pay.

## What you need
- [ ] To know which Notion plan you are on: Free, Plus, Business or Enterprise.
- [ ] Notion's pricing page open: notion.com/pricing. It may show your local currency; the box called Price in switches it.
- [ ] For work: your employer's rules on which tools you may put work notes into.

## What each plan lists
- [ ] Free and Plus: "Trial of Notion AI". A limited number of responses for trying it out; no number published. Each response counts, and so does each click on Try again.
- [ ] When the trial is used up: "you will see a message that an upgrade to the Business or Enterprise Plan is necessary to continue using AI features."
- [ ] Business and Enterprise: "Notion AI is available on Business and Enterprise Plans." Business lists the Notion Agent and AI Meeting Notes.
- [ ] Enterprise: "Custom pricing", and "Zero data retention with LLM providers".
- [ ] No add-on for Notion AI is listed on the pricing page.

## Prices, in US dollars, when checked 2026-11-17
- [ ] Plus: $10 per member a month paid yearly, or $12 paid monthly.
- [ ] Business: $20 per member a month paid yearly, or $24 paid monthly.
- [ ] Other countries are shown other currencies. Fill in today's figures yourself: Plus ____ / ____ ; Business ____ / ____ ; date ____.

## Credits (Business and Enterprise)
- [ ] The credit system started on 19 October 2026; existing customers moved over on 2 November 2026.
- [ ] Each member: 1,500 Standard credits and 500 Select credits a month. They reset monthly and don't roll over.
- [ ] Standard: work where Notion picks the model. Select: work where you pick a model yourself, or use a Custom Agent you own.
- [ ] Out of one kind: the features that need it pause until the next reset, unless an owner allows Notion credits.
- [ ] Extra Notion credits, bought by an owner, Business and Enterprise only: $10 per 1,000 bought monthly, or $13 per 1,000 bought annually, when checked.
- [ ] From 1 December 2026, AI Meeting Notes begin using Standard credits: about 10 for a one-hour meeting, by Notion's figure.
- [ ] Custom Agents need Business or Enterprise. The pricing page says "Free to try, then $10 per 1,000 monthly Notion credits." and "Requires Notion credits"; Notion's blog of 19 October 2026 says "You also no longer need to buy credits to start building custom agents." Ask Notion before you budget for them.

## Students and teachers
- [ ] The pricing page: "The Plus Plan (with a 1-member limit) is free for students and educators." The help centre calls it the Education Plan, for students and teachers at accredited colleges and universities.
- [ ] To get it, with your school email as your account's main email: Settings, then Upgrade plan, then Get free education plan.
- [ ] Its help page says K-12 students and K-12 educators are not eligible.
- [ ] Its help page does not mention Notion AI. Don't count on it including Notion AI.

## A route that needs no paid Notion plan
- [ ] Claude's Notion connector. Notion's developer docs: "Notion MCP works on every plan." No charge for it is listed by Notion. Anthropic's pricing page lists Connectors on every Claude plan.
- [ ] It is Claude working with your pages, with the reach your Notion account has. For work notes, follow your employer's rules first.
- [ ] Part 5 of this series sets it up.

## The check: do you know which plan you need?
- [ ] Curious, writing on your own: the trial on Free or Plus.
- [ ] A team using the agent or meeting notes every week: Business.
- [ ] On Free, wanting an assistant over your notes: Claude's connector.
- [ ] Run the plan worksheet prompt and fill in the prices yourself.

## If you try Business and change your mind
- [ ] Notion's pricing page: "We'll be happy to refund you the full amount (not pro-rated) if you downgrade your subscription within three days of signing up for monthly billing, or within 30 days of signing up for annual billing."
- [ ] Delete the worksheet page when you're done: select the three dots at the very top right of the page, then Delete.

Sources: notion.com/pricing ; notion.com/help/notion-ai-faqs ; notion.com/help/complimentary-ai-responses ; notion.com/help/what-are-notion-credits ; notion.com/help/standard-select-and-notion-credits-eligible-features ; notion.com/blog/notion-ai-more-for-less ; notion.com/help/custom-agents ; notion.com/help/notion-for-education ; developers.notion.com/guides/mcp/get-started-with-mcp.md ; claude.com/connectors/notion ; claude.com/pricing
```
