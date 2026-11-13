# Full code: Claude Code with Ollama? Free Local Coding Agents That Support It

Written for this video from Ollama's, OpenCode's and Codex's own docs and source (checked 2026-11-12). The TOML and JSONC were parsed with comments stripped; nothing was installed or run. Use your test folders, never your home folder.

### 1. setup-checklist.md
```
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
```

### 2. Install and start lines (PowerShell on Windows, Terminal on Mac)
```
# Install Ollama (ollama.com/download, checked 2026-11-12). Windows PowerShell:
irm https://ollama.com/install.ps1 | iex
# Mac Terminal:
curl -fsSL https://ollama.com/install.sh | sh
# Then open a new window. Same on Windows and Mac:
ollama --version
ollama pull gpt-oss:20b
# Set Context length to 64k in the Ollama app's Settings (slider). Then, after an agent has used the model:
ollama ps
# Linux, or Ollama without the app: start the server with a 64k context instead (Ollama docs, Context length):
#   OLLAMA_CONTEXT_LENGTH=64000 ollama serve
# OpenCode 2 (nothing to configure for Ollama on this computer):
cd opencode-test
opencode
# Inside OpenCode: /models, then pick gpt-oss:20b under Ollama.
# Codex CLI: first add oss_provider = "ollama" to config.toml (section 3). Open it with the line for your system.
# Windows PowerShell (if Notepad offers to create the file, choose Yes):
notepad "$env:USERPROFILE\.codex\config.toml"
# Mac Terminal (opens it in TextEdit):
mkdir -p ~/.codex && touch ~/.codex/config.toml && open -e ~/.codex/config.toml
# Then, in your test folder:
cd codex-test
codex --oss -m gpt-oss:20b
# Inside Codex: /status shows the permissions, /exit quits.
# One run with the model named and the provider chosen on the command line, instead:
#   codex --oss --local-provider ollama -m gpt-oss:20b
# (With oss_provider set in config.toml, --local-provider isn't needed.)
```

### 3. ~/.codex/config.toml, the line to add (Windows: %USERPROFILE%\.codex\config.toml)
```
# Make Ollama the default local provider for codex --oss (Codex docs, Advanced Configuration, checked 2026-11-12).
# Paste this line at the very top of the file, above any line in [square brackets].
# Keep the Part 3 lines below it as they are, and don't add a second copy of any of them.
oss_provider = "ollama"
# The Part 3 lines stay below it, unchanged (shown here as comments so a paste can't duplicate them):
# approval_policy = "on-request"
# sandbox_mode = "workspace-write"
# sandbox_workspace_write.network_access = false
```

### 4. opencode-remote-ollama.jsonc (only for Ollama on another machine)
```
// Only when Ollama runs on another machine (OpenCode docs: Providers, Ollama, checked 2026-11-12).
// For Ollama on this computer you need none of this: OpenCode finds it by itself.
// Merge the "providers" part into your existing ~/.config/opencode/opencode.jsonc; never paste a second { }.
// Change the address to your server's, keep /v1 at the end, and keep your Part 4 permissions as they are.
{
  "$schema": "https://opencode.ai/config.json",
  "providers": {
    "ollama": {
      "settings": {
        "baseURL": "https://ollama.example.com/v1",
        "apiKey": "{env:OLLAMA_API_KEY}"
      }
    }
  }
}
```

### 5. Saving the files
```
# config.toml: add one line to the file you made in Part 3, at the very top, then save (Ctrl+S or Command+S).
# If the file already has an oss_provider line, change it instead of adding a second one (a duplicate is an error).
# opencode.jsonc: no change for Ollama on this computer.
# setup-checklist.md is a new file, saved wherever you keep notes:
#   Windows, Notepad: paste, then File, Save as. Set the box called Save as type to All files, and name it setup-checklist.md.
#   Mac, TextEdit: Format, then Make Plain Text, then paste, then save; if TextEdit asks, choose Use .md.
#   (Shift-Command-G in a Finder window or the save box reaches hidden folders such as ~/.codex.)
```
