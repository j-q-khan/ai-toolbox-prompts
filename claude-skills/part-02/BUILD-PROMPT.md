# Claude build prompt: Claude Skills Part 2

Use this in Claude Code (Pro or higher, or a Console account), in the folder you work in. Start in plan mode.

Goal: sort what I've told Claude so far into the right place: CLAUDE.md, a skill, a subagent, an MCP server or a hook. You look and suggest; you change nothing until I say yes, and you install nothing.
Steps, in order:
1. Look at the CLAUDE.md in this folder and in my home folder's .claude folder, if they exist, and at any skills in .claude/skills. Don't open any file named .env.
2. Ask me what I keep pasting into chat, which side jobs fill up my chats, which apps I copy things out of, and which rules I need to hold every time. Wait for my answers.
3. Make a table with one row per rule or job: what it is, where it is now, where it should go (CLAUDE.md, skill, subagent, MCP server or hook), and one sentence of why, using these tests from Anthropic's docs: always-on house rules go in CLAUDE.md; a procedure pasted for the third time becomes a skill; a side task that floods the chat goes to a subagent; data from an app Claude can't see means an MCP server; anything that must happen every time, or never, is a hook.
4. Keep CLAUDE.md under 200 lines: list what to move out of it.
5. Wait for my yes on each row. Then, for each row I approve, show me the exact file you would write (the CLAUDE.md lines, the SKILL.md, or the hook settings and script) before writing it, and wait for my yes again.
6. For skills, use only name and description in the frontmatter, a name without the words claude or anthropic, and a description that says what the skill does and when to use it.
7. For hooks, write them into .claude/settings.json in this folder only, with scripts that need only bash (no jq), and tell me how to test each one safely.
8. For MCP servers, don't add any: name the app and tell me to find its official server and check it first.
Safety: never open, print or edit a .env file or any file with passwords or keys. Don't install, download or run anything. Write only the files I approved.
Output: the table, the files I approved, and a three-line summary of what goes where.
