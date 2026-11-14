# Claude build prompt: Is Google AI Studio Free? Limits, Costs and What Google Does With Your Prompts

Part 2 of the Google AI Studio series. Copy everything below the line into Claude Code.
What it builds follows Google's official Gemini API docs (checked 2026-11-13). Try it in a test folder first, and read every file it writes before you use it; it asks before it writes anything, and you run the install yourself.

---

Use this in Claude Code, in a new, empty test folder (never your home folder). Start in plan mode.

Goal: build a tiny Python script that sends one test question to the Gemini API and prints the response's token usage, plus what that call would cost at Google's paid prices, so I can see what a call would cost before I turn on billing. Use a throwaway key with a spend cap, and dummy questions only.
Steps, in order:
1. Look up three Google pages and tell me what you find before you write anything: the model Google labels "Default general-purpose" on https://aistudio.google.com/docs/latest-model; that model's paid "Input price" and "Output price (including thinking tokens)" per 1M tokens on https://aistudio.google.com/docs/pricing; and the usage fields on an Interactions response on https://aistudio.google.com/docs/tokens (interaction.usage.total_input_tokens, total_output_tokens, total_thought_tokens, total_tokens). If any page has changed, tell me what changed.
2. Don't install anything yourself. Give me the exact commands to make a virtual environment in this test folder and install the only package, google-genai, with pip install -U google-genai, which gets the newest version (Google says the usage fields need a version newer than 2.0.0), and I'll run them.
3. Write token_cost.py: it reads the key only from the environment variable GEMINI_API_KEY and passes it to the client explicitly (genai.Client(api_key=...)), so GOOGLE_API_KEY is never used by accident, and if that variable is missing it stops with a plain message telling me to set it (Part 4 of the series shows how). It never prints, logs or writes the key. It sends one dummy question to the default model from step 1 with client.interactions.create, prints the answer, then prints the input, output and thinking tokens, and the cost at the paid prices from step 1, counting thinking tokens at the output price, with the date the prices were checked and a note that the free tier charges nothing.
4. Write a .gitignore that covers .env, .env.* and the virtual environment folder.
5. Show me both files and wait for my yes before saving them. I'll switch you out of plan mode so you can save.
6. Tell me to read every line before I run it, and remind me: on the free tier Google may use what I send to improve its products and human reviewers may see it, so I should send dummy questions only, never personal or confidential information.
Safety: work only in this folder, never put a key in any file, don't run the script yourself, and don't go online except to the three Google pages above.
Output: token_cost.py, .gitignore, and a three-line summary of how to run it.
