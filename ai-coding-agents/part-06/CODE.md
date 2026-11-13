# Full code: Run Claude Code, Codex and OpenCode in a Docker Sandbox

Written for this video from Docker's, Anthropic's, OpenAI's and OpenCode's own docs (checked 2026-11-12). The YAML and JSONC were parsed with a parser; nothing was built, installed or run. Use a test folder, never your home folder, and a throwaway key with a spend limit.

### 1. sandbox-checklist.md
```
# Coding agents in a Docker sandbox: checklist (facts checked 2026-11-12)
# sbx v0.53.0; OpenCode 2.2.7 image; Claude Code and Codex as Docker's sbx starts them

## 1. What Docker's sandbox (sbx) stops, in Docker's words
- [ ] Each sandbox is a microVM with its own Linux kernel, its own Docker Engine and its own network.
- [ ] It can't reach your other folders or your computer's own Docker daemon.
- [ ] The key stays on your computer: "The raw credential values never enter the VM." A proxy adds it to requests.
- [ ] Network: blocked by default unless a rule allows it. Choose the Balanced preset, not Open.

## 2. What it doesn't stop
- [ ] The shared folder is writable: the agent "can read, write, and delete any file within that directory, including hidden files, configuration files, build scripts, and Git hooks."
- [ ] The agent can't see the key, but requests it makes are billed to it: use a throwaway key with a spend limit.
- [ ] Allowed network traffic goes through. Docker: "The default allowed domains include broad wildcards." Check with sbx policy ls.
- [ ] Treat the agent's changes "the same way you would treat a pull request from an untrusted contributor."

## 3. Before you start
- [ ] sbx: Windows 11 (64-bit Intel or AMD, Windows Hypervisor Platform) or a Mac with Apple silicon on macOS Sonoma 14 or newer. No Docker Desktop needed. A free Docker account.
- [ ] Do-it-yourself route: Docker Desktop.
- [ ] git installed. A test folder, never your home folder.
- [ ] First commit before any agent starts: git init, git add -A, git commit --allow-empty -m "before the agent".

## 4. sbx: approvals are off by default
- [ ] Claude Code starts as: claude --dangerously-skip-permissions
- [ ] Codex starts as: codex --dangerously-bypass-approvals-and-sandbox
- [ ] OpenCode starts with no implicit flags, so its own defaults apply (allow-all for its build agent).
- [ ] Docker: "The sandbox itself is the safety boundary." Prompts back: change the mode inside the session (Claude Code: /permissions; Codex has /permissions too).
- [ ] Home-folder settings stay behind: ~/.claude, ~/.codex, ~/.config/opencode. Settings inside the test folder come in.
- [ ] Claude Code: a .claude/settings.json in the test folder still applies. "Deny rules block in every mode, including bypassPermissions", and explicit ask rules still ask (Claude Skills Part 5 has the file). Commit it first: the agent can change it.
- [ ] Docker's OpenCode template installs the npm package opencode-ai, OpenCode's V1 line (checked 2026-11-12). For OpenCode 2, use the do-it-yourself files.
- [ ] Gemini CLI and Antigravity CLI aren't on Docker Sandboxes' agent list.

## 5. Afterwards, on your own computer
- [ ] Before git status, look at .git/config as plain text (sbx-lines.txt). A core.fsmonitor or core.hooksPath line you didn't add can make git run a program, and fsmonitor runs on git status itself: delete that line first.
- [ ] git status, then git diff.
- [ ] Hooks don't show in git diff: list .git/hooks (sbx-lines.txt). A fresh repo has only .sample files; delete anything else you didn't add before your next commit.
- [ ] Undo: git restore . puts changed files back; git clean -nd previews, git clean -fd removes new files.
- [ ] In direct mode the agent can also change .git itself, history included; clone mode keeps your repo and its history out of reach.
- [ ] Stronger option: clone mode (sbx run --clone claude .). Your repo comes in read-only and the agent works on its own copy.
- [ ] sbx stop pauses a sandbox; sbx rm deletes it and everything installed inside. Your folder's files stay.

## 6. Do-it-yourself: OpenCode 2 in a container
- [ ] One folder, opencode-sandbox, holding Dockerfile, docker-compose.yml and your test folder sandbox-test.
- [ ] Copy opencode.jsonc (Part 4's ask-first file) into sandbox-test so OpenCode asks first in the container.
- [ ] docker compose run --rm opencode, then /connect inside OpenCode with your throwaway key.
- [ ] What it gives up next to sbx: the key sits inside the container, the network is open, the kernel is shared.
- [ ] Never mount /var/run/docker.sock. Docker: it "would give the agent full access to your environment."
- [ ] Done: docker compose down --volumes wipes the key and history.
- [ ] For Claude Code instead: Anthropic's reference dev container with init-firewall.sh (code.claude.com/docs/en/devcontainer).

## 7. Re-check before you rely on it
- [ ] Versions, startup lines, presets and requirements change. Check the links in SOURCES.md.
```

### 2. sbx-lines.txt (PowerShell on Windows, Terminal on Mac)
```
# Docker Sandboxes (sbx), from docs.docker.com/ai/sandboxes (checked 2026-11-12, sbx v0.53.0).
# Windows 11, once: open PowerShell as administrator (right-click PowerShell, Run as administrator):
Enable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -All
# Restart if Windows asks. Then, in a normal PowerShell window (installs for your user only):
winget install -h Docker.sbx
# Mac with Apple silicon, Terminal:
brew trust docker/tap
brew install docker/tap/sbx
# Then, on both. Sign in with a Docker account (a browser opens):
sbx login
# Store your throwaway key; it asks for the value. Claude Code:
sbx secret set anthropic
# Codex:
sbx secret set openai
# A test folder and a first commit, before any agent starts:
mkdir sandbox-test
cd sandbox-test
git init
git add -A
git commit --allow-empty -m "before the agent"
# Start an agent in this folder. The first time, choose the Balanced network preset when asked.
sbx run claude
#   or
sbx run codex
# In a second window: your sandboxes, their agents and the folder each one shares.
sbx ls
# The network rules in effect:
sbx policy ls
# Inside Claude Code, to get approval prompts back: /permissions
# Afterwards, in sandbox-test on your own computer. First, git's own settings file, as plain text:
# a core.fsmonitor or core.hooksPath line you didn't add can make git run a program, so delete it before git status.
# Windows PowerShell:
Get-Content .git\config
# Mac Terminal:
cat .git/config
# Then:
git status
git diff
# Git hooks don't show in git diff. Windows PowerShell:
Get-ChildItem -Force .git\hooks
# Mac Terminal:
ls -la .git/hooks
# A fresh repo has only files ending in .sample there; delete anything else you didn't add.
# Undo the agent's changes: put changed files back, preview new files, then remove them.
git restore .
git clean -nd
git clean -fd
# Clone mode instead: your repo comes in read-only, the agent works on its own copy.
sbx run --clone claude .
# Stop or delete a sandbox, by the name sbx ls shows (my-sandbox here):
sbx stop my-sandbox
sbx rm my-sandbox
# Linux (Ubuntu 24.04 or newer, KVM turned on): see docs.docker.com/ai/sandboxes/install for the apt route.
```

### 3. Dockerfile
```
# OpenCode 2 in a do-it-yourself Docker sandbox (The AI Toolbox, AI Coding Agents Part 6, checked 2026-11-12).
# OpenCode's own official image at one exact version, plus git and a normal user. Test folders only.
FROM ghcr.io/anomalyco/opencode:2.2.7

# git, so OpenCode can see the folder's history. Your undo button is git on your own computer.
RUN apk add --no-cache git

# A normal user, with no sudo and no root password.
RUN addgroup -g 1000 agent && adduser -D -u 1000 -G agent agent

USER agent
WORKDIR /workspace
# The image's own ENTRYPOINT ["opencode"] stays as it is.
```

### 4. docker-compose.yml
```
# OpenCode 2 in a do-it-yourself Docker sandbox (The AI Toolbox, AI Coding Agents Part 6, checked 2026-11-12).
# Folder layout: opencode-sandbox/Dockerfile, opencode-sandbox/docker-compose.yml, opencode-sandbox/sandbox-test/
# Start it from opencode-sandbox with:  docker compose run --rm opencode
# Inside OpenCode: /connect, pick your provider, paste a throwaway key with a spend limit.
# Wipe it afterwards, key and history included, with:  docker compose down --volumes
services:
  opencode:
    build: .
    image: ai-sandbox/opencode:2.2.7
    pull_policy: build                 # always build from the Dockerfile here; never pull this name from a registry
    volumes:
      - ./sandbox-test:/workspace      # the ONLY folder on your computer the agent can see, and it can change all of it
      - agent-home:/home/agent         # OpenCode's settings, history and the key you add with /connect live here
    working_dir: /workspace
    cap_drop: [ALL]                    # no extra kernel powers
    security_opt:
      - no-new-privileges:true         # nothing inside can gain root
    mem_limit: 4g
    cpus: 2
    pids_limit: 256                    # a runaway loop can't fork-bomb the machine
    stdin_open: true
    tty: true
    # Deliberately absent: privileged, network_mode: host, and any mount of /var/run/docker.sock.
    # The Docker socket is your computer's own Docker; an agent that can reach it can reach everything.
    # Not here, unlike Docker's sbx: network rules. The network is open, so whatever the agent fetches or sends goes through.
    # Not here either: read_only: true, because OpenCode in this image hasn't been tested with a read-only system folder.

volumes:
  agent-home:
```

### 5. sandbox-test/opencode.jsonc (Part 4's ask-first file, copied into the test folder)
```
// Make OpenCode 2 ask first (OpenCode docs: Permissions and Agents, checked 2026-11-12).
// Saved inside the test folder, it counts as that folder's own settings (OpenCode docs: Config, Locations),
// so it applies inside the container too. Every agent asks before shell commands, folders outside this one,
// and starting a helper (subagent). The build agent also asks before editing files. Last matching rule wins.
{
  "$schema": "https://opencode.ai/config.json",
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" },
    { "action": "external_directory", "resource": "*", "effect": "ask" },
    { "action": "subagent", "resource": "*", "effect": "ask" }
  ],
  "agents": {
    "build": {
      "permissions": [
        { "action": "edit", "resource": "*", "effect": "ask" }
      ]
    }
  }
}
```

### 6. Saving the files
```
# Make one folder called opencode-sandbox, and put your test folder sandbox-test inside it.
# Save section 3 as opencode-sandbox/Dockerfile (no extension) and section 4 as opencode-sandbox/docker-compose.yml.
# Save section 5 as opencode-sandbox/sandbox-test/opencode.jsonc, then commit it in sandbox-test.
#   Windows, Notepad: paste, then File, Save as. Set the box called Save as type to All files,
#   and type the name exactly, so Notepad doesn't add .txt.
#   Mac, TextEdit: Format, then Make Plain Text, then paste, then save with the exact name.
#   If TextEdit offers to add .txt, choose Don't Append (or Use .yml / .jsonc).
# Claude Code in sbx: Claude Skills Part 5's settings.json goes in a hidden folder, sandbox-test/.claude/settings.json.
#   Make the folder first. PowerShell:  New-Item -ItemType Directory sandbox-test\.claude   Terminal:  mkdir -p sandbox-test/.claude
#   Mac, in TextEdit's Save box: press Shift-Command-G and type the folder's path, such as ~/sandbox-test/.claude
#   Windows, in Notepad's Save as box: type the full name, sandbox-test\.claude\settings.json, with Save as type set to All files.
#   Then commit it in sandbox-test before the agent starts.
# sandbox-checklist.md and sbx-lines.txt are notes: save them wherever you keep notes, the same way.
# Check the names in PowerShell with:  Get-ChildItem opencode-sandbox
# or in Terminal with:  ls opencode-sandbox
```
