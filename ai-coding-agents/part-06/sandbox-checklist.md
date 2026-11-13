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
