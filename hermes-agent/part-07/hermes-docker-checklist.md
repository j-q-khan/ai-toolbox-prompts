# Hermes Agent in Docker: checklist (facts checked 2026-11-16)

Every line comes from the Hermes Agent docs or repo (v0.23.1, published 2026-11-10)
or Docker's docs, with the source at the bottom. Nothing here was installed or run.
Not affiliated with Nous Research, Docker, Microsoft or Apple.
Part 2's safe choices still apply: Blank Slate, a throwaway key with a spend limit.

## Before you start (the main points of Docker's requirements; the full list is on the install pages)
- [ ] Windows: Windows 10 64-bit 22H2 (build 19045) or Windows 11 64-bit 23H2
      (build 22631) or higher; WSL version 2.1.5 or later; 8GB system RAM;
      hardware virtualization turned on in BIOS/UEFI; a 64-bit processor
      with SLAT; the WSL 2 feature turned on.
- [ ] Mac: the current or one of the two previous major macOS releases; at least 4 GB of RAM.
- [ ] Docker Desktop installed and running (Windows: docs.docker.com/desktop/setup/install/windows-install/
      Mac: docs.docker.com/desktop/setup/install/mac-install/).
- Docker's terms: commercial use in larger enterprises (more than 250 employees or more
  than $10 million USD in annual revenue) requires a paid subscription.
- The image is about 1 GB to download the first time (Docker Hub, v0.23.1).

## Step by step (PowerShell on Windows, Terminal on Mac; the same commands)
1. Make the folder and move into it:
     mkdir hermes-docker
     cd hermes-docker
2. Save compose.yaml in that folder (Notepad: Save as type, All files.
   TextEdit: Format, Make Plain Text).
3. Run setup once:
     docker compose run --rm hermes setup
   The setup wizard opens. Pick Blank Slate and a throwaway key with a spend limit.
   It writes your keys to hermes-data/.env (the docs: "write them to ~/.hermes/.env",
   which is /opt/data inside the container).
4. Start it:
     docker compose up -d
5. Check it:
     docker compose ps
   You should see hermes-docker-hermes-1 with STATUS Up.
6. Chat:
     docker compose exec hermes hermes
7. Stop it:  docker compose down     Logs:  docker compose logs -f

## If something goes wrong (Hermes docs, Troubleshooting)
- Container exits immediately: "Missing or invalid .env file — run interactively first
  to complete setup" (step 3).
- Permission denied on Linux: set HERMES_UID and HERMES_GID to the owner of hermes-data
  (see the comment in compose.yaml).
- Don't point two Hermes gateways at the same data folder: "Never run two Hermes gateway
  containers against the same data directory simultaneously."

## What our file does, and why
- image nousresearch/hermes-agent:v0.23.1: the official image, pinned. On 2026-11-16,
  latest and stable point to the same image as v0.23.1.
- ./hermes-data:/opt/data: the container's only folder from your computer. It holds .env
  (keys), config.yaml, memories, skills, sessions and logs.
  A fresh folder, not your Part 2 ~/.hermes: an existing database on a Docker Desktop
  mount "logs a one-time error" and needs a manual fix (docs, Filesystem requirements).
- command gateway run: the always-on part that answers chat apps you add in setup.
- restart: unless-stopped: comes back after a crash.
- No ports: the gateway's port 8642 is "optional if you only use chat platforms".
- The image sets HERMES_WRITE_SAFE_ROOT=/opt/data, so Hermes' file tools save only there.

## The repo's own compose files (tag v0.23.1)
- docker-compose.yml: gateway with build: . (builds from source, so you clone the repo),
  restart: unless-stopped, network_mode: host, ~/.hermes:/opt/data; a dashboard service
  on 127.0.0.1. Usage line: HERMES_UID=$(id -u) HERMES_GID=$(id -g) docker compose up -d
  Host networking: the container's network "isn't isolated from the Docker host" (Docker docs).
  On Docker Desktop it's an opt-in setting from version 4.34 (sign in to your Docker account,
  then Settings, Resources, Network, Enable host networking, Apply and restart).
- docker-compose.windows.yml: image nousresearch/hermes-agent:latest, no host networking
  (its note: "not supported on Docker Desktop for Windows"), ${USERPROFILE}/.hermes:/opt/data.
  Its dashboard runs --host 0.0.0.0 --insecure. Hermes docs: "--insecure is a no-op";
  a non-loopback bind needs an auth provider, or the dashboard fails at startup.

## The docker terminal backend (Hermes installed normally, like Part 2)
- Switch:  hermes config set terminal.backend docker      Back:  hermes config set terminal.backend local
- Commands then run in a sandbox container: "all capabilities dropped, no privilege
  escalation, PID limits". Needs Docker Desktop running.
- Hermes docs, backend table: dangerous command check "❌ Skipped (container is boundary)".
  So approvals set to manual won't prompt for commands in there.
- Hermes source, v0.23.1: once a folder from your computer is mounted into the sandbox
  (terminal.docker_volumes with a host path, or terminal.docker_mount_cwd_to_workspace: true),
  the normal check runs again. Your own approvals.deny rules apply either way.
- Cut the sandbox off from the network:  hermes config set terminal.docker_network false

## What a container does and doesn't stop
- Keeps Hermes away from your other files, apps and settings.
- The folder you mount: Docker docs, "Bind mounts have write access to files on the host
  by default". Mount a folder made for Hermes, never your home folder. Add :ro to a mount
  to make it unwritable from the container.
- The network: on by default; host networking shares your computer's network.
- Keys: any key in hermes-data/.env, or passed in with -e, is one the agent can use.
  Use a throwaway key with a spend limit.
- Never add the Docker socket (/var/run/docker.sock) to the container.

## Upgrading (Hermes docs)
- Change the tag in compose.yaml to the new version, then:
     docker compose pull
     docker compose up -d
  "Hermes writes timestamped backups next to config.yaml and .env first."

## Sources (checked 2026-11-16)
- Hermes Docker Setup: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Configuration, Docker Backend: https://hermes-agent.nousresearch.com/docs/user-guide/configuration#docker-backend
- Security (backend table, HERMES_WRITE_SAFE_ROOT): https://hermes-agent.nousresearch.com/docs/user-guide/security
- Web Dashboard (--insecure): https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard
- Repo compose files: https://github.com/NousResearch/hermes-agent/blob/v0.23.1/docker-compose.yml
  and https://github.com/NousResearch/hermes-agent/blob/v0.23.1/docker-compose.windows.yml
- Source: tools/approval.py and tools/terminal_tool.py at https://github.com/NousResearch/hermes-agent (tag v0.23.1)
- Image tags: https://hub.docker.com/r/nousresearch/hermes-agent/tags
- Docker host networking: https://docs.docker.com/engine/network/drivers/host/
- Docker bind mounts: https://docs.docker.com/engine/storage/bind-mounts/
- Docker Desktop requirements: https://docs.docker.com/desktop/setup/install/windows-install/
  and https://docs.docker.com/desktop/setup/install/mac-install/
- Releases: https://github.com/NousResearch/hermes-agent/releases
