# Full code: Prompt Engineering for Claude: What Anthropic's Own Guide Says

The prompts from this video, plus the checklist, checked 2026-11-17. Sections 1 to 4 and 13 to 14 are Anthropic's own examples from its Prompting best practices page, word for word (the page prints each as one line; here they're broken at 68 characters). Sections 5 to 12 are ours, written on that page's rules. None was run for this video. Each prompt file holds only the prompt, so it can be pasted whole; the checklist says where each one goes and what to swap in. Test Bakery and its reviews are made up.

### 1. 1-clear-before.txt
```
Create an analytics dashboard
```

### 2. 1-clear-after.txt
```
Create an analytics dashboard. Include as many relevant features
and interactions as possible. Go beyond the basics to create a
fully-featured implementation.
```

### 3. 2-why-before.txt
```
NEVER use ellipses
```

### 4. 2-why-after.txt
```
Your response will be read aloud by a text-to-speech engine, so
never use ellipses since the text-to-speech engine will not know
how to pronounce them.
```

### 5. 3-examples-before.txt
```
Reply to this Test Bakery review: "The rolls were cold."
```

### 6. 3-examples-after.txt
```
Reply to this Test Bakery review: "The rolls were cold."
Here's an example of a reply in our style:
Review: "The queue was slow."
Reply: "Sorry about the wait. We've added a second till."
```

### 7. 4-tags-before.txt
```
Reply to this Test Bakery review: "The rolls were cold."
Here's an example of a reply in our style:
Review: "The queue was slow."
Reply: "Sorry about the wait. We've added a second till."
```

### 8. 4-tags-after.txt
```
Reply to the Test Bakery review, in the style of the example.
<example>
Review: The queue was slow.
Reply: Sorry about the wait. We've added a second till.
</example>
<review>
The rolls were cold.
</review>
```

### 9. 5-role-before.txt
```
Suggest three names for a new Test Bakery loaf.
```

### 10. 5-role-after.txt
```
You are a marketing writer for a small local bakery.
Suggest three names for a new Test Bakery loaf.
```

### 11. 6-long-document-before.txt
```
What are the three most common complaints in this document?
[PASTE YOUR LONG DOCUMENT HERE]
```

### 12. 6-long-document-after.txt
```
<document>
[PASTE YOUR LONG DOCUMENT HERE]
</document>
What are the three most common complaints in this document?
```

### 13. 7-format-before.txt
```
Do not use markdown in your response
```

### 14. 7-format-after.txt
```
Your response should be composed of smoothly flowing prose
paragraphs.
```

### 15. checklist.md
```
# Prompting Claude, from Anthropic's own guide: checklist (facts checked 2026-11-17)

For Claude in a browser, on Windows or Mac. Nothing here was run for the video, and no result is promised. "Seven habits" is our count; the order is the guide's.

## Before you paste anything
- [ ] Take out anything private: passwords, real customer details, anything your employer wouldn't want shared.
- [ ] At work: follow your employer's rules first.
- [ ] Anthropic's privacy page is under Sources.

## The seven habits
- [ ] 1. Be clear and direct. Anthropic: "If you want Claude to do more than the task strictly requires, explicitly request it".
- [ ] 2. Say why. Give the reason behind a rule. Anthropic: "Claude can generalize from the explanation."
- [ ] 3. Show examples. Anthropic: "Include 3-5 examples for best results." One is a start; Part 4 of the series goes further.
- [ ] 4. Label the parts with tags. A tag is a label inside angle brackets, with a matching ending tag that adds a slash. Anthropic: "Use consistent, descriptive tag names across your prompts."
- [ ] 5. Give a role. Anthropic: "Even a single sentence makes a difference". The guide sets it in the system prompt; opening a chat message with it is our suggestion.
- [ ] 6. Long document at the top, question last. Anthropic: "Queries at the end can improve response quality by up to 30 percent in tests". That's its figure for large inputs, not a promise.
- [ ] 7. Say what to do instead of what not to do.

## Your model
- [ ] Each Claude model has its own prompting page (9 on 2026-11-17), in the table at the top of the guide. Start with yours.

## One more from the guide
- [ ] "The formatting style used in your prompt might influence Claude's response style." Want plain paragraphs back? Write your prompt in plain paragraphs.

## The files, and where each one goes
Open a file from the link in the description, copy all of it, and paste it into the message box at the bottom of a new chat.
- [ ] 1-clear-before.txt, 1-clear-after.txt: Anthropic's own pair for habit 1, to compare.
- [ ] 2-why-before.txt, 2-why-after.txt: Anthropic's own pair for habit 2. Add the after to a prompt whose reply will be spoken by software.
- [ ] 3-examples-before.txt, 3-examples-after.txt: ours. Swap the two reviews and the reply for your own.
- [ ] 4-tags-before.txt, 4-tags-after.txt: ours. The before is the same text as 3-examples-after.txt. Swap the text between each pair of tags; keep the tags.
- [ ] 5-role-before.txt, 5-role-after.txt: ours. Swap the first line for the role that suits your task.
- [ ] 6-long-document-before.txt, 6-long-document-after.txt: ours. Swap the line in square brackets, brackets included, for your document, and the last line for your question.
- [ ] 7-format-before.txt, 7-format-after.txt: Anthropic's own pair for habit 7. Add the after to a prompt when you want plain paragraphs.
- [ ] BUILD-PROMPT.md: paste it into a new chat, put your own prompt where the last line says so, and answer its questions.

Sources: platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview ; privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
```
