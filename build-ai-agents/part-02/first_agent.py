# first_agent.py: a first, safe agent with the Claude Agent SDK (claude-agent-sdk 0.2.182)
# Written for this video from the docs' quickstart, approvals and custom-tool patterns. Not run.
# Test folder only. Needs ANTHROPIC_API_KEY set in this terminal (never in this file).
import asyncio
import warnings
from typing import Any

from claude_agent_sdk import (
    query,
    tool,
    create_sdk_mcp_server,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    CanUseToolShadowedWarning,
)
from claude_agent_sdk.types import (
    HookMatcher,
    PermissionResultAllow,
    PermissionResultDeny,
    ToolPermissionContext,
)


# A pretend tool: fixed made-up data, no network, nothing written
@tool(
    "check_calendar",
    "List my free hours on a given day (made-up data for testing)",
    {"day": str},
)
async def check_calendar(args: dict[str, Any]) -> dict[str, Any]:
    free = f"Free on {args['day']}: 2pm to 3pm and 4pm to 5pm (made-up data)"
    return {"content": [{"type": "text", "text": free}]}


calendar_server = create_sdk_mcp_server(
    name="calendar", version="1.0.0", tools=[check_calendar]
)

# The SDK warns about every allowed_tools entry that skips can_use_tool. The calendar skips it
# on purpose, so hide only that exact warning: add any other tool there and you'll still be warned.
warnings.filterwarnings(
    "ignore",
    message=r"can_use_tool will not be invoked for: mcp__calendar__check_calendar\.",
    category=CanUseToolShadowedWarning,
)


# Ask first: every call that needs approval stops here for a y or n
async def can_use_tool(
    tool_name: str, input_data: dict, context: ToolPermissionContext
) -> PermissionResultAllow | PermissionResultDeny:
    print(f"\nApproval needed: {tool_name}")
    print(f"Input: {input_data}")
    if input("Allow this action? (y/n): ").strip().lower() == "y":
        return PermissionResultAllow(updated_input=input_data)
    return PermissionResultDeny(message="User denied this action")


# From the docs' approvals page ("Required workaround: dummy hook keeps the stream open for
# can_use_tool"). In 0.2.182 the SDK also keeps the stream open by itself, so this is harmless.
async def dummy_hook(input_data, tool_use_id, context):
    return {"continue_": True}


# The prompt goes in as a stream, as the docs' approvals example does
async def prompt_stream():
    yield {
        "type": "user",
        "message": {
            "role": "user",
            "content": "Check my calendar for Tuesday and save one free hour to notes.txt in this folder.",
        },
    }


async def main():
    options = ClaudeAgentOptions(
        model="claude-sonnet-5-5",  # today's Sonnet; the quickstart names no model
        tools=["Read", "Write"],  # the only built-in tools: no shell, no web
        mcp_servers={"calendar": calendar_server},
        allowed_tools=["mcp__calendar__check_calendar"],  # harmless, so no question
        permission_mode="default",  # anything else needing approval goes to can_use_tool
        can_use_tool=can_use_tool,
        setting_sources=[],  # no Claude Code settings, allow rules or skills (see the checklist for skills)
        hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[dummy_hook])]},
        max_turns=5,  # step limit; the default is no limit
        max_budget_usd=0.50,  # spending cap in US dollars; the default is no limit
    )
    async for message in query(prompt=prompt_stream(), options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")
            # Uncomment the two lines below to see what each run cost:
            # if message.total_cost_usd is not None:
            #     print(f"Cost: ${message.total_cost_usd:.4f}")


asyncio.run(main())
