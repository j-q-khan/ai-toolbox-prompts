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
