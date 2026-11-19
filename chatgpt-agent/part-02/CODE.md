# Full code: ChatGPT Agent Mode Missing? Where It Went and What to Use Now

The copy-paste prompt and a checklist, written from OpenAI's help pages (checked 2026-11-19). They were written from the docs, not run for this video.

### 1. agent-mode-jobs-to-work.txt
```
# Paste this into ChatGPT, not into Claude.
# If you have Work, switch the toggle above the message box to Work first; if you can't find Work yet, it also works in Chat.
# Replace the words in square brackets with your own jobs, then paste everything below the # lines and send.
# Written from OpenAI's help pages, checked 2026-11-19, not run. Check each answer against the OpenAI page it names before you rely on it.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste into ChatGPT.

Goal: help me find where the jobs I've done with agent mode fit in ChatGPT Work.
Steps, in order:
1. Before you start, ask me three things and wait for my answers: which plan I'm on (Free, Go, Plus, Pro, Business, Enterprise or Edu), which device I use (the desktop app on Mac, Windows or Linux, the website, or the phone app), and whether this is a personal account or a work or school workspace.
2. These are the jobs I used agent mode for, one per line:
[job 1, for example: compare three made-up hotel prices for a trip]
[job 2]
[job 3]
3. Ask me before you look anything up. Then, for each job, use OpenAI's own help pages at learn.chatgpt.com and chatgpt.com/pricing to say which part of ChatGPT Work would handle it today (for example a Work task, the cloud browser, Computer Use, a scheduled task or a plugin) and where to find it.
4. If a page doesn't say, write "Not in OpenAI's docs" for that job instead of guessing.
5. If my plan, device or workspace can't use that part, say so, and quote the line from OpenAI's page that says it.
6. Give me the answer as a short table with four columns: job, part of ChatGPT Work, where to find it, OpenAI page. Then stop.
Rules: ask me before you visit a website, sign in, buy, send or delete anything. Never ask me for a password or a payment detail. Don't do any of the jobs, only map them. If anything is unclear, ask me first.
Reminder for me: check each answer against the OpenAI page it names before I rely on it.
```

### 2. agent-mode-missing-checklist.md
```
# ChatGPT agent mode missing? Checklist (facts checked 2026-11-19, from OpenAI's own pages)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Where to look
- [ ] OpenAI's Work admin FAQ: "ChatGPT Work lets users delegate longer, multi-step tasks to ChatGPT." Look for Work.
- [ ] In the desktop app, use the toggle above the message box to pick Chat or Work.
- [ ] OpenAI's Work FAQ: availability "depends on role, plan, workspace, and region". Check the four reasons below in order.

## 1. Your plan
- [ ] Pricing page, ChatGPT Work: Free and Go "Limited (desktop app)"; Plus and Pro "Desktop, web, and mobile" (checked 2026-11-19): https://chatgpt.com/pricing
- [ ] On Free or Go: get the ChatGPT desktop app, offered for macOS (Apple Silicon), Windows and Linux: https://learn.chatgpt.com/docs/app
- [ ] Prices and plan details change; check the pricing page before you pay: https://learn.chatgpt.com/docs/pricing

## 2. A work or school account (a workspace)
- [ ] For eligible Enterprise and Edu workspaces, the default role includes Work unless an authorized administrator turns it off.
- [ ] Ask your workspace owner to check Workspace settings, then Permissions & roles, where admins give people access to ChatGPT Work.
- [ ] Enterprise admins must also enable cloud browsing for their workspace.

## 3. An out-of-date desktop app
- [ ] The desktop app normally checks for and installs updates on its own.
- [ ] Use the Check for Updates option.
- [ ] Quit the app fully and open it again: shutting the window isn't always enough to restart it.
- [ ] OpenAI's setup notes ask for the latest version for Local computer access with Work Cloud to take effect.

## 4. Your region (Computer Use)
- [ ] Computer Use (ChatGPT operating apps on your computer) is in supported regions only, on macOS and Windows. The page lists no regions.
- [ ] Check it: Settings, then Computer use, shows which apps it can control.
- [ ] The cloud browser is in all regions on paid plans other than Free and Go.
- [ ] During rollout, the browser might not appear immediately even when your plan supports it.

## Check it worked
- [ ] The toggle above the message box shows Work.
- [ ] Send a small task: you can follow progress, answer questions, change direction and approve important actions.
- [ ] Work conversation missing on another device? Sign in to the same account and workspace on each device and look in Work history (Codex keeps its own history).

## Developers: Agent Builder
- [ ] Agent Builder is scheduled to shut down on 30 November 2026. OpenAI's deprecations page names the Agents SDK or ChatGPT Workspace Agents as the replacement; ChatKit remains available: https://developers.openai.com/api/docs/deprecations

## Safety
- [ ] Never type a password or a card number into the chat. Safety settings are Part 4 of this series.

Sources: learn.chatgpt.com/docs/enterprise/work-admin-faq ; /docs/app ; /docs/pricing ; /docs/enterprise/chatgpt-work-overview ; /docs/enterprise/manage-app-updates ; /docs/computer-use ; /docs/browser ; /docs/get-started-with-work ; /docs/reference/troubleshooting ; chatgpt.com/pricing ; developers.openai.com/api/docs/deprecations
```
