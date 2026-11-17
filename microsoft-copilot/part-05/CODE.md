# Full code: Copilot Studio Agent Tutorial: Build Your First Agent Without Code

A made-up help document, the setup file for the agent and a checklist, written for this video from Microsoft Learn's Agent Builder pages (checked 2026-11-17). Nothing here was run for this video; use them with your own work account, in a test agent you keep private, only.

### 1. office-help-test.txt
```
Office help: questions and answers (made-up test document)
This is a made-up office for testing an agent in Agent Builder. The office, the rooms, the rules and the email address are not real.

How do I book a meeting room?
The three meeting rooms are called Oak, Birch and Cedar. Book them in the shared room calendar. A booking longer than two hours needs the office manager's OK.

How much notice do I need to give for time off?
For a single day off, give two working days' notice. For a week or more, give ten working days' notice. Ask through the time-off form on the staff page.

When is the office open?
Monday to Friday, from 7:30 in the morning to 6:00 in the evening. The office is shut on public holidays.

How do I get on the guest Wi-Fi?
The guest network is called MapleGuest. The password changes every Monday and is printed on the card at reception.

How do I report a broken printer?
Email the help desk at helpdesk@example.com with the printer's floor and its name, which is on the label on top.

Where do I leave parcels for posting?
Leave them at reception before 3:00 in the afternoon for same-day posting.
```

### 2. agent-setup.txt
```
Agent Builder setup for the test agent (Microsoft Copilot series, Part 5). Made-up test agent; follow your employer's rules.
Paste each part into the box with the same name on the Configure tab.

=== Name (30 characters at most) ===
Office Help Test

=== Description (1,000 characters at most) ===
Answers staff questions about a made-up office, using only the uploaded test document office-help-test.txt. For testing only.

=== Instructions (8,000 characters at most) ===
You answer staff questions about a made-up office that is used for testing.
Use only the office help test document for office facts, uploaded as office-help-test.txt or pasted at the end of these instructions. Don't use general knowledge or the web for them.
Keep each answer short: two or three plain sentences.
Say which question in the document your answer comes from.
If the answer isn't in the document, say that you don't know, and suggest emailing the help desk at helpdesk@example.com. Never guess or make up a rule, a time or a number.
Don't ask for personal details, and don't repeat any that someone types.

=== No upload? (a Basic label without pay-as-you-go) ===
Microsoft's licence table allows instructions without pay-as-you-go, but not uploaded files.
So skip the Upload step: paste the whole of office-help-test.txt into the Instructions box instead, on a new line after the six lines above.
Together they come to about 1,750 characters, well under the 8,000 limit.
```

### 3. agent-builder-checklist.md
```
# Agent Builder: your first agent, from a test document (checked 2026-11-17)
# Work or school account. Made-up test document only. Follow your employer's rules.
# Test on the Try it tab. Keep the agent private: never select Share for a test agent.

## 0. What you need
- [ ] A work or school account, on a computer (Agent Builder isn't on the mobile apps)
- [ ] Your label (Part 1): on the Copilot home page, scroll to the bottom; the label is under your name
- [ ] M365 Copilot (Premium), the paid add-on: uploaded files work as knowledge
- [ ] Either Basic label, Copilot Chat (Basic) or M365 Copilot (Basic): Microsoft's table allows instructions and public websites; an uploaded file needs your organisation's pay-as-you-go billing (Copilot Credits), so ask the people who run your work accounts first
- [ ] Basic label and no pay-as-you-go? Build from instructions only: see step 3 (SharePoint and OneDrive files need the same licence or billing as uploads, so they're no way round it)
- [ ] office-help-test.txt and agent-setup.txt from this folder

## 1. Start the agent
- [ ] Open the Microsoft Copilot app at microsoft365.com/chat (also office.com/chat, or Teams on the desktop or the web)
- [ ] Select New agent in the left pane
- [ ] No New agent button? Your admins control who can use agents: ask them
- [ ] Select Skip to configure (the Configure tab opens)

## 2. Fill the boxes (from agent-setup.txt)
- [ ] Name: Office Help Test (30 characters at most)
- [ ] Description: paste it (1,000 characters at most)
- [ ] Instructions: paste them (8,000 characters at most)

## 3. Add the test document
- [ ] Knowledge section, Upload, choose office-help-test.txt
- [ ] It shows under Uploaded files, grey until the upload finishes
- [ ] Basic label and no pay-as-you-go: skip Upload; paste the whole of office-help-test.txt at the end of the Instructions box instead (see agent-setup.txt, "No upload?")
- [ ] The toggle called Search all websites: off
- [ ] Never upload real staff, customer or company files to a test agent

## 4. Test it on the Try it tab
- [ ] Try it switches on once Name, Description and Instructions are filled in
- [ ] Ask: How much notice do I need for a week off?
- [ ] Expect: ten working days. Check it by hand in office-help-test.txt
- [ ] Ask: Is there parking at the office?
- [ ] Expect: it says it doesn't know and suggests helpdesk@example.com
- [ ] It made up a parking rule? Make the "say that you don't know" line in Instructions plainer, then ask again

## 5. Keep it private
- [ ] Select Create: Microsoft says the agent is private and only available to you
- [ ] Don't select Share for a test agent (anyone who can use it can get answers from the uploaded file)

## 6. Later: copy it to Copilot Studio (optional)
- [ ] Open the agent, the More options (...) menu, Copy to Copilot Studio
- [ ] Upload office-help-test.txt again there: uploaded files aren't copied
- [ ] Copilot Studio needs the Premium label: Microsoft's licensing page says the Microsoft 365 Copilot add-on licence "is required for authoring agents in Copilot Studio"

## 7. Delete it when you've finished testing
- [ ] New agent in the left pane, then View all agents
- [ ] The three dots (...) beside Office Help Test, then Delete
- [ ] Microsoft says deleting is permanent and can't be reversed

Sources: learn.microsoft.com "Agent Builder overview"; "Build agents in Agent Builder"; "Add knowledge sources to an agent in Agent Builder"; "Share and manage agents built in Agent Builder"; "Copy an agent from Agent Builder to Copilot Studio"; "Choose between Agent Builder and Copilot Studio to build your agent"; "Set up your development environment" (agent capabilities and licensing models); microsoft.com Copilot Studio pricing page
```
