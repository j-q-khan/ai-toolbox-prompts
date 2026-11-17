# Full code: Copilot in Outlook: Summarize Emails, Draft Replies and Manage Your Inbox

A test thread and a prompt sheet written for this video from Microsoft's Copilot in Outlook help pages (checked 2026-11-17). Nothing here was run through Copilot for this video; use them in your own mailbox, sent to yourself, only.

### 1. team-lunch-thread.txt
```
Made-up test thread for Copilot in Outlook (Microsoft Copilot series, Part 3)
Test mailbox only. Every name, place and detail below is made up.
Follow your employer's rules. Send these to yourself only.

HOW TO BUILD THE THREAD
1. Start a new email to yourself. Title (subject): Team lunch
2. Paste MESSAGE 1 as the body and send it.
3. When it arrives, select Reply, paste MESSAGE 2 and send it.
4. When that arrives, select Reply, paste MESSAGE 3 and send it.
You now have one conversation with three emails in it.
Open it and select Summary by Copilot (or Summarize) at the top.

----- MESSAGE 1 -----
Hi team,

I'd like to book our end-of-quarter team lunch. My suggestion is
next Thursday at 12:30 in the café on the ground floor. The budget
is $25 a person, and the company covers it.

Please reply by Monday if you can come, and tell Priya about any
dietary needs.

Thanks,
Sam

----- MESSAGE 2 -----
Hi Sam,

Thursday clashes with the monthly client call for four of us.
Could we move it to next Friday, same time? So far two people have
told me they're vegetarian.

Thanks,
Priya

----- MESSAGE 3 -----
Hi all,

Friday works. I've booked the café for next Friday at 12:30, a
table for nine.

Priya, could you send me the full dietary list by Wednesday? The
budget stays at $25 a person.

Thanks,
Sam
```

### 2. outlook-copilot-prompt-sheet.md
```
# Copilot in Outlook: prompt sheet (checked 2026-11-17)
# Made-up mail only, sent to yourself. Follow your employer's rules.

## 0. Build the test thread (once)
- [ ] Download team-lunch-thread.txt: in the GitHub folder, select the file, then the Download raw file button
- [ ] New email to yourself, title "Team lunch", paste MESSAGE 1, send
- [ ] Reply to it with MESSAGE 2, send; reply again with MESSAGE 3, send

## 1. Summarize (top of the thread)
- [ ] Select the conversation, then Summary by Copilot (or Summarize) at the top
- [ ] Select a number in the summary: it opens the email that point came from

## 2. Check one point by hand
- [ ] Email 1 says Thursday, email 2 asks for Friday, email 3 confirms Friday at 12:30
- [ ] The summary should say Friday at 12:30, a table for nine, Priya collects the dietary list by Wednesday, $25 a person
- [ ] Says Thursday? Fix it before you pass the summary on

## 3. Draft a reply (Reply on the last email, then Help me reply)
Confirm I'll be there on Friday at 12:30 and that I'm vegetarian. Friendly and short.
- [ ] Nothing is sent until you select Send; this reply goes only to you
- [ ] Shortcut: type / in the message body, then choose Draft with Copilot
- [ ] No drafting in new Outlook or on the web? Settings → Mail → Compose and reply → HTML (plain text isn't supported)

## 4. Coaching (write it yourself, then Copilot icon on the toolbar → Coaching by Copilot)
Paste this blunt test draft into a new email to yourself, then ask for coaching:
Sam, Friday is fine I guess, but next time please check the calendar before booking anything. I need the vegetarian option. Thx
- [ ] Look at the suggestions for tone, clarity and reader sentiment
- [ ] Apply all suggestions, or make only the changes you like by hand
- [ ] Microsoft's coaching steps cover Windows, Mac and the phone apps; they have no web steps

## 5. Prioritize (rolling out gradually)
- [ ] Windows: the arrow next to the Copilot button, top right → Prioritize
- [ ] Mac: What's New tab in the pane on the right → Prioritize your mail → Try it
- [ ] Give at least one instruction, written as a phrase:
It's from my manager
- [ ] Change it later in Settings → Copilot → Prioritize
- [ ] Your test thread gets no arrow: Prioritize skips mail you send to yourself and mail that arrived before you turned it on

## 6. Tidy up by asking (Copilot chat pane, English only)
- [ ] Open an email, then select the Copilot button at the top of Outlook to open the chat pane (Microsoft's chat page is written for work or school accounts)
Flag this message
- [ ] A request that would change more than five emails? Copilot asks you to confirm first

## Copilot missing in Outlook?
- [ ] Work account: check the label under your name in the Copilot app (Part 1); ask the people who run your work accounts
- [ ] Copilot Chat (Basic) label: Microsoft doesn't say whether it gets Summary, Draft or Coaching. Look in your own Outlook: Summary by Copilot (or Summarize) at the top of a thread, and the Copilot icon on the toolbar when you write an email
- [ ] Home plan: only the person who owns the Microsoft 365 Personal, Family, Premium or Pro plan gets Copilot
- [ ] Mac: Copilot needs the latest Outlook for Mac; legacy Outlook isn't supported
- [ ] Signed or encrypted emails aren't supported

Sources: support.microsoft.com "Summarize an email thread with Copilot in Outlook"; "Draft an email message with Copilot in Outlook"; "Get email coaching with Copilot in Outlook"; "Prioritize my inbox"; "Triage email with Microsoft Copilot in Outlook"; "Frequently asked questions about Copilot in Outlook"; "What Copilot license do I have"; "Sharing Copilot in Outlook"
```
