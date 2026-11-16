# team_crew.py: a first, safe two-agent crew (crewai 1.15.41)
# Written for this video from CrewAI's docs (Crews, Agents, Tasks, LLMs, Tool Call Hooks). Not run.
# Test folder only. Needs ANTHROPIC_API_KEY set in this terminal (never in this file).
from crewai import Agent, Crew, LLM, Process, Task
from crewai.hooks import HookAborted, InterceptionPoint, ToolCallHookContext, on
from crewai.tools import tool

# Today's Sonnet. The docs show "anthropic/claude-sonnet-4-6".
# No temperature: Anthropic's Sonnet 5.5 page says setting it returns a 400 error.
llm = LLM(model="anthropic/claude-sonnet-5-5", max_tokens=4096)


# A harmless pretend tool: made-up data, no network, nothing written
@tool("check_calendar")
def check_calendar(day: str) -> str:
    """List my free hours on a given day (made-up data for testing)."""
    return f"Free on {day}: 2pm to 3pm and 4pm to 5pm (made-up data)"


# A pretend tool that "sends": the hook below asks first, and even on yes it only prints
@tool("send_invite")
def send_invite(to: str, time: str) -> str:
    """Send a meeting invite (pretend: nothing is sent)."""
    print(f"[pretend] Invite to {to} for {time} (nothing was sent)")
    return f"Invite sent to {to} for {time} (pretend)"


# Ask first: the docs' Human Approval Gate, on the tool that sends.
# Add every tool that writes, sends or spends to this list.
@on(InterceptionPoint.PRE_TOOL_CALL, tools=["send_invite"])
def require_approval(ctx: ToolCallHookContext) -> None:
    response = ctx.request_human_input(
        prompt=f"Approve {ctx.tool_name}?",
        default_message=f"Input: {ctx.tool_input}\nType 'yes' to approve:",
    )
    if response.lower() != "yes":
        raise HookAborted(reason="denied by operator", source="approval-gate")


planner = Agent(
    role="Calendar Planner",
    goal="Find one free hour on the day I ask for",
    backstory="You check calendars carefully and never guess a time.",
    tools=[check_calendar],
    llm=llm,  # every agent needs it, or it falls back to an OpenAI model
    max_iter=5,  # step limit (the docs say the default is 20; the code sets 25)
    max_execution_time=120,  # seconds (default: none)
)

sender = Agent(
    role="Invite Sender",
    goal="Send one meeting invite for the hour the planner found",
    backstory="You write short, clear invites and send only what you're asked to.",
    tools=[send_invite],
    llm=llm,
    max_iter=5,
    # No max_execution_time here: its clock would include the time you take to answer the approval
)

find_hour = Task(
    description="Check my calendar for {day} and pick one free hour.",
    expected_output="One free hour on {day}, like 'Tuesday 2pm to 3pm'.",
    agent=planner,
)

send = Task(
    description=(
        "Send {email} an invite for the free hour the planner picked. "
        "If the tool is blocked, don't try again: say it wasn't sent."
    ),
    expected_output="One line saying whether the invite was sent.",
    agent=sender,
    context=[find_hour],  # the planner's answer is passed along to this task
)

crew = Crew(
    agents=[planner, sender],
    tasks=[find_hour, send],
    process=Process.sequential,  # one task after another, in this order
    tracing=False,  # no CrewAI AMP tracing
    # output_log_file=True,  # bonus: saves a log of each run as logs.txt in this folder
)

result = crew.kickoff(inputs={"day": "Tuesday", "email": "sam@example.com"})
print(f"Crew: {result.raw}")
