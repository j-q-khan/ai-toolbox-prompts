# Full code: Context Engineering vs Prompt Engineering: What Changed and Why

The messages and instructions from this video, plus the checklist, checked 2026-11-18. Every line here is ours, built on Anthropic's article and on Claude's and OpenAI's own pages; none was run for this video and no reply is shown. Each text file holds only the text to paste; the checklist says where each one goes and what to swap in. Test Bakery is made up.

### 1. 1-long-chat-before.txt
```
Now write a sign for our holiday hours too.
```

### 2. 1-new-chat-after.txt
```
Write a sign for Test Bakery's holiday hours.
We're shut on 25 and 26 December, and open again on the 27th.
It goes on the shop door, so keep it under 40 words.
Match this sign of ours: "Fresh sourdough, baked daily."
```

### 3. 2-instructions-too-rigid.txt
```
ALWAYS open with "Dear neighbours". NEVER go over 60 words.
If the sign is about hours, list every day, Monday to Sunday.
If the sign is about a price, put the price in the first line.
If the sign is about a new loaf, name two ingredients.
```

### 4. 2-instructions-too-vague.txt
```
Make our signs nice.
```

### 5. 2-instructions-after.txt
```
You are a writer for Test Bakery, a small local shop.
Our customers are neighbours, so keep the tone warm and plain.
Keep replies under 80 words, because they go on small cards.
If a fact is missing, ask me instead of guessing.
```

### 6. 3-new-chat-template.txt
```
Write [WHAT YOU WANT] for [WHO OR WHAT IT'S FOR].
[THE FACTS THIS TASK NEEDS, AND NOTHING ELSE]
It goes [WHERE IT WILL BE SEEN], so keep it [LENGTH OR STYLE].
Match this example of ours: "[ONE SHORT EXAMPLE]"
```

### 7. checklist.md
```
# Context checklist: what goes in front of the model (facts checked 2026-11-18)

For Claude or ChatGPT in a browser, on Windows or Mac. Nothing here was signed into or run for the video, no screen of either app was seen, and no result is promised. The Test Bakery lines are ours; the quoted lines are Anthropic's, Claude Help Center's and OpenAI's, word for word, from the pages under Sources. Anthropic's article is written for developers building agents: using it in a chat app is our reading. Pages change: if a quote doesn't match what you see, open the page it came from.

## What the words mean
- [ ] Context: everything the model can see when it answers (our short form). Anthropic's article lists "system prompts, tools, examples, message history, etc".
- [ ] Context engineering: choosing what goes in. Anthropic's article: "we view context engineering as the natural progression of prompt engineering".
- [ ] Why it matters, in the article's words: models have an "attention budget", and context is "a finite resource with diminishing marginal returns". Anthropic's docs: "more context isn't automatically better".

## Before you start a task
- [ ] Is this a new task? Give it a new chat. ChatGPT's docs, about chats in a project: "Start a separate chat for each distinct outcome so its messages and results stay focused while the project keeps related work organized." Claude's help page: "Claude remembers context from earlier in the conversation."
- [ ] One chat, one outcome.

## What to put in
- [ ] The task, in one line.
- [ ] The facts this task needs, and nothing else.
- [ ] Where the result will be seen, with any limit and its reason.
- [ ] One short example to match. The article: "examples are the "pictures" worth a thousand words".
- [ ] Leave out anything about other people, every password, and anything your employer wouldn't want shared.

## Your standing instructions
- [ ] Not too rigid: a rule for every case. The article calls that "brittle".
- [ ] Not too vague: one line that assumes the app knows your shop. The article: "vague, high-level guidance".
- [ ] In between. The article: "specific enough to guide behavior effectively, yet flexible enough".
- [ ] Lean, but complete. The article: "minimal does not necessarily mean short".
- [ ] Claude Help Center: "Keep project instructions concise: Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role."
- [ ] A rule list that keeps growing? Swap rules for one or two examples.

## When a reply misses
- [ ] Add one line for what went wrong, and try again. The article: "start by testing a minimal prompt … and then add clear instructions and examples to improve performance based on failure modes found during initial testing".

## The files, and where each one goes
Open a file from the link in the description and copy all of it.
- [ ] 1-long-chat-before.txt: ours. A new task typed at the bottom of a long chat, to compare. Not to use.
- [ ] 1-new-chat-after.txt: ours. Paste it into the message box of a new chat.
- [ ] 2-instructions-too-rigid.txt and 2-instructions-too-vague.txt: ours. The two extremes, to compare. Not to use.
- [ ] 2-instructions-after.txt: ours. Part 5's four lines; they go where Part 5's checklist says.
- [ ] 3-new-chat-template.txt: the blank version. Swap everything in square brackets, brackets included, for your own words.
- [ ] BUILD-PROMPT.md: paste it into a new chat, describe your task and what you were going to paste, and answer its questions.

Sources: anthropic.com/engineering/effective-context-engineering-for-ai-agents ; platform.claude.com/docs/en/build-with-claude/context-windows ; support.claude.com/en/articles/9797557-usage-limit-best-practices ; support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features ; support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans ; learn.chatgpt.com/docs/projects ; developers.openai.com/cookbook/examples/agents_sdk/session_memory ; developers.openai.com/api/docs/guides/prompt-engineering
```
