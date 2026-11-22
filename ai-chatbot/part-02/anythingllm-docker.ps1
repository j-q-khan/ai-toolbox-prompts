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
