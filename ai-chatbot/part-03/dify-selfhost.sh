#!/usr/bin/env bash
# Self-host Dify with Docker Compose. From AI Chatbot, Part 3.
# Written from Dify's docs, "Deploy Dify with Docker Compose", and docker/README.md at release 1.20.0:
#   https://docs.dify.ai/en/self-host/deploy/quick-start/docker-compose  (checked 2026-11-22; written from the docs, not run)
# Before you start (the docs' list): Docker with Docker Compose 2.35.0 or later, with Docker running; Git; OpenSSL.
#   At least 2 CPU cores and 4 GiB of RAM. On a Mac, give Docker Desktop's virtual machine at least 2 virtual CPUs
#   and 8 GiB of memory. On Windows, use Docker Desktop with WSL 2, and run this file in a WSL terminal, inside the
#   Linux file system (for example your Linux home folder), not in a Windows folder.
# What it does: downloads Dify 1.20.0 into a folder called dify, copies the settings template to .env, puts a random
#   secret into .env (the docs' openssl step), starts every service, then lists them.
# Lines marked "Not from Dify's docs" are safety steps we added.
# This is for a new install only. For an existing install, the docs say follow their Upgrade steps instead.
# How to save it: on a Mac, open TextEdit, choose Format, Make Plain Text, paste this text and save it as
#   dify-selfhost.sh in an empty folder. On Linux, use any plain text editor. On Windows, don't save it with Notepad
#   (Notepad can add Windows line endings, which bash rejects; this note is not from Dify's docs): in the WSL terminal,
#   type  nano dify-selfhost.sh , paste the text, press Ctrl+O, Enter and Ctrl+X, or download the file from the GitHub folder.
# How to run it: open Terminal (Mac) or your WSL terminal (Windows), go to that folder, type  bash dify-selfhost.sh
#   and press Enter. Then open http://localhost/install in your browser and create the administrator account.
# Before anyone else can reach it, the docs say: configure HTTPS and replace the bundled development credentials
#   in docker/.env (DB_PASSWORD, REDIS_PASSWORD and the others under "Secure the Deployment" on the docs page).
# Licence: Dify is "a modified version of the Apache License 2.0" with extra conditions. Check the LICENSE file in
#   the dify folder before any business use, and ask Dify in writing if you're unsure.
# Test use only: run it on a test machine with made-up documents, like the Test Bakery price list, and keep it
#   off the internet until HTTPS is set up and the development credentials are replaced.
set -euo pipefail

# Not from Dify's docs: stop if a dify folder is already here, so nothing is overwritten.
if [ -e dify ]; then
  echo "A folder called dify already exists here. Run this from an empty folder." >&2
  exit 1
fi

# Not from Dify's docs: if a step fails before Dify starts, remove the half-made dify folder and the temporary
# file, so nothing is left behind and you can run this again.
clone_dir="$(pwd)/dify"
tmp_env=""
started=no
cleanup() {
  status=$?
  if [ -n "$tmp_env" ]; then rm -f "$tmp_env"; fi
  if [ "$status" -ne 0 ] && [ "$started" = no ] && [ -d "$clone_dir" ]; then
    rm -rf "$clone_dir"
    echo "Something failed before Dify started, so the dify folder was removed. Fix the error above and run this again." >&2
  fi
}
trap cleanup EXIT

docker compose version

git clone --branch 1.20.0 --depth 1 https://github.com/langgenius/dify.git
cd dify/docker

cp .env.example .env

# The docs: generate a token with  openssl rand -hex 32  and set DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN in .env to it.
# Not from Dify's docs: this writes it into .env for you, without printing it.
if ! grep -q '^DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=' .env; then
  echo "DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN wasn't found in .env. Set it by hand, as the docs say." >&2
  exit 1
fi
token="$(openssl rand -hex 32)"
tmp_env="$(mktemp)"
DIFY_TOKEN="$token" awk '/^DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=/ { print "DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN=" ENVIRON["DIFY_TOKEN"]; next } { print }' .env > "$tmp_env"
mv "$tmp_env" .env
tmp_env=""
unset token

started=yes
docker compose up -d
docker compose ps --all
# The docs: long-running services should show Up or healthy, and init_permissions shows Exited (0) when it's done.
