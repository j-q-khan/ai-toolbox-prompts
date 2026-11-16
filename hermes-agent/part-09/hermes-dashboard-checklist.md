# Hermes Agent dashboard: checklist (facts checked 2026-11-16)

Facts come from the Hermes Agent docs or source (v0.23.1, published 2026-11-10), with the
sources at the bottom; our own advice is marked (our note). Nothing here was installed or run.
Not affiliated with Nous Research, Anthropic, Microsoft, Apple, GitHub or Tailscale.
You need Hermes installed first (Part 2: https://youtu.be/gdebKsAZ-ts).

## Start it (PowerShell on Windows, Terminal on Mac; the same command)
1. Type:  hermes dashboard
2. The first time, Hermes builds the page first. Docs: "If the frontend hasn't been built
   yet, it builds automatically on first launch".
3. Your browser opens http://127.0.0.1:9119
   - 127.0.0.1 = the number every computer uses for itself (also called localhost).
   - 9119 = the port, the numbered door the dashboard listens behind.
   - Didn't open? Type http://127.0.0.1:9119 into your browser yourself. (our note)
4. You should see the Status page: the Hermes version and release date, the gateway
   status, and the 20 most recent sessions. It refreshes every 5 seconds.
5. Docs: "The dashboard runs entirely on your machine — no data leaves localhost."
   Your chats still go to the model provider you set up (for example Anthropic).

## Check it's only on this computer
- The defaults are --host 127.0.0.1 and --port 9119. Plain "hermes dashboard" uses them.
- Docs: "It binds to 127.0.0.1 by default — only accessible from your local machine,
  with no login required."
- Docs: the dashboard "reads and writes your .env file, which contains API keys and secrets."
- Any other --host, including 0.0.0.0 (every network your computer is on), switches on the
  sign-in gate. Docs: "the server refuses to start until an auth provider
  (username/password or OAuth) is configured."
- Run that way in a terminal, Hermes offers to set one up:
  [1] Username & password  [2] OAuth via Nous Portal  [3] Cancel
- The username and password option, docs: "Use it only on a trusted network or behind
  a VPN — not for public-internet exposure."
- --insecure: "Deprecated / no-op." Docs: "--insecure is a no-op — it does not disable
  auth" (since the June 2026 hardening). Guides that still use it are out of date. (our note)

## From another computer
- Docs: "If you want an auth-free dashboard, bind to 127.0.0.1 and reach it over an
  SSH tunnel or Tailscale."
- The docs' example port forward: ssh -L 8000:localhost:9119
  (our note: you add your own user and server, then open http://127.0.0.1:8000 on the computer
  you're using; the docs give this form in their CORS section, not as a step-by-step guide).
- Tailscale Serve, docs: it "is still treated as a non-loopback browser-facing origin and
  therefore requires a dashboard auth provider" (a username and password or OAuth).
- Never forward 9119 on your router. (our note)

## Which page for which job
| Job | Page | What the docs say it does |
|---|---|---|
| Check approvals still says manual | Config | form for config.yaml; approvals dropdown: smart / manual / off |
| Save a setting | Config | Save "writes changes to config.yaml immediately"; takes effect "on the next agent session or gateway restart" |
| Check or change a key | API Keys | whether each key is set, with a redacted preview; set, update or delete |
| Find an old chat | Sessions | full-text search; rename, export, prune, delete |
| See what it cost | Analytics | tokens, cache hits, estimated or actual cost; 7, 30 or 90 days; per model |
| Find why a job failed | Logs | agent, errors and gateway logs; filter by level and component |
| Start or stop the gateway, update, back up | System | gateway start/stop/restart; update after a confirmation; backup and restore |
| Shell hooks | System | "Hooks run arbitrary commands"; a warning, and they only fire after consent |
| Chat in the browser | Chat | the same chat as hermes --tui |
| Scheduled jobs | Cron | create, pause, edit, trigger now, delete |
| Add-ons | Skills, MCP | toggle skills and toolsets; add, test and remove MCP servers |
| Setups kept apart | Profiles | isolated Hermes setups with their own config, skills and sessions |
| Chat apps | Channels, Pairing, Webhooks | connect platforms; approve users; webhook subscriptions |

## Chat tab on native Windows: the docs disagree
- Web Dashboard page: "on a native Windows install the rest of the dashboard
  (sessions, jobs, metrics, config editor) works but the /chat tab will show a banner
  telling you to use WSL2 for that feature."
- CLI reference: "The embedded Chat tab requires a POSIX PTY environment, such as
  Linux, macOS, or WSL2."
- Windows (Native) guide: "Dashboard /chat embedded terminal pane: ConPTY through pywinpty".

## Stop it
1. Open another PowerShell or Terminal window and type:  hermes dashboard --stop
2. Type:  hermes dashboard --status
3. You should see: No hermes dashboard or serve processes running.

## Changed a key?
- In a chat that's already open in your terminal, type /reload. Docs: it re-reads
  ~/.hermes/.env, "Reloaded .env (3 var(s) updated)", so the new key works without a restart.

## Sources (checked 2026-11-16, v0.23.1 tag)
- Web Dashboard: https://github.com/NousResearch/hermes-agent/blob/v0.23.1/website/docs/user-guide/features/web-dashboard.md
- CLI reference: https://github.com/NousResearch/hermes-agent/blob/v0.23.1/website/docs/reference/cli-commands.md
- Windows (Native) guide: https://github.com/NousResearch/hermes-agent/blob/v0.23.1/website/docs/user-guide/windows-native.md
- Source: https://github.com/NousResearch/hermes-agent/blob/v0.23.1/hermes_cli/main_dashboard.py
