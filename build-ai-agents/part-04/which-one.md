# LangChain vs LangGraph vs Deep Agents: which one when? (facts checked 2026-11-16)

All three are from LangChain, Inc., MIT licensed, and they stack:
LangGraph (runtime) -> LangChain create_agent (framework, built on LangGraph) -> Deep Agents (harness, built on create_agent).

## Pick by what you need
- LangChain create_agent: a working agent fast. One call: model + tools + system prompt. Add behaviour with middleware.
  LangChain's docs: "Getting started quickly", "Standardizing how a team builds".
- LangGraph: you draw every node and edge yourself. Fixed steps mixed with model steps, loops you control, runs that pause.
  LangChain's docs: "Low-level control", "Long running, stateful workflows and agents".
- Deep Agents: long, messy, multi-step jobs. File tools, subagents and history summaries come switched on.
  LangChain's docs: "More autonomous agents", "Agents faced with complex, non-deterministic tasks".

## Defaults to change before you run anything
| | Step limit (default) | Asking first (default: off) | Needs |
|---|---|---|---|
| LangGraph | recursion_limit (10,007 super-steps) | interrupt() inside a node, resume with Command(resume=...) | checkpointer + thread_id |
| LangChain create_agent | recursion_limit 9,999 (set in create_agent's source); ModelCallLimitMiddleware / ToolCallLimitMiddleware (no limit) | HumanInTheLoopMiddleware(interrupt_on={...}) | checkpointer + thread_id |
| Deep Agents | recursion_limit 9,999 (set in create_deep_agent's source); the same call-limit middleware works via middleware=[...] | interrupt_on={...} on create_deep_agent | checkpointer + thread_id |

## Deep Agents, out of the box
- File tools: ls, read_file, write_file, edit_file, delete (0.7+), glob, grep. Files live in the agent's state by default, not on your disk.
- execute (shell): only with sandbox backends.
- Its README: "Deep Agents follows a "trust the LLM" model. The agent can do anything its tools allow."

## Python
- langchain 1.5.0 and deepagents 0.7.39: Python 3.11 or later (PyPI). LangChain's install page still says 3.10+.
- langgraph 1.2.22: Python 3.10 or later.
- pip install langchain also installs langgraph. pip install deepagents also installs langchain, langchain-anthropic, langchain-google-genai and langsmith.

## Cost (prices as they were when checked on 2026-11-16)
- The code is free (MIT). You pay your model provider: Claude Sonnet 5.5 was $2 per million input tokens and $10 per million output (platform.claude.com/docs/en/about-claude/pricing).
- LangSmith is optional (www.langchain.com/pricing): Developer was $0, 1 seat, up to 5k base traces a month; Plus was $39 per seat per month, up to 10k base traces a month; Enterprise custom. Past those allowances it's pay-as-you-go, metered in LangChain Standard Units, LSUs ($1.00 per LSU); no per-trace price is shown.
- Tracing is switched on with LANGSMITH_TRACING=true.

Sources: docs.langchain.com/oss/python/concepts/products ; docs.langchain.com/oss/python/langchain/middleware/built-in ; docs.langchain.com/oss/python/langchain/human-in-the-loop ; docs.langchain.com/oss/python/langgraph/graph-api ; docs.langchain.com/oss/python/deepagents/overview ; github.com/langchain-ai/deepagents (README) ; pypi.org
