Paste this into Claude Code, Anthropic's coding assistant, opened in a new, empty test folder. It makes one small file there and asks before every change. Written from Anthropic's docs, not run.

Goal: make me a small Python cost calculator for the Claude API that works out what a call, or a batch of calls, costs from token counts and prices I type in.
Rules:
1. Work only in this folder. Don't open, change or delete any file outside it, don't install anything, and don't go online.
2. Before you write anything, show me your plan in three lines and wait for my OK.
3. Make claude_cost.py, using only Python's standard library (Python 3.10 or later). It needs no API key and makes no network calls.
4. Don't hard-code any price as current. The script asks me for four numbers: the input price per million tokens, the output price per million tokens, the input tokens per call, and the output tokens per call. Then it asks how many calls.
5. It also asks two yes or no questions: is this a batch (if yes, halve every price, including the cache hit price, because the Batches API is 50 percent off and Anthropic's pricing page says the discounts stack), and do some input tokens come from a prompt cache (if yes, ask how many cached input tokens per call and the cache hit price per million, and charge those tokens at that price instead). When the cache is used, print one line saying the one-time cache write (1.25 times the input price for the 5-minute cache) isn't counted.
6. Print one call's cost and the total, in dollars to six decimal places, and show the sum it used, line by line.
7. Check every input: no negative numbers, no text where a number goes, and the cached tokens can't be more than the input tokens. On a bad input, say what's wrong and ask again.
8. At the top of the output, print one line: "Prices are what you typed in; check platform.claude.com/docs/en/about-claude/pricing for the day's prices."
9. Ask me before every file change, and change nothing else.
10. When it's done, tell me how to run it on Windows (PowerShell) and on a Mac (Terminal), and test it once with the made-up numbers 4, 20, 2000 and 500 for one call, no batch and no cache, which should come to 0.018000 dollars.
Output: claude_cost.py, and a one-line summary of what you made.
