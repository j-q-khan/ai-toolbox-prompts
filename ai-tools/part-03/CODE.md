# Full code: AI Tools for Business: The Ones Worth Paying For

The first-week checklist and the made-up price file for this video, written from each company's own pages (checked 2026-11-21). They were written from the docs, not run for this video.

### 1. first-week-ai-at-work.md
```
# Your first week with AI at work: a checklist (facts checked 2026-11-21)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as first-week-ai-at-work.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every price and quote below is from the company's own page on 2026-11-21, in US dollars, per user a month. Nothing was signed up for, installed or run. Plans and prices change often: check each page before you buy.

## Before you pay (day 1)
- [ ] Where are your business email and documents now: Outlook, Word and Excel, or Gmail, Docs and Drive?
- [ ] On Microsoft 365? Ask your admin whether you already have Copilot Chat: Microsoft says it is "included at no additional cost with eligible Microsoft 365 plans".
- [ ] On Google Workspace? Check your level: Gemini in Docs and Meet starts at Business Standard. Business Starter has Gemini in Gmail and the Gemini app.
- [ ] Pick one job for the week, such as customer replies or Monday meeting notes.
- [ ] Pick the two or three people who write the most emails. Don't buy a seat for everyone yet.

## The plans, by job (was this when checked, 2026-11-21)
| Job | Plan | Price per user a month | In the maker's words, on training | Source |
|---|---|---|---|---|
| Email and documents (Microsoft) | Microsoft 365 Copilot Business (add-on, on top of a Microsoft 365 business plan) | $18.00 paid yearly, an offer from July 1 to December 31, 2026, first year only; usually $21.00; $25.20 monthly | "Prompts, responses, and data accessed through Microsoft Graph aren't used to train foundation LLMs" | https://www.microsoft.com/en-us/copilot/pricing/business and https://learn.microsoft.com/en-us/copilot/plan/microsoft-365-copilot-privacy |
| Email and documents (Microsoft, all in one) | Microsoft 365 Business Standard with Copilot | $23.50 paid yearly; $28.20 monthly | as above; "Usage-based billing for select advanced AI features." | https://www.microsoft.com/en-us/copilot/pricing/business |
| Email and documents (Google) | Google Workspace Business Standard, Gemini built in | $14 Annual plan; $16.80 Flexible plan | "Workspace does not use customer data for training models without customer's prior permission or instruction." | https://knowledge.workspace.google.com/admin/billing/compare-flexible-and-annual-fixed-term-payment-plans |
| Team chat with company files | ChatGPT Business | $20 billed annually; $25 monthly | "No training on your business data by default." | https://learn.chatgpt.com/docs/pricing |
| Team chat with company files | Claude Team, Standard seat (teams of 2 to 150) | $20 billed annually; $25 monthly | "No model training on your content by default" | https://claude.com/pricing |
| Bigger teams | Claude Enterprise | "US$20/seat/month, billed annually, 20 seat minimum. Usage cost scales with model and task." | "No model training on your content by default" | https://claude.com/pricing |
| Meeting notes | Notion Business (AI Meeting Notes; Free and Plus get only a trial of Notion AI) | $20 billed yearly; $24 monthly | "Notion AI will not use your data to train our models unless you opt in to a request to share your data." | https://www.notion.com/pricing and https://www.notion.com/help/ai-meeting-notes |

## Set it up (days 2 and 3)
- [ ] Outlook, customer replies: start a reply, then select Help me reply in the message area. New email: Home, New mail, the Copilot icon, Draft, Generate, Keep it.
- [ ] Gmail, customer replies: Compose or reply, type in the prompt bar at the bottom, then Create (no prompt bar? click Help me write). Then Formalize, Friendly or Shorten.
- [ ] ChatGPT Business, company files: Settings, then Plugins, choose the app (for example Google Drive), Connect. In a chat, type @ or select + to pick it.
- [ ] Claude Team, company files: an owner turns the connector on in Organization settings, then Connectors. Owners can allow Claude to summarize email but stop it from sending messages.
- [ ] Notion, meeting notes: in the desktop app, type /meet in any page, then Start transcribing. Notion: by doing this, "you're confirming that everyone in the meeting has given their consent". The desktop app hears your system audio and mic; the browser hears your mic only. Limit: 10 hours a day per user.

## Use it on one job (days 4 and 5)
- [ ] Use it only for the one job you picked.
- [ ] Read every draft before you send it. Never send a reply you haven't checked.
- [ ] Working alone for clients? Keep each client's files in their own folder.
- [ ] Don't paste anything into a personal account that belongs in the business workspace.

## Check it worked (end of the week)
- [ ] Ask the people with seats: did it save them time on that job?
- [ ] Yes: add seats one or two at a time. No: try another job for a week, or stop before the next bill.
- [ ] Microsoft's $18 is an offer that ends December 31, 2026: check the price on the day you buy.
- [ ] Check the company's own pricing page on the day you buy.
```

### 2. test-plan-prices.csv
```
# Business plan prices for trying the build prompt, per seat a month in US dollars, from each company's own page on 2026-11-21. Prices change: check each page before you buy.
# To keep a copy: paste this into Notepad and save it as test-plan-prices.csv with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you: the script skips them. Empty min_seats or max_seats means the page gives none here.
tool,plan,price_per_seat,billing,min_seats,max_seats,offer_ends,note
Microsoft 365 Copilot Business,add-on (offer price),18.00,yearly,,300,2026-12-31,On top of a Microsoft 365 business plan. First year only
Microsoft 365 Copilot Business,add-on (usual price),21.00,yearly,,300,,On top of a Microsoft 365 business plan
Microsoft 365 Copilot Business,add-on (monthly),25.20,monthly,,300,,On top of a Microsoft 365 business plan
Microsoft 365,Business Standard with Copilot,23.50,yearly,,,,Apps and Copilot together
Google Workspace,Business Standard,14.00,yearly,,300,,Gemini built in. Annual plan
Google Workspace,Business Standard,16.80,monthly,,300,,Gemini built in. Flexible plan
ChatGPT,Business,20.00,yearly,,,,Billed annually. OpenAI's pages differ on a seat minimum: check before you buy
ChatGPT,Business,25.00,monthly,,,,Billed monthly
Claude,Team (Standard seat),20.00,yearly,2,150,,Billed annually
Claude,Team (Standard seat),25.00,monthly,2,150,,Billed monthly
Claude,Enterprise,20.00,yearly,20,,,Plus usage that scales with model and task
Notion,Business,20.00,yearly,,,,AI Meeting Notes included
Notion,Business,24.00,monthly,,,,AI Meeting Notes included
```
