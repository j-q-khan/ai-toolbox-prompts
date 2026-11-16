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
