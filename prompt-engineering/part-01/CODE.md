# Full code: Prompt Engineering for Beginners: How to Write a Prompt That Works

The prompts from this video, built on Anthropic's and OpenAI's published prompting guides (checked 2026-11-17), plus the checklist. They were written from the guides, not run for this video. Each prompt file holds only the prompt, so it can be pasted whole; the checklist says where each one goes and what to swap in. Test Bakery is made up.

### 1. 1-email-before.txt
```
Write an email about our new opening hours.
```

### 2. 1-email-after.txt
```
Write an email telling customers Test Bakery now opens at 7, not 8.
They're regulars who asked for earlier hours, so thank them.
Keep it under 80 words, friendly, with a short title line.
If you're unsure of a detail, say so instead of guessing.
```

### 3. 2-example-after.txt
```
Write an email telling customers Test Bakery now opens at 7, not 8.
They're regulars who asked for earlier hours, so thank them.
Keep it under 80 words, friendly, with a short title line.
If you're unsure of a detail, say so instead of guessing.
Here's an example of the style I want:
Title: Fresh rolls on Fridays
Hi all, you asked, so we now bake rolls on Fridays too.
Come early, they go fast. Thank you, Test Bakery
```

### 4. 3-try-again.txt
```
Make it shorter, and put the new time in the first sentence.
```

### 5. 4-your-prompt-template.txt
```
[WHAT YOU WANT DONE, IN ONE PRECISE SENTENCE]
[WHO IT'S FOR, AND WHY YOU'RE ASKING]
[HOW LONG, WHAT TONE, AND HOW TO LAY IT OUT]
If you're unsure of a detail, say so instead of guessing.
Here's an example of the style I want:
[PASTE AN EXAMPLE YOU LIKE, OR DELETE THIS LINE AND THE ONE ABOVE]
```

### 6. checklist.md
```
# How to write a prompt that works: checklist (facts checked 2026-11-17)

Works in Claude and in ChatGPT, in a browser, on Windows or Mac. Nothing here was run for the video, and no result is promised.

## Before you paste anything
- [ ] Take out anything private: passwords, real customer details, anything your employer wouldn't want shared.
- [ ] At work: follow your employer's rules first.
- [ ] Look at the app's own privacy page before you paste. Anthropic's is under Sources.

## The five parts
- [ ] The task: one precise thing to do. Anthropic: "The more precisely you explain what you want, the better the result."
- [ ] The context: who it's for and why you're asking.
- [ ] The format: how long, what tone, how it's laid out.
- [ ] An example: a sample of the style you want, pasted under the words "Here's an example of the style I want:".
- [ ] A check: show the prompt to a colleague who knows nothing about the task. Anthropic: "If they'd be confused, Claude will be too."

## One more line
- [ ] End with: If you're unsure of a detail, say so instead of guessing.

## The files, and where each one goes
Open a file from the link in the description, copy all of it, and paste it into the message box at the bottom of a new chat.
- [ ] 1-email-before.txt: the weak prompt, to compare.
- [ ] 1-email-after.txt: the fixed prompt. Swap Test Bakery, the times and the reason for your own.
- [ ] 2-example-after.txt: the fixed prompt with an example under it. Swap the last three lines for an email you liked.
- [ ] 3-try-again.txt: a follow-up for the same chat when the reply misses. Say what to change in your own words.
- [ ] 4-your-prompt-template.txt: the blank version. Swap every line in square brackets, brackets included, for your own words.
- [ ] BUILD-PROMPT.md: paste it into a new chat, put your own prompt where the last line says so, and answer its questions.

## If it misses
- [ ] Stay in the same chat and say what to change. OpenAI's Cookbook guide: "Don't expect your first prompt to work perfectly."
- [ ] A prompt you saved a while ago may need changing on a newer model. If it shouts in capitals, soften it and test it again.

Sources: platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; claude.com/blog/best-practices-for-prompt-engineering ; developers.openai.com/api/docs/guides/prompt-engineering ; developers.openai.com/cookbook/examples/chatgpt/chatgpt_prompt_guide/chatgpt_prompt_guide ; privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
```
