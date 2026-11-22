# Full code: AI Chatbot Free: An Open-Source Chatbot That Answers From Your Documents (AnythingLLM)



### 1. anythingllm-docker.sh
```
#!/usr/bin/env bash
# Start AnythingLLM in Docker, with its built-in model turned on. From AI Chatbot, Part 2.
# Copied from AnythingLLM's docs, Built-in LLM for Docker, "CPU only", Linux/Mac tab:
#   https://docs.anythingllm.com/installation-docker/built-in-llm  (checked 2026-11-22; written from the docs, not run)
# It is the docs' regular install command (https://docs.anythingllm.com/installation-docker/local-docker)
# with one line added: -e ENABLE_BUILT_IN_LLM=true. Delete that line if you'd rather pick a cloud provider in the app.
# What it does: downloads the image, makes a storage folder at $HOME/anythingllm (your documents and settings live
# there, so they survive a restart), and starts a container called anythingllm on port 3001.
# No provider key goes in this file: if you choose a cloud provider, you enter its key in the app.
# How to save it: on a Mac, open TextEdit, choose Format, Make Plain Text, paste this text and save it as
# anythingllm-docker.sh. On Linux, use any plain text editor.
# How to run it: open Terminal in the folder where you saved it, type  bash anythingllm-docker.sh  and press Enter.
# Then open http://localhost:3001 in your browser and click Get Started.
# Needs Docker installed and running. The docs list 2GB of RAM and a 2-core CPU with AVX2 as the minimum.
# For testing first: try it on a test machine with made-up documents, like the Test Bakery price list, not real customer files.
# Run it once. After a restart, start the same container again with: docker start anythingllm (a standard Docker
# command, not from AnythingLLM's docs). Running this file a second time stops with a name clash, because a container
# called anythingllm already exists; the docs' advice for a dead container is to remove it (docker rm anythingllm)
# and run the install command again. Your data stays in the storage folder.
set -euo pipefail

docker pull mintplexlabs/anythingllm:latest

export STORAGE_LOCATION=$HOME/anythingllm && \
mkdir -p $STORAGE_LOCATION && \
touch "$STORAGE_LOCATION/.env" && \
docker run -d -p 3001:3001 \
--cap-add SYS_ADMIN \
--name anythingllm \
-v ${STORAGE_LOCATION}:/app/server/storage \
-v ${STORAGE_LOCATION}/.env:/app/server/.env \
-e STORAGE_DIR="/app/server/storage" \
-e ENABLE_BUILT_IN_LLM=true \
mintplexlabs/anythingllm
```

### 2. anythingllm-docker.ps1
```
# Start AnythingLLM in Docker on Windows, with its built-in model turned on. From AI Chatbot, Part 2.
# Copied from AnythingLLM's docs, Built-in LLM for Docker, "CPU only", Windows tab:
#   https://docs.anythingllm.com/installation-docker/built-in-llm  (checked 2026-11-22; written from the docs, not run)
# It is the docs' regular install command (https://docs.anythingllm.com/installation-docker/local-docker)
# with one line added: -e ENABLE_BUILT_IN_LLM=true. Delete that line if you'd rather pick a cloud provider in the app.
# What it does: downloads the image, makes a storage folder at Documents\anythingllm (your documents and settings
# live there, so they survive a restart), and starts a container called anythingllm on port 3001.
# No provider key goes in this file: if you choose a cloud provider, you enter its key in the app.
# How to save it: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
# and name it anythingllm-docker.ps1
# How to run it: open PowerShell from the Start menu, then copy every line below the comments from this file
# and paste them into PowerShell, and press Enter.
# Then open http://localhost:3001 in your browser and click Get Started.
# Needs Docker Desktop installed and running. The docs list 2GB of RAM and a 2-core CPU with AVX2 as the minimum.
# For testing first: try it on a test machine with made-up documents, like the Test Bakery price list, not real customer files.
# Run it once. After a restart, start the same container again with: docker start anythingllm (a standard Docker
# command, not from AnythingLLM's docs). Running these lines a second time stops with a name clash, because a container
# called anythingllm already exists; the docs' advice for a dead container is to remove it (docker rm anythingllm)
# and run the install command again. Your data stays in the storage folder.

docker pull mintplexlabs/anythingllm:latest

$env:STORAGE_LOCATION="$HOME\Documents\anythingllm"; `
If(!(Test-Path $env:STORAGE_LOCATION)) {New-Item $env:STORAGE_LOCATION -ItemType Directory}; `
If(!(Test-Path "$env:STORAGE_LOCATION\.env")) {New-Item "$env:STORAGE_LOCATION\.env" -ItemType File}; `
docker run -d -p 3001:3001 `
--cap-add SYS_ADMIN `
--name anythingllm `
-v "$env:STORAGE_LOCATION`:/app/server/storage" `
-v "$env:STORAGE_LOCATION\.env:/app/server/.env" `
-e STORAGE_DIR="/app/server/storage" `
-e ENABLE_BUILT_IN_LLM=true `
mintplexlabs/anythingllm;
```

### 3. embed-snippet.html
```
<!--
  The AnythingLLM chat widget's script tag, in the shape the app itself writes it (CodeSnippetModal in
  github.com/Mintplex-Labs/anything-llm at v1.20.0, MIT), plus two options from the widget's README (MIT):
  https://github.com/Mintplex-Labs/anythingllm-embed  (checked 2026-11-22; written from the code and docs, not run)
  The app starts both URLs with the address you opened it at; here that is http://localhost:3001, and the
  embed id is a placeholder. Don't copy these values: AnythingLLM makes your real
  tag for you. In the app, open the settings, then Tools, then Chat Embed, then Create embed. Then click
  Code on your widget's line, and copy the tag from the window called Copy your embed code.
  REQUIRED data attributes, in the README's words:
    data-embed-id      The unique id of your embed with its default settings
    data-base-api-url  The URL of your anythingLLM instance backend
  localhost only works on your own computer. For real visitors, AnythingLLM must run on a server that stays
  online, with Password Protection turned on, under Security. The docs say: do not tunnel your personal machine to the
  public internet.
  The two optional lines below are documented options: data-greeting is the first message a visitor sees,
  and data-support-email lets a visitor email a person. Swap in your own business name and email.
  Paste the tag at the bottom of your page, before the closing body tag, as the app's own note says.
-->
<script
  data-embed-id="YOUR-EMBED-ID-FROM-ANYTHINGLLM"
  data-base-api-url="http://localhost:3001/api/embed"
  data-greeting="Hi, I'm Test Bakery's AI assistant, not a person."
  data-support-email="test@example.com"
  src="http://localhost:3001/embed/anythingllm-chat-widget.min.js"
></script>
```

### 4. widget-checklist.txt
```
# AnythingLLM chat widget: a settings checklist. From AI Chatbot, Part 2.
# Facts checked 2026-11-22 from AnythingLLM's docs (docs.anythingllm.com) and its MIT repo. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it widget-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as widget-checklist.txt
# How to use it: tick every line before you paste the widget's code into a real website.

BEFORE YOU START
[ ] I'm using the Docker version ("These settings are only available in the Docker version of AnythingLLM")
[ ] My computer meets the docs' minimum: 2GB of RAM, a 2-core CPU with AVX2, 5GB of storage
[ ] If the container stops with "Illegal instruction (core dumped)", my CPU lacks AVX2: the docs' System Requirements page says what to do
[ ] I started it with the storage folder in the command, so my data survives a restart
[ ] After a reboot I start it with docker start anythingllm, not by running the install file again (that stops with a name clash)

THE MODEL
[ ] Built-in model: one of Fastest, Balanced or Most capable is downloaded (our file runs on the processor; a graphics card needs the docs' GPU command)
[ ] Or a cloud provider: I know they bill me, and that questions and document snippets go to them
[ ] My provider key is only in the app's settings, never in a web page or the embed code
[ ] Telemetry: I've decided whether to switch it off (Privacy and Data, in the settings)

THE WORKSPACE
[ ] My documents are embedded in the workspace (Move to Workspace, then Save and Embed), not attached in a chat
[ ] Chat Settings is set to Query mode, and I've tested 10 real customer questions
[ ] I've tested a question that isn't in my documents, and it says it couldn't find it
[ ] If it misses answers that are there: workspace settings, Vector Database, Document similarity threshold, No restriction

THE WIDGET (settings, Tools, Chat Embed, Create embed)
[ ] Workspace: the right one
[ ] Allowed chat method: Query ("only respond to chats related to documents in the workspace")
[ ] Restrict requests from domains: my own domain is filled in ("Leaving this field empty means anyone can use your embedded chat widget on any site")
[ ] Max chats per day: a number, not zero (zero means unlimited)
[ ] Max chats per session: a number, not zero
[ ] A greeting that says it's an AI, not a person (data-greeting)
[ ] A way to reach a person (data-support-email)

GOING ONLINE
[ ] It runs on a server that stays online, not my laptop
[ ] I have not tunnelled my own computer to the internet ("Do not tunnel your personal machine to the public internet")
[ ] Password Protection (the docs call it Password Protect Instance) or Multi-User Mode is on, under Security
[ ] HTTPS: a reverse proxy with a TLS certificate in front, as the docs' Cloud Docker page says
[ ] Someone checks for new releases and keeps backups of the storage folder
[ ] Someone looks at Embed Chat History every week and adds the documents it was missing
```
