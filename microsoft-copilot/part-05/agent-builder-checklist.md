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
