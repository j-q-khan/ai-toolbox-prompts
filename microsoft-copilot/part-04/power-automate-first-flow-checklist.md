# Power Automate: your first flow, Outlook to OneDrive to Excel (checked 2026-11-17)
# Work or school account. Test folder, test table, emails to yourself only.
# Follow your employer's rules. This flow sends nothing to anyone.

## 0. What you need
- [ ] A work or school account (the OneDrive for Business and Excel Online (Business) connectors are the work versions)
- [ ] All three connectors are Standard: Office 365 Outlook, OneDrive for Business, Excel Online (Business)
- [ ] Microsoft 365 work plans include automated cloud flows with standard connectors

## 1. Test folder and table (before Copilot)
- [ ] OneDrive on the web: New, then Folder, name it: Flow test
- [ ] Download flow-test-log-headers.csv and open it in Excel
- [ ] Select a heading, then Home, then Format as Table, choose a style, tick My table has headers, select OK
- [ ] Save As: Excel Workbook, name flow-test-log.xlsx, in the Flow test folder (in Excel on your computer, signed in with your work account, choose your OneDrive, then Flow test)
- [ ] Only Excel on the web? In the Flow test folder select New, then Excel workbook, name it flow-test-log, type Received, Sender and File name in A1 to C1, then Format as Table as above
- [ ] Shut the workbook

## 2. Describe it to Copilot
- [ ] Go to make.powerautomate.com and sign in; Home is selected
- [ ] In the box called Create your automation with Copilot, paste:
When a new email arrives in Outlook with an attachment and the subject Flow test, save each attachment to the Flow test folder in my OneDrive for Business, then add a row to the table in Flow test/flow-test-log.xlsx in Excel Online (Business) with the received time, the sender and the attachment's name.
- [ ] Select Generate, then Keep it and continue
- [ ] Every connection shows a green check mark (a red exclamation mark: select it and sign in)
- [ ] Select Create flow

## 2b. No Copilot box? Build it by hand
- [ ] My flows, then New flow, then Automated cloud flow
- [ ] Name it, search the triggers for: When a new email arrives (V3), select it, then Create
- [ ] Select + below the trigger, search for: Create file (OneDrive for Business)
- [ ] Select + below that, search for: Add a row into a table (Excel Online (Business))
- [ ] Then set every card as in section 3

## 3. Check every card
Trigger: When a new email arrives (V3)
- [ ] It comes from the Office 365 Outlook connector (one Learn tutorial calls it Microsoft 365 Outlook; if the name differs, search for Outlook)
- [ ] A setting not showing? Look under the card's advanced parameters
- [ ] Only with Attachments: Yes
- [ ] Include Attachments: Yes
- [ ] Subject Filter: Flow test
- [ ] Optional second guard, From: your own address
Create file (OneDrive for Business)
- [ ] Folder Path: /Flow test
- [ ] File Name: Attachments Name (lightning bolt button)
- [ ] File Content: Attachments Content (lightning bolt button)
- [ ] It sits inside a loop that repeats for each attachment: that's expected (the Excel card can sit in the same loop)
Add a row into a table (Excel Online (Business))
- [ ] Location and Document Library: your OneDrive
- [ ] File: /Flow test/flow-test-log.xlsx
- [ ] Table: the table in that file
- [ ] Received: Received Time
- [ ] Sender: From
- [ ] File name: Attachments Name (lightning bolt button)
- [ ] Select Save: "Your flow is ready to go. We recommend you test it."

## 4. Test it
- [ ] Keep flow-test-log.xlsx shut (manual edits at the same time aren't supported)
- [ ] Select Test, then Manually, then Test
- [ ] Send yourself an email, subject Flow test, with test-attachment.txt attached
- [ ] Usually fires almost immediately; rarely up to an hour
- [ ] Every card shows a green check mark with the seconds it took
- [ ] Open the Flow test folder: test-attachment.txt is there
- [ ] Open flow-test-log.xlsx: one new row per attachment (it can take up to 30 seconds)
- [ ] Testing again? Delete the saved test-attachment.txt from Flow test first, or rename the file you attach
- [ ] Back to the flow's page: the 28-day run history shows each run

## 5. Turn it off
- [ ] My flows, the three dots beside your flow, Turn off
- [ ] The Details page shows Status: Off (runs already going finish first)
- [ ] To use it again: the same menu, Turn on

## Check it with Copilot
- [ ] Open the flow and ask the Copilot pane:
What does my flow do?

Sources: learn.microsoft.com "Create your first cloud flow using Copilot"; "Tutorial: Get started with cloud flows"; "Explore the cloud flows designer"; "Create a cloud flow in Power Automate"; "Turn a flow on or off, and delete a flow"; "Power Automate licensing FAQ"; connector references for Office 365 Outlook, OneDrive for Business and Excel Online (Business); support.microsoft.com "Create and format tables"
