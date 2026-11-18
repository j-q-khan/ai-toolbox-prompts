# Full code: Copilot Studio Agent Flows: Make Your Agent Run a Power Automate Flow

The test table's headings and a checklist of every step, written for this video from Microsoft Learn's agent flow pages (checked 2026-11-17). Nothing here was run for this video; use them with a made-up request, a test table and your own email only, and test in the test pane without publishing the agent.

### 1. agent-flow-test-log-headers.csv
```
Item,Problem
```

### 2. agent-flow-checklist.md
```
# Copilot Studio agent flows: make your agent run a flow (checked 2026-11-17)
# Made-up requests only. Write to a test table, email only yourself. Test in the test pane; don't publish the agent.
# Follow your employer's rules on what you may build and connect.

## 0. What you need
- [ ] The agent from Part 5 (Office Help Test), built in Agent Builder
- [ ] The Premium label under your name (the paid Microsoft 365 Copilot add-on) or a Copilot Studio licence
- [ ] Microsoft's words: "a license that includes the use of flows in Copilot Studio"; if you're not sure, ask the people who run your work accounts
- [ ] An environment with a Dataverse database (not a Dataverse for Teams environment)
- [ ] agent-flow-test-log-headers.csv from this folder

## 1. Copy the agent into Copilot Studio (Agent Builder agents can't call a flow)
- [ ] In the Copilot app, open the agent's More options (...) menu, then Copy to Copilot Studio
- [ ] Pick an environment; if none can be picked, ask the people who run your work accounts
- [ ] Uploaded files aren't copied (this test doesn't need them)
- [ ] Open the copy in Copilot Studio and go to its Tools page
- [ ] No Tools page, only a Build tab? Microsoft's agent flow steps are written for agents with a Tools page; ask the people who run your work accounts before going further

## 2. The test table
- [ ] Open agent-flow-test-log-headers.csv in Excel
- [ ] Select a heading, then Home, Format as Table, any style, tick My table has headers, OK
- [ ] File, Save As: Excel Workbook, name agent-flow-test-log, in OneDrive (for example a folder called Flow test)
- [ ] Shut the workbook before you test

## 3. Create the agent flow from the Tools page
- [ ] Tools, Add a tool, Agent flow (under Create new)
- [ ] The designer opens with When an agent calls the flow at the top and Respond to the agent at the bottom
- [ ] Microsoft's other route, not used here: Workflows page, More create options, under Build with standard orchestration, Agent flows

## 4. The trigger: When an agent calls the flow
- [ ] Add an input: Text, named Item
- [ ] Add an input: Text, named Problem

## 5. Action 1: Excel Online (Business), Add a row into a table
- [ ] Location and Document Library: your OneDrive
- [ ] File: agent-flow-test-log.xlsx
- [ ] Table: your table
- [ ] Item: the Item input
- [ ] Problem: the Problem input

## 6. Action 2: Office 365 Outlook, Send an email (V2)
- [ ] To: your own email only
- [ ] Subject: Test request logged
- [ ] Body: the Item input, then the Problem input

## 7. Respond to the agent
- [ ] Add an output: Text, named Result, value Logged in the test table
- [ ] Settings, Asynchronous response: Off (Copilot Studio sets this off for flows made there)
- [ ] The flow must answer the agent within 100 seconds

## 8. Publish the flow (not the agent)
- [ ] Select Publish at the top of the designer (fix any errors the flow checker lists first)
- [ ] The agent stays unpublished

## 9. Add it to the agent as a tool
- [ ] Tools, Add a tool, Flow, pick the flow, Add and configure
- [ ] Not listed? It needs the When an agent calls the flow trigger, Respond to the agent, and Publish
- [ ] Description: Use this when someone asks to log a test request. It adds the item and the problem to a test table and emails the maker.
- [ ] Inputs: let the agent fill Item and Problem from the chat
- [ ] Save

## 10. Test it in the test pane
- [ ] Hidden? Select Test at the top of the page
- [ ] Workbook shut in Excel
- [ ] Type: Please log a test request: the projector in room 2 is flickering.
- [ ] The activity map shows the agent calling your flow, and it replies with the Result
- [ ] Check the new line in agent-flow-test-log.xlsx (it can take up to 30 seconds) and the email in your inbox, by hand
- [ ] The agent answered without calling the flow? Make the tool's description plainer, then ask again

## 11. Credits, and turning it off
- [ ] Agent flow actions: 13 Copilot Credits per 100 actions (when checked 2026-11-17)
- [ ] Test runs from the test pane or the designer: no capacity used
- [ ] Runs through this trigger by a user signed in with a Microsoft 365 Copilot licence: no charge
- [ ] Environment out of Copilot Credits: new agent flow runs are blocked; the agent keeps answering
- [ ] When you've finished: open the flow's Overview tab and turn it off

## 12. Later
- [ ] One agent flow can be a tool in any of your agents
- [ ] An existing Power Automate cloud flow can be converted to an agent flow (in a solution, change its plan to Copilot Studio); it's one way only, because its billing changes
- [ ] Desktop flows can't be a tool in Copilot Studio

Sources: learn.microsoft.com "Agent flows overview"; "Create an agent flow as a tool"; "Add an agent flow to an agent"; "Call an agent flow from an agent"; "FAQ for agent flows"; "Edit and manage your agent flow in the designer"; "Monitor your agent flows"; "Test your agent"; "Billing rates and management"; "Agent Builder overview"; "Copy an agent from Agent Builder to Copilot Studio"; "Excel Online (Business)" and "Office 365 Outlook" connector references; Microsoft Support "Create and format tables"
```
