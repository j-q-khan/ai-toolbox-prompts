Paste this into Claude Code, Anthropic's coding assistant, opened in a new, empty test folder. It makes one small file there and asks before every change. Written from Anthropic's docs, not run.

Goal: make me first_call.py, a small Python script that sends one message to the Claude API and explains the common errors in plain words.
Rules:
1. Work only in this folder. Don't open, change or delete any file outside it, and don't install anything without asking me first.
2. Before you write anything, show me your plan in three lines and wait for my OK.
3. Use Python 3.10 or later and Anthropic's anthropic package (pip install anthropic). Follow Anthropic's quickstart at platform.claude.com/docs/en/get-started: client = anthropic.Anthropic(), then client.messages.create with model "claude-opus-5-5", max_tokens=1000 and one user message, then print only the text blocks of the reply.
4. The key comes only from the ANTHROPIC_API_KEY environment variable. Never put a key in the file, never print the key or any part of it, and never write it to disk. If the variable isn't set, print one plain line saying so and stop.
5. Don't send temperature, top_p or top_k: API version 2026-10-21, which the anthropic package uses from version 2.0.0, returns a 400 error for any of them. Add a comment saying so.
6. Catch these errors and print one plain line for each, using the wording of Anthropic's errors page (platform.claude.com/docs/en/api/errors): anthropic.AuthenticationError (401, an issue with your API key: check ANTHROPIC_API_KEY or make a new key), anthropic.RateLimitError (429, a rate limit or the monthly spend cap: the package already retried twice, so wait and try again, and if it keeps failing, check the limits page at platform.claude.com/usage/limits), and anthropic.APIStatusError with status_code 402 (billing_error, an issue with your billing or payment information: check the Billing page at platform.claude.com/settings/billing). Also handle anthropic.BadRequestError (400: check for temperature, top_p or top_k, a spend limit you set, or a key that isn't tied to a workspace), any other anthropic.APIStatusError (print its status code), and anthropic.APIConnectionError (the API couldn't be reached). Catch the specific errors before APIStatusError. Never print the full response.
7. After the reply, print the input and output tokens the call used, from message.usage.
8. Put the question in one variable near the top, so I can change it.
9. Don't run the script yourself, because a run spends credits. When it's done, tell me how to run it on Windows (PowerShell) and on a Mac (Terminal), from a virtual environment with the package installed.
10. Ask me before every file change, and change nothing else.
Output: first_call.py, and a one-line summary of what you made.
