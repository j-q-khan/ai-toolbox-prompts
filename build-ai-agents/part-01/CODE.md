# Full code: AI Agents for Beginners: What Makes an AI an Agent?

A cheat sheet and the pseudo-code loop written for this video from Anthropic's agent-loop docs and the frameworks' own docs (checked 2026-11-16). The pseudo-code is not any real framework's code and isn't meant to run; Part 2 builds a real agent.

### 1. agent-loop-pseudocode.txt
```
for step in range(10):
    reply = ask_model(task, results)
    if reply.wants_no_tool:
        break
    if reply.tool.writes_sends_or_spends and not you_say_yes():
        break
    results.add(run_tool(reply.tool))
```

### 2. agent-cheat-sheet.md
```
# What makes an AI an agent: cheat sheet (facts checked 2026-11-16)

## Four words
- Model: the trained AI that takes in your words and writes back. On its own it only writes text.
- Tool: a small piece of code the model is allowed to ask for (check a calendar, send an email). The model only asks; your program runs the tool and hands the result back.
- Agent: a model that can ask for tools, in a loop, choosing its next step until the job is done.
- Step limit: the most times the loop may go round before it has to stop.

## The loop
1. The model looks at the task and the results so far, and decides.
2. It asks for a tool, or answers with no tool request.
3. Your program runs the tool and passes the result back.
4. Repeat. No tool requested means finished.

## Two safety rules
- [ ] Set a small step limit yourself. Defaults when checked: Claude Agent SDK max_turns, no limit; LangGraph recursion_limit, 10,007 super-steps; CrewAI max_iter, 20 (then it must give its best answer).
- [ ] Ask first (human in the loop) before anything that writes, sends or spends. Switch it off only for harmless jobs.

## Workflow or agent?
- Workflow: a fixed path a person set in advance. Easier to predict.
- Agent: the model picks each next step from what happened last.
- Same steps every time? A workflow may be all you need.

## Before your first tool
- [ ] A plain name and a one-line description of what it does and when to use it. That description is all the model goes on.

Sources: code.claude.com/docs/en/agent-sdk/agent-loop ; anthropic.com/engineering/building-effective-agents ; docs.langchain.com/oss/python/langgraph/graph-api ; docs.crewai.com/en/concepts/agents
```
