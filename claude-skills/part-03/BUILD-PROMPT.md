# Claude build prompt: Claude Code Skills Tutorial: Make Your First Skill

Use this in Claude Code (Pro or higher, or a Console account). Start it in any folder, in plan mode.

Goal: help me make my first personal skill, for a job I repeat, and test it. You ask and suggest; you write nothing until I say yes, and you install nothing.
Steps, in order:
1. Ask me which job I keep pasting the same instructions for, and wait for my answer. Then ask for one real example of the input, with anything private taken out, and what a good result looks like.
2. Suggest a skill name: lowercase letters, numbers and hyphens only, at most 64 characters, and without the words claude or anthropic. Wait for my yes.
3. Write a description under 1,024 characters that says what the skill does and when to use it, in the words I would naturally type, starting with the job. Show it to me and wait for my yes.
4. Write the steps as a short numbered list, the way I'd explain the job to a new colleague. Keep SKILL.md well under 500 lines. If there's a checklist, template or long reference, put it in a supporting file next to SKILL.md and add one step that says when to open it.
5. Use only name and description in the frontmatter, with the first three dashes on line 1, so the skill also uploads to the Claude app. No scripts, no shell commands, no allowed-tools.
6. Show me every file in full and wait for my yes. Then create ~/.claude/skills/the-skill-name/ and write the files there, and nowhere else.
7. Tell me how to test it two ways: a plain request that should match the description, and /the-skill-name. If the skills folder didn't exist when this session started, remind me to type /reload-skills first.
8. If the plain request doesn't use the skill but the slash does, suggest a better description and explain what changed.
Safety: don't open, print or edit any file with passwords or keys, or any .env file. Don't install, download or run anything. Write only the files I approved, only in that skill's folder.
Output: the skill's files, the two test prompts, and one line saying what the description now matches.
