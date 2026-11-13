# Full code: Claude Code vs Cursor in 2026: Pricing, Claude Models and Who Should Pick Which

A side-by-side sheet and a test-folder AGENTS.md written for this video from Cursor's and Anthropic's own pages (checked 2026-11-13). Prices, plans and defaults are what they were when checked; re-check the source link in each row before you rely on one. The CSV was parsed with Python's csv module; nothing was installed or run. Save each file in a new test folder that isn't inside another project: in Notepad, set the box called Save as type to All files; in TextEdit, choose Format, then Make Plain Text, first.

### 1. claude-code-vs-cursor-2026-11-13.csv
```
topic,claude_code_in_anthropics_words,cursor_in_cursors_words,checked,sources
What it is,"A coding agent in the terminal, VS Code (also an Install for Cursor link), the desktop app and the web","A desktop app ""available for macOS, Windows, and Linux"", a CLI started with agent, and Cloud Agents from Premium",2026-11-13,https://code.claude.com/docs/en/overview ; https://code.claude.com/docs/en/vs-code ; https://cursor.com/download ; https://cursor.com/docs/cli/overview ; https://cursor.com/pricing
Claude models,"The opus alias is Opus 5.5 on the Anthropic API","Lists Claude Opus 5.5; third-party models ""aren't part of the included pool""; Free and Plus don't include them; Premium and above at API list price from prepaid credit",2026-11-13,https://code.claude.com/docs/en/model-config ; https://cursor.com/docs/models
Plans and prices (monthly),"Free $0 (no Claude Code); Pro $20, or $17 a month billed yearly; Max $100; Ultra $200; Claude Code in all paid plans","Free $0; Plus $8 (Grok models only); Premium $30; Super $100; Ultra $200; Teams $30+ a user; Enterprise Custom; yearly $80 / $300 / $1,000 / $2,000",2026-11-13,https://claude.com/pricing ; https://cursor.com/pricing ; https://cursor.com/docs/models
Older plans,"Not applicable","Pro, Pro+, Ultra, Start and Teams Standard or Premium seats are legacy plans that ""keep working as they are""",2026-11-13,https://cursor.com/docs/models
Usage pool,"Your work in the terminal and your chats draw from one pool; limits every 5 hours and every week on Pro and Max; Ultra: no 5-hour limit for verified accounts","""Every tier includes a pool of AI usage shared across Cursor and Grok""; the allowance refreshes weekly",2026-11-13,https://claude.com/pricing ; https://cursor.com/pricing
At the limit,"Wait for it to reset, move to a higher plan, or on paid plans turn on usage credits at standard API rates","Keep going with top-offs, or wait for your allowance to refresh",2026-11-13,https://claude.com/pricing ; https://cursor.com/pricing
How it is sold,"From Anthropic (claude.com/pricing)","""Sold as part of The X Subscription, one subscription for Grok, Cursor, and X""; ""only sold directly through X Subscription Corp.""",2026-11-13,https://cursor.com/docs/models ; https://cursor.com/pricing
Approval default,"Auto mode is the built-in starting mode for terminal and VS Code sessions (v2.1.283 or later); a second model, the classifier, reviews actions","Auto-review ""shipped as the recommended default"" (3.6); the security page also says terminal commands need approval by default",2026-11-13,https://code.claude.com/docs/en/permission-modes ; https://cursor.com/docs/agent/security/run-modes ; https://cursor.com/docs/agent/security
Edits in your folder,"Read-only actions and file edits in your working directory are auto-approved in auto mode","Agents can modify workspace files without approval, except for configuration files",2026-11-13,https://code.claude.com/docs/en/permission-modes ; https://cursor.com/docs/agent/security
Files outside your folder,"The first read outside the working directories prompts you","Read Access System (the default): the agent can read files outside the workspace without approval; Workspace asks first (Cursor 3.23 or later)",2026-11-13,https://code.claude.com/docs/en/permission-modes ; https://cursor.com/docs/agent/security/run-modes
Their own caveat,"Auto mode reduces permission prompts but does not guarantee safety","Auto-review is not a security boundary; the classifier can make mistakes",2026-11-13,https://code.claude.com/docs/en/permission-modes ; https://cursor.com/docs/agent/security/run-modes
Make it ask first,"Shift+Tab to Manual: it asks before most actions that edit files, run shell commands, or reach the network","Settings, Agents, Approvals & Execution: Allowlist with an empty allowlist, and Read Access set to Workspace",2026-11-13,https://code.claude.com/docs/en/permission-modes ; https://cursor.com/docs/agent/security/run-modes
Instructions file,"CLAUDE.md at the start of every session; reads AGENTS.md when there is no CLAUDE.md or CLAUDE.local.md in the working directory or above it","Project rules: .mdc files in .cursor/rules (a plain .md there is ignored); AGENTS.md in the root and subdirectories",2026-11-13,https://code.claude.com/docs/en/memory ; https://cursor.com/docs/rules
Skills,"Skills in .claude/skills","Also loads .claude/skills, .codex/skills, ~/.claude/skills and ~/.codex/skills for compatibility",2026-11-13,https://cursor.com/docs/skills
MCP,"Supported (MCP servers work across all surfaces)","All MCP connections need your approval; each tool call needs approval unless allowlisted",2026-11-13,https://code.claude.com/docs/en/overview ; https://cursor.com/docs/agent/security
Training,"Model training: Opt-out (Free, Pro, Max, Ultra); trains when this setting is on","Privacy Mode on: Customer Data will not be used for training by Cursor; off: may use codebase data, prompts and code snippets to train its models",2026-11-13,https://claude.com/pricing ; https://code.claude.com/docs/en/data-usage ; https://cursor.com/data-use
Training default for a new account,"Not stated in the docs","Not stated in the docs",2026-11-13,https://code.claude.com/docs/en/data-usage ; https://cursor.com/security
```

### 2. AGENTS.md
```
# Test folder instructions (Claude Code and Cursor)

- This is a throwaway test folder. Nothing in it is private.
- Only create or edit counter.html in this folder.
- Don't install anything and don't go online.
- Ask before running any command.
- Don't open files outside this folder.
- When you finish, list every file you changed.
```
