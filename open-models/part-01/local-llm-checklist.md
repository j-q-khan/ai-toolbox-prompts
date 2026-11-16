# Run a local LLM with LM Studio: checklist (facts checked 2026-11-16)

## 1. Can your computer run it?
- [ ] Mac: Apple Silicon (M1 to M4) and macOS 14 or newer. Intel Macs are not supported. 16GB of memory recommended; 8GB may work with smaller models.
- [ ] Windows: an x64 PC with AVX2, or an ARM laptop (Snapdragon X Elite). 16GB of memory recommended; 4GB of graphics memory (VRAM) recommended.
- [ ] Find your memory: Mac, Apple menu, About This Mac. Windows, Ctrl+Shift+Esc, Task Manager, Performance.

## 2. Install the right thing
- [ ] Go to lmstudio.ai/download.
- [ ] Skip the first button, Download Bionic (LM Studio's agent app).
- [ ] Click Download LM Studio for Windows or for macOS (0.4.28 when checked).
- [ ] Skip the two install commands under Install llmster: they install a server version with no window.
- [ ] Run the installer (Windows) or open the downloaded file and install the app (Mac), then open LM Studio.

## 3. First model, first chat
- [ ] Discover tab (Ctrl+2 on Windows, Cmd+2 on a Mac): pick one of the smaller curated models. LM Studio's docs: choose a 4-bit download option or higher if your machine can run it (Part 2 explains). This step needs the internet.
- [ ] Chat tab: open the model loader (the bar that says Select a model to load) and pick your model.
- [ ] Type a message. Nothing comes back? Check the model is loaded.
- [ ] Wi-Fi off: chatting with a downloaded model still works.

## 4. Know the terms
- [ ] LM Studio app: free, under its App Terms ("personal and / or internal business purposes"), not open source. Free for use at work (LM Studio blog, 2025).
- [ ] lms (command line) and the SDKs: MIT.
- [ ] Ollama: open source, MIT; command line plus a desktop app; runs on Intel Macs on the processor only.

Sources: lmstudio.ai/download ; lmstudio.ai/docs/app/system-requirements ; lmstudio.ai/docs/app/basics ; lmstudio.ai/docs/app/offline ; lmstudio.ai/app-terms ; docs.ollama.com/macos
