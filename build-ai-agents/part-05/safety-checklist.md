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
