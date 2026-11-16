# Full code: LangGraph Tutorial for Beginners: Your First Agent Graph

Written for this video from LangGraph's docs (langgraph 1.2.22, langchain 1.5.0, langchain-anthropic 1.7.10, checked 2026-11-16). Section 2 is the docs' quickstart Full code example, quoted exactly. Section 3 is ours, built from the docs' quickstart and interrupts patterns; nothing here was run. Use a test folder and a throwaway key.

### 1. setup-commands.txt
```
# 1. A new, empty test folder
mkdir my-graph
cd my-graph

# 2. A virtual environment, switched on (needs Python 3.11 or later:
#    check with python --version, or python3 --version on a Mac)
# Windows (PowerShell):
py -m venv .venv
# (Several Pythons installed? py -3.11 -m venv .venv picks 3.11)
.venv\Scripts\Activate.ps1
# If PowerShell blocks Activate.ps1, run this first:
#   Set-ExecutionPolicy -Scope Process RemoteSigned
# Mac (Terminal):
python3 -m venv .venv
source .venv/bin/activate

# 3. The quickstart's three packages, one exact version each
pip install langgraph==1.2.22 langchain==1.5.0 langchain-anthropic==1.7.10

# 4. A throwaway API key, for this terminal window only
#    Make it at platform.claude.com, and set a monthly spend limit at
#    platform.claude.com/settings/spend-limits
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY = "your-api-key"
# Mac (Terminal):
export ANTHROPIC_API_KEY="your-api-key"

# 5. Run the agent
python first_graph.py

# 6. Switch the key off when you've finished (or shut the window),
#    then delete the key on platform.claude.com
# Windows (PowerShell):
Remove-Item Env:ANTHROPIC_API_KEY
# Mac (Terminal):
unset ANTHROPIC_API_KEY
```

### 2. docs-quickstart-graph.py
```
# From the docs: docs.langchain.com/oss/python/langgraph/quickstart, Full code example (langgraph 1.2.22)
# Shown for comparison only. It sets no step limit, never asks first, and names an older model.
# If you swap in "claude-sonnet-5-5", delete temperature=0 too: langchain-anthropic refuses it for that model.
# Step 2: Define tools and model

from langchain.tools import tool
from langchain.chat_models import init_chat_model


model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)


# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b


@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b


# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

# Step 3: Define state

from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int

# Step 4: Define model node
from langchain.messages import SystemMessage


def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }


# Step 5: Define tool node

from langchain.messages import ToolMessage


def tool_node(state: MessagesState):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

# Step 6: Define end logic

from typing import Literal
from langgraph.graph import StateGraph, START, END


# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END

# Step 7: Build and compile the agent

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()


# Step 8: Set up LangSmith tracing (optional)
# export LANGSMITH_TRACING=true
# export LANGSMITH_API_KEY="your-langsmith-api-key"

# Step 9: Run the agent
from langchain.messages import HumanMessage
messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

### 3. first_graph.py
```
# first_graph.py: a first, safe LangGraph agent (langgraph 1.2.22, langchain 1.5.0, langchain-anthropic 1.7.10)
# Written for this video from the LangGraph quickstart and interrupts docs. Not run.
# Test folder only. Needs ANTHROPIC_API_KEY set in this terminal (never in this file).
import operator
from typing import Literal

from typing_extensions import TypedDict, Annotated
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from langchain.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command, interrupt
from langgraph.errors import GraphRecursionError

# Today's Sonnet. The docs show "claude-sonnet-4-6" with temperature=0; leave temperature out,
# because langchain-anthropic 1.7.10 refuses a non-default temperature for Sonnet 5.5
model = init_chat_model("claude-sonnet-5-5")


# A harmless pretend tool: made-up data, no network, nothing written
@tool
def check_calendar(day: str) -> str:
    """List my free hours on a given day (made-up data for testing)."""
    print("Tool: check_calendar")
    return f"Free on {day}: 2pm to 3pm and 4pm to 5pm (made-up data)"


# A pretend tool that "sends": it asks first, and even on yes it only prints
@tool
def send_invite(to: str, time: str) -> str:
    """Send a meeting invite (pretend: nothing is sent)."""
    # Ask first: this pauses the whole graph until you answer.
    # Nothing that sends or writes goes above this line: the node starts again from the top.
    approved = interrupt(
        {"message": "Approve sending this invite?", "to": to, "time": time}
    )
    if approved:
        print(f"[pretend] Invite to {to} for {time} (nothing was sent)")
        return f"Invite sent to {to} for {time} (pretend)"
    return "Invite cancelled by user"


tools = [check_calendar, send_invite]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)


# State: the shared notepad every node can see and add to
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int


# Model node: Claude decides whether to call a tool
def llm_call(state: MessagesState):
    return {
        "messages": [
            model_with_tools.invoke(
                [SystemMessage(content="You help me plan meetings. Use the tools.")]
                + state["messages"]
            )
        ],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


# Tools node: runs each tool Claude asked for
def tool_node(state: MessagesState):
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}


# Conditional edge: a tool call goes to the tools node, otherwise the graph ends
def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    if state["messages"][-1].tool_calls:
        return "tool_node"
    return END


# The graph: model node, tools node, and the edges between them
agent_builder = StateGraph(MessagesState)
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges("llm_call", should_continue, ["tool_node", END])
agent_builder.add_edge("tool_node", "llm_call")
# The checkpointer saves state at each step, so a pause can carry on
agent = agent_builder.compile(checkpointer=InMemorySaver())

config = {
    "configurable": {"thread_id": "test-1"},  # names this run, so the pause carries on from its save
    "recursion_limit": 10,  # step limit: top level, not inside configurable (default 10,007)
}
# Wrong: inside configurable it doesn't count, and the 10,007 default stays:
# config = {"configurable": {"thread_id": "test-1", "recursion_limit": 10}}

question = "Check my calendar for Tuesday, then send sam@example.com an invite for one free hour."

try:
    result = agent.invoke({"messages": [HumanMessage(content=question)]}, config)
    while "__interrupt__" in result:  # the graph paused at an interrupt
        details = result["__interrupt__"][0].value
        print(f"{details['message']} To {details['to']}, {details['time']}")
        approved = input("Allow this action? (y/n): ").strip().lower() == "y"
        result = agent.invoke(Command(resume=approved), config)  # same config, same thread
    print(f"Claude: {result['messages'][-1].text}")
    print(f"Model calls: {result['llm_calls']}")
except GraphRecursionError:
    print("Stopped: hit the step limit (recursion_limit)")

# Bonus: print the graph you drew as Mermaid text, then paste it into any Mermaid viewer
# print(agent.get_graph().draw_mermaid())
```

### 4. example-output.txt
```
Example output (not run; your wording will differ)

Tool: check_calendar
Approve sending this invite? To sam@example.com, Tuesday 2pm to 3pm
Allow this action? (y/n): y
[pretend] Invite to sam@example.com for Tuesday 2pm to 3pm (nothing was sent)
Claude: Tuesday 2pm to 3pm was free, so I sent Sam an invite for then (pretend).
Model calls: 3

Example output with n at the question (not run):

Tool: check_calendar
Approve sending this invite? To sam@example.com, Tuesday 2pm to 3pm
Allow this action? (y/n): n
Claude: I didn't send the invite, because you cancelled it.
Model calls: 3

Example output with "recursion_limit": 2 (not run; a line or two may print first):

Stopped: hit the step limit (recursion_limit)
```

### 5. safety-checklist.md
```
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
```
