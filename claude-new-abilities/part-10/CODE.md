# Full code: Claude Voice Mode: Make Claude Code Talk Back, Free and Local

A checklist and commands written for this video from the repo's files at tag v9.0.2 (read as text), its release and issue pages, PyPI, Anthropic's Claude Code docs, uv's docs and Microsoft's WSL docs, checked 2026-11-15. Not run by us: try it in a test folder first.

### 1. claude-voice-mode-checklist.md
```
# Claude voice mode with VoiceMode: checklist (checked 2026-11-15)

## Built in first
- Claude Code's /voice is dictation only: your speech goes to Anthropic's
  servers to become text, it needs a Claude.ai sign-in, and Claude answers
  in text.
- The Claude app's voice mode talks back (phone, desktop, web; every plan,
  beta), but not in Claude Code.

## Before you install
- Repo: github.com/mbailey/voicemode. Not from Anthropic.
- Licence: MIT
- Latest release: 9.0.2, 2026-10-29 (PyPI voice-mode and
  voice-mode-install 9.0.2)
- Real use: about 1,460 stars, 199 forks; issues 106 closed, 44 open;
  7 closed issues sampled: its team replied on 5
- Reaches: your microphone (while it waits for your reply) and speakers.
  Audio is saved only if you set VOICEMODE_SAVE_AUDIO=true. A text log of
  what you both say always goes to ~/.voicemode/logs/conversations (local).
  No setting turns it off in 9.0.2; clear it with:
  rm -rf ~/.voicemode/logs/conversations
  Event logs go to ~/.voicemode/logs/events (local); to switch them off,
  add -e VOICEMODE_EVENT_LOG_ENABLED=false to the add line (section 3).
- Telemetry: none found in the 9.0.2 code.
- Costs: free locally. OpenAI only if OPENAI_API_KEY is set (and the
  add line below takes OpenAI off the list anyway): speech to text was
  $0.006 per 60 seconds and voice $15 per 1M characters when checked
  (2026-11-15, developers.openai.com/api/docs/pricing); whisper-1 and
  tts-1 are deprecated, shutdown 2027-02-26 and 2027-01-06
  (developers.openai.com/api/docs/deprecations).
- Installs: Homebrew (Mac, only if missing), portaudio, ffmpeg, git, cmake,
  whisper.cpp built from source, a Kokoro-FastAPI server, their models
  (about 0.5 GB by the guides; the installer warns 2-4 GB), and services
  that start at login. The voices themselves aren't fixed to a version;
  VoiceMode is.
- Windows: the installer stops on native Windows ("Unsupported operating
  system"), so use WSL (below). Not tested by us.

## Mac (Terminal)
0. No Homebrew? Install it from brew.sh first: it asks for your Mac
   password and to press Return, and may show a dialog offering the
   command line developer tools (Install). Then run the two lines it
   prints under "Next steps" and open a new window (the installer only
   finds brew on your PATH).
1. Install uv, then open a NEW Terminal window.
2. Run the installer (section 2). Answer its questions (at most two
   once Homebrew is in place):
   Install Homebrew now? (only if Homebrew is still missing): y
   Install missing dependencies?: y
   Install local voice services now?: y
   Type your Mac password if asked.
   (Already have VoiceMode? It may ask to upgrade or reinstall: say no to
   keep 9.0.2.)
3. mkdir ~/voice-test && cd ~/voice-test
4. Run the add line (section 3). It writes voice-test/.mcp.json. Open it:
   voice-mode==9.0.2 and both 127.0.0.1 addresses, no key.
5. claude --permission-mode manual   (status bar: manual mode on)
   Trust the folder: Yes. The new server in .mcp.json: use this server.
6. Type: Use VoiceMode to talk with me.
   Approve the converse tool: Yes. (It asks each time it speaks; "don't
   ask again" covers only that tool in this folder.)
7. "Terminal" would like to access the microphone: Allow.
8. Wait for the chime, talk, stop: Claude answers out loud.

## If the installer never asked about local voices
- On smaller machines (under 8 GB of memory or 4 cores; WSL gets about
  half your PC's memory) it prints "Cloud services recommended" and skips
  them, and Claude then reports "All TTS providers failed". Install them:
  voicemode service install whisper
  voicemode service install kokoro

## Windows (through WSL; not tested by us)
1. In the Start menu, right-click PowerShell, Run as administrator (Windows asks: Yes):
   wsl --install, then restart.
2. Open Ubuntu from the Start menu; set its user name and password (the
   password stays hidden as you type).
3. Install Claude Code inside Ubuntu (Anthropic's setup docs) and sign in.
4. Windows Settings › Privacy & security › Microphone: microphone access
   on, and Let desktop apps access your microphone on.
5. Inside Ubuntu, follow the Mac steps 1 to 8 (the installer uses apt and
   asks for your Ubuntu password; there's no Homebrew question, and no
   step 7 prompt: the Windows switch in step 4 covers the microphone).
6. Voices not starting? Run: systemctl --user status voicemode-whisper
   (they need systemd, on by default in new Ubuntu installs on WSL).
   WSL audio has open bug reports (#341: replies cut off at about 19 s).

## The common mistake
- Don't Allow on the microphone question: Claude speaks but never hears.
  /exit, System Settings › Privacy & Security › Microphone › Terminal on,
  quit Terminal with Command-Q, open it again, cd ~/voice-test,
  claude --permission-mode manual.

## While you talk (bonus)
- Say "say that again" to hear the last reply again.
- Say "wait" to pause for 60 seconds.

## Switch it off (section 4)
- In Claude Code: /exit
- In voice-test: claude mcp remove --scope project voicemode
- voicemode whisper service uninstall --remove-models   (Are you sure? y)
- voicemode kokoro uninstall --remove-models            (Are you sure? y)
- uv tool uninstall voice-mode
- Delete ~/.voicemode (the text log, event logs, models, settings) and
  ~/voice-test.
- uv and any Homebrew tools stay until you remove them.
```

### 2. Mac Terminal (or Ubuntu on Windows): uv, then the installer
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# open a NEW window, then:
uvx voice-mode-install@9.0.2 --voice-mode-version=9.0.2
```

### 3. Same window: a test folder, then add VoiceMode to this folder only (one line)
```
mkdir ~/voice-test && cd ~/voice-test
claude mcp add -e VOICEMODE_STT_BASE_URLS=http://127.0.0.1:2022/v1 -e VOICEMODE_TTS_BASE_URLS=http://127.0.0.1:8880/v1 --transport stdio --scope project voicemode -- uvx --from voice-mode==9.0.2 voicemode-mcp-launcher
claude --permission-mode manual
```

### 4. Only when you're done: leave Claude Code, then switch it all off
```
/exit
claude mcp remove --scope project voicemode
voicemode whisper service uninstall --remove-models
voicemode kokoro uninstall --remove-models
uv tool uninstall voice-mode
# deletes VoiceMode's logs, models and settings, and the test folder:
rm -rf ~/.voicemode ~/voice-test
```

### 5. Windows PowerShell, as administrator: WSL first
```
wsl --install
# restart; in Windows Settings › Privacy & security › Microphone, turn on
# microphone access for desktop apps; then open Ubuntu from the Start menu,
# install Claude Code inside it, and use sections 2 to 4 there
```
