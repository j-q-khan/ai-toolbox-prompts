# Full code: Claude Obsidian Second Brain: Set Up Obsidian Skills for Free

A checklist and setup files written for this video from the obsidian-skills repo at release 1.1.0 (read as text), Obsidian's help docs and Anthropic's Claude Code docs, checked 2026-11-15 (Claude Code 2.1.325). Not run by us: use a copy of your vault, never your real one.

### 1. obsidian-skills-checklist.md
```
# Obsidian Skills for Claude Code: checklist (checked 2026-11-15)

## Before you install
- Repo: github.com/obsidianmd/obsidian-skills, under Obsidian's own GitHub organisation
- Licence: MIT
- Latest release: 1.1.0, 2026-11-11 (main already says 1.2.0, not released)
- Real use: about 52,800 stars, 3,800 forks, 3 open and 58 closed issues;
  in 5 sampled closed issues a maintainer replied
- Reach: skills only, no MCP server, hooks or background processes
- Your notes: vault notes you ask about go to the AI model
- Reaches further: obsidian-cli can run JavaScript in the app (obsidian eval);
  defuddle fetches web pages; defuddle and knap ask before installing from npm
- Telemetry: none in the files; cost: free (Obsidian is free, no sign-up)

## Safe setup
1. Copy your vault folder; leave out anything private.
   Vault uses Obsidian Sync or a cloud folder (iCloud, OneDrive, Dropbox)?
   Make a new vault with a few notes outside that folder instead.
2. Obsidian: Vault profile (bottom left), Open folder as vault, Open, pick the copy.
3. Go into the copy (cd, then the path in double quotes), make the .claude folder
   and save .claude/settings.json (section 3).
4. Start claude in the copy; the status bar should say manual mode on.
5. In Claude Code: the two lines in section 4. Choose
   Install for you, in this repo only.
6. Check: claude plugin list shows obsidian@obsidian-skills, 1.1.0, local.

## The Obsidian command line (optional)
- Needs the Obsidian installer 1.12.7 or later.
- Settings, General, Command line interface, then follow the prompt to register it.
- Do NOT install the npm package obsidian-cli: it is an unrelated tool.

## Before Claude renames notes
- Settings, Files and links: turn on Automatically update internal links.

## Manual route (no marketplace)
- From the 1.1.0 zip, copy plugins/obsidian/skills/ into .claude/skills/ in the vault copy.

## Switch it off
- Pause: claude plugin disable obsidian@obsidian-skills
- Remove: claude plugin marketplace remove obsidian-skills
- Then delete the vault copy if you no longer need it.
```

### 2. Make the .claude folder (PowerShell on Windows or Terminal on a Mac, inside the vault copy)
```
mkdir .claude
```

### 3. .claude/settings.json (save in the vault copy; Notepad: Save as type, All files)
```
{
  "permissions": {
    "defaultMode": "default"
  }
}
```

### 4. Inside Claude Code, started in the vault copy
```
/plugin marketplace add obsidianmd/obsidian-skills#1.1.0
/plugin install obsidian@obsidian-skills
```

### 5. Check it worked (a second PowerShell or Terminal window, in the vault copy)
```
claude plugin list
```

### 6. Switch it off (PowerShell or Terminal, in the vault copy)
```
claude plugin disable obsidian@obsidian-skills
claude plugin marketplace remove obsidian-skills
```
