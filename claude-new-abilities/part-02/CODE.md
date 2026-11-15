# Full code: Claude Video Skill: Can Claude Watch Videos? Yes, Here's How

A checklist, setup files and a first prompt written for this video from the claude-video repo at release v0.3.2 (read as text) and Anthropic's Claude Code docs, checked 2026-11-15 (Claude Code 2.1.325). Not run by us: use a test folder and a clip of your own, never private or work videos.

### 1. claude-video-checklist.md
```
# claude-video for Claude Code: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/bradautomates/claude-video, by Bradley Bonanno (the original;
  claude-watch is a rewrite of it)
- Licence: MIT
- Latest release: v0.3.2, 2026-09-25 (last commit the same day)
- Real use: about 20,900 stars, 2,219 forks, 60 open and 17 closed issues;
  in 10 sampled closed issues the author closed 7 and replied on 3; one maintainer
- Works in: Claude Code (terminal, VS Code, the desktop app's Code tab).
  Not in Claude's chat or Cowork.
- Runs by itself: a setup check at the start of every Claude Code session
  (hooks/hooks.json; it doesn't go online)
- Reaches: the video you point it at, a temporary folder, ~/.config/watch/.env
- Local engine: frames and captions on your computer, no key, never contacts Google
- Gemini engine (the setup's "recommended" answer): YouTube links go to Google;
  local files are uploaded to Google and deleted after the answer
- Telemetry: none found in the files; cost: free on the local engine

## What you install first
- Windows: Python 3.10+ (python.org), then in PowerShell:
  winget install --id Gyan.FFmpeg --exact
  winget install --id yt-dlp.yt-dlp --exact
  (YouTube links also need: winget install --id DenoLand.Deno --exact)
- Mac: Homebrew (brew.sh), then in Terminal: brew install python ffmpeg yt-dlp
- Quit and reopen the terminal afterwards.

## Safe setup
1. Make a folder called Watch test with one short clip of your own, named example.mp4.
2. Go into it (cd, then the path in double quotes), make the .claude folder
   and save .claude/settings.json (section 4).
3. Start claude in the folder, say yes to trusting it; the status bar should say
   manual mode on (if it says auto mode, press Shift+Tab once).
4. In Claude Code: the two lines in section 5. Choose
   Install for you, in this repo only.
5. Check: claude plugin list shows watch@claude-video, 0.3.2, local.
6. Paste the prompt in section 7. When setup asks how to view videos, choose local.

## Speech from your own clips (optional)
- Captions only (none) gives pictures, no speech, for a clip with no captions.
- Local WhisperX: no key; at least 3 GB disk and 8 GB RAM;
  verified on Apple Silicon Macs, untested on Windows.
- Cloud: a Groq or OpenAI key (GROQ_API_KEY or OPENAI_API_KEY).

## Keys, if you ever add one
- The setup offers to take a key pasted in the chat. Don't: the key would sit
  in the conversation.
- Set GEMINI_API_KEY, GROQ_API_KEY or OPENAI_API_KEY as an environment variable,
  or type it into ~/.config/watch/.env yourself.

## YouTube
- YouTube's terms restrict downloading. Use your own videos.

## Long videos
- Name the stretch: /watch video.mp4 --start 2:15 --end 2:45
  (in Claude Code, pick /watch:watch from the list)

## Desktop app route (takes the newest version, not a fixed release)
- Customize, Plugins, Add, Add marketplace, Add from a repository,
  https://github.com/bradautomates/claude-video, Sync, then install Watch.

## Switch it off
- Pause: claude plugin disable watch@claude-video
- Remove: claude plugin marketplace remove claude-video
- Then delete ~/.config/watch/.env and ~/.cache/watch if you no longer need them,
  and the test folder.
```

### 2. Install the tools (type one system's lines yourself, then open a fresh window)
```
# Windows, in PowerShell, after Python 3.10 or later from python.org:
winget install --id Gyan.FFmpeg --exact
winget install --id yt-dlp.yt-dlp --exact

# Mac, in Terminal, after Homebrew from brew.sh:
brew install python ffmpeg yt-dlp
```

### 3. Make the .claude folder (PowerShell on Windows or Terminal on a Mac, inside the test folder)
```
mkdir .claude
```

### 4. .claude/settings.json (save in the test folder; Notepad: Save as type, All files)
```
{
  "permissions": {
    "defaultMode": "default"
  }
}
```

### 5. Inside Claude Code, started in the test folder
```
/plugin marketplace add bradautomates/claude-video#v0.3.2
/plugin install watch@claude-video
```

### 6. Check it worked (a second PowerShell or Terminal window, in the test folder)
```
claude plugin list
```

### 7. The first prompt (paste into Claude Code, in the test folder)
```
Use the watch skill on example.mp4 in this folder.
For setup, choose the local engine, balanced detail and captions only (none).
Summarize what is visible, with timestamps.
```

### 8. Switch it off (PowerShell or Terminal, in the test folder)
```
claude plugin disable watch@claude-video
claude plugin marketplace remove claude-video
```
