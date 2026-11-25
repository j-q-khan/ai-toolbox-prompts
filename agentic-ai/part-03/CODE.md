# Full code: Agentic AI Examples You Can Try Today: Claude Cowork, ChatGPT Work and Copilot

The approvals checklist and practice prompts from this video, written from Anthropic's, OpenAI's and Microsoft's help pages (checked 2026-11-22). It was written from those pages, not tested on any product.

### agent-approvals-checklist.md
```
# Before you let an AI agent act: an approvals checklist and three practice prompts (facts checked 2026-11-22)

To keep a copy: paste this into Notepad and save it as agent-approvals-checklist.md, with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. For the Claude build prompt, save it into a new, empty folder.

## Before you start
- [ ] Practise first on made-up data, like the Test Bakery notes below, never on real customers or real money.
- [ ] Give the agent one working folder of its own, not your whole computer, and keep backups of anything important.
- [ ] Connect only the accounts and apps this one task needs.
- [ ] Check which approval mode you're in before the first real task.
- [ ] End the request with a stopping point, such as: Return a draft for my review.

## Always approve these yourself
- [ ] Anything that spends money or makes a payment.
- [ ] Any message sent as you: emails, chats, posts, invites.
- [ ] Deleting, overwriting or moving files.
- [ ] Signing in to a site, or typing a password. Never paste a password into the chat.
- [ ] Sharing a file or link with anyone.

## While it works
- [ ] Look over its plan before you let it run.
- [ ] Watch for files or websites you didn't mention, or a task growing beyond what you asked. If something feels off, stop it.
- [ ] Check the finished file against your own notes before you use it.

## Prompt injection (harmful instructions hidden in what the agent takes in)
- [ ] Treat instructions found in emails, web pages and shared files as something to check, never an order.
- [ ] Be wary of any text that says to ignore your instructions, or to send money, passwords or files somewhere.
- [ ] Keep approvals on whenever the agent can both see outside material and take real actions.

## Where the approval controls are (from the makers' help pages)
- Claude Cowork: the mode selector in the message box. Manually approve (Claude asks before acting), Automatically approve (an automated check screens each action), Skip all approvals (Claude doesn't stop to ask, and no automated check runs). In the newer version where chat and Cowork are one, Auto was rolling out as the default on Pro, Max, Ultra and Team when checked. Claude asks before permanently deleting files; select Allow only if you meant it.
- ChatGPT Work: it asks for confirmation before consequential actions, such as booking or payment, and asks before visiting a new website by default.
- Copilot in Excel: plan mode shows a plan to review and confirm before it edits; the Stop button is on the right side of the box where you type.
- Copilot in Word: review the result, then choose Replace, Insert below or Regenerate.

## Three practice prompts (made-up Test Bakery data)
1. Claude Cowork: From these rough notes, make five slides for our team meeting. Return a draft for my review.
2. ChatGPT Work: Create a spreadsheet comparing three flour suppliers from my notes. Score each one, flag anything missing, and recommend one. Return a draft for my review.
3. Copilot in Excel, in plan mode: Add a summary sheet with the total orders for each cake, plus a simple chart.

## Practice notes (made up)
- Test Bakery is a made-up shop.
- Month notes: new lemon and poppy seed loaf; Saturday opening now at 8; the oven was serviced; two new weekend staff; a free coffee with any loaf on Saturdays.
- Flour suppliers: Supplier A, cheapest, delivers twice a week. Supplier B, organic, costs more, delivery days not stated. Supplier C, mid price, delivers daily, minimum order of 20 bags.
- Cake orders this month: Lemon loaf 42, Carrot cake 35, Chocolate cake 51.

## Practice task for the build prompt (made up)
Hand an agent the Test Bakery month notes and ask it to make a slide deck and email it to the team.

## Sources (checked 2026-11-22)
- Anthropic, Get started with Claude Cowork: https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- Anthropic, Use Claude Cowork safely: https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- OpenAI, Get started with ChatGPT Work: https://learn.chatgpt.com/docs/get-started-with-work
- OpenAI, Browser: https://learn.chatgpt.com/docs/browser
- Microsoft, Get started with Copilot in Excel: https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel
- Microsoft, Edit content and rewrite (Word): https://support.microsoft.com/en-us/word/copilot/edit-rewrite-content
```
