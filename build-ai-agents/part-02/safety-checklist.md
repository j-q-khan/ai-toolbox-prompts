# First Claude Agent SDK agent: safety checklist (facts checked 2026-11-16)

## Before you run it
- [ ] A new, empty test folder. The agent can reach files in the folder you start it from and the folders below it.
- [ ] A virtual environment, switched on: you see (.venv) before your prompt.
- [ ] One exact version: pip install claude-agent-sdk==0.2.182 (Python 3.10 or later).
- [ ] A throwaway API key with a monthly spend limit (platform.claude.com/settings/spend-limits).
- [ ] The key in ANTHROPIC_API_KEY for this terminal only. Never in a script, a prompt or a file you might share.

## In the code
- [ ] max_turns set small. Default: no limit. Count one extra turn for the final answer.
- [ ] max_budget_usd set small. Default: no limit. It can go a little over, so leave room.
- [ ] permission_mode="default" with a can_use_tool callback. No callback means deny.
- [ ] allowed_tools holds only harmless tools. It approves; it doesn't limit.
- [ ] tools (or disallowed_tools) limits which built-in tools exist.
- [ ] setting_sources=[] so your own Claude Code allow rules can't skip the question. (It also turns skills off. To use skills later: setting_sources=["project"], skills="all", and "Skill" added to tools. Skill calls then skip the question.)

## Check it worked
- [ ] Type n at the question: nothing is written.
- [ ] Set max_turns=1: the run ends with error_max_turns. Then set it back.

## When you've finished
- [ ] Close the terminal, or Remove-Item Env:ANTHROPIC_API_KEY (Windows) / unset ANTHROPIC_API_KEY (Mac).
- [ ] Delete the throwaway key on platform.claude.com.

## Licence and sign-in
- The GitHub repo is MIT, but use of the SDK is governed by Anthropic's Commercial Terms of Service, and the bundled Claude Code says "All rights reserved".
- Sign in with an API key. Anthropic: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."

Sources: code.claude.com/docs/en/agent-sdk/quickstart ; code.claude.com/docs/en/agent-sdk/agent-loop ; code.claude.com/docs/en/agent-sdk/python ; code.claude.com/docs/en/agent-sdk/user-input ; code.claude.com/docs/en/agent-sdk/custom-tools ; code.claude.com/docs/en/agent-sdk/overview
