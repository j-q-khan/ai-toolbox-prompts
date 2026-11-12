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
