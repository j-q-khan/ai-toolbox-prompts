# Full code: Claude Code Context Limit Reached: Compact, Clear and Fix Slow Long Sessions

A context limit checklist written for this video from Anthropic's Claude Code docs (checked 2026-11-15, Claude Code 2.1.325). Messages and commands are as the docs gave them that day; check the linked page if one looks different.

### 1. claude-code-context-limit-checklist.md
```
# Claude Code "Context limit reached": checklist (from Anthropic's docs, checked 2026-11-15)

## Which message?
- Context limit reached · /compact or /clear to continue
  The conversation plus attached files exceeds the model's context window.
  In -p output and the transcript it reads:  Prompt is too long
- Context limit reached · /compact or /clear to continue · auto-compact is off · /config to turn it on
  You turned auto-compact off. Turn Auto-compact back on in /config,
  or run /compact yourself before the window fills. (No hint before v2.1.235.)
- Context limit reached · /clear to continue
  DISABLE_COMPACT is set, so only /clear is offered.
- Prompt is too long · automatic compaction failed: <the underlying error>
  Fix the named error first; /compact fails on the same error until you do.
- Prompt is too long · this conversation is a single exchange and cannot be compacted ...
  One prompt (or the system prompt, tools and attachments) fills the window. /clear and start with less.
- Autocompact is thrashing: the context refilled to the limit...
  Compaction worked, but a file or tool output refilled the window several times in a row.
- Not enough messages to compact.
  A single exchange has nothing earlier to summarize. /clear, then send it again with less pasted text.
- API Error: Usage credits required for 1M context · run /usage-credits to turn them on (they take effect after you restart Claude Code), or /model to switch to standard context
  An entitlement check, not a used-up quota. Mid-conversation, Claude Code compacts on its own.
  If you selected a [1m] model yourself: /model, then the variant without [1m].

## Fix it
- [ ] Mid-task:  /compact   (replaces the conversation with a summary)
- [ ] Choose what the summary keeps:  /compact focus on the auth bug fix
- [ ] Switching to unrelated work:  /clear
- [ ] Summarize only part of it:  /rewind, pick a message, then Summarize from here or Summarize up to here
- [ ] Compact earlier:  /autocompact 500k   (sets how full the window gets before the automatic pass)

## "Autocompact is thrashing": Anthropic's four steps
- [ ] 1. Ask Claude to open the big file in smaller chunks: a line range or one function, not the whole file
- [ ] 2. /compact keep only the plan and the diff
- [ ] 3. Move the big-file work to a subagent (its own context window; its requests count toward the same usage limits)
- [ ] 4. /clear if you don't need the earlier conversation

## Check it worked
- [ ] /context   (what fills the window: system prompt, system tools, MCP tools, memory files, skills, messages)
- [ ] Error back after /clear? Compare Messages with the categories above it:
      Messages largest: a file or tool output is refilling the window. Go back to steps 1 to 3.
      The rest larger: what loads at startup leaves too little room. Trim CLAUDE.md,
      move instructions into path-scoped rules, turn off unused MCP servers:  /mcp disable <name>

## Slow or frozen
- [ ] One slow turn after /model, or after a long break: the prompt cache is rebuilding.
      (Cache lifetime: one hour for the main conversation on a Claude subscription within plan usage,
      five minutes on usage credits, an API key or a cloud provider.)
- [ ] Edited CLAUDE.md mid-session? It applies after /clear, /compact or a restart.
- [ ] Frozen: Ctrl+C. Still frozen: shut the terminal and restart. Restarting doesn't lose your conversation:
      claude --continue   (most recent conversation in this folder)
      claude --resume     (the troubleshooting page's command, run in the same folder)
- [ ] High memory: /compact regularly, restart between major tasks.

## Still stuck?
- [ ] /feedback inside Claude Code, or search or open an issue with your version and the full message:
      github.com/anthropics/claude-code/issues

Docs: code.claude.com/docs/en/errors (Prompt is too long; Usage credits required for 1M context), code.claude.com/docs/en/troubleshooting (Auto-compaction stops with a thrashing error; Command hangs or freezes; High CPU or memory usage), code.claude.com/docs/en/context-window, code.claude.com/docs/en/prompt-caching, code.claude.com/docs/en/debug-your-config, code.claude.com/docs/en/cli-reference.
```
