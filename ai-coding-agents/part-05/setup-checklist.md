# Local coding agents with Ollama: setup checklist (facts checked 2026-11-12)
# Ollama 0.40.16, OpenCode 2.2.7, Codex CLI 0.167.2

## 1. Claude Code and Ollama: both sides
- [ ] Ollama's docs give a route: ollama launch claude, or ANTHROPIC_BASE_URL=http://localhost:11434 (docs.ollama.com/integrations/claude-code).
- [ ] Anthropic's docs: it "doesn't support routing Claude Code to non-Claude models through any gateway" (code.claude.com/docs/en/llm-gateway).
- [ ] This checklist uses the two agents with official local support: OpenCode 2 and Codex CLI.

## 2. Before you start
- [ ] OpenCode 2 or Codex CLI installed, with the ask-first settings from Part 4 (OpenCode) or Part 3 (Codex).
- [ ] Windows 10 22H2 or newer, or macOS Sonoma (14) or newer.
- [ ] About 14 GB free for gpt-oss:20b, plus room for Ollama itself.
- [ ] Ollama's download page: "Speed depends on the hardware. Large models are slow on a computer without a strong GPU."
- [ ] A model name ending in :cloud or -cloud (gemma4:cloud, gpt-oss:20b-cloud) runs on Ollama's servers, not your computer. To stay local, turn off the Cloud switch in Ollama's Settings ("Enable cloud models and web search").

## 3. Install Ollama and a model
- [ ] Windows PowerShell: irm https://ollama.com/install.ps1 | iex
- [ ] Mac Terminal: curl -fsSL https://ollama.com/install.sh | sh
- [ ] The Ollama app then runs in the background (Windows: system tray; Mac: menu bar).
- [ ] New window: ollama --version (0.40.16 when checked).
- [ ] ollama pull gpt-oss:20b (14 GB, tools, 128K context window).

## 4. Set the context to 64k (the step most guides skip)
- [ ] Ollama's default context is 4k on computers with under 24 GiB of graphics memory (VRAM).
- [ ] Ollama's docs: agents and coding tools should be set to at least 64000 tokens.
- [ ] Click the Ollama icon (Windows: system tray; Mac: menu bar), choose Settings, then Context length: drag the slider to 64k. A bigger context needs more memory.
- [ ] After an agent has used the model: ollama ps. CONTEXT should be 64k (65536) or more; PROCESSOR 100% GPU is the fast case, a CPU/GPU split is slower.

## 5. OpenCode 2
- [ ] Nothing to configure for Ollama on the same computer: OpenCode finds it at 127.0.0.1:11434.
- [ ] Keep ~/.config/opencode/opencode.jsonc from Part 4 as it is (edits, commands, outside folders and helper agents ask).
- [ ] cd opencode-test, then opencode, then /models, and pick gpt-oss:20b under Ollama.
- [ ] First task: make a page called index.html with a button that counts clicks, then tell me what you did. Expect "Permission required": pick Allow once.
- [ ] Ollama on another machine only: add the providers block from opencode-remote-ollama.jsonc to your opencode.jsonc.

## 6. Codex CLI
- [ ] Needs Ollama 0.13.4 or newer.
- [ ] Open ~/.codex/config.toml with the line in install-lines.txt, and add oss_provider = "ollama" at the very top, above any [section] line.
- [ ] Keep approval_policy = "on-request" and sandbox_mode = "workspace-write" from Part 3.
- [ ] cd codex-test, then codex --oss -m gpt-oss:20b (the model named, as in Ollama's Codex docs).
- [ ] /status: Permissions should still say Workspace, Ask for approval.

## 7. Re-check before you rely on it
- [ ] Versions, model names and sizes, context defaults and menu names change. Check the links in SOURCES.md.
