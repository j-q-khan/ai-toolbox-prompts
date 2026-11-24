Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new, empty folder holding only jarvis-pc-setup-checklist.md from this video's files. It writes one small script that asks which system you're on and which chat window you want, then prints the matching steps from the checklist, with each program's licence, last release and what it can reach. The script only prints: it installs, downloads and runs nothing, and Claude Code asks before it creates anything. Written from the makers' docs, checked 2026-11-23. Nothing here was run for the video.

Goal: write print_setup_steps.py, a small Python script that prints my setup steps for a local assistant (Ollama plus Open WebUI or Jan), taken only from jarvis-pc-setup-checklist.md.
Steps, in order:
1. Look through jarvis-pc-setup-checklist.md in this folder. Tell me in two sentences what the script will do and which one file you'll create, then wait for me to say go.
2. Use Python 3 and its standard library only. No installs, no internet requests, no subprocess calls, no shell commands, and no writing or deleting of any file except print_setup_steps.py itself.
3. The script asks two questions: which system (Windows, Mac or Linux) and which chat window (Open WebUI in Docker, or Jan). It then prints, in order: the three checks to make before installing anything; Ollama's licence, last release and reach; the Ollama install step for that system; the chat window's licence, last release and reach; its setup steps; and the local-only setting for Ollama.
4. Copy every command, path, version and date word for word from the checklist, each with its source link, and label commands "Type this yourself after checking it". Never run them.
5. For Open WebUI, always print the troubleshooting warning from the checklist next to the OLLAMA_HOST step, and the firewall advice.
6. Never overwrite a file that already exists: if print_setup_steps.py is there, stop and tell me.
7. Then test it by running it twice with made-up answers (Windows with Open WebUI; Mac with Jan), and show me both outputs.
Safety: look only at jarvis-pc-setup-checklist.md. Don't change, move or delete it or anything else. Don't open any website, call any API, download or install anything, or run any command from the checklist.
Output: print_setup_steps.py, the two test outputs, and a three-line note saying what you created.
