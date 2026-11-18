# Claude build prompt: Copilot Studio Agent Flows: Make Your Agent Run a Power Automate Flow

Paste this into Microsoft Copilot (Copilot Chat) or into Claude, with made-up examples only. Follow your employer's rules on what you may build, connect and paste, and never describe real customers, staff or real company files: use a made-up test table and send emails only to yourself. It turns your own idea for an agent flow into the inputs, steps and tool description to build in Copilot Studio, written from Microsoft Learn's agent flow pages, checked 2026-11-17.

Goal: plan one agent flow in Copilot Studio that my agent calls as a tool, writing only to a test table and emailing only me, so I can build it step by step and test it in the test pane without publishing the agent.
Steps, in order:
1. Restate my idea in one sentence: what the person asks the agent, which details the agent collects, and what the flow does with them.
2. List the inputs for the When an agent calls the flow trigger: a name and a type (Text, Number, Yes/No or Date) for each, and keep them to the fewest that do the job.
3. List the actions between the trigger and Respond to the agent, in order, each with its connector (for example Excel Online (Business) or Office 365 Outlook), the action's name and which input goes in which box.
4. Every write goes to a test table in a test workbook, and every email goes to my own address only.
5. List the outputs for Respond to the agent: a name, a type and what the agent should say with each.
6. Write the tool's description in one or two plain sentences: when the agent should use this flow and what it does.
7. Give me two test messages for the test pane: one that should call the flow and one that shouldn't.
8. Remind me to publish the flow (not the agent), keep the test workbook shut while testing, check the new line and the email by hand, and turn the flow off on its Overview tab when I've finished.
If you're not sure of an action's or a setting's exact name, write [CHECK: name in Copilot Studio].
My idea: (for example: when someone asks the agent to book a made-up meeting room, log the room and the time in a test table and email me)
