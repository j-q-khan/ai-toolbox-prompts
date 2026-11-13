# Full code: Claude vs ChatGPT for Coding: Claude Pro or ChatGPT Plus in 2026?

A comparison sheet and a checklist written for this video from Anthropic's and OpenAI's own pages (checked 2026-11-13). Prices are what they were when checked; re-check the source link in each row before you pay for anything. The CSV was parsed with Python's csv module; nothing was installed or run.

### 1. claude-vs-chatgpt-2026-11-13.csv
```
plan,price_when_checked,coding_agent,where_the_agent_works,chat_usage_in_their_words,agent_usage_in_their_words,model_training_in_their_words,checked,source
Claude Free,$0,No (Claude Code is not on Free),Not included,"Limited usage every 5 hours and every week",Not included,"Model training: Opt-out",2026-11-13,https://claude.com/pricing ; https://code.claude.com/docs/en/setup
Claude Pro,"$20 a month, or $17 a month billed yearly ($200 up front)",Claude Code,"Terminal, code editors, desktop app, web","More usage than Free, every 5 hours and every week","These limits are shared across Claude and Claude Code","Model training: Opt-out; trains when this setting is on, including Claude Code",2026-11-13,https://claude.com/pricing ; https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan ; https://code.claude.com/docs/en/data-usage
ChatGPT Free,$0,Codex (limited),"Desktop app, subject to rollout","Unlimited text chats, subject to abuse guardrails","Limited Codex access","Content is used to train our models; Opt-out available",2026-11-13,https://chatgpt.com/pricing ; https://learn.chatgpt.com/docs/pricing
ChatGPT Go,$8 a month (may include ads),Codex (limited),"Desktop app, subject to rollout","Unlimited text chats, subject to abuse guardrails",Limited,"Content is used to train our models; Opt-out available",2026-11-13,https://chatgpt.com/pricing ; https://learn.chatgpt.com/docs/pricing
ChatGPT Plus,$20 a month (no yearly price shown on the pages checked),Codex,"Web, terminal (CLI), IDE extension, iOS","Everyday text chats: Unlimited; usage must be reasonable","ChatGPT Work and Codex share usage; ranges per 5 hours are not fixed message limits; weekly limits may also apply","Content is used to train our models; Opt-out available",2026-11-13,https://chatgpt.com/pricing ; https://learn.chatgpt.com/docs/pricing
```

### 2. twenty-dollar-checklist.md
```
# Claude Pro or ChatGPT Plus? A checklist (facts checked 2026-11-13)

## 1. Try before you pay
- [ ] Want to try a coding agent free? ChatGPT Free lists limited Codex in its desktop app (subject to rollout).
- [ ] Claude Free has chat that runs code, but no Claude Code.

## 2. The $20 plans (prices when checked)
- [ ] Claude Pro: $20 a month, or $17 a month billed yearly. Includes Claude Code.
- [ ] ChatGPT Plus: $20 a month. Includes Codex on the web, in the terminal, in the editor extension and on iOS.

## 3. Limits, in each company's words
- [ ] Claude: chats and Claude Code share the same limits, every 5 hours and every week.
- [ ] ChatGPT: everyday text chats listed as unlimited (usage must be reasonable); Work and Codex share usage.
- [ ] Both: extra usage credits can be bought at the limit.

## 4. Before you paste in any code
- [ ] Claude training setting (personal plans say opt-out): claude.ai/settings/data-privacy-controls
- [ ] ChatGPT training setting (personal plans say opt-out available): see the privacy row on chatgpt.com/pricing
- [ ] Use a new test folder, never your home folder, with nothing private in it.
- [ ] Re-check prices at claude.com/pricing and chatgpt.com/pricing: they change.
```
