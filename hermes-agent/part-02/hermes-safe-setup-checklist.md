# Hermes Agent: the safe setup checklist (facts checked 2026-11-14, v0.23.1)

Every step comes from the Hermes Agent README and docs, or from its installer read as text.
Nothing here was run for the video. What you see on your screen may be worded differently.

## 0. Before you start
- [ ] A terminal: PowerShell on Windows 10 or 11 (Start, type PowerShell, open it; no admin rights needed),
      or Terminal on a Mac (Command + Space, type Terminal, Return).
- [ ] A brand-new key made only for Hermes, from a provider Hermes lists (for example OpenRouter),
      with a spend limit set on it. OpenRouter documents per-key credit limits:
      https://openrouter.ai/docs/api-reference/limits
- [ ] Never paste your key into a chat or a file other than where Hermes' setup asks for it.

## 1. Install (the README's official lines)
Windows, in PowerShell:

    iex (irm https://hermes-agent.nousresearch.com/install.ps1)

Mac, in Terminal:

    curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

- [ ] You see one status line per step. Don't type until it asks you something.
      By default it also adds a browser (Chromium) and a computer-use driver; Blank Slate keeps their tools off.
- [ ] Mac: "git needs Apple's Command Line Tools"? Click Install in the window that pops up and accept the licence.
      The installer waits and carries on by itself.
- [ ] Windows: antivirus quarantined uv.exe? The README calls this a false positive. Run the README's
      check (hermes-uv-check-from-readme.ps1, from the same folder) before you change any antivirus setting.
- [ ] An error? The installer prints its last lines and the path of its log file. Look there first.
- [ ] The setup wizard opens by itself. If it doesn't, type: hermes setup

## 2. The setup wizard
- [ ] "Import your setup from ...?" (only if it finds another agent; the default is yes): choose No for a clean start.
      You can import later.
- [ ] "How would you like to set up Hermes?": choose Blank Slate.
- [ ] Step 1, Provider & Model: choose the provider you made the key with, paste the key, pick a model.
- [ ] Step 2, Terminal Backend: keep "Local - run directly on this machine (default)".
      (Running it in a container is Part 7 of the series.)
- [ ] "Your minimal agent is ready. What next?": choose "Start with everything disabled".
- [ ] "Help improve Hermes?": "No thanks" is pre-selected. Your choice. Change it later with: hermes setup telemetry
- [ ] Windows: "Start the gateway now after install? [Y/n]" type n, then Enter.
      "Start the gateway automatically on Windows login with a Scheduled Task? [Y/n]" type n, then Enter.
      (Enter alone means yes.)

## 3. Open a fresh PowerShell or Terminal window, then check the gateway is off
    hermes gateway status

- [ ] If it shows a gateway installed or running (on a Mac the installer sets one up and starts it
      without asking), stop it, then remove it:

    hermes gateway stop
    hermes gateway uninstall

## 4. Switch approvals to manual
    hermes config set approvals.mode manual
    hermes config get approvals.mode

- [ ] The second command prints: manual
- [ ] Know what manual covers: it asks for commands on its dangerous-pattern list, and only those.
      Ordinary commands can run without asking. Ordinary file edits never go through this check; the file
      tools only refuse a short list of protected places (like ~/.ssh/), and ~/.ssh/config asks first.
- [ ] Where the settings file is: hermes config path

## 5. Optional: if you also use Claude Code or Codex
    hermes config set auth.adopt_external_logins false

- [ ] By default Hermes borrows their logins when it has none of its own; the docs say programs sharing
      one login can sign each other out. This stops the borrowing.

## 6. First run in a test folder
    mkdir hermes-test
    cd hermes-test
    hermes

- [ ] The welcome banner shows your model.
- [ ] A first request: make a text file called dinner with three dinner ideas in it.
      It makes the file without asking. That's expected: file writes aren't in the approval check.
- [ ] The folder doesn't fence Hermes in: the local backend is "Isolation: None — runs on host".
- [ ] An approval box offers once / session / always / deny, and Enter means deny.
      Choose once or deny. Leave always alone: it adds that command type to a permanent allowlist.
- [ ] Something off? In a fresh window: hermes doctor

## Sources (checked 2026-11-14)
- README: https://github.com/NousResearch/hermes-agent
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Quickstart (setup modes): https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Security (approvals, isolation, logins): https://hermes-agent.nousresearch.com/docs/user-guide/security
- Windows (native): https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- CLI reference: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
