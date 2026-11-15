# Full code: Claude Code API Error 529 Overloaded and Rate Limits: Is It You or Anthropic?

A server-errors and rate-limits checklist written for this video from Anthropic's Claude Code docs and help centre (checked 2026-11-14, Claude Code 2.1.325). Messages and command names are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-529-rate-limit-checklist.md
```
# Claude Code error 529, 500 and rate limit checklist (from Anthropic's docs, checked 2026-11-14)

## Whose side is it?
- [ ] "API Error: 500 Internal server error": a failure inside Anthropic's API. Not caused by your prompt, settings or account.
- [ ] "API Error: Repeated 529 Overloaded errors": the API is at capacity across all users. It is not your usage limit and doesn't count against your quota.
- [ ] "API Error: Server is temporarily limiting requests (not your usage limit)": a short-lived throttle, unrelated to your plan. Retried for you from Claude Code 2.1.199.
- [ ] "API Error: Request rejected (429)": the rate limit set for your API key or your cloud provider's account. This one can be yours.
- [ ] "You've hit your session limit" (or weekly, Opus, Sonnet) is your plan's usage limit: the previous video in this series.
- [ ] Before any of these shows, Claude Code has already made whatever retries apply (up to 10, with "Retrying in Ns · attempt x/y" under the spinner).

## 500 or 529
- [ ] Check https://status.claude.com in your browser for an incident or capacity notice.
- [ ] Wait a few moments, then send your message again. To save pasting a long prompt, type: try again
- [ ] 529 keeps coming back? Type /model at the Claude Code prompt and pick a different model (capacity is tracked per model).
- [ ] In the Claude Desktop app, switch with the app's model picker.

## 429 (Request rejected)
- [ ] Type /status at the Claude Code prompt: which sign-in is active, your Claude account or a key?
- [ ] A key you use on purpose: check that account's limits and request a higher tier if needed (platform.claude.com/docs/en/api/rate-limits).
- [ ] Run fewer subagents at once.

## The mistake: a forgotten ANTHROPIC_API_KEY
- [ ] An ANTHROPIC_API_KEY environment variable is used instead of your Claude subscription, billed per request on that key's account.
- [ ] Check it without showing the key: /status inside Claude Code, or the copy-paste check (BUILD-PROMPT.md).
- [ ] Clear it for one window (exit Claude Code first). This changes only that window; nothing is deleted from your Anthropic account:
      Windows PowerShell:  Remove-Item Env:ANTHROPIC_API_KEY
      Mac or Linux:        unset ANTHROPIC_API_KEY
- [ ] Stop it coming back in new windows:
      Windows: open the Environment Variables settings, find ANTHROPIC_API_KEY under User variables (or System variables), and delete it.
      Mac: open the startup file the copy-paste check found (usually ~/.zshrc) in a text editor (in Finder, Shift-Command-G, type the path), delete the line that sets ANTHROPIC_API_KEY, and save it as plain text.
- [ ] Open a new PowerShell or Terminal window and start Claude Code again.
- [ ] Sign-in trouble after that? The next video in this series covers it.

## Check it worked
- [ ] /status shows your Claude account, not a key.
- [ ] Send a short message: Claude answers, with no retrying countdown.

## Still stuck?
- [ ] Persists with nothing posted on status.claude.com? Type /feedback inside Claude Code (it can open a prefilled GitHub issue).
- [ ] Search existing issues: github.com/anthropics/claude-code/issues

Docs: code.claude.com/docs/en/errors and support.claude.com/en/articles/12304248
```
