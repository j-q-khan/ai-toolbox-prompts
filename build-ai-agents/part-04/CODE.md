# Full code: LangChain vs LangGraph vs Deep Agents: Which One When?

Written for this video from LangChain's docs and source (langchain 1.5.0, langgraph 1.2.22, deepagents 0.7.39, checked 2026-11-16). Section 2 quotes the docs exactly. Section 4 is ours, built from the docs' patterns; nothing here was run. Use a test folder and a throwaway key.

### 1. which-one.md
```
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
```

### 2. docs-excerpts.txt
```
Lines quoted exactly from each project's docs (checked 2026-11-16). "…" marks skipped lines.

A. LangChain create_agent: asking first and a call limit
   Two examples from docs.langchain.com/oss/python/langchain/middleware/built-in, joined (langchain 1.5.0)

middleware=[
    HumanInTheLoopMiddleware(
        interrupt_on={
            "your_send_email_tool": {
…
    ModelCallLimitMiddleware(
        thread_limit=10,
        run_limit=5,

B. LangGraph: asking first and the step limit
   From docs.langchain.com/oss/python/langgraph/interrupts and
   docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT (langgraph 1.2.22)

from langgraph.types import interrupt

def approval_node(state: State):
    # Pause and ask for approval
    approved = interrupt("Do you approve this action?")
…
graph.invoke({...}, {"recursion_limit": 1000})

C. Deep Agents: asking first
   From docs.langchain.com/oss/python/deepagents/human-in-the-loop (deepagents 0.7.39)

checkpointer = MemorySaver()

agent = create_deep_agent(
…
    interrupt_on={
        "remove_file": True,  # Default: approve, edit, reject, respond
        "fetch_file": False,  # No interrupts needed
…
    checkpointer=checkpointer,  # Required!

Defaults (docs and source, checked 2026-11-16):
- LangGraph recursion_limit: 10,007 super-steps (graph-api docs).
- create_agent and create_deep_agent: recursion_limit 9,999, set in their source
  (langchain 1.5.0 agents/factory.py; deepagents 0.7.39 graph.py). Deep Agents' docs give no number.
- ModelCallLimitMiddleware thread_limit and run_limit: "Defaults to no limit."
- Asking first: off in all three until you set it. All three need a checkpointer and a thread_id.
```

### 3. setup-commands.txt
```
# 1. A new, empty test folder
mkdir small-agent
cd small-agent

# 2. A virtual environment, switched on (Python 3.11 or later: langchain 1.5.0 needs it)
# Windows (PowerShell):
py -m venv .venv
.venv\Scripts\Activate.ps1
# Mac (Terminal):
python3 -m venv .venv
source .venv/bin/activate

# 3. Exact versions (langchain also installs langgraph)
pip install langchain==1.5.0 langchain-anthropic==1.7.10

# 4. A throwaway API key with a spend limit, for this terminal window only
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY = "your-api-key"
# Mac (Terminal):
export ANTHROPIC_API_KEY=your-api-key

# 5. Run the agent
python small_agent.py

# 6. Switch the key off when you've finished (or close the window), then delete the key
# Windows (PowerShell):
Remove-Item Env:ANTHROPIC_API_KEY
# Mac (Terminal):
unset ANTHROPIC_API_KEY
```

### 4. small_agent.py
```
# small_agent.py: a small, safe LangChain agent (langchain 1.5.0, langchain-anthropic 1.7.10)
# Written for this video from LangChain's docs (overview, built-in middleware, human-in-the-loop). Not run.
# Test folder only. Needs Python 3.11 or later and ANTHROPIC_API_KEY set in this terminal (never in this file).
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware, ModelCallLimitMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command


def check_calendar(day: str) -> str:
    """List my free hours on a given day (made-up data for testing)."""
    return f"Free on {day}: 2pm to 3pm and 4pm to 5pm (made-up data)"


def save_note(text: str) -> str:
    """Save a short note (pretend: it prints the note and writes nothing)."""
    print(f"(pretend save) {text}")
    return "Saved."


agent = create_agent(
    model="claude-sonnet-5-5",  # today's Sonnet; the docs show claude-sonnet-4-6
    tools=[check_calendar, save_note],
    system_prompt="You are a helpful assistant",
    checkpointer=InMemorySaver(),  # asking first needs a checkpointer
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "save_note": {"allowed_decisions": ["approve", "reject"]},  # ask first
                "check_calendar": False,  # harmless, so no question
            }
        ),
        ModelCallLimitMiddleware(thread_limit=5, exit_behavior="end"),  # step limit; default: no limit
    ],
)

config = {"configurable": {"thread_id": "test-1"}}  # the same thread_id resumes the paused run
request = "Check my calendar for Tuesday and save one free hour as a note."
result = agent.invoke(
    {"messages": [{"role": "user", "content": request}]}, config=config, version="v2"
)

# Ask first: one decision per paused tool call, in the same order
while result.interrupts:
    decisions = []
    for action in result.interrupts[0].value["action_requests"]:
        print(f"\nApproval needed: {action['name']} {action['args']}")
        if input("Allow this action? (y/n): ").strip().lower() == "y":
            decisions.append({"type": "approve"})
        else:
            decisions.append({"type": "reject", "message": "The user said no. Do not retry."})
    result = agent.invoke(Command(resume={"decisions": decisions}), config=config, version="v2")

print(result.value["messages"][-1].text)
```

### 5. example-output.txt
```
Example output (not run; your wording will differ)

Approval needed: save_note {'text': 'Tuesday: 2pm to 3pm'}
Allow this action? (y/n): y
(pretend save) Tuesday: 2pm to 3pm
I've saved Tuesday's free hour, 2pm to 3pm, as a note.

With thread_limit=1, the run stops after the first model call and ends with:
Model call limits exceeded: thread limit (1/1)
```
