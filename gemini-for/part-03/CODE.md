# Full code: Gemini for Work in Google Sheets and Meet: the AI Formula and Take Notes for Me

The formulas, the practice comments, the Build prompts and the meeting-notes checklist from this video, written from Google's Docs Editors Help and Google Meet Help (checked 2026-11-27). They were written from the docs, not tried on a real account. Every name, shop, comment and email address in them is made up.

### 1. gemini-sheets-ai-formulas.txt
```
# AI function formulas for Google Sheets (facts checked 2026-11-27)
# To keep a copy: paste into Notepad and save with the box called Save as type set to All files,
# as gemini-sheets-ai-formulas.txt. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.
# Made-up data only. These assume the practice sheet: column A = Order, column B = Comment, header in line 1.

# Steps (from Docs Editors Help, answer 15877199):
# Click C2, paste, press Enter
# Select the cell
# Generate and insert
# To do the whole column: copy the cell into the cells below, select them, Generate and insert again.
# New answer: select the cell, then Refresh and insert (you can't undo or redo the function).

1. Paste into C2:
=AI("Sort this comment as praise, a complaint or a question. Answer with one word.", B2)

2. Paste into D2:
=AI("Is this comment positive, negative or neutral? Answer with one word.", B2)

3. Paste into E2:
=AI("Write a short, friendly reply to this customer from Harbor Street Bakery.", B2)

4. =Gemini() works the same way:
=Gemini("Write a one sentence summary of this comment.", B2)

5. Paste into F2 (a cell range: the order and the comment together):
=AI("For the customer, write a one sentence summary of their feedback.", A2:B2)

# Limits (Google's words): "Responses are limited to text."
# "only the first 350 selected cells with AI functions will be generated."
# It can't see your whole spreadsheet or your Drive files, only the cells you give it.
# Needs an eligible Google Workspace or Google AI plan.
```

### 2. practice-comments.csv
```
Order,Comment
"Chocolate cake","The cake was perfect and everyone at the party loved it."
"Sourdough loaf","My loaf was burnt on the bottom this time."
"Birthday cake","Can I pick up my order on Sunday instead of Saturday?"
"Lemon tart","Lovely tart, and the staff were so friendly."
"Croissants","Two of the six croissants were missing from the box."
"Wedding cake","Do you deliver to the town hall, and is there a charge?"
"Carrot cake","Best carrot cake in town, we'll be back."
"Rye bread","The bread was stale by the next morning."
"Cupcakes","Do you have a gluten-free option for cupcakes?"
"Apple pie","The pie was great, but the queue was very long."
```

### 3. gemini-sheets-build-prompts.txt
```
# Prompts for Build, the side panel in Google Sheets (facts checked 2026-11-27)
# To keep a copy: paste into Notepad and save with the box called Save as type set to All files,
# as gemini-sheets-build-prompts.txt. On a Mac, open TextEdit, choose Format, then Make Plain Text, first.

# Where (from Docs Editors Help, answer 16959434):
# Open Google Sheets on a computer → the side panel on the right opens with Build → type your prompt
# Answer any questions it asks, then check the plan and outline it shows.
# Personal Google account: "you might be able to use Canvas and Build up to 3 times a month."

1. Create a sheet to track cake orders with columns for customer, cake, pickup day and status.
2. Create a weekly staff rota for a small bakery with columns for day, name, start time and finish time.
3. Create a visual dashboard of this sales data set.
```

### 4. gemini-meet-notes-checklist.md
```
# Take notes for me in Google Meet: checklist (facts checked 2026-11-27)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as gemini-meet-notes-checklist.md. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before the meeting
- [ ] The organiser's plan includes it. Google: "The meeting organizer must have the Workspace edition that includes 'Take notes for me.'"
- [ ] Work plans: Business Standard, Business Plus, Enterprise (not Business Starter). Personal accounts: Google AI Pro or Ultra. You must be 18 or over.
- [ ] Prices for your country: https://workspace.google.com/pricing
- [ ] Optional, ahead of time. Calendar path: Google Calendar → your meeting → Edit event → Video call options → Meeting records (left) → tick Take notes with Gemini.

## In the meeting (on a computer)
- [ ] At the top right, click Take notes for me.
- [ ] Optional: Settings. Send notes to: "All invited guests, including those outside of my organization", "Invited guests in my organization", or "Hosts and co-hosts only". Also Notes length and Meeting language.
- [ ] Click Start taking notes.
- [ ] Everyone is told: "Google Meet informs all meeting participants that notes are being taken", and a pencil icon appears on everyone's screen.
- [ ] Languages: English, French, German, Italian, Japanese, Korean, Portuguese, Spanish (one at a time).
- [ ] When host controls are on, only the host and co-hosts can start and stop taking notes.

## After the meeting
- [ ] The notes are in the organiser's Google Drive, in the Google Meet folder, with a folder for each meeting.
- [ ] The organiser gets an email with a link shortly after the meeting ends.
- [ ] Check them first. Google: "Sometimes, the meeting summary can be incomplete, inaccurate, or not generated."
- [ ] Google recommends meetings of 15 minutes to 8 hours.

Example meeting name for practice: Harbor Street Bakery weekly sync (made up). Example guest: test@example.com.

Sources: support.google.com/meet/answer/14754931 ; support.google.com/mail/answer/13952129 ; workspace.google.com/pricing
```
