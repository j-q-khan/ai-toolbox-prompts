# Full code: Claude Code vs Codex vs OpenCode vs Gemini CLI: Which AI Coding Agent in 2026?

A comparison sheet and a picker checklist written for this video from each vendor's own docs and pricing pages (checked 2026-11-12). Prices are what they were when checked; re-check the source link in each row before you pay for anything. The CSV was parsed with Python's csv module; nothing was installed or run.

### 1. comparison-2026-11-12.csv
```
tool,maker,licence,latest_version,version_date,cheapest_plan_with_it,price_when_checked,pay_as_you_go_key,default_approvals,sandbox_default,sandbox_on_native_windows,local_models,models,ask_first_setting,config_file,instructions_file,checked,source
Claude Code,Anthropic,"Not open source (All rights reserved)",2.1.322,2026-11-10,Claude Pro (not on the free plan),"$20 a month, or $17 a month billed yearly",Yes (Anthropic API key),"auto mode from v2.1.283 (a second model reviews its actions); Manual mode (config value default) asks before most edits, shell commands and network",Off (turn on with /sandbox),"No (Mac, Linux, WSL 2 only)","Not supported by Anthropic (Ollama documents a route)",Claude models only,"permissions.defaultMode set to default (Manual), plus ask and deny rules in .claude/settings.json",~/.claude/settings.json and .claude/settings.json,CLAUDE.md (reads AGENTS.md if there is no CLAUDE.md),2026-11-12,https://code.claude.com/docs/en/setup ; https://claude.com/pricing ; https://code.claude.com/docs/en/sandboxing
Codex CLI,OpenAI,Apache-2.0,0.167.2,2026-11-11,ChatGPT Plus (Free and Go list only the desktop app),$20 a month,"Yes (OpenAI API key, no cloud features)","Auto: workspace-write and on-request, network off",On,Yes,"Official: --oss with Ollama or LM Studio","OpenAI models, plus custom providers","approval_policy = ""on-request"" with sandbox_mode = ""workspace-write""",~/.codex/config.toml,AGENTS.md,2026-11-12,https://learn.chatgpt.com/docs/pricing ; https://learn.chatgpt.com/docs/agent-approvals-security ; https://learn.chatgpt.com/docs/sandboxing
OpenCode,Anomaly,MIT,2.2.7,2026-11-10,"None needed: free models for a limited time, Go, or your own key","$0, or Go at $10 a month",Yes (your own provider key),"build agent: allow all, only .env reads ask",None described,None described,"Official: Ollama, LM Studio, vLLM found automatically","Many providers: OpenAI, Anthropic, Google and more","change the build agent's allow-all default to ask in opencode.jsonc",~/.config/opencode/opencode.jsonc,AGENTS.md,2026-11-12,https://opencode.ai/docs/console/go/ ; https://opencode.ai/docs/permissions ; https://opencode.ai/docs/providers/
Gemini CLI,Google,Apache-2.0,0.68.0,2026-11-10,"Gemini Code Assist Standard, through your company","About $22.80 a month per person (listed as $0.031232877 an hour)",Yes (paid Gemini API or Vertex AI key),default: asks,Off (turn on with --sandbox),"Yes, when turned on (Windows native sandbox)","No (only a local Gemma model that routes requests)",Gemini models only,--approval-mode default,~/.gemini/settings.json,GEMINI.md,2026-11-12,https://github.com/google-gemini/gemini-cli ; https://cloud.google.com/gemini/pricing ; https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/cli-reference.md
Antigravity CLI,Google,"None given on its repo",1.5.7,2026-11-12,"Free Google account (Pro and Ultra get more)","$0, with a weekly quota (no numbers published)",Not checked (see Part 2),"v1.5.7+ starts new sessions in auto mode (release notes; the modes docs still say default); Agent Mode default with Tool Permission request-review asks","Terminal sandbox: workspace and temp folders, no network, under Default and Auto",Not checked (see Part 2),Not checked (see Part 2),Not checked for the CLI (see Part 2),"Agent Mode set to default in /config, and Tool Permission kept on request-review",~/.gemini/antigravity-cli/settings.json,Not checked (see Part 2),2026-11-12,https://antigravity.google/docs/plans ; https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
```

### 2. agent-picker.md
```
# Which AI coding agent? A picker checklist (facts checked 2026-11-12)

## 1. Start from what you already pay for
- [ ] Claude Pro or Max: Claude Code is included (not on Claude's free plan).
- [ ] ChatGPT Plus: Codex is included in the terminal (Free and Go list only the desktop app).
- [ ] Gemini Code Assist through work: Gemini CLI.
- [ ] A free, Pro or Ultra Google account: Antigravity CLI (Gemini CLI stopped serving these on 18 June 2026).
- [ ] None of these, or you want any provider: OpenCode (the tool is free; free models for a limited time, Go at $10 a month, or your own key).

## 2. Decide how much it may do without asking
- [ ] Ask before most edits and commands: Gemini CLI (default), Antigravity CLI (v1.5.7+ starts in auto mode; set Agent Mode to default in /config and keep Tool Permission on request-review to make it ask; see Part 2), Claude Code in Manual mode (newer versions start in auto mode, where a second model reviews its actions).
- [ ] Work inside my folder, ask before leaving it, sandbox on, Windows included: Codex (Auto).
- [ ] OpenCode: change the build agent's allow-all default to ask before the first task (Part 4).

## 3. Local models?
- [ ] Officially supported: Codex (--oss with Ollama or LM Studio) and OpenCode (finds Ollama by itself).
- [ ] Claude Code: Ollama documents a route; Anthropic says it doesn't support it.
- [ ] Gemini CLI: no local main model.

## 4. Before the first task, whichever you pick
- [ ] A new test folder, never your home folder.
- [ ] A throwaway key with a spend limit, if you pay as you go.
- [ ] The ask-first setting from comparison-2026-11-12.csv, written exactly as shown there.
- [ ] Prices re-checked at the source links: they change.
```
