# Which Claude agent fits you? (facts checked 2026-11-24 from Anthropic's docs)
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## 1. Do you work on code, in Claude Code?
- [ ] No, I don't write code: go to 3 (Cowork).
- [ ] I'm building an agent into my own app: go to 4.
- [ ] Yes, and it's one side job (search a big folder, review some files): a SUBAGENT.
      Anthropic: subagents are for "quick, focused workers that report back".
      Each runs "in its own context window", and its requests "count toward the same usage limits as your main conversation".
- [ ] Yes, and several helpers need to share findings and challenge each other: an AGENT TEAM (go to 2).

## 2. Before you try an agent team
- [ ] Agent teams "are experimental and disabled by default".
- [ ] They cost more: "each teammate is a separate Claude instance".
- [ ] "For routine tasks, a single session is more cost-effective."
- [ ] Try them only in a scratch folder with a throwaway repo first (Part 3 of this series).

## 3. You don't write code: COWORK
- [ ] Cowork is "built for non-coding knowledge work".
- [ ] "Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them." You don't build these agents.
- [ ] Paid plans only (Pro, Max, Ultra, Team, and Enterprise). "agentic tasks consume more capacity than regular chat".
- [ ] Start: find the message box and select "Cowork". No Chat or Cowork choice? You have the new Claude experience: any conversation can take on a Cowork task.

## 4. You're building your own app
- [ ] The AGENT SDK: "the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript", in a process you operate. You set an API key: keep it private.
- [ ] MANAGED AGENTS: Anthropic hosts the agent, "configured through the Claude API". It "is in beta".

## 5. The habit that burns usage fastest
- [ ] A team on a routine job. Start with one session, add a subagent when the chat gets cluttered, try a team for research, review or new features.

## The sample subagent (file 2)
- [ ] Save file 2 as code-reviewer.md inside a .claude/agents/ folder in your scratch folder. It is Anthropic's own example: its tools line lists only Read, Glob and Grep, so it can look at files but not change them. Part 2 of this series walks through it.
- [ ] Try it by typing: Use the code-reviewer agent to look over this folder and tell me what you'd improve.

## Plans (check before you start; prices change)
- [ ] Pro was $20 a month billed monthly ($17 a month billed yearly) when checked 2026-11-24, and includes Claude Code. https://claude.com/pricing

Sources: code.claude.com/docs/en/sub-agents ; code.claude.com/docs/en/agent-teams ; claude.com/product/cowork ; support.claude.com/en/articles/13345190 ; code.claude.com/docs/en/agent-sdk/overview ; platform.claude.com/docs/en/managed-agents/overview ; claude.com/pricing
