# Full code: Gemini for Workspace: How to Use Gemini in Gmail and Google Docs

The prompts, the button paths and the plan checklist from this video, written from Google's Gmail, Docs Editors and Workspace help pages (checked 2026-11-26). They were written from the docs, not tried on a real account. Every name, shop and email address in them is made up.

### 1. gmail-reply-prompts.txt
```
# Gmail prompts for Gemini's Help me write and Ask Gemini (facts checked 2026-11-26)
# To keep a copy: paste into Notepad and save with the box called Save as type set to All files,
# as gmail-reply-prompts.txt. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.
# Made-up names only. Fill in the [square brackets] with your own details.

# Where to paste (from Gmail Help, answer 13955415):
# Compose (top left) → prompt bar (bottom), or the Help me write icon → type your prompt → Create
# Refine: Formalize, Friendly, Shorten, or type an instruction. Undo and Redo sit at the right of the prompt bar.

1. Ask [Sam] to confirm the [chocolate cake order] for [Saturday] at [10 AM]. Sign it [Harbor Street Bakery].
   Example: Ask Sam to confirm the chocolate cake order for Saturday at 10 AM. Sign it Harbor Street Bakery.
2. Reply to say thanks for the order, and that delivery is free within [5 miles].
3. Write a short, polite email asking [test@example.com] to send the invoice by [Friday].
4. Make it more professional.

# Where to paste (from Gmail Help, answers 14355636 and 14199860):
# Ask Gemini (top right) → side panel → prompt box at the bottom → Submit

5. Summarise this thread in 3 bullet points.
6. What time is my next flight?

# Before you send: check every date, name and price in the draft.
```

### 2. docs-rewrite-prompts.txt
```
# Google Docs prompts for Gemini (facts checked 2026-11-26)
# To keep a copy: paste into Notepad and save with the box called Save as type set to All files,
# as docs-rewrite-prompts.txt. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.

# New or changed text (from Docs Editors Help, answer 13447609):
# Gemini (bottom of the page) → bottom bar → type your prompt
# Then: Accept suggestion, Accept all, or Reject all

1. Add a short section on delivery times.
2. Turn the opening hours list into a table.
3. Rewrite this paragraph in plain English for a customer.

# A paragraph you already have:
# Select it → Refine (floating bar) → Rephrase / Shorten / More
# More → More formal, More casual, Summarize

# Move the bar:
# Send a prompt from the bar → Switch to side panel
# Switch to bottom bar (top of the side panel) takes you back

# Side panel (from Docs Editors Help, answer 14206696):
# Ask Gemini (top right) → type a prompt → Insert to keep the answer
# Add files: the Sources button, or type @
```

### 3. gemini-gmail-docs-checklist.md
```
# Gemini in Gmail and Google Docs: which plan gets what (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as gemini-gmail-docs-checklist.md. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Work accounts (Google Workspace plans)
- [ ] Gemini in Gmail: Business Starter, Business Standard, Business Plus, Enterprise.
- [ ] Gemini in Docs: Business Standard, Business Plus, Enterprise (not Business Starter).
- [ ] Prices on Google's Netherlands page, 2026-11-26, per user a month, excluding tax: Business Starter EUR 6.80, Business Standard EUR 13.60. Your country: https://workspace.google.com/pricing

## Personal accounts (Google AI plans)
- [ ] Google AI Plus: Gemini in Gmail (EUR 4.99 a month on the Netherlands page, 2026-11-26).
- [ ] Google AI Pro: Gemini in Gmail and Docs (EUR 21.99 a month on the Netherlands page, 2026-11-26).
- [ ] You must be 18 or over.
- [ ] In the US, at no charge on a personal account: Help me write, AI Overviews for email threads, Suggested replies.
- [ ] Help me write on a personal account: "restricted to the US only". With a Workspace or Google AI plan: supported languages, globally.

## Side panel (Ask Gemini, top right)
- [ ] Needs an eligible Google Workspace or Google AI plan.
- [ ] Personal accounts: offered through Google Workspace Experiments, a tester program, so it may not show yet.
- [ ] In Docs, click Insert to keep an answer. Google: "You lose your conversation history when: You refresh your browser. You close and reopen the document. Your computer goes offline."

## Privacy (Workspace)
- [ ] Google: "Workspace does not use customer data for training models without customer's prior permission or instruction."
- [ ] Google: "Your interactions with Gemini stay within your organization."
- [ ] Google AI plans (personal): see Google's page on how Gemini in Gmail and Docs protects your data, https://support.google.com/docs/answer/14615114

## Admin (work accounts)
- [ ] Default: on. "The default setting for Gemini features in Workspace services is on."
- [ ] Path: Google Admin console → Menu → Generative AI → Gemini for Workspace → Feature access → Edit (next to the service) → On or Off → Save.
- [ ] Needs the Gemini Settings administrator privilege.

Sources: support.google.com/mail/answer/13952129 ; support.google.com/mail/answer/13955415 ; support.google.com/mail/answer/14355636 ; support.google.com/docs/answer/13447609 ; support.google.com/docs/answer/14206696 ; workspace.google.com/pricing ; gemini.google/subscriptions ; knowledge.workspace.google.com (privacy hub; manage access to Gemini features)
```
