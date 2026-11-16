# Full code: Claude Video Editing with Remotion: Make Videos with Claude Code

A checklist and commands written for this video from the toolkit's files at release v0.29.1 (read as text), Remotion's licence page and docs, and Anthropic's Claude Code docs, checked 2026-11-15. Not run by us: try it in a test folder with nothing private in it first.

### 1. video-toolkit-checklist.md
```
# Claude video editing with Remotion: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/digitalsamba/claude-code-video-toolkit (Digital Samba)
- Licence: MIT (the toolkit). It renders with Remotion, which has its own licence:
  "Remotion is free to use for individuals and companies up to three people."
  (remotion.dev/license). Bigger companies need a Company License
  (Remotion for Creators was $25 a month per seat on 2026-11-15). Non-profits
  are free too (LICENSE.md).
- Latest release: v0.29.1, 2026-11-14
- Real use: about 2,600 stars, 450 forks, 33 closed and 1 open issue;
  7 closed issues sampled: a maintainer replied on all 7
- Reaches: the toolkit folder. The cloud tools send your files to a rented GPU.
  Without Cloudflare R2, tools/file_transfer.py uploads them to public file
  hosts: litterbox.catbox.moe (24 hours), then 0x0.st (30 days).
- /setup asks for keys (R2, ElevenLabs) in the chat and writes them to .env.
  Skip it to render locally.
- Telemetry: none found in README, CLAUDE.md, setup.md, file_transfer.py,
  .claude/settings.json ({}) and the hello-world sample.
- Costs: the hello-world sample is free. Optional paid extras use your own
  accounts: ElevenLabs (Starter was $6 a month, $1 the first month),
  Modal cloud GPU (Starter: $0 plus compute, $30 a month free credits).
- Never use the voice-cloning or talking-head tools on anyone but yourself.
  Skip the watermark remover: removing someone else's watermark can break
  their rights.

## Setup (one test folder, no keys)
1. Node.js 22 or newer (nodejs.org) and Git (git-scm.com).
   Check: node --version and git --version
   Mac: the first git command may offer Apple's developer tools: accept.
2. Make a test folder and cd into it (path in double quotes):
   mkdir "$HOME/video-test" then cd "$HOME/video-test" (the same on Windows and Mac).
3. Save the address, then clone the release (each command is one line):
   Windows: $repo = "https://github.com/digitalsamba/claude-code-video-toolkit"
   Mac:     repo=https://github.com/digitalsamba/claude-code-video-toolkit
   Both:    git clone -b v0.29.1 --depth 1 $repo
   A "detached HEAD" note is normal: you're on the release tag.
4. cd claude-code-video-toolkit/examples/hello-world
5. npm install
   Windows: "running scripts is disabled"? Type npm.cmd install instead
   (and npm.cmd run render below). Don't change the execution policy.
   npm suggests npm audit fix --force? Say no: it replaces the locked versions.
   A notice about a newer npm (npm install -g npm@...)? Ignore it.
   Never run npm run upgrade: it moves Remotion off the fixed 4.0.539.
6. npm run render
   The first render downloads Chrome Headless Shell into node_modules.
   Your video: examples/hello-world/out/video.mp4. Double-click it.
   No uv sync, no Python and no FFmpeg needed for this sample.

## Let Claude change it
1. cd ../..   (back to claude-code-video-toolkit)
2. claude. Say yes to trusting the folder.
   If it says auto mode, press Shift+Tab once: manual mode on.
3. Ask: Change the hello-world video's title slide to say "My First Video",
   ask me for three highlights, then render it again.
4. Approve the edit to examples/hello-world/src/config/sprint-config.ts and
   npm run render. Say no to /setup, upgrades and anything outside this folder.
5. Quick drafts: npm run render:preview (half size, out/preview.mp4).

## If you add the cloud tools later
- Set up Cloudflare R2 first, so nothing goes to public file hosts.
- In the toolkit folder, copy .env.example to a new file named .env (only /setup
  makes it for you), then type each value into .env yourself. Never paste a key
  into the chat.

## Remove it
- Copy out/video.mp4 somewhere else.
- In Claude Code: /exit
- Shut the terminal window (Windows won't delete a folder a window is still in).
- Delete the test folder in File Explorer or Finder.
- Node and Git stay until you uninstall them.
```

### 2. Commands (Windows PowerShell)
```
node --version
git --version
mkdir "$HOME/video-test"
cd "$HOME/video-test"
$repo = "https://github.com/digitalsamba/claude-code-video-toolkit"
git clone -b v0.29.1 --depth 1 $repo
cd claude-code-video-toolkit/examples/hello-world
# "running scripts is disabled"? use npm.cmd install and npm.cmd run render instead
npm install
npm run render
```

### 3. Commands (Mac Terminal)
```
node --version
git --version
mkdir "$HOME/video-test"
cd "$HOME/video-test"
repo=https://github.com/digitalsamba/claude-code-video-toolkit
git clone -b v0.29.1 --depth 1 $repo
cd claude-code-video-toolkit/examples/hello-world
npm install
npm run render
```

### 4. Then Claude Code (from hello-world)
```
cd ../..
claude
```

### 5. Then type this inside Claude Code (manual mode on: Shift+Tab once if it says auto mode)
```
Change the hello-world video's title slide to say "My First Video", ask me for three highlights, then render it again.
```

### 6. Only when you're done, leave Claude Code
```
/exit
```

### 7. Quick drafts (in examples/hello-world)
```
npm run render:preview
```
