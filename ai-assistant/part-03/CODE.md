# Full code: AI Voice Assistant: Talk to It and Hear It Answer, on Your Phone or Your Own PC

The voice-pipeline list for this video, written from each maker's own help pages, GitHub pages and docs (checked 2026-11-23). It was written from the docs, not run for this video.

### 1. voice-pipeline-list.md
```
# AI voice assistant: the voice-pipeline list (facts checked 2026-11-23)

To keep a copy: paste this into Notepad and save it as voice-pipeline-list.md with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every fact below is from the maker's own help page, GitHub page or docs on 2026-11-23. Nothing was installed or run. Treat every repo as untrusted code: check its licence, last release and reach on its GitHub page before you install it, and type each command yourself only after you've looked at it. Versions, menus and licences change: check each page first. Nothing here is legal advice.

## A. The app route (no install)
- [ ] ChatGPT (OpenAI): tap the Voice icon in the message bar (iPhone or Android), allow the microphone, choose a voice the first time, start talking. On a computer: chatgpt.com, the Voice icon in the prompt window. Voice in the desktop app is a different feature (to "start tasks, check progress, ask questions about your agents") and "has separate pricing and limits" (https://learn.chatgpt.com/docs/pricing). https://help.openai.com/en/articles/8400625-voice-chat-faq
  - "Both Advanced and Standard voice are retiring on December 11, 2026. If you have either one selected, ChatGPT will switch you to Live automatically on that date."
  - Limits (rolling 24 hours): Free "Limited access to GPT-Live-1.1 Quip. Limits may change."; Plus "3 hours with GPT-Live-1.1". Voice clips "are retained for 30 days."
- [ ] Gemini Live (Google): iPhone or Android, Gemini app, at the bottom tap Live or swipe left, start talking. "For now, Gemini Live isn't available in the Gemini web app." https://support.google.com/gemini/answer/15274899
- [ ] Claude voice mode (Anthropic): "a beta feature available to all plans". App: the sound wave symbol next to the microphone icon. Web and desktop: the sound wave symbol in the lower right corner of the chat window. "By default, we don't keep the audio from your voice conversations." Noisy room: switch to push-to-talk. https://support.claude.com/en/articles/11101966-use-voice-mode
- [ ] Alexa+ (Amazon, US): "free for Prime members", who "can start by saying, "Alexa, upgrade to Alexa+""; without Prime it was $19.99 a month when checked on 2026-11-23. https://www.aboutamazon.com/news/devices/alexa-plus-available-free-prime-members-us

## B. The build route: three checks before you install anything
- [ ] Licence: the rules for using the code.
- [ ] Last release: the newest finished version, and its date.
- [ ] Reach: what it can touch on your machine (microphone, files, network).
- [ ] You need a terminal, Python (https://www.python.org/downloads/), and for whisper.cpp, Git (https://git-scm.com/downloads) and CMake (https://cmake.org/download/).

## 1. Wake word: openWakeWord
- Licence: code Apache 2.0 (use, change and share it; keep the notice). Pre-trained models: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (non-commercial). The pre-trained phrases include "alexa", "hey mycroft", "hey jarvis" and "hey rhasspy". https://github.com/dscripka/openWakeWord
- Last release: v0.6.0, 2024-02-11 (last push 2025-12-30). English models only.
- Reach: your microphone, the whole time it runs; the network to download its models.
- [ ] Install (from the README):
    pip install openwakeword
- [ ] Try it: the README's example script, examples/detect_from_microphone.py in the repo. It prints "Listening for wakewords..." and "Wakeword Detected!" when it hears one.
- [ ] The example script imports pyaudio and numpy in its first lines, so those Python packages must be installed too.
- [ ] Models, before the example script: the README's Python example starts with a "One-time download of all pre-trained models". Type python in the same terminal, then these two lines from the README, then exit():
    import openwakeword
    openwakeword.utils.download_models()
  With no --model_path, the example script loads all of them, "hey jarvis" included, so the non-commercial licence above applies.
- [ ] Windows: the README says "On Windows, only onnxruntime is installed", and the example script defaults to --inference_framework tflite, so pass the script's own option --inference_framework onnx.
- [ ] Your own phrase: the README links a Colab notebook that trains a custom model "very quickly", in under an hour. For models with looser terms, the README asks you to raise an issue.

## 2. Hear: whisper.cpp (speech-to-text)
- Licence: MIT (use, change and share it). https://github.com/ggml-org/whisper.cpp
- Last release: v1.9.6, 2026-11-23. https://github.com/ggml-org/whisper.cpp/releases
- Reach: the sound files you give it; your microphone with whisper-stream; the network when its script downloads a model from Hugging Face (https://huggingface.co/ggerganov/whisper.cpp).
- [ ] Quick start, from the README (Mac or Linux terminal):
    git clone https://github.com/ggml-org/whisper.cpp.git
    cd whisper.cpp
    sh ./models/download-ggml-model.sh base.en
    cmake -B build
    cmake --build build -j --config Release
    ./build/bin/whisper-cli -f samples/jfk.wav
  base.en is 142 MiB (models/README.md). The sample's words appear with timestamps.
- [ ] Windows: the releases page lists ready-built Windows files on the numbered builds marked Pre-release (for example whisper-bin-x64.zip in build b5907, 2026-11-20); the v1.9.6 release itself has no files attached. You still copy the code with Git for the Windows model script, which the README shows (in its AMD section) as:
    .\models\download-ggml-model.cmd base
  base is the multilingual model (142 MiB), saved as models\ggml-base.bin; the Mac and Linux lines use base.en (ggml-base.en.bin), so on Windows use ggml-base.bin wherever a command names ggml-base.en.bin.
- [ ] Your microphone, from the README's "Real-time audio input example" (needs SDL2, linked on that page; the README calls it "a naive example"):
    cmake -B build -DWHISPER_SDL2=ON
    cmake --build build -j --config Release
    ./build/bin/whisper-stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000

## 3. Think: a model in Ollama
- Ollama: MIT; last release v0.40.17, 2026-11-10; listens on 127.0.0.1 port 11434 by default. Setup: Part 2 of this series. https://github.com/ollama/ollama

## 4. Speak: Piper (text-to-speech)
- Moved: rhasspy/piper is archived; development is at OHF-Voice/piper1-gpl (Open Home Foundation). https://github.com/OHF-Voice/piper1-gpl
- Licence: GPL-3.0 (copyleft: if you share a changed version, share its code under the same licence). The old repo was MIT. Voices carry their own terms (docs/LICENSING.md).
- Last release: v1.8.0, 2026-09-04.
- Reach: the network to download voices; the sound file it writes; your speakers when you play it.
- [ ] From the docs (docs/CLI.md), in a terminal:
    pip install piper-tts
    python3 -m piper.download_voices en_US-lessac-medium
    python3 -m piper -m en_US-lessac-medium -f test.wav -- 'This is a test.'
  This writes test.wav with the sentence "This is a test." The voice "will download to the current directory", and test.wav lands there too: open it from that folder to play it.
- [ ] Licence check: en_US-lessac-medium was trained on a corpus "whose license limits use to "research and exploration of speech technologies" and excludes commercial use" (docs/LICENSING.md). For commercial use, pick from https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/COMMERCIAL_USE.md (for example en_US-joe-medium, dataset CC0), and check the voice's MODEL_CARD.

## 5. Smart home
- [ ] Voice for lights and switches: Home Assistant has its own voice setup (https://www.home-assistant.io/voice_control/). The Home Assistant with AI series on this channel covers it once it's out.
```
