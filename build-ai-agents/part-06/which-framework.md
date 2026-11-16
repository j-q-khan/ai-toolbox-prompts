# Claude Agent SDK vs LangGraph vs CrewAI: which should you use? (facts checked 2026-11-16)

This channel's videos are made with Claude's help, and the Claude Agent SDK is Anthropic's,
so every line below comes from each project's own docs, source or pricing page.

## Pick by what you need
- Claude Agent SDK (claude-agent-sdk 0.2.182): Claude only, and a ready-made loop: Claude Code's loop and built-in
  file, shell and web tools as a Python library. You write a prompt and options.
- LangGraph (langgraph 1.2.22): you draw the loop yourself: nodes, edges and a shared state. Any LangChain chat model.
  LangChain's docs: "Low-level control", "Long running, stateful workflows and agents".
  Want LangGraph's engine without drawing? LangChain's create_agent runs on it in one call (Part 4).
- CrewAI (crewai 1.15.41): a team. Agents with a role, goal and backstory; tasks handed to agents; results passed along.
  Native connectors for OpenAI, Anthropic, Google, Azure, Bedrock and Snowflake; every other provider via LiteLLM.

## The four differences, and the licence
| | Claude Agent SDK | LangGraph | CrewAI |
|---|---|---|---|
| What you write | a prompt and options | every node and edge | roles and tasks |
| Models | Claude only | any LangChain chat model | many native connectors; the rest via LiteLLM |
| Step limit (default) | max_turns (no limit); max_budget_usd (no limit) | recursion_limit (10,007 super-steps) | max_iter (docs: 20; code at 1.15.41: 25) |
| When the limit hits | result subtype error_max_turns | raises GraphRecursionError | one more call for a best answer, no error |
| Asking first | permission_mode="default" + can_use_tool callback (no callback = deny) | interrupt() in a node or tool + checkpointer + thread_id | PRE_TOOL_CALL tool hook (human_input on a Task only reviews the final answer, after tools run) |
| Licence | MIT repo; use governed by Anthropic's Commercial Terms; bundled Claude Code "All rights reserved" | MIT | MIT |
| Python | 3.10+ | 3.10+ (3.11+ with langchain 1.5.0) | 3.10 to 3.13 |
| Install (pinned) | pip install claude-agent-sdk==0.2.182 (about 150 MB, bundles Claude Code) | pip install langgraph==1.2.22 langchain==1.5.0 langchain-anthropic==1.7.10 | pip install "crewai[anthropic]==1.15.41" |

## Gotchas
- Claude Agent SDK: allowed_tools approves, it doesn't limit; restrict with tools or disallowed_tools.
  Sign-in is an API key: "Unless previously approved, Anthropic does not allow third party developers to offer
  claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."
- LangGraph: recursion_limit only counts at the top level of the config, not inside configurable.
- CrewAI: give every agent llm=, or it falls back to an OpenAI model. Telemetry is on by default;
  CREWAI_DISABLE_TELEMETRY=true turns it off.
- All three: never set temperature with claude-sonnet-5-5 (Anthropic: it returns a 400 error).

## Cost (prices as they were when checked on 2026-11-16)
- The code is free (MIT). You pay your model provider: Claude Sonnet 5.5 was $2 per million input tokens and $10 per
  million output (platform.claude.com/docs/en/about-claude/pricing).
- LangSmith (optional, for LangGraph traces; www.langchain.com/pricing): Developer was $0, 1 seat, up to 5k base traces
  a month, then pay-as-you-go; Plus was $39 per seat per month. No per-trace price is shown.
- CrewAI AMP (optional; www.crewai.com/pricing): Basic was Free, 50 workflow executions a month; Enterprise custom.
  No seat price is shown.

## Left out of this series
- OpenAI Agents SDK (openai-agents 0.24.0): OpenAI's models by default; Claude only through LiteLLM or Any-LLM adapters
  its docs call "best-effort, beta"; max_turns defaults to 10 in its source (the docs state no number);
  tracing is on by default and goes to OpenAI.

## Tools from anywhere: MCP
- Claude Agent SDK: mcp_servers. LangGraph and LangChain: LangChain's MCPAdapter (langchain 1.4.0+; it turns a server's tools into LangChain tools). CrewAI: mcps=[...].

Sources: code.claude.com/docs/en/agent-sdk/overview ; code.claude.com/docs/en/agent-sdk/agent-loop ;
docs.langchain.com/oss/python/langgraph/graph-api ; docs.langchain.com/oss/python/concepts/products ;
docs.crewai.com/en/concepts/agents ; docs.crewai.com/en/concepts/tasks ; docs.crewai.com/en/learn/tool-hooks ;
docs.crewai.com/en/concepts/llms ; openai.github.io/openai-agents-python/models ; pypi.org
