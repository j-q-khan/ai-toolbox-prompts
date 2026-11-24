Paste this into Claude Code, Anthropic's coding tool, after you've saved workflow-or-agent.md into a new, empty folder and opened Claude Code in that folder. Claude Code needs a Claude subscription or an Anthropic Console account (Anthropic's docs, checked 2026-11-21). It runs the made-up Test Bakery newsletter job twice, first as a fixed-steps workflow and then as an agent, so you can see the difference. It uses only that one file, writes two new files beside it, and asks before it writes anything. Written from Anthropic's engineering blog, checked 2026-11-21. Nothing here was run for the video.

Goal: using my file workflow-or-agent.md, run the Test Bakery newsletter job twice, once as a workflow and once as an agent, and show me the difference.
Steps, in order:
1. Look only at workflow-or-agent.md in this folder. Don't open any other file, and don't use the internet. Use only the made-up practice notes in that file.
2. Part A, the workflow: follow the prompt-chaining template in the file exactly, one step at a time. Show me the outline from step 1, then run the gate check and tell me whether it passed. Don't start step 2 until I say yes.
3. When I say yes, write the newsletter from the outline and show it to me. Ask me before saving it as newsletter-workflow.md in this folder.
4. Part B, the agent: start again from only the goal line in the file. Write your own plan for reaching the goal, in your own order, show it to me, and wait for me to say yes.
5. When I say yes, follow your plan and show me the result. Ask me before saving it as newsletter-agent.md in this folder.
6. Then tell me in five lines, in the chat, how the two runs differed: who picked the steps, what was checked, and which one you'd trust for a job that repeats every month.
Safety: change nothing else. Don't edit, rename, move or delete workflow-or-agent.md or any other file. If newsletter-workflow.md or newsletter-agent.md already exists, stop and ask me before replacing it. Don't run any commands. Don't add facts, numbers or claims that aren't in the practice notes.
Output: the names of the two new files, and your five-line comparison.
