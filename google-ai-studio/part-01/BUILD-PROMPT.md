# Claude build prompt: Google AI Studio Tutorial for Beginners (2026): Your First Prompt

Part 1 of the Google AI Studio series. Copy everything below the line into Claude Code.
What it builds follows Google's official Gemini API docs (checked 2026-11-13). Try it in a test folder first, and read every file it writes before you use it; it asks before it writes anything, and you run the install yourself.

---

Use this in Claude Code, in a new, empty test folder (never your home folder). Start in plan mode.

Goal: build a tiny Python app that sends one question to the Gemini API and prints the answer, so I can see what Get code in Google AI Studio leads to. Use a throwaway key with a spend cap, and dummy questions only.
Steps, in order:
1. Look up Google's current Gemini API quickstart at https://aistudio.google.com/docs/quickstart and tell me the model name Google labels "Default general-purpose" on https://aistudio.google.com/docs/latest-model today, and the exact Interactions call it shows (client.interactions.create and interaction.output_text). If the page has changed, tell me what changed before you write anything.
2. Don't install anything yourself. Give me the exact commands to make a virtual environment in this test folder and install the only package, google-genai (pip install -U google-genai), and I'll run them.
3. Write first_prompt.py: it reads the key only from the environment variable GEMINI_API_KEY and passes it to the client explicitly (genai.Client(api_key=...)), so GOOGLE_API_KEY is never used by accident, and if that variable is missing it stops with a plain message telling me to set it (Part 4 of the series shows how). It never prints, logs or writes the key. It asks me for one question in the terminal, sends it to the default model from step 1 with the Interactions call, and prints only the answer text.
4. Write a .gitignore that covers .env, .env.* and the virtual environment folder.
5. Show me both files and wait for my yes before saving them. I'll switch you out of plan mode so you can save.
6. Tell me to read every line before I run it, and remind me: on the free tier Google may use what I send to improve its products and human reviewers may see it, so I should type dummy questions only, never personal or confidential information.
Safety: work only in this folder, never put a key in any file, don't run the app yourself, and don't go online except to the two Google pages above.
Output: first_prompt.py, .gitignore, and a three-line summary of how to run it.
