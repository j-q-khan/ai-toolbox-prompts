# Full code: Jarvis AI Assistant on Your PC: Build Your Own With Open-Source Tools

The setup checklist for this video, written from each maker's own GitHub page and docs (checked 2026-11-23). It was written from the docs, not run for this video.

### 1. jarvis-pc-setup-checklist.md
```
# Jarvis-style assistant on your own PC: the setup checklist (facts checked 2026-11-23)

To keep a copy: paste this into Notepad and save it as jarvis-pc-setup-checklist.md with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from the maker's own GitHub page or docs on 2026-11-23. Nothing was installed or run. Treat every repo as untrusted code: check the three things below on its GitHub page before you install it, and type each command yourself only after you've looked at it. Versions and menus change: check each page first.

## 0. Three checks before you install anything
- [ ] Licence: the rules for using the code.
- [ ] Last release: the newest finished version, and its date.
- [ ] Reach: what it can touch on your machine (files, microphone, network, a terminal).

## 1. Ollama (runs the model)
- Licence: MIT (use, change and share it).
- Last release: v0.40.17, 2026-11-10. https://github.com/ollama/ollama/releases
- Reach: listens on 127.0.0.1 port 11434 by default (this computer only). Cloud models and web search when you sign in (see step 6 to switch them off). The Windows and Mac apps download updates automatically (Ollama's FAQ).
- [ ] Install: download the installer for Windows or Mac from https://ollama.com/download (Linux: the one-line command below).
- [ ] Or the one-line command from https://github.com/ollama/ollama (the Linux route), after opening the script in your browser and looking through it:
    Windows (PowerShell):  irm https://ollama.com/install.ps1 | iex
    macOS or Linux:        curl -fsSL https://ollama.com/install.sh | sh
- [ ] First model, from Ollama's GitHub page (PowerShell on Windows, Terminal on a Mac):
    ollama run gemma4
  Ollama's library page listed gemma4 at 6.6GB - 9.5GB on 2026-11-23: https://ollama.com/library/gemma4

## 2. Open WebUI (chat window in your browser, needs Docker)
- Licence: the Open WebUI License. Clause 4: licensees are "strictly prohibited from altering, removing, obscuring, or replacing any "Open WebUI" branding", except (i) deployments with no more than fifty (50) end users within any rolling thirty (30) day period, (ii) with specific prior written permission from the copyright holder, or (iii) with a duly executed enterprise license. https://github.com/open-webui/open-webui/blob/main/LICENSE
- Its own licence page: "Open WebUI v0.6.6+ is not an OSI-approved "open source" license." All of its source code is public. https://docs.openwebui.com/license/
- Last release: v0.13.4, 2026-11-17. https://github.com/open-webui/open-webui/releases
- Reach: a page at http://localhost:3000, which with this command other devices on your network can reach too (Docker's docs: "Publishing container ports is insecure by default", https://docs.docker.com/engine/network/port-publishing/), so create the admin account straight away; the network for extra model downloads, and for web search when you turn it on; your microphone when you click voice input; a terminal only with the add-on Open Terminal. With --restart always it comes back after every reboot.
- [ ] Docker installed and running: https://docs.docker.com/get-docker/
- [ ] The command from https://github.com/open-webui/open-webui (one line):
    docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
- [ ] Open http://localhost:3000 and choose Create Admin Account (the first account is the administrator; "Everything, including this login, stays in your own volume").
- [ ] Ollama on this machine is picked up at http://host.docker.internal:11434 . Click New Chat, pick a model in the selector inside the message box, type, press Enter.

## 3. Open WebUI shows no models: the fix, and its risk
- [ ] Open WebUI's troubleshooting page: set OLLAMA_HOST=0.0.0.0 so Ollama listens on all network interfaces, then restart Ollama. Windows (Ollama's FAQ, https://docs.ollama.com/faq): quit Ollama from the taskbar, search Settings for environment variables, click Edit environment variables for your account, add OLLAMA_HOST with the value 0.0.0.0, click OK, then start Ollama again from the Start menu. Mac (Terminal), then restart the Ollama app:
    launchctl setenv OLLAMA_HOST "0.0.0.0:11434"
  https://docs.openwebui.com/troubleshooting/connection-error
- [ ] Warning, same page: "Ollama's local API does not require authentication", so "any device that can reach the host on port 11434 can use it". Block port 11434 in your firewall for every other device.
- [ ] Check (Windows):
    netstat -an | findstr 11434
  127.0.0.1:11434 means this computer only; 0.0.0.0:11434 means every connection.

## 4. Jan (desktop chat app, no Docker)
- Licence: Apache 2.0 (use, change and share it; keep the licence notice). https://github.com/janhq/jan
- Last release: v0.8.8, 2026-10-28. https://github.com/janhq/jan/releases
- Reach: the network for web search ("Web Search is on by default"); add-on tools you connect ask for approval on each call (unless you turn on Allow All MCP Tool Permissions); cloud providers only if you add their key.
- [ ] Download: https://jan.ai/download . On first launch Jan downloads its own default model ("Sit tight, Jan is getting ready"), so it can run a model without Ollama.
- [ ] The Hub (left sidebar) shows whether each model fits your hardware.
- [ ] To use Ollama's models: Settings, then Model Providers, then Add Provider. API format: OpenAI-compatible. Provider name: any. Base URL: http://localhost:11434/v1 . API key: any placeholder, such as sk-no-key. Then Create. https://jan.ai/docs/desktop/remote-models/custom-endpoint
- [ ] Leave off /v1 and the request fails with a 404 (Jan's docs: "A common mistake").

## 5. A ready-made "Jarvis" repo from GitHub
- [ ] isair/jarvis (a community repo): "free for personal use", commercial users contact the author; last release v2.9.0, 2026-11-12; it listens continuously and keeps "a short, temporary rolling transcript of nearby speech"; file browsing and edits stay inside your home directory; web search, weather and connected tools use the network. https://github.com/isair/jarvis

## 6. Keep Ollama local only (switch off its cloud features)
- [ ] From Ollama's FAQ: in your user folder's .ollama folder, put these lines in server.json (save from Notepad with Save as type set to All files):
    {
      "disable_ollama_cloud": true
    }
- [ ] Or set the environment variable OLLAMA_NO_CLOUD=1 instead (on Windows, in the same Edit environment variables for your account window as in step 3).
- [ ] Restart Ollama. Its logs then show: Ollama cloud disabled: true . https://docs.ollama.com/faq
```
