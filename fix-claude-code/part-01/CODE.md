# Full code: Claude Code Usage Limit Reached? What It Means and How to Keep Working

A usage-limits checklist written for this video from Anthropic's Claude Code docs and help centre (checked 2026-11-14, Claude Code 2.1.325). Setting and menu names are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-usage-limit-checklist.md
```
# Claude Code usage limit checklist (from Anthropic's docs, checked 2026-11-14)

## Which limit is it?
- [ ] Read the exact word: session, weekly, Opus or Sonnet. The time at the end is when it resets.
- [ ] Session limit: a five-hour window from your first message (Pro and Max). Verified Ultra accounts have no five-hour limit.
- [ ] Weekly limit: resets at a fixed day and time set for your account. It counts at the same time as the session limit.
- [ ] Max and Ultra also have a weekly limit for Fable.
- [ ] These limits are shared with the Claude app (web, desktop, mobile) and Claude Code in your editor.
- [ ] Anthropic publishes no exact message counts.

## Let it carry on by itself (Claude Code 2.1.234 or later)
- [ ] Signed in with your Claude subscription, in a normal interactive session.
- [ ] Keep the window open. Exiting Claude Code ends the wait, and it doesn't restart when you come back to the session.
- [ ] Reset more than 24 hours away (often the weekly limit)? Pick "Wait here, then continue automatically" from the menu, or type /rate-limit-options.
- [ ] After a long sleep, press Enter at "Press enter to continue".
- [ ] It stops after three automatic continuations in a row: type /rate-limit-options.
- [ ] Upgraded or bought credits in your browser on your own? The waiting session doesn't notice: send a prompt (or use /usage-credits from inside Claude Code).
- [ ] The continued task still asks for permissions, so it can stop on a prompt while you're away.
- [ ] Don't want it? /config, then turn off "Continue automatically at usage limit". The Desktop app's "Auto-continue when limits reset" is a separate checkbox.
- [ ] Signed in with an API key or a cloud provider? There is no reset to wait for: usage is billed per request.

## Can't wait?
- [ ] /usage: your plan's limits and when each one resets.
- [ ] Opus or Sonnet limit only: /model, then a model outside that family. The next reply takes in the whole conversation again.
- [ ] Usage credits (Pro, Max, Ultra): /usage-credits opens Settings, then Usage, in your browser. Turn them on, add credits and set a monthly spend limit.
- [ ] A bigger plan: claude.com/pricing (Anthropic suggests Max for Pro users who keep hitting limits, Ultra for Max users).
- [ ] An account for the Anthropic API, billed at standard API rates, apart from your plan. Monthly API credits included with Max or Ultra can't be used in Claude Code.

## The mistake
- [ ] Switching models doesn't fix a session or weekly limit: they're shared across all models.

## Check it worked
- [ ] "Usage limit reset · Continuing automatically" appears in the conversation, or /usage shows the session refilled.
- [ ] Send a short message: Claude answers.

## Next time
- [ ] /usage on a paid plan shows what's been using your limit, with suggested changes (press d or w for the last day or week; figures are rough and from this computer only).
- [ ] Still stuck? Check /status shows the account you expect, then /feedback inside Claude Code, or github.com/anthropics/claude-code/issues

Docs: code.claude.com/docs/en/errors and code.claude.com/docs/en/interactive-mode
```
