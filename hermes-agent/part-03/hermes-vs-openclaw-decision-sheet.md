# Hermes Agent vs OpenClaw: the decision sheet (facts checked 2026-11-14)

Every row comes from each tool's own GitHub page, docs or official pages, quoted or
summarised, with the source at the bottom. Nothing here was installed or run.
Versions checked: Hermes Agent v0.23.1 (2026-11-10), OpenClaw 2026.11.3 (2026-11-10).
Not affiliated with Nous Research or the OpenClaw Foundation.

## Side by side
| Topic | Hermes Agent | OpenClaw |
|---|---|---|
| Who's behind it | Nous Research, a company | The OpenClaw Foundation, an independent nonprofit (501(c)(3)) |
| Licence | MIT | MIT |
| Runs on | Windows, macOS, Linux (and WSL2) | macOS, Linux, Windows (and WSL2) |
| Chat apps | Telegram, Discord, Slack, WhatsApp, Signal and more, through its gateway | Discord, iMessage, Slack, Teams, Telegram, WhatsApp and 20+ more, through its Gateway |
| Cost of the software | Free | Free |
| Paid plan | Optional Nous Portal: Free $0, Plus $20, Super $100, Ultra $200 a month (when checked 2026-11-14) | None: "no paid tier, hosted service, or token" |
| Runs it for you in the cloud | Every paid Portal plan includes one cloud agent | No hosted service |
| Default for commands | approvals.mode smart: a second model judges commands on its dangerous-pattern list; low-risk ones run, clearly dangerous ones are denied, unsure ones ask | tools.exec.mode full: "No-approval host exec is the default" |
| Sandbox by default | No: the local backend is the default, "Commands run directly on your machine with no isolation" | No: "Sandboxing is off by default" |
| Strictest asking mode | manual: asks for commands on its dangerous-pattern list only | ask: asks about every command not on your allowlist |
| Middle setting | smart (the default) | auto: a reviewer model decides; the docs recommend it "for coding agents" |
| Memory | MEMORY.md and USER.md, loaded at session start | MEMORY.md and USER.md (plain Markdown), loaded at session start |
| Self-saved skills | Yes; memory and skills write freely by default | Yes; Skill Workshop is on by default, with undo |
| Review before saving | memory.write_approval / skills.write_approval: true | Skill Workshop autonomous.mode: propose (saves drafts) |
| Import from the other | hermes import-agent openclaw (official agent-importers plugin), with --dry-run | openclaw migrate hermes, with --dry-run (needs a fresh OpenClaw setup) |

Hermes Agent's README calls it "the only agent with a built-in learning loop". That is
Nous Research's claim, in its words.

## Which one fits you (answer each, then count)
1. Would one optional plan that bundles models, tools and an always-on cloud agent be handy? Yes points to Hermes Agent.
2. Do you want a tool with no paid tier at all, run by a nonprofit? Yes points to OpenClaw.
3. Do you want to okay every new command before it runs? Yes points to OpenClaw's ask mode.
   Happy to be stopped only for commands on a dangerous list? That's Hermes Agent's manual mode.
4. Do you want risky commands checked out of the box, before you change any setting? Yes points to Hermes Agent's smart default.
   (OpenClaw's default doesn't prompt; its docs recommend its auto mode for coding agents.)
5. Still torn? Both are free: try one first with a throwaway key that has a spend limit.

## Switch each one to asking before commands
Hermes Agent, in PowerShell or Terminal:

    hermes config set approvals.mode manual
    hermes config get approvals.mode

- [ ] The second command prints: manual

OpenClaw, in PowerShell or Terminal:

    openclaw config set tools.exec.mode ask
    openclaw gateway restart
    openclaw exec-policy show

- [ ] The last command shows the effective policy. Check that it now asks on allowlist misses.

Neither tool sandboxes the agent by default: both run commands straight on your computer.
A sandbox (a container) is a separate setup.

## Changed your mind? Each one imports from the other (dry runs change nothing)
OpenClaw to Hermes Agent, in PowerShell or Terminal, after installing Hermes Agent:

    hermes plugins install agent-importers
    hermes import-agent openclaw --dry-run

- [ ] It lists what would come across (persona, memories, skills, settings) and stops.
- [ ] API keys come across only if you add --migrate-secrets to a real import.
- [ ] A real import (without --dry-run) shows the same preview and asks you to confirm,
      and saves a backup of ~/.hermes first unless you add --no-backup.

Hermes Agent to OpenClaw, in PowerShell or Terminal, after installing OpenClaw:

    openclaw migrate hermes --dry-run

- [ ] It previews every change and stops. Secrets are redacted in the plan.
- [ ] A real interactive import asks before importing logins and keys, with yes selected
      by default: say no unless you mean to move them.
- [ ] A real import needs a fresh OpenClaw setup (see OpenClaw's "Migrating from Hermes" page).

## Sources (checked 2026-11-14)
- Hermes Agent README: https://github.com/NousResearch/hermes-agent
- Hermes Agent security: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Hermes Agent configuration (backends): https://hermes-agent.nousresearch.com/docs/user-guide/configuration
- Hermes Agent memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory
- Hermes Agent skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Hermes Agent, migrate from OpenClaw: https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw
- Nous Portal plans: https://portal.nousresearch.com
- OpenClaw README: https://github.com/openclaw/openclaw
- OpenClaw exec tool: https://docs.openclaw.ai/tools/exec
- OpenClaw permission modes: https://docs.openclaw.ai/tools/permission-modes
- OpenClaw sandboxing: https://docs.openclaw.ai/gateway/sandboxing
- OpenClaw memory: https://docs.openclaw.ai/concepts/memory
- OpenClaw Skill Workshop: https://docs.openclaw.ai/tools/skill-workshop
- OpenClaw, migrating from Hermes: https://docs.openclaw.ai/install/migrating-hermes
