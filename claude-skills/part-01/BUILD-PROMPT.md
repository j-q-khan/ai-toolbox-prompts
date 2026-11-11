# Claude build prompt: Claude Skills, Part 1

Use this in Claude Code (Pro or higher, or a Console account), in any folder. Start in plan mode.

Goal: turn one set of instructions I keep pasting into chats into a personal skill, written in the portable format so it also uploads to the Claude app. You run nothing and install nothing.
Steps, in order:
1. Ask me what I keep pasting or retyping into Claude, and ask me for one real example of it. Wait for my answer.
2. Propose a skill name: lowercase letters, numbers and hyphens only, at most 64 characters, and without the words claude or anthropic.
3. Propose a description of at most 1,024 characters that says what the skill does, then "Use when" and the words I'd actually type when I want it. Show me the name and description and wait for my yes.
4. Write the instructions as short numbered steps, the way I'd explain the job to a new colleague, plus one line saying what to do when something is unclear. Keep SKILL.md under 500 lines; put any long reference material or template in a second file in the same folder and point to it from the steps.
5. Use only name and description in the frontmatter, so the skill also works on the Claude app and the API. No scripts, no shell commands, no web requests.
6. Show me the full SKILL.md and any second file, and wait for my yes. Then save them in ~/.claude/skills/your-skill-name/ (using the name we agreed), creating only that folder.
7. Give me two test prompts: one in my own words that should make Claude pick the skill by itself, and the slash command with the skill's name. Tell me that if the first one doesn't pick it, the description is the first thing to change.
8. Tell me how to zip the folder for the Claude app: Customize, then Skills, then +, Create skill, Upload a skill.
Safety: create files only in that one skill folder. Don't edit any other file, and don't run anything.
Output: the skill folder, the two test prompts and a three-line summary.
