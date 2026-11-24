# Full code: LLM Council: Ask Several AI Models, Then Let Them Judge Each Other

The two prompts from this video, written by us on 2026-11-23. No text or code from Karpathy's llm-council (no licence file) or from any community skill is copied into them. Nothing was run. `council-prompt.txt` is for Claude Code and runs the council with Claude sub-agents, so every member is Claude; `by-hand-review-prompt.txt` is for any chatbot and keeps answers from several companies' models, with you doing the copying. Both are plain text: in Notepad, set the box called "Save as type" to "All files"; on a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

### council-prompt.txt
```
# Council prompt for one Claude Code session, from the video "LLM Council: Ask Several AI Models, Then Let Them Judge Each Other" (2026-11-23). Written by us.
# This is the Claude sub-agent style: every council member is Claude, each with a different role.
# It is not Karpathy's llm-council app, which sends your question to several companies' models through OpenRouter.
# To use it: replace the question on the last line first, then start Claude Code in an empty folder, copy everything in this file and paste it in.
# Each sub-agent's requests count toward your Claude plan's usage limits, so save it for questions worth it.
Run a council on my question below, in three stages.
Stage 1, first answers: start four sub-agents at the same time. Give each one only my question and one of these roles, and nothing else from this chat.
- Skeptic: looks for what could go wrong.
- Planner: wants the simplest plan that works.
- Newcomer: answers as someone new to the topic.
- Checker: lists what would need checking, and where to check it.
Stage 2, blind review: label the four answers A, B, C and D in a random order and remove the roles. Start four new sub-agents. Give each one all four answers and ask it to rank them from best to worst, for how correct and how useful each one is, with one sentence on each.
Stage 3, final answer: you are the chairman. Show me each answer's average rank and which role wrote it, where the answers agree and where they clash, then one final answer and one next step.
Rules: don't create, change or delete any files, don't run commands, and don't search the web unless I say so. If a stage fails, tell me which one and stop.
My question: Should I learn Python or JavaScript first?
```

### by-hand-review-prompt.txt
```
# Review prompt for a council by hand, from the video "LLM Council: Ask Several AI Models, Then Let Them Judge Each Other" (2026-11-23). Written by us.
# Step 1: ask the same question in two or three chatbots you already use, and copy each answer.
# Step 2: open a fresh chat, paste this prompt, then fill in the question and the answers below, labelled A, B and C, with no chatbot names.
# Step 3: send it. For a second opinion, paste the same thing into another chatbot and compare the two rankings.
Below are one question and three answers to it, labelled A, B and C. You don't know who wrote them, so judge only what each answer says.
First, rank them from best to worst, for how correct and how useful each one is, with one sentence on why for each.
Then act as chairman: write one final answer that keeps the strongest parts, says plainly where the answers disagreed, and ends with one next step.
Question:
[paste the question here]
Answer A:
[paste the first answer here]
Answer B:
[paste the second answer here]
Answer C:
[paste the third answer here]
```
