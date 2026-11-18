# Prompting ChatGPT, from OpenAI's own guides: checklist (facts checked 2026-11-18)

For ChatGPT in a browser, on Windows or Mac. Nothing here was run for the video, and no result is promised. The Test Bakery prompts are ours; the three headings and the two accuracy lines are OpenAI's, word for word.

## Before you paste anything
- [ ] Take out anything private: passwords, real customer details, anything your employer wouldn't want shared.
- [ ] At work: follow your employer's rules first.
- [ ] Look at your app's own privacy page. (OpenAI's couldn't be opened on 2026-11-18, so it isn't linked here.)

## The three steps (OpenAI Cookbook, ChatGPT prompt guide)
- [ ] 1. Okay prompt (task): the one thing you want done.
- [ ] 2. Good prompt (+ context / persona): who you are, who it's for and why. The guide: "In Context, we recommend you encourage the model to adopt a persona."
- [ ] 3. Excellent prompt (+ output): the length, tone and layout you want.

## The three headings
- [ ] "# Context", "# Instructions", "# Additional info / Constraints". A hash sign at the start of a line makes it a heading.
- [ ] The guide: "You can add, remove, or rename headers as needed to fit the task."

## Two lines for when the facts matter
- [ ] "Label anything uncertain with (needs verification)."
- [ ] "Before finishing, list any assumptions you made."
- [ ] They don't make a reply correct. They show you where to check, so check.

## The kind of model (OpenAI's developer guide)
- [ ] "A reasoning model is like a senior co-worker. You can give them a goal to achieve and trust them to work out the details."
- [ ] "A GPT model is like a junior coworker. They'll perform best with explicit instructions to create a specific output."
- [ ] Our reading, not OpenAI's: start with the goal; if the reply misses, spell out the steps.

## One more from the guide
- [ ] "Scope first: one prompt, one deliverable." Two things wanted? Send two prompts.

## Where OpenAI's and Anthropic's guides agree and differ
- [ ] Agree: the model as a new starter; XML tags; diverse examples.
- [ ] Differ, in the one place we found: this ChatGPT guide lays a prompt out under headings, Anthropic's under tags (OpenAI's developer guide recommends both).
- [ ] Mostly ChatGPT: try the headings. Mostly Claude: try the tags (Part 2's folder has a tagged prompt). Neither is ranked here.

## The files, and where each one goes
Open a file from the link in the description, copy all of it, and paste it into the message box at the bottom of a new chat.
- [ ] 1-steps-okay.txt, 1-steps-good.txt, 1-steps-excellent.txt: ours, built on OpenAI's Okay / Good / Excellent levels; OpenAI didn't write them. The same prompt at each of the three steps, to compare.
- [ ] 2-sections-before.txt, 2-sections-after-chatgpt.txt: ours. The before is the same text as 1-steps-excellent.txt; the after puts it under OpenAI's three headings.
- [ ] 3-accuracy-before-chatgpt.txt, 3-accuracy-after-chatgpt.txt: ours. The before is the same text as 2-sections-after-chatgpt.txt; the after adds OpenAI's two accuracy lines.
- [ ] 4-template-chatgpt.txt: the blank version. Swap each line in square brackets, brackets included, for your own words. Keep the heading lines and the last two lines.
- [ ] example-output.txt: not a prompt. It's the example reply shown in the video, which we wrote; nothing was run.
- [ ] BUILD-PROMPT.md: paste it into a new chat, put your own prompt where the last line says so, and answer its questions.

Sources: developers.openai.com/cookbook/examples/chatgpt/chatgpt_prompt_guide/chatgpt_prompt_guide ; developers.openai.com/api/docs/guides/prompt-engineering ; platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
