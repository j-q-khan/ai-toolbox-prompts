# Full code: Agentic Workflow Explained: Workflows vs Agents, With Real Examples

The decision sheet and template from this video, written from Anthropic's engineering blog and Microsoft Learn (checked 2026-11-21). It was written from those pages, not tested on any product.

### workflow-or-agent.md
```
# Workflow or agent? A decision sheet and a prompt-chaining template (facts checked 2026-11-21)

To keep a copy: paste this into Notepad and save it as workflow-or-agent.md, with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. For the Claude build prompt, save it into a new, empty folder.

## The one difference
- Workflow: a person fixed the steps in advance, and they run the same way every time.
- Agent: the AI model picks its own steps as it goes, towards a goal.
- Ask: who picks the steps, a person ahead of time, or the model as it goes?

## Three questions, in order
1. Does one prompt do the job? Stop there.
2. Can you write the steps down in advance? Build a workflow, and pick a pattern below.
3. Can't predict the steps? Use an agent, tested in a sandbox (a practice space where nothing real can break), with guardrails (safety checks) and a point where it asks you first.

## The five workflow patterns (Anthropic's names)
1. Prompt chaining: split the job into steps, each answer feeding the next.
   Use when: the job splits cleanly into fixed steps.
   Example: write an outline, check it, then write the newsletter from it.
2. Routing: sort what comes in by kind, and send each kind down its own path.
   Use when: there are clear categories, and the sorting can be done accurately.
   Example: customer emails sorted into general questions, refund requests and custom cake orders.
3. Parallelization: several calls on one job at the same time.
   Sectioning: independent parts side by side (one answers a message, another checks it).
   Voting: the same task several times, answers compared (ask three times if every allergen is named).
4. Orchestrator-workers: one model breaks the job down, hands out the pieces, and puts the results together.
   Use when: you can't predict the pieces in advance.
   Example: everything needed for a stall at the town fair.
5. Evaluator-optimizer: one call writes, another judges and sends notes back, in a loop.
   Use when: there are clear rules for what good looks like.
   Example: a cake description under 50 words that names every allergen.

## Before you choose an agent
- Agents suit open-ended problems where you can't predict the number of steps.
- They often trade waiting time and cost for better results.
- Anthropic warns of higher costs and mistakes that pile up, and recommends testing in a sandbox with guardrails.
- Watch out for names: Microsoft's agent flows follow a rule-based path, so they sit on the workflow side.

## Prompt-chaining template (copy, then change the words in capitals)
Goal: WRITE A SHORT MONTHLY NEWSLETTER FOR TEST BAKERY FROM THE PRACTICE NOTES.
Step 1 prompt: From the notes below, write an outline with exactly three sections: news, a new cake, and an offer. One line per section.
Gate (a check between steps): Check: does the outline have exactly three sections, news, a new cake and an offer? If not, fix the outline first.
Step 2 prompt: Using only this outline and the notes, write the newsletter in under 150 words, friendly and plain.
Step 3 prompt (optional): Check the newsletter against the notes, and list anything it says that isn't in them.

## Practice notes (made up, for trying the template)
- Test Bakery is a made-up shop.
- News: the shop now opens at 8 on Saturdays.
- New cake: a lemon and poppy seed loaf. Contains wheat, eggs and milk.
- Offer: a free coffee with any loaf, on Saturdays this month.

## Sources (checked 2026-11-21)
- Anthropic, Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Microsoft Learn, Agent flows overview: https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview
```
