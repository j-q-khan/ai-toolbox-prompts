# Full code: n8n Tutorial for Beginners: Install n8n Free with Docker

The two commands from this video, written from n8n's README and Docker image README (checked 2026-11-16), plus a safe-setup checklist. They are copied from the docs, not run for this video.

### 1. start-n8n.txt
```
# n8n 2.47.7 with Docker Desktop. Works in Windows PowerShell and Mac Terminal.
# Copy one command at a time (lines starting with # are notes, not commands).

# Command 1, once: make the volume that keeps your workflows and n8n's encryption key
docker volume create n8n_data

# Command 2: start n8n at a fixed version, open to this computer only (one line).
# Changed from n8n's README: 127.0.0.1 added, because Docker's docs say a plain -p 5678:5678 publishes to other machines too.
docker run -it --rm --name n8n -p 127.0.0.1:5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n:2.47.7

# Then open http://localhost:5678 in your browser and create the owner account.

# Stop: press Ctrl+C in that window, or type this in a second window
docker stop n8n

# Start again: run Command 2 again. Your workflows are in the volume.
# Update: stop n8n first, change 2.47.7 to the newer stable version, then run Command 2 again.
```

### 2. n8n-safe-setup-checklist.md
```
# n8n safe setup checklist (facts checked 2026-11-16)

## Is it free for me?
- [ ] Only you or people in your organization create or change the workflows: free under n8n's Sustainable Use License (self-hosted).
- [ ] Not allowed: hosting n8n as a service where clients build workflows, or letting outside users build workflows through a custom UI, n8n's API, MCP or an AI agent acting for them.
- [ ] Features in .ee files (Enterprise) need a paid licence.
- [ ] n8n is fair-code, not open source, in n8n's own words.
- [ ] Docker Desktop is free for personal use, education and small businesses (under 250 employees and under 10 million dollars a year); check its terms otherwise.

## Install
- [ ] Docker Desktop installed and open.
- [ ] docker volume create n8n_data
- [ ] docker run with a fixed version tag (2.47.7 or newer stable), never latest.
- [ ] Port published as 127.0.0.1:5678:5678, so only this computer can open it (Docker's docs: a plain -p publishes to other machines too).

## First login
- [ ] Open http://localhost:5678 and create the owner account.
- [ ] Password: at least 8 characters, one number, one capital letter, kept in a password manager (no email set up means no reset link).

## Keep it safe
- [ ] Never delete the n8n_data volume. It holds the encryption key; without it, saved credentials can't be decrypted.
- [ ] Never open port 5678 to the internet. To reach n8n from outside, put a reverse proxy with SSL in front first (docs.n8n.io, Set up SSL).
- [ ] Update at least once a month: check the release notes, change the tag, run the same line again.
- [ ] Community nodes are third-party code that runs inside n8n. n8n's docs: "Be aware of the Risks when installing community nodes, or choose to disable them."

## Free extra
- [ ] Settings, Plan & usage, Unlock: a free licence key adds folders, debug in editor and custom execution data.

Sources: github.com/n8n-io/n8n (README, docker/images/n8n/README.md, LICENSE.md) ; docs.n8n.io/n8n-community-license ; docs.n8n.io/deploy/host-n8n ; docs.docker.com/subscription/desktop-license ; docs.docker.com/engine/network/port-publishing
```
