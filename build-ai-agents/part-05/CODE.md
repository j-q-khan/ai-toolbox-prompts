# Full code: CrewAI Tutorial: Build a Team of AI Agents in Python

Written for this video from CrewAI's docs (crewai 1.15.41, checked 2026-11-16). Section 2 quotes three short patterns from the docs exactly. Section 3 is ours, built from the docs' Crews, Agents, Tasks, LLMs and Tool Call Hooks pages; nothing here was run. Use a test folder and a throwaway key.

### 1. setup-commands.txt
```
# 1. A new, empty test folder
mkdir my-crew
cd my-crew

# 2. A virtual environment, switched on (CrewAI 1.15.41 needs Python 3.10 to 3.13:
#    check with python --version, or python3 --version on a Mac)
# Windows (PowerShell):
py -m venv .venv
# (Several Pythons installed? py -3.12 -m venv .venv picks 3.12)
.venv\Scripts\Activate.ps1
# If PowerShell blocks Activate.ps1, run this first:
#   Set-ExecutionPolicy -Scope Process RemoteSigned
# Mac (Terminal):
python3 -m venv .venv
source .venv/bin/activate

# 3. One exact version, with the Anthropic extra (the connector to Claude)
pip install "crewai[anthropic]==1.15.41"
# Windows: if it stops with a chroma-hnswlib build error ('float.h'), the docs say to
# install Visual Studio Build Tools with "Desktop development with C++", then try again.

# 4. A throwaway API key, for this terminal window only
#    Make it at platform.claude.com, and set a monthly spend limit at
#    platform.claude.com/settings/spend-limits
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY = "your-api-key"
# Mac (Terminal):
export ANTHROPIC_API_KEY="your-api-key"

# 5. CrewAI's anonymous telemetry is on by default; this turns it off
# Windows (PowerShell):
$env:CREWAI_DISABLE_TELEMETRY = "true"
# Mac (Terminal):
export CREWAI_DISABLE_TELEMETRY=true

# 6. Run the crew
python team_crew.py

# 7. Switch the key off when you've finished (or shut the window),
#    then delete the key on platform.claude.com
# Windows (PowerShell):
Remove-Item Env:ANTHROPIC_API_KEY
# Mac (Terminal):
unset ANTHROPIC_API_KEY
```

### 2. docs-crew-pattern.py
```
# From the docs (crewai 1.15.41), three short patterns quoted exactly, for comparison only.
# They are fragments: my_agents, my_tasks and the tools are not defined here.
# The docs name an older model; our team_crew.py uses "anthropic/claude-sonnet-5-5".

# 1. docs.crewai.com/en/concepts/processes, "Assigning Processes to a Crew"
from crewai import Crew, Process

# Example: Creating a crew with a sequential process
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.sequential
)

# 2. docs.crewai.com/en/concepts/llms, Anthropic, "Basic Usage"
from crewai import LLM

llm = LLM(
    model="anthropic/claude-sonnet-4-6",
    api_key="your-api-key",  # Or set ANTHROPIC_API_KEY
    max_tokens=4096  # Required for Anthropic
)

# 3. docs.crewai.com/en/learn/tool-hooks, "Human Approval Gate"
#    (imports from the same page's "Hook Signature" block)
from crewai.hooks import on, HookAborted, InterceptionPoint, ToolCallHookContext

@on(InterceptionPoint.PRE_TOOL_CALL, tools=["send_email", "make_purchase", "delete_file"])
def require_approval(ctx: ToolCallHookContext) -> None:
    response = ctx.request_human_input(
        prompt=f"Approve {ctx.tool_name}?",
        default_message=f"Input: {ctx.tool_input}\nType 'yes' to approve:",
    )
    if response.lower() != 'yes':
        raise HookAborted(reason="denied by operator", source="approval-gate")
```

### 3. team_crew.py
```
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
```

### 4. example-output.txt
```
Example output (not run; your wording will differ)

Approve send_invite?
Input: {'to': 'sam@example.com', 'time': 'Tuesday 2pm to 3pm'}
Type 'yes' to approve:
yes

Processing your input...
[pretend] Invite to sam@example.com for Tuesday 2pm to 3pm (nothing was sent)
Crew: Invite sent to sam@example.com for Tuesday 2pm to 3pm.

Example output with anything but yes (not run):

Approve send_invite?
Input: {'to': 'sam@example.com', 'time': 'Tuesday 2pm to 3pm'}
Type 'yes' to approve:
no

Processing your input...
Crew: The invite wasn't sent: the send_invite tool was blocked.

Example output with max_iter=1 and verbose=True on the planner (not run; trimmed):

Maximum iterations reached. Requesting final answer.
```

### 5. safety-checklist.md
```
# First CrewAI crew: safety checklist (facts checked 2026-11-16)

## Before you run it
- [ ] A new, empty test folder, so the venv, the package and the file stay in one throwaway place.
- [ ] Python 3.10 to 3.13 (CrewAI 1.15.41 on PyPI: >=3.10, <3.14).
- [ ] A virtual environment, switched on: you see (.venv) before your prompt.
- [ ] One exact version, with the Anthropic extra: pip install "crewai[anthropic]==1.15.41"
- [ ] A throwaway API key with a monthly spend limit (platform.claude.com/settings/spend-limits).
- [ ] The key in ANTHROPIC_API_KEY for this terminal only. Never in a script, a prompt or a file you might share.
- [ ] Telemetry off if you'd rather: CREWAI_DISABLE_TELEMETRY=true. The docs: "We do collect Tool's names and Agent's roles", and no personal data by default.

## In the code
- [ ] llm= on every agent. An agent without one falls back to an OpenAI model and needs an OpenAI key.
- [ ] No temperature, top_p or top_k with claude-sonnet-5-5: Anthropic says they return a 400 error.
- [ ] max_iter set small on every agent (ours: 5). The docs say the default is 20; the code at 1.15.41 sets 25.
- [ ] max_execution_time set on agents that don't ask you anything (ours: the planner, 120 seconds). The default is none. It's a wall-clock limit on the whole task, and when it runs out the task stops with a timeout error, so on an agent whose tool asks for approval it would count your time answering. max_rpm is also none unless you set it; a crew-level max_rpm overrides the agents'.
- [ ] A PRE_TOOL_CALL hook that asks first, listing every tool that writes, sends or spends.
- [ ] Tool names in snake_case (send_invite), so the hook's tools= list matches them.
- [ ] Pretend tools only while you learn: no real email, calendar, files or payments.
- [ ] No memory=True for now: its embedder defaults to OpenAI.
- [ ] tracing=False on the Crew, so nothing goes to CrewAI AMP.
- [ ] No code execution: allow_code_execution is deprecated and CodeInterpreterTool has been removed.

## Check it worked
- [ ] Answer anything but yes at the question: the tool is blocked and nothing is "sent".
- [ ] Set the planner's max_iter=1 and verbose=True: you'll see "Maximum iterations reached. Requesting final answer." Then set it back to 5 and verbose off.

## Switching asking off
- [ ] Only for a harmless tool: leave it out of the hook's tools= list. Keep anything that writes, sends or spends in it.
- [ ] Human input on a Task (human_input=True) reviews the agent's final answer, after its tools have run. It doesn't stop a send.

## When you've finished
- [ ] Shut the terminal, or Remove-Item Env:ANTHROPIC_API_KEY (Windows) / unset ANTHROPIC_API_KEY (Mac).
- [ ] Delete the throwaway key on platform.claude.com.

## Licence
- CrewAI is MIT ("Copyright (c) 2025 crewAI, Inc."). You pay only for the model calls. CrewAI's hosted platform (AMP) is optional; its Basic plan was free with 50 workflow executions a month when checked on 2026-11-16.

Sources: docs.crewai.com/en/concepts/agents ; docs.crewai.com/en/concepts/tasks ; docs.crewai.com/en/concepts/llms ; docs.crewai.com/en/learn/tool-hooks ; docs.crewai.com/en/telemetry ; pypi.org/pypi/crewai/json ; platform.claude.com/docs/en/models/sonnet-5-5/overview
```
