# Full code: Local LLM for Beginners: Run AI on Your Own PC or Mac with LM Studio

A checklist and a test script written for this video from LM Studio's own docs (checked 2026-11-16). Nothing was installed or run; the output shown is an example. ask_local.py talks only to LM Studio's server on your own computer (localhost, port 1234) and needs no key. Test only.

### 1. local-llm-checklist.md
```
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
```

### 2. ask_local.py
```
# ask_local.py: send one chat message to LM Studio's local server and print the reply.
# Test only. Written from LM Studio's docs (checked 2026-11-16), not run.
# Before running: open LM Studio, load a model, then start the server
# (Developer tab, Start server, or: lms server start --port 1234).
# Run: python ask_local.py            (on a Mac: python3 ask_local.py)
#      uses the first chat model the server lists (it may list downloaded models
#      that LM Studio loads on first use, which can take a while)
# Or:  python ask_local.py model-id   (a model id from: lms ps)
import json
import sys
import urllib.request

BASE = "http://localhost:1234/v1"
QUESTION = "In two sentences, what is a local LLM?"


def call(path, payload=None, timeout=10):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        BASE + path, data=data, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def main():
    try:
        models = call("/models").get("data", [])
    except (OSError, ValueError):
        sys.exit("No LM Studio server on localhost:1234. Start it in the Developer tab, "
                 "or run: lms server start --port 1234")
    chat_models = [m["id"] for m in models if "embed" not in m["id"].lower()]
    if len(sys.argv) > 1:
        model = sys.argv[1]
    elif chat_models:
        model = chat_models[0]
    else:
        sys.exit("The server lists no chat models. Load one in LM Studio first.")
    try:
        reply = call(
            "/chat/completions",
            {"model": model, "messages": [{"role": "user", "content": QUESTION}]},
            timeout=300,
        )
        text = reply["choices"][0]["message"]["content"]
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        sys.exit(f"The chat call failed ({error!r}). Pass a model id from lms ps: "
                 "python ask_local.py model-id (python3 on a Mac)")
    print("Model:", model)
    print(text)


if __name__ == "__main__":
    main()
```

### 3. example-output.txt
```
Example output (not run; your model id and wording will differ):
Model: your-model-id
A local LLM is a language model that runs on your own computer
instead of a company's servers. Once it is downloaded, you can chat with it offline.
```
