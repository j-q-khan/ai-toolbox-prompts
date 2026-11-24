# Agent-loop checklist (facts checked 2026-11-24)
# From the video "LLM Agents Explained: How an LLM Becomes an Autonomous Agent". Written by us.
# Use it to size up any agent before you let it act: one you try, one you're sold, or one you build.
# Settings and defaults change. Everything below is as written when checked, on 2026-11-24. Check each page again on your day.

## 1. The loop
- [ ] Which tools can it ask for? List them.
- [ ] Which of those only look (list, open, search), and which write, send or spend?
- [ ] What ends the loop? A plain answer with no tool request ("until it produces a response with no tool calls", code.claude.com/docs/en/agent-sdk/agent-loop).
- [ ] Is there a turn cap? (Claude Agent SDK: max_turns / maxTurns, default "No limit". OpenAI Agents SDK: max_turns, raises MaxTurnsExceeded.)
- [ ] Is there a spending cap? (Claude Agent SDK: max_budget_usd / maxBudgetUsd, default "No limit". Its docs: "Setting a budget is a good default for production agents.")

## 2. The three parts (Lilian Weng, "LLM Powered Autonomous Agents", Lil'Log, June 23, 2023)
- [ ] Planning: does it show its plan as steps before it acts? If not, ask for one (section 5).
- [ ] Short-term memory: what's in its context window right now? Long tool results fill it fast.
- [ ] Long-term memory: does it keep anything between chats? Where, and can you see and delete it?
- [ ] Tool use: what does it need that the model's training can't know (today's facts, your files, running code)?

## 3. The brakes
- [ ] Does anything that writes, sends or spends wait for your yes? (Claude Code: "permissions control what Claude can do without asking". OpenAI Agents SDK: human-in-the-loop can "pause agent execution until a person approves or rejects sensitive tool calls".)
- [ ] Which permission mode does it start in? (Claude Code: Manual "asks before file edits and shell commands"; Auto, the starting mode from v2.1.283 when checked, has "a classifier" review most actions "instead of asking you". Shift+Tab switches modes.)
- [ ] What happens when you say no? (Claude Agent SDK: "Claude receives a rejection message as the tool result and typically attempts a different approach or reports that it couldn't proceed.")
- [ ] What can be undone? Claude Code's checkpoints undo file changes, but "Actions that affect remote systems (databases, APIs, deployments) can't be checkpointed." An email or a payment can't be taken back.

## 4. Where it goes wrong (watch for these)
- [ ] Memory: the context window is finite, so history, instructions and tool results compete for room (Weng 2023, her "Challenges" section).
- [ ] Planning: models find it hard to change a plan when something unexpected goes wrong (Weng 2023). Is it repeating the same request?
- [ ] Tools: models can get the format of a request wrong (Weng 2023). Did a tool request fail to run?
- [ ] Loops: agents "might find themselves repeatedly calling the same tools, causing infinite feedback loops" (IBM, ibm.com/think/topics/ai-agents).

## 5. Do you need an agent at all?
- [ ] Could one well-built request do it? Anthropic: "For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough." (Building effective agents, Dec 19, 2024)
- [ ] Do you trust it with this job? Anthropic: "you must have some level of trust in its decision-making." Start where a wrong step is cheap to undo.
- [ ] The line to type first, in any agent:
      Before you do anything, show me your plan as numbered steps and wait for my OK.

## Sources (checked 2026-11-24)
- https://lilianweng.github.io/posts/2023-06-23-agent/
- https://www.anthropic.com/engineering/building-effective-agents
- https://code.claude.com/docs/en/how-claude-code-works
- https://code.claude.com/docs/en/agent-sdk/agent-loop
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://www.ibm.com/think/topics/ai-agents
