# Hermes Agent desktop app: setup checklist (facts checked 2026-11-15)

Every row comes from Hermes Agent's own docs, its desktop README or its download page,
with the source at the bottom. Version checked: Hermes Agent v0.23.1 (published 2026-11-10).
Nothing here was installed or run. Not affiliated with Nous Research, Microsoft, Apple, Intel or GitHub.

## The download page and the docs say different things (both as written, 2026-11-15)
- Download page: "macOS 12+" and "Windows 10/11".
- Docs: the Windows package (MSIX) "requires Windows 11 22H2 or later".
- Docs: "The macOS installer is Apple Silicon only." On an Intel Mac the Mac download
  reports "not supported on this Mac". "Intel Macs can install the CLI and run hermes desktop."

## Check your computer
- Windows version: Settings, then System, then About. Check it says Windows 11 first (Windows 10's
  last update is also called 22H2), then look for "Version" 22H2 or later.
- Mac chip: Apple menu, then About This Mac (Apple Silicon Macs list an M chip).

## Pick your route
| Your computer | Route |
|---|---|
| Hermes already installed from the terminal (Part 2) | Type: hermes desktop (the first run builds the app, so give it time) |
| Windows 11, version 22H2 or later | Download page, then Microsoft Store button |
| Apple Silicon Mac | Download page, then Mac download (Hermes-Setup.dmg, which the docs call a bootstrap installer: it downloads Hermes and builds the app, so the first run takes a while) |
| Intel Mac | Install Hermes from the terminal (Part 2), then: hermes desktop |
| Windows 10 | Install Hermes from the terminal (Part 2), then: hermes desktop. (The page's "Download .exe instead" is, in the docs' words, "a different, bootstrap installer" that "provisions a source checkout through the scripts".) |
| Linux | The download page: "installs through the terminal" (then hermes desktop) |

## First launch
- [ ] A setup screen asks for your provider and model. If you did Part 2, they're already set.
      Not ready? Click "Choose provider later" to look around first.
- [ ] Send a small request in the chat. You see each step the agent takes as it works.
- [ ] The YOLO switch in the bar along the bottom of the chat is OFF.
      Docs: "YOLO bypasses the dangerous-command approval prompts, so know what
      you're turning off." It is saved with that chat.
- [ ] Approvals: in PowerShell or Terminal, type hermes config get approvals.mode
      It prints manual if you did Part 2. The default is smart. To switch (Part 2):
      hermes config set approvals.mode manual
      No hermes command in your terminal? Do Part 2's install first.
- [ ] Optional, to keep first tries in a test folder (terminal route only):
      hermes desktop --cwd PATH-TO-YOUR-TEST-FOLDER

## Before you finish
The app starts Hermes' gateway, the background program it talks to. Docs: "it keeps
running after you quit and has no idle shutdown". To stop it, use the gateway controls in Settings,
or in PowerShell or Terminal:

    hermes gateway stop
    hermes gateway list

- [ ] The list command shows no gateway running (it lists each profile and whether its
      gateway is currently running).

## Shortcut: Quick Entry
- Settings, then Advanced, then Quick Entry: turn it on.
- Then Ctrl+Shift+Space (Windows) or Cmd+Shift+Space (Mac) opens a small box from any app.

## Good to know
- The app checks for updates in the background (it asks the GitHub API).
- Uninstall, app-managed installs: Settings, then About, then Danger zone
  ("Uninstall Chat GUI only", "Uninstall GUI + agent, keep my data", "Uninstall everything").
- Uninstall, Microsoft Store or MSIX: Windows Settings, then Apps, then Installed apps.
- Preview what a terminal uninstall of the app would remove: hermes uninstall --gui --dry-run

## Sources (checked 2026-11-15)
- Hermes Desktop docs: https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Platform support: https://hermes-agent.nousresearch.com/docs/getting-started/platform-support
- Windows (native): https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Security (YOLO): https://hermes-agent.nousresearch.com/docs/user-guide/security
- Desktop README: https://github.com/NousResearch/hermes-agent/blob/main/apps/desktop/README.md
- Download page: https://hermes-agent.nousresearch.com/desktop
- Releases: https://github.com/NousResearch/hermes-agent/releases
