Use this in Claude Code, or any chat assistant that can work with files, in a new folder with only hermes-safe-setup-checklist.md in it. Start in plan mode, or the assistant's read-only mode.

Goal: walk me through the safe Hermes Agent setup from the checklist, one step at a time, and check what I paste back. I type every command myself; you run nothing and install nothing.
Steps, in order:
1. Find hermes-safe-setup-checklist.md in this folder. If it's missing, stop and tell me to save it from the link in the video's description.
2. Ask whether I'm on Windows or a Mac, and whether I already use Claude Code or Codex. Use only the sections of the checklist that apply to me.
3. Give me one step at a time: the exact command from the checklist, where to type it, and what the checklist says I should see. Wait for me to say done, or to paste what I saw, before the next step.
4. When I paste the output of hermes config get approvals.mode or hermes gateway status, compare it with what the checklist says to expect, and tell me plainly whether it matches. If it doesn't, point me to the checklist's fix for that step, or to hermes doctor. Never invent a command, flag or setting that isn't in the checklist.
5. Remind me, in the checklist's own words, that manual approval only asks for commands on the dangerous-pattern list, and that the test folder doesn't fence Hermes in.
6. At the end, write my-hermes-setup-notes.md: my system, which steps I finished, the outputs I pasted (with any key or secret replaced by the word REMOVED), and anything still to do. Show it to me and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: never ask me to paste a key, password or token, and if I paste one by mistake, tell me to delete that key at my provider and make a new one. Create only my-hermes-setup-notes.md in this folder. Don't edit any other file, don't run commands, don't install anything and don't go online.
Output: my-hermes-setup-notes.md and a three-line summary of where my setup stands.
