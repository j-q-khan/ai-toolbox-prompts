# Claude build prompt: Google AI Studio vs the Gemini App: Which One Do You Need?

Part 3 of the Google AI Studio series. Copy everything below the line into Claude Code.
What it builds follows Google's official Gemini API docs (checked 2026-11-13). Try it in a test folder first, and read every file it writes before you use it; it asks before it writes anything, and you run the install yourself.

---

Use this in Claude Code, in a new, empty test folder (never your home folder). Start in plan mode.

Goal: build a tiny Python script that sends one test question to the Gemini API with standing rules (system instructions) read from a text file, then prints the reply and the model name, so I can try in code what Run settings' System Instructions do in Google AI Studio. Use a throwaway key with a spend cap, and dummy questions only.
Steps, in order:
1. Look up two Google pages and tell me what you find before you write anything: the model Google labels "Default general-purpose" on https://aistudio.google.com/docs/latest-model, and the system instructions example for client.interactions.create on https://aistudio.google.com/docs/text-generation (the system_instruction= argument). If either page has changed, tell me what changed.
2. Don't install anything yourself. Give me the exact commands to make a virtual environment in this test folder and install the only package, google-genai, with pip install -U google-genai, and I'll run them.
3. Write rules.txt with two short dummy rules, for example "Answer in plain English." and "Use three sentences or fewer."
4. Write rules_test.py: it reads the key only from the environment variable GEMINI_API_KEY and passes it to the client explicitly (genai.Client(api_key=...)), so GOOGLE_API_KEY is never used by accident, and if that variable is missing it stops with a plain message telling me to set it (Part 4 of the series shows how). It never prints, logs or writes the key. It reads rules.txt from the script's own folder as UTF-8, and stops with a plain message if the file is missing or empty. It sends one dummy question to the default model from step 1 with client.interactions.create, passing the rules as system_instruction, prints interaction.output_text, then prints the model name it asked for (Google's docs name no model field on the response, so don't invent one). No temperature setting: Google's page says these models ignore it.
5. Write a .gitignore that covers .env, .env.* and the virtual environment folder.
6. Show me all three files and wait for my yes before saving them. I'll switch you out of plan mode so you can save.
7. Tell me to read every line before I run it, and remind me: on the free tier Google may use what I send to improve its products and human reviewers may see it, so I should send dummy questions only, never personal or confidential information.
Safety: work only in this folder, never put a key in any file, don't run the script yourself, and don't go online except to the two Google pages above.
Output: rules_test.py, rules.txt, .gitignore, and a three-line summary of how to run it, including trying the same question with different rules.
