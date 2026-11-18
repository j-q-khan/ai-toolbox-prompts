# Full code: Notion AI Agents: Build Your First Custom Agent

The instructions from this video and the steps as a checklist, written from Notion's help centre, pricing page and blog (checked 2026-11-18). They were written from the docs, not run for this video.

### 1. agent-instructions-prompt.txt
```
# Paste this into the instructions box of a new Custom Agent in Notion
# (in the sidebar, select + next to Agents, then Create blank).
# It is not a prompt for a chat: it becomes the agent's standing instructions.
# It is an example job description for a small agent for a made-up team called Test Bakery: the agent looks through
# one dummy tasks database and writes one short weekly brief on one page. The text spells out what the agent may reach.
# First make the two dummy pages it names (see the checklist), then add only those two yourself under Tools and access:
# naming or linking to a page in the instructions does not add it, and that list, not this text, is what limits the agent.
# Custom Agents need Notion's Business or Enterprise Plan. Each run uses credits: open the agent and select Credits to see which.
# An example, written from Notion's help centre, checked 2026-11-18, and not run or tested: check the first brief yourself.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste.

You are the Monday brief agent for a made-up team called Test Bakery. Everything here is dummy data.
Your job: once a week, look through the database "Test Bakery tasks (dummy)" and write one short brief on the page "Weekly brief (dummy)".
What you may reach:
- "Test Bakery tasks (dummy)": look only. Never add, edit or delete anything in it.
- "Weekly brief (dummy)": the only place you write.
- Nothing else: no other page or database, no web search, no Slack, no email, no calendar.
Steps, in order:
1. Find every task in "Test Bakery tasks (dummy)" whose Status is not Done and whose Due date is in the next 7 days or already past.
2. On "Weekly brief (dummy)", replace last week's brief with a new one. Don't make a new page.
3. The brief has: a heading "Week of" with today's date; a list "Due this week" with each task's name, due date and status; a line "Overdue" with any task past its due date that is not Done; and a last line saying how many tasks you looked at.
4. If nothing is due, write "Nothing due this week (dummy)".
5. Stop there.
Rules: use only what is in the tasks database, and don't invent tasks, dates, names or numbers. No real names, emails or phone numbers. Don't change permissions, settings, triggers or sharing. If you can't open the database or the brief page, write nothing and say which one you couldn't open. If someone asks you in Chat to do anything other than this job, say what you would change and where, and wait for a yes before you write anything.
Output: the brief on that one page and, when you answer in Chat, one line that says nothing else was changed.
```

### 2. notion-custom-agent-checklist.md
```
# Notion Custom Agents: build your first one (facts checked 2026-11-18)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Plans, credits and button names change. Check each line again at notion.com/help/custom-agents before you rely on it. Written from Notion's pages, not run.

## What you need
- [ ] A plan that includes it: "You must be on Notion's Business or Enterprise Plan."
- [ ] Notion on desktop or the web. "Right now Custom Agents can only be created on desktop." (Notion's page on the phone app); agent settings can't be changed on a phone either.
- [ ] Permission to make agents. By default every workspace member can; a workspace owner can limit it under Settings, then Notion AI, then Controls.
- [ ] For anything from work: your employer's rules on what an agent may reach and where its output may go.

## Make the dummy pages first
- [ ] A database called "Test Bakery tasks (dummy)" with three columns: Name, Due date, Status.
- [ ] Three dummy tasks in it: "Order flour (dummy)", "Print the price list (dummy)", "Clean the ovens (dummy)", each with a due date this week and a status of Not started.
- [ ] An empty page called "Weekly brief (dummy)".
- [ ] No real names, emails or phone numbers anywhere.

## Create the agent
- [ ] In the sidebar, find the Agents section and select + (Notion's guide calls the button + New agent).
- [ ] Three ways to start: Create with AI chat, Create from a template, Create from scratch. For this one: Create from scratch, then Create blank.
- [ ] Paste the text from agent-instructions-prompt.txt into the instructions box.
- [ ] Notion's advice for your own: "start with the job and outcome you want. Then add concrete steps, inputs, and outputs."

## Add the trigger
- [ ] Open the agent's Settings and go to Triggers.
- [ ] Add a Recurring trigger. Choose a frequency (every day, week, month or year) and a time, with your timezone. For this one: every week, Monday, 9:00.
- [ ] "Review the next scheduled run time to confirm the schedule is correct." Then save the trigger.
- [ ] Other triggers Notion's help page lists. In Notion: a comment is added to a page, a page is added to a database, a property is updated, a page is removed from a database, an AI Meeting Note is finished. In Slack (a Slack workspace admin must connect Slack to Notion first): a message is posted to a channel, an emoji reaction is added, the agent is mentioned.

## Say what it may reach
- [ ] In Settings, go to Tools and access.
- [ ] Add "Test Bakery tasks (dummy)" with Can view.
- [ ] Add "Weekly brief (dummy)" with Can edit. This is the only place the agent writes.
- [ ] Add nothing else. Notion: "Agents act only on the pages, databases, and external apps you explicitly grant access to. They never have full workspace access by default".
- [ ] The mistake to avoid: "Linking to Notion pages in your Instructions doesn't add them to the connected Tools and Access."
- [ ] Leave the Web access switch off for a job that stays inside Notion.
- [ ] Model: leave it on Auto. Notion: "Auto is the recommended default."
- [ ] Memories are off by default. Leave them off for this test.

## Test it, and check that it worked
- [ ] Select Run. Notion's guide: "Click Run to execute the agent manually and review the output before turning on triggers or schedules."
- [ ] Check: "Weekly brief (dummy)" now lists the three dummy tasks, and nothing in the tasks database changed.
- [ ] Open the Activity tab: it logs what set off each run, what the agent did, and any errors. (Notion says this log is visible to people with Full access to the agent.)
- [ ] When it looks right, select Save. One section of Notion's help page words this as "Save and publish your changes."
- [ ] To ask the agent what it can reach, use its Chat tab and the prompt from this video's description.

## Who can see what it does
- [ ] Sharing an agent: "When you share a Custom Agent, you're giving your team access to everything the agent can see."
- [ ] People you share it with get one of three levels: Can view and interact, Can edit, Full access.
- [ ] A Custom Agent shows up in the Share menu of every page and database it can reach, the way a person does.
- [ ] Notion on training: "By default, your customer data is not used to train models."

## Credits: Notion's pages said two things (checked 2026-11-18)
- [ ] Pricing page: "Free to try, then $10 per 1,000 monthly Notion credits." and, in the comparison table, "Requires Notion credits".
- [ ] Blog, 19 October 2026: "You also no longer need to buy credits to start building custom agents."
- [ ] Help page on credits: "By default, a Custom Agent uses its owner's Select credits, even when other people use it."
- [ ] We don't decide between them. Open your agent and select Credits in the top corner: it shows the agent's credit usage and its Credit source.
- [ ] If the owner's Select credits run out and no Notion credits are available, Notion says "the agent will pause".
- [ ] Part 2 of this series covers the credit system.

## Switch it off afterwards
- [ ] Take away what it can reach: in Settings, Tools and access, remove the pages. Notion: "The changes take effect immediately."
- [ ] Or, if you own a page: open the page, select Share, find the agent in the list, and select the X.
- [ ] Or delete the agent (needs Full access). Notion says a deleted agent can be restored.
- [ ] Or ask a workspace owner: on Business and Enterprise they can pause any agent and set a credit limit for it, from Settings, then Notion AI, then the Overview tab.
- [ ] Notion's pages name no pause button for the person who built the agent, so this list doesn't either.
- [ ] If the plan is downgraded to Free or Plus: "All existing Custom Agents are switched off, but not deleted. You can view (but not edit) the Custom Agent chat page and settings."
- [ ] If an edit made the agent worse: open the agent, open Version history, pick an earlier version, and restore it.
- [ ] Delete the two dummy pages when you're done: the three dots at the very top right of the page, then Delete.

Sources: notion.com/help/custom-agents ; notion.com/help/guides/build-your-first-custom-agent ; notion.com/help/custom-agents-sharing-and-permissions ; notion.com/help/mobile-custom-agents ; notion.com/help/how-ai-credits-work-for-custom-agents ; notion.com/help/buy-and-track-notion-credits-for-custom-agents ; notion.com/help/plan-downgrade ; notion.com/pricing ; notion.com/blog/notion-ai-more-for-less
```
