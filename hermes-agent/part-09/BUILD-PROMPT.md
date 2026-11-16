Use this in Claude Code, or any chat assistant that can work with files, in a new folder with only hermes-dashboard-checklist.md in it. Start in plan mode, or the assistant's read-only mode.

Goal: help me start the Hermes Agent v0.23.1 web dashboard, keep it on this computer, find the pages I need, and stop it, using only the checklist. I type and click everything myself; you run nothing and install nothing.
Steps, in order:
1. Find hermes-dashboard-checklist.md in this folder. If it's missing, stop and tell me to save it from the link in the video's description.
2. Ask me, one at a time and waiting for each answer: Windows or Mac; whether Hermes is already installed (if not, point me to Part 2 and stop); and whether I want the dashboard on this computer only or from another computer too.
3. Walk me through the checklist's "Start it" section one step at a time. After each step, tell me what the checklist says I should see, and wait for me to say it worked.
4. Walk me through the checklist's "Check it's only on this computer" section. If my command has --host with anything other than 127.0.0.1, or has --insecure, quote the checklist's lines about the sign-in gate and --insecure word for word, and tell me to go back to plain hermes dashboard.
5. If I want it from another computer, quote the checklist's "From another computer" section word for word and stop there; don't build any tunnel, network or password setup for me.
6. Ask which jobs I want to do in the dashboard (check approvals, see cost, find an old chat, check a key, find why a scheduled job failed) and, for each, tell me the page from the checklist's "Which page for which job" table.
7. Walk me through the checklist's "Stop it" section.
8. Write my-hermes-dashboard-notes.md: my system, the date, the command I used, whether the Status page showed my version, the pages I'll use and what for, and whether hermes dashboard --status said none are running after I stopped it. Show it to me and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: never ask me to paste a key, password or token, and if I paste one by mistake, tell me to delete it at the provider and make a new one. Never suggest --host 0.0.0.0, --insecure, or opening a port on my router. Create only my-hermes-dashboard-notes.md in this folder. Don't edit any other file, don't run commands, don't install anything and don't go online.
Output: my-hermes-dashboard-notes.md and a three-line summary of my setup.
