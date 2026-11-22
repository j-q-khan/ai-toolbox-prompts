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
