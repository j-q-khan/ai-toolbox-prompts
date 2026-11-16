Use this in Claude Code, or any chat assistant that can work with files, in a new folder with only hermes-docker-checklist.md and compose.yaml in it. Start in plan mode, or the assistant's read-only mode.

Goal: help me run Hermes Agent v0.23.1 in Docker with the compose.yaml from the video, using only the checklist. I type and click everything myself; you run nothing and install nothing.
Steps, in order:
1. Find hermes-docker-checklist.md and compose.yaml in this folder. If either is missing, stop and tell me to save it from the link in the video's description.
2. Ask me, one at a time and waiting for each answer: Windows or Mac; whether Docker Desktop is installed and running; and whether I've done Part 2's Hermes setup.
3. Using only the checklist's "Before you start" section, check my computer against Docker's requirements with me, one line at a time.
4. Walk me through the checklist's "Step by step" section one command at a time. After each, tell me what the checklist says I should see, and wait for me to say it worked. If I paste an error, match it to the checklist's "If something goes wrong" lines, in the checklist's words.
5. If I ask about the repo's own compose files or the docker terminal backend, answer only from the checklist's sections on them, and say plainly what the docs say about the skipped dangerous command check.
6. Write my-hermes-docker-notes.md: my system, the date, the image tag, the data folder's full path, each step and whether it worked. Show it to me and wait for my yes. I'll switch you out of plan or read-only mode so you can save it.
Safety: never ask me to paste a key, password or token, and if I paste one by mistake, tell me to delete that key at its provider and make a new one. Never suggest mounting my home folder, publishing ports or adding the Docker socket. Create only my-hermes-docker-notes.md in this folder. Don't edit any other file, don't run commands, don't install anything and don't go online.
Output: my-hermes-docker-notes.md and a three-line summary of my setup.
