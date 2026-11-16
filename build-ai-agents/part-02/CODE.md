# Full code: Claude Agent SDK Python Tutorial: Build Your First Agent

Written for this video from Anthropic's Agent SDK docs (claude-agent-sdk 0.2.182, checked 2026-11-16). Section 2 is the docs' quickstart, quoted exactly. Section 3 is ours, built from the docs' quickstart, approvals and custom-tool patterns; nothing here was run. Use a test folder and a throwaway key.

### 1. setup-commands.txt
```
# 1. A new, empty test folder (from the docs' quickstart)
mkdir my-agent
cd my-agent

# 2. A virtual environment, switched on
# Windows (PowerShell):
py -m venv .venv
.venv\Scripts\Activate.ps1
# If PowerShell blocks Activate.ps1, run this first:
#   Set-ExecutionPolicy -Scope Process RemoteSigned
# Mac (Terminal):
python3 -m venv .venv
source .venv/bin/activate

# 3. One exact version of the SDK (about 150 MB: it bundles Claude Code)
pip install claude-agent-sdk==0.2.182

# 4. A throwaway API key, for this terminal window only
#    Make it at platform.claude.com, and set a monthly spend limit at
#    platform.claude.com/settings/spend-limits
# Windows (PowerShell):
$env:ANTHROPIC_API_KEY = "your-api-key"
# Mac (Terminal):
export ANTHROPIC_API_KEY=your-api-key

# 5. Run the agent
python first_agent.py

# 6. Switch the key off when you've finished (or close the window),
#    then delete the key on platform.claude.com
# Windows (PowerShell):
Remove-Item Env:ANTHROPIC_API_KEY
# Mac (Terminal):
unset ANTHROPIC_API_KEY
```

### 2. docs-quickstart-agent.py
```
# From the docs: code.claude.com/docs/en/agent-sdk/quickstart (claude-agent-sdk 0.2.182)
# Shown for comparison only. It auto-approves file edits and sets no step limit.
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage


async def main():
    # Agentic loop: streams messages as Claude works
    async for message in query(
        prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob"],  # Auto-approve these tools
            permission_mode="acceptEdits",  # Auto-approve file edits
        ),
    ):
        # Print human-readable output
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)  # Claude's reasoning
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")  # Tool being called
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")  # Final result


asyncio.run(main())
```

### 3. first_agent.py
```
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
```

### 4. example-output.txt
```
Example output (not run; your wording will differ)

Tool: mcp__calendar__check_calendar
Tool: Write

Approval needed: Write
Input: {'file_path': '.../my-agent/notes.txt', 'content': 'Tuesday: 2pm to 3pm'}
Allow this action? (y/n): y
I saved Tuesday's free hour, 2pm to 3pm, to notes.txt.
Done: success
```

### 5. safety-checklist.md
```
# First Claude Agent SDK agent: safety checklist (facts checked 2026-11-16)

## Before you run it
- [ ] A new, empty test folder. The agent can reach files in the folder you start it from and the folders below it.
- [ ] A virtual environment, switched on: you see (.venv) before your prompt.
- [ ] One exact version: pip install claude-agent-sdk==0.2.182 (Python 3.10 or later).
- [ ] A throwaway API key with a monthly spend limit (platform.claude.com/settings/spend-limits).
- [ ] The key in ANTHROPIC_API_KEY for this terminal only. Never in a script, a prompt or a file you might share.

## In the code
- [ ] max_turns set small. Default: no limit. Count one extra turn for the final answer.
- [ ] max_budget_usd set small. Default: no limit. It can go a little over, so leave room.
- [ ] permission_mode="default" with a can_use_tool callback. No callback means deny.
- [ ] allowed_tools holds only harmless tools. It approves; it doesn't limit.
- [ ] tools (or disallowed_tools) limits which built-in tools exist.
- [ ] setting_sources=[] so your own Claude Code allow rules can't skip the question. (It also turns skills off. To use skills later: setting_sources=["project"], skills="all", and "Skill" added to tools. Skill calls then skip the question.)

## Check it worked
- [ ] Type n at the question: nothing is written.
- [ ] Set max_turns=1: the run ends with error_max_turns. Then set it back.

## When you've finished
- [ ] Close the terminal, or Remove-Item Env:ANTHROPIC_API_KEY (Windows) / unset ANTHROPIC_API_KEY (Mac).
- [ ] Delete the throwaway key on platform.claude.com.

## Licence and sign-in
- The GitHub repo is MIT, but use of the SDK is governed by Anthropic's Commercial Terms of Service, and the bundled Claude Code says "All rights reserved".
- Sign in with an API key. Anthropic: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."

Sources: code.claude.com/docs/en/agent-sdk/quickstart ; code.claude.com/docs/en/agent-sdk/agent-loop ; code.claude.com/docs/en/agent-sdk/python ; code.claude.com/docs/en/agent-sdk/user-input ; code.claude.com/docs/en/agent-sdk/custom-tools ; code.claude.com/docs/en/agent-sdk/overview
```
