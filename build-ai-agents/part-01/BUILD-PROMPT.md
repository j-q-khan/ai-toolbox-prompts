Paste this into Claude Code, started in a new, empty test folder (not your home folder and not real work). First press Shift+Tab until the status bar says manual mode on, so Claude Code asks before it writes or runs anything. It builds a pretend agent in plain Python, with a fake model and dummy tools, so you can watch the loop, the step limit and asking first work. No API key, no internet and nothing installed. Written from Anthropic's agent-loop docs, checked 2026-11-16.

Goal: build a tiny pretend AI agent in one Python file, using only the standard library, so I can watch the agent loop run: the model picks a step, asks for a tool, the program runs it, the result goes back, and it repeats until done or a step limit stops it.
Steps, in order:
1. Tell me in one sentence what you'll build, and that you'll ask me before writing any file or running anything.
2. Check that python --version works here (3.10 or later). If it doesn't, stop and tell me where to get Python from python.org.
3. Plan one file, toy_agent.py, and show me the plan before writing it. It must have: a fake model function (plain if/else rules, no AI, no network) that, given the task and the results so far, returns either a tool request or a final answer; a dummy check_calendar tool that returns made-up free times; a dummy send_meeting_request tool that only prints what it would send; a step limit called MAX_STEPS set to 5; and an ask-first rule, so before any tool marked as one that writes, sends or spends, it asks me yes or no with input() and, on no, stops the agent cleanly with a message.
4. Each tool gets a plain name and a one-line description of what it does and when to use it.
5. On every trip round the loop, print the step number, what the model asked for, and the result that went back.
6. If the step limit is reached, print that the step limit stopped the agent, and end cleanly.
7. Wait for my yes, then write toy_agent.py.
8. Ask me before running it with python toy_agent.py, then explain the output in three plain lines.
9. Show me how to see the step limit work: change MAX_STEPS to 1, run it again, and point out the message.
Safety: create only toy_agent.py in this folder. No installs, no network, no API keys, no real email or calendar, and nothing outside this folder.
Output: toy_agent.py and a short explanation of which lines are the loop, the step limit and asking first.
