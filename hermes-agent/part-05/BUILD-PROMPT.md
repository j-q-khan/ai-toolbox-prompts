Use this in Claude Code, or any chat assistant that can work with files, in a new folder with only hermes-ollama-setup-checklist.md in it. Start in plan mode, or the assistant's read-only mode.

Goal: help me connect Hermes Agent to Ollama on my own computer, using only the checklist, and write my own short setup notes. I download, click and type everything myself; you run nothing and install nothing.
Steps, in order:
1. Find hermes-ollama-setup-checklist.md in this folder. If it's missing, stop and tell me to save it from the link in the video's description.
2. Ask me, one at a time and waiting for each answer: Windows or Mac; how much memory (RAM) my computer has (Windows: Settings, System, About; Mac: Apple menu, About This Mac); whether I have a graphics card with its own memory, and how much; and whether I've done Part 2's Hermes setup.
3. Using only the checklist's "Will it fit?" section, tell me whether the checklist's model fits my memory, quoting the row and its date. If it doesn't fit, say so plainly and quote the checklist's note on smaller models. Never name a model, size or speed that isn't in the checklist.
4. Walk me through the checklist's sections in order (install Ollama, the model, the context window, connect Hermes, the checks), one box at a time, and wait for me to say each one is done.
5. Remind me, in the checklist's words, that the context must be set in the Ollama app, not in Hermes, and that a local model still runs commands, so approvals stay on manual.
6. Write my-ollama-setup.md: my computer, my memory, the model I pulled, the context I set, what ollama ps showed, what hermes config get approvals.mode printed, and the date the checklist was checked. Show it to me and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: never ask me to paste a key, password or token, and if I paste one by mistake, tell me to delete that key at my provider and make a new one. Create only my-ollama-setup.md in this folder. Don't edit any other file, don't run commands, don't install anything and don't go online.
Output: my-ollama-setup.md and a three-line summary of my setup.
