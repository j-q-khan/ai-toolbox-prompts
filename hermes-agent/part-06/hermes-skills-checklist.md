# Hermes Agent skills: check before you trust (facts checked 2026-11-16)

Every line comes from the Hermes Agent docs or source (v0.23.1, published 2026-11-10)
or ClawHub's docs, with the source at the bottom. Nothing here was installed or run.
Not affiliated with Nous Research, the OpenClaw Foundation, Microsoft, Apple or GitHub.
Do Part 2's safe setup first (Hermes installed, approvals on manual, a test folder).

## Where things are kept
- Skills:  Mac ~/.hermes/skills/    Windows %LOCALAPPDATA%\hermes\skills\
- Memory:  Mac ~/.hermes/memories/  Windows %LOCALAPPDATA%\hermes\memories\
  MEMORY.md = the agent's notes (2,200 characters). USER.md = your profile (1,375 characters).
- See what you have:  hermes skills list
- Blank Slate may have left the bundled skills out. To add them:  hermes skills opt-in --sync
- Blank Slate turns memory off (memory.memory_enabled and memory.user_profile_enabled: false,
  and the memory toolset disabled). Hermes setup code: optional features "opt back in via
  hermes setup agent". Then check the memory toolset is on:  hermes tools
  Check:  hermes config get memory.memory_enabled   (should print true)

## Install (Hermes docs)
- Official extra (built-in trust):   hermes skills install official/CATEGORY/NAME
  Example:                           hermes skills install official/productivity/memento-flashcards
- ClawHub (community trust):         hermes skills install clawhub/NAME
- A link to a SKILL.md (community):  hermes skills install https://example.com/SKILL.md
- Installed skills take effect in new sessions. Each one is a slash command: /NAME

## Before you install (anything not official)
- [ ] Preview:  hermes skills inspect SOURCE/NAME
      Shows the source and a SKILL.md preview. In v0.23.1 the preview is the first 50 lines only.
- [ ] Open the skill's page (ClawHub or GitHub) and go through EVERY file as text,
      SKILL.md to the end and everything under scripts/, references/, templates/, assets/.
- [ ] Web links and download tools: curl, wget, Invoke-WebRequest, irm, pip install, npm install.
- [ ] Anything touching secrets: .env files, ~/.ssh, ~/.aws, API_KEY, TOKEN, PASSWORD,
      os.environ, process.env.
- [ ] Keys it asks for (required_environment_variables in the header). Hermes docs:
      declared keys are "automatically passed through" to its scripts.
- [ ] Lines telling the agent to ignore its rules, act as someone else, or hide something
      from you. Hidden HTML comments. Odd invisible characters.
- [ ] Scripts: what each one does, line by line. The agent can run them through its terminal.
- ClawHub's docs: "Install only content you understand and trust."
- Optional helper: download the skill to a review folder OUTSIDE your skills folder
  (GitHub: Code > Download ZIP), then in Hermes:  /skill-check PATH-TO-THE-REVIEW-FOLDER

## The scan (Hermes docs and source)
- Every hub install is scanned for "data exfiltration, prompt injection, destructive commands,
  supply-chain signals, and other threats".
- Verdict: safe, caution or dangerous.
- Community sources: a caution verdict blocks the install unless you add --force.
  (Medium and low findings alone give a safe verdict, which installs.)
  --force never overrides a "dangerous" verdict.
- Use --force only after you've looked at the flagged lines yourself.
  A clean scan is a good sign, not a guarantee.
- Re-scan installed hub skills later:  hermes skills audit
- Remove a hub skill:                  hermes skills uninstall NAME

## Save skill-check (the skill from the video)
- Windows (PowerShell):
    New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills\safety\skill-check"
  Save skill-check-SKILL.md in that folder as SKILL.md (Notepad: Save as type, All files).
- Mac (Terminal):
    mkdir -p ~/.hermes/skills/safety/skill-check
  Save it there as SKILL.md (TextEdit: Format, Make Plain Text; Shift-Command-G for ~/.hermes).
- Start a fresh chat, then:  /skill-check PATH-TO-THE-REVIEW-FOLDER
- Stop Hermes rewriting it:  hermes curator lock skill-check   (your own edits still work)

## Write approval (both default to false = write freely)
- In a chat:  /skills approval on     /memory approval on     (switches it on and keeps it on)
- Config keys: skills.write_approval and memory.write_approval
- Skills:  /skills pending   /skills diff ID   /skills approve ID   /skills reject ID
- Memory:  asks inline in the CLI; elsewhere queued:  /memory pending   /memory approve ID   /memory reject ID
- The gate covers the memory and skill tools, not edits made with the general file tools
  or the terminal in a chat.

## Look at, edit or delete memory
- Mac:      cat ~/.hermes/memories/MEMORY.md     cat ~/.hermes/memories/USER.md
- Windows:  cat $env:LOCALAPPDATA\hermes\memories\MEMORY.md   (PowerShell)
- List what Hermes has learned:  hermes journey list
- Edit one:    hermes journey edit ID   (Hermes source: opens $EDITOR, else $VISUAL, else vi.
                Not from the docs: on Windows, set EDITOR first to an editor that waits until you close the file.)
- Delete one:  hermes journey delete ID   (skills are archived and restorable; memory entries are removed)
- Turn memory off entirely: set memory.memory_enabled and memory.user_profile_enabled to false.

## Sources (checked 2026-11-16)
- Working with Skills: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills
- Skills System: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Persistent Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Skills catalogs: https://hermes-agent.nousresearch.com/docs/reference/skills-catalog
  and https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog
- Windows native: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Curator (lock): https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- Source: hermes_cli/skills_hub.py, tools/skills_guard.py and hermes_cli/journey.py at https://github.com/NousResearch/hermes-agent (tag v0.23.1)
- ClawHub security audits: https://github.com/openclaw/clawhub/blob/main/docs/security-audits.md
- Releases: https://github.com/NousResearch/hermes-agent/releases
