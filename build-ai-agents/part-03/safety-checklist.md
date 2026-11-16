# First LangGraph agent: safety checklist (facts checked 2026-11-16)

## Before you run it
- [ ] A new, empty test folder, so the venv, the packages and the file stay in one throwaway place.
- [ ] Python 3.11 or later (LangGraph alone needs 3.10, but langchain 1.5.0 needs 3.11).
- [ ] A virtual environment, switched on: you see (.venv) before your prompt.
- [ ] Exact versions: pip install langgraph==1.2.22 langchain==1.5.0 langchain-anthropic==1.7.10
- [ ] A throwaway API key with a monthly spend limit (platform.claude.com/settings/spend-limits).
- [ ] The key in ANTHROPIC_API_KEY for this terminal only. Never in a script, a prompt or a file you might share.

## In the code
- [ ] recursion_limit set small (ours: 10). Default: 10,007 super-steps from langgraph 1.1.4 (it was 25 up to 1.0.5).
- [ ] recursion_limit at the top level of the config, beside configurable, never inside it.
- [ ] GraphRecursionError caught, so hitting the limit prints a plain message.
- [ ] interrupt() first in every tool that writes, sends or spends. Nothing that acts goes above it: the node starts again from the top when the graph carries on.
- [ ] A checkpointer (InMemorySaver for a test) and a thread_id, both required for interrupts.
- [ ] The same config (same thread_id) when you carry on with Command(resume=True or False).
- [ ] Pretend tools only while you learn: no real email, calendar, files or payments.
- [ ] LangSmith tracing is optional and stays off unless you set LANGSMITH_TRACING=true.

## Check it worked
- [ ] Type n at the question: the tool returns "Invite cancelled by user" and nothing goes out.
- [ ] Set "recursion_limit": 2: the run prints "Stopped: hit the step limit (recursion_limit)". Then set it back to 10.

## Switching asking off
- [ ] Only for a harmless tool: take its interrupt() out. Keep it in anything that writes, sends or spends.

## When you've finished
- [ ] Shut the terminal, or Remove-Item Env:ANTHROPIC_API_KEY (Windows) / unset ANTHROPIC_API_KEY (Mac).
- [ ] Delete the throwaway key on platform.claude.com.

## Licence
- LangGraph is MIT ("Copyright (c) 2024 LangChain, Inc."). You pay only for the model calls.

Sources: docs.langchain.com/oss/python/langgraph/quickstart ; docs.langchain.com/oss/python/langgraph/graph-api ; docs.langchain.com/oss/python/langgraph/interrupts ; docs.langchain.com/oss/python/langgraph/graph-api-control-flow ; pypi.org/pypi/langchain/json
