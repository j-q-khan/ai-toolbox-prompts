# Full code: Prompt Engineering Tutorial: Few-Shot Examples and XML Tags, Before and After

The prompts from this video, plus the checklist, checked 2026-11-18. Every prompt here is ours, written on the rules in Anthropic's Prompting best practices and OpenAI's Prompt engineering guide; the tag names example, examples and instructions are from Anthropic's page, and notes is ours. None was run for this video, and section 6 is example output we wrote, not a real reply. Each prompt file holds only the prompt, so it can be pasted whole; the checklist says where each one goes and what to swap in. Test Bakery and its labels are made up.

### 1. 1-plain.txt
```
Write a shelf label for our new loaf: sesame rye, baked daily.
```

### 2. 2-examples-too-alike.txt
```
Write a shelf label for our new loaf: sesame rye, baked daily.
Here are three of our labels:
White loaf: freshly baked, soft and tasty.
Brown loaf: freshly baked, soft and tasty.
Seeded loaf: freshly baked, soft and tasty.
```

### 3. 2-examples.txt
```
Write a shelf label for our new loaf: sesame rye, baked daily.
Here are three of our labels:
Cheese scone: sharp cheddar, baked this morning.
Oat cookie: chewy, with raisins. Contains nuts.
Sourdough loaf: slow-proved, with a crisp crust.
```

### 4. 3-tags.txt
```
<instructions>Write a shelf label for our new loaf.</instructions>
<examples>
<example>Cheese scone: sharp cheddar, baked this morning.</example>
<example>Oat cookie: chewy, with raisins. Contains nuts.</example>
<example>Sourdough loaf: slow-proved, with a crisp crust.</example>
</examples>
<notes>Our new loaf: sesame rye, baked daily.</notes>
```

### 5. 4-template.txt
```
<instructions>[THE ONE THING YOU WANT DONE]</instructions>
<examples>
<example>[EXAMPLE 1]</example>
<example>[EXAMPLE 2, DIFFERENT FROM EXAMPLE 1]</example>
<example>[EXAMPLE 3, THE UNUSUAL CASE]</example>
</examples>
<notes>[THE FACTS OR THE DOCUMENT TO WORK FROM]</notes>
```

### 6. example-output.txt
```
Sesame rye loaf: dark and nutty, baked daily. Contains sesame.
```

### 7. checklist.md
```
# Few-shot examples and XML tags: checklist (facts checked 2026-11-18)

For Claude or ChatGPT in a browser, on Windows or Mac. Nothing here was run for the video, and no result is promised. The Test Bakery prompts are ours; the quoted lines are Anthropic's and OpenAI's, word for word, from the two pages under Sources.

## Before you paste anything
- [ ] Take out anything private: passwords, real customer details, anything your employer wouldn't want shared.
- [ ] At work: follow your employer's rules first.

## Step 1: add examples (few-shot prompting)
- [ ] Put a few examples of the result you want inside the prompt. Anthropic: "Examples are one of the most reliable ways to steer Claude's output format, tone, and structure."
- [ ] How many. Anthropic: "Include 3–5 examples for best results." Its figure, not a promise.
- [ ] Relevant. Anthropic: "Mirror your actual use case closely."
- [ ] Diverse. Anthropic: "Cover edge cases and vary enough that Claude doesn't pick up unintended patterns." If every example ends the same way, change two of them.
- [ ] If your task has an input (a review and its reply, a question and its answer), show both halves in each example. OpenAI: "try to show a diverse range of possible inputs with the desired outputs." Our shelf labels have no input, so each example is the label alone.

## Step 2: put each part inside its own tag
- [ ] A tag is a word inside angle brackets. The closing tag is the same word with a slash in front. The text goes between the two.
- [ ] The request between instructions tags; each example between its own example tags, all of them inside one examples tag; the facts or a pasted document between notes or document tags.
- [ ] Names. Anthropic: "Use consistent, descriptive tag names across your prompts." The names example, examples and instructions are on Anthropic's page; notes is ours. Neither page lists names you have to use.
- [ ] Anthropic says tags help "especially when your prompt mixes instructions, context, examples, and variable inputs". Our reading, not Anthropic's: a one-line question doesn't need them.
- [ ] In ChatGPT: OpenAI's developer guide recommends tags too, and Markdown headings for a prompt's sections (Part 3 of this series). Either layout is its own advice.

## One more from Anthropic's page
- [ ] "You can also ask Claude to evaluate your examples for relevance and diversity, or to generate additional ones based on your initial set." With one good example: ask for two more that differ from it, then check them yourself.

## The files, and where each one goes
Open a file from the link in the description, copy all of it, and paste it into the message box at the bottom of a new chat.
- [ ] 1-plain.txt: ours. The prompt before either step, to compare.
- [ ] 2-examples.txt: ours. Step 1: the same request with three examples.
- [ ] 2-examples-too-alike.txt: ours, the mistake. Three examples that end on the same words. Kept to compare with 2-examples.txt, not to use.
- [ ] 3-tags.txt: ours. Step 2: the request, the examples and the facts, each inside its own tag. This is the finished prompt.
- [ ] 4-template.txt: the blank version. Swap everything in square brackets, brackets included, for your own words. Keep the tags.
- [ ] example-output.txt: not a prompt. It's the example reply shown in the video, which we wrote; nothing was run.
- [ ] BUILD-PROMPT.md: paste it into a new chat, put your own prompt where the last line says so, and answer its questions.

Sources: platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; developers.openai.com/api/docs/guides/prompt-engineering
```
