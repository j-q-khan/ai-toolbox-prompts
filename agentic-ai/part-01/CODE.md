# Full code: Agentic AI Explained: Agentic vs Generative AI vs AI Agents

The checklist from this video, written from Anthropic's engineering blog, Microsoft Learn and the Amazon Web Services "What is agentic AI?" page (checked 2026-11-21). It was written from those pages, not tested on any product.

### is-it-agentic-checklist.md
```
# Is it agentic? A five-question checklist (facts checked 2026-11-21)

To keep a copy: paste this into Notepad and save it as is-it-agentic-checklist.md, with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. For the Claude build prompt, save it into a new, empty folder.

## The three words
- Generative: the tool makes something new when you ask (text, pictures, code), then stops.
- Agent: AI that uses tools (web search, a calendar, email) and decides its own steps for a task.
- Agentic: a describing word for a system that takes a goal, plans, acts with tools and checks its own work in a loop.

## The five questions (tick each yes)
- [ ] 1. Goal: did you give it a finished result to reach, not a single request?
      Yes looks like: "Sort out a team lunch next Friday for 8 people, within our budget, with a vegetarian option."
- [ ] 2. Plan: does it write its own list of steps?
      Yes looks like: it shows or follows steps you didn't write, in an order it chose.
- [ ] 3. Tools: can it act beyond writing words?
      Yes looks like: it searches the web, checks a calendar, drafts an email or uses a file.
- [ ] 4. Check: does it look at the results and go round again when something's wrong?
      Yes looks like: the first cafe has nothing vegetarian, so it crosses it off and searches again.
- [ ] 5. Stop and ask: does it check with you before anything important, and is there a point where it stops?
      Yes looks like: "Shall I book the table and send it?" before anything goes out.

## How to score it
- Yes to 1 to 4: you're looking at something agentic.
- A no on 1 to 4: it's a generative tool or a simpler agent. That can be all you need.
- A no on 5: be careful. Give it a stopping point yourself (below).

## Give it a stopping point
Add a line like this to your request:
Ask me before you send, buy or delete anything, and stop after three tries.

## Companies use the word differently
- Anthropic calls both workflows (steps fixed in code ahead of time) and agents (the AI directs its own steps) "agentic systems".
- Amazon Web Services says agentic AI "typically builds upon multiple hyperspecialized agents".
- So ask: which steps does it choose for itself, and which were fixed in advance?

## Sources (checked 2026-11-21)
- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Microsoft Learn, AI technology overview: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/ai-overview
- Amazon Web Services, What is agentic AI?: https://aws.amazon.com/what-is/agentic-ai/
```
