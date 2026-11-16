# Full code: Hermes Agent with Ollama: Run It Free on Local Models

A setup checklist written for this video from the Hermes Agent docs and Ollama's docs and library (checked 2026-11-15, Hermes Agent v0.23.1, Ollama v0.40.16). Defaults change between versions; check the source links before you rely on a row. Nothing was installed or run.

### 1. hermes-ollama-setup-checklist.md
```
# Hermes Agent with Ollama: setup checklist (facts checked 2026-11-15)

Every row comes from the Hermes Agent docs or Ollama's docs and library, with the source
at the bottom. Versions checked: Hermes Agent v0.23.1 (published 2026-11-10),
Ollama v0.40.16 (published 2026-11-09). Nothing here was installed or run.
Not affiliated with Nous Research, Ollama, Google, Microsoft, Apple, Intel, NVIDIA or GitHub.
Do Part 2's safe setup first (Hermes installed, approvals on manual, a test folder).

## What "free" means (the Hermes guide, as written)
- No provider bill: the model runs on your computer.
- "Your only cost is electricity — roughly $0.01–0.05 per session depending on hardware"
  (the guide's own figure).
- Cloud models are "noticeably better" at "very complex multi-step reasoning" (the guide).

## Will it fit? (Hermes guide, "What You Need" and Step 2)
- Check your memory. Windows: Settings, then System, then About (Installed RAM).
  Mac: Apple menu, then About This Mac (Memory).
| Model (guide's table) | Disk | RAM needed | Tool calling |
|---|---|---|---|
| gemma4:31b | about 20 GB | 24+ GB | Yes |
| gemma2:27b | about 16 GB | 20+ GB | No |
| gemma2:9b | about 5 GB | 8+ GB | No |
| llama3.2:3b | about 2 GB | 4+ GB | No |
- Smaller models: the guide's table marks none of its smaller models for tools.
  For other models, use the Ollama library's tools filter (ollama.com/search?c=tools)
  and check with: ollama show MODEL-NAME
- GPU: "Not required"; an NVIDIA GPU with 8+ GB VRAM "speeds things up significantly".
- CPU only (the guide's claim): a 31B model gives about 2-5 tokens per second,
  "each response takes 30–120 seconds".
- A bigger context window needs more memory too (Ollama docs).

## 1. Install Ollama
- [ ] Windows: download OllamaSetup.exe from https://ollama.com/download and run it.
      Needs Windows 10 22H2 or newer. No administrator rights needed.
      Or, in PowerShell (Ollama README):  irm https://ollama.com/install.ps1 | iex
- [ ] Mac: download Ollama.dmg from https://ollama.com/download, open it and drag Ollama
      to Applications. Needs macOS Sonoma (14) or newer. Intel Macs run on CPU only.
      Or, in Terminal (Ollama README):  curl -fsSL https://ollama.com/install.sh | sh
- [ ] Open a fresh PowerShell or Terminal window and type:  ollama --version
      You see a version number (0.40.16 when checked).
- Ollama listens on this computer at port 11434.

## 2. Pull a model that can call tools
- [ ] ollama pull gemma4:31b      (about 20 GB; give it time)
- Names ending in :cloud run on Ollama's servers and need an Ollama account. Skip them
  for a local setup.

## 3. Set the context window in Ollama (the step most guides miss)
- Hermes needs at least 64,000 tokens. "Smaller windows are rejected at startup."
- Ollama's default (Ollama docs): under 24 GiB of graphics memory, 4k; 24-48 GiB, 32k;
  48 GiB or more, 256k. So below 48 GiB, change it.
- The Hermes guide still says "By default, Ollama uses a 2048-token context". Both
  figures were read on 2026-11-15; Ollama's own page is the newer one. Either way,
  it's below 64,000.
- [ ] Ollama app (system tray icon on Windows, menu bar icon on a Mac), then Settings,
      then drag the Context length slider to 64k.
- Set it in Ollama, not in Hermes. Hermes docs: "You cannot set context length through
  the OpenAI-compatible API." model.context_length in Hermes only tells Hermes what to expect.
- Running Ollama yourself instead of the app (Linux or a server, bash):
      OLLAMA_CONTEXT_LENGTH=64000 ollama serve

## 4. Connect Hermes
- [ ] Quit Hermes if it's running. In PowerShell or Terminal:  hermes model
- [ ] Choose "Custom endpoint" (Hermes docs: "Custom endpoint (self-hosted / VLLM / etc.)";
      Ollama docs: "Custom endpoint (enter URL manually)", under "More providers...").
      Not "Local models" (Hermes' own llama.cpp engine) and not "Ollama Cloud" (hosted).
- [ ] URL:  http://127.0.0.1:11434/v1    (Hermes docs write localhost; same computer)
- [ ] API key: leave empty (local Ollama doesn't need one).
- [ ] Model: gemma4:31b
- [ ] Context length, if asked: leave blank to auto-detect (Ollama docs).
- Or the one-line route from the Ollama docs:  ollama launch hermes
  It "points Hermes at http://127.0.0.1:11434/v1". If it offers to connect a messaging
  platform, skip it (Part 2 left the gateway off).
- What hermes model saves in ~/.hermes/config.yaml (Hermes docs; don't paste over the file):

      model:
        default: gemma4:31b
        provider: custom
        base_url: http://127.0.0.1:11434/v1

## 5. Check it worked
- [ ] Start Hermes from your test folder (Part 2). The startup line shows
      "Context limit: ..." of 64000 or more, and your model.
- [ ] Ask for something small (for example, a text file with three dinner ideas).
- [ ] In a second window:  ollama ps
      The CONTEXT column says 64000 or more.
- [ ] Approvals: a local model still runs commands through Hermes.
      hermes config get approvals.mode      prints: manual
      If not:  hermes config set approvals.mode manual

## If something's off
- First reply silent for a long time: "expected behaviour, not a hang" (Hermes docs).
  Hermes waits up to 1800 seconds for local endpoints.
- To make the first reply quicker:  hermes prompt-size   then   hermes tools
  (switch off toolsets you don't use).
- "Connection refused": Ollama isn't running. Open the Ollama app.
- "Context limit: 2048 tokens" or a startup rejection: raise the slider in step 3.
- Model writes {"name": ...} as text instead of acting: the model doesn't support tools.
- Hermes inside WSL2 and Ollama on Windows: localhost points at WSL, not Windows.
  See the Hermes docs, Providers, "WSL2 Networking". (Native Windows Hermes, as in Part 2,
  doesn't need this.)

## Sources (checked 2026-11-15)
- Run Hermes Locally with Ollama: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Providers (Ollama, context, WSL2): https://hermes-agent.nousresearch.com/docs/integrations/providers
- Local Models: https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- CLI reference: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Ollama, Hermes Agent: https://docs.ollama.com/integrations/hermes
- Ollama, context length: https://docs.ollama.com/context-length
- Ollama, Windows: https://docs.ollama.com/windows
- Ollama, macOS: https://docs.ollama.com/macos
- Ollama, Cloud: https://docs.ollama.com/cloud and https://docs.ollama.com/cloud/models
- Ollama README (install lines): https://github.com/ollama/ollama
- Ollama library, gemma4: https://ollama.com/library/gemma4
- Releases: https://github.com/NousResearch/hermes-agent/releases and https://github.com/ollama/ollama/releases
```
