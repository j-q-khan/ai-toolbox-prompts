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
