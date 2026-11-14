# Claude build prompt: Google AI Studio Build Mode: Make a Web App With Vibe Coding

Part 6 of the Google AI Studio series. Copy everything below the line into Claude Code.
What it builds follows Google's official Gemini API docs (checked 2026-11-14). Try it in a test folder first, and read every file it writes before you use it; it asks before it writes anything, and you run the install yourself. Use a throwaway key with a spend cap and a billing alert, and dummy recipes only.

---

Use this in Claude Code, in a new, empty test folder (never your home folder). Start in plan mode.
Goal: build a tiny recipe-scaler web app with Node.js that calls the Gemini API from the server only, so the key never reaches the browser. It gets my key only from the GEMINI_API_KEY environment variable. Use a throwaway key with a spend cap and a billing alert, and dummy recipes only: no personal or confidential data, because free-tier prompts can be used to improve Google's products.
Steps, in order:
1. Look up Google's quickstart at https://aistudio.google.com/docs/quickstart and tell me, before you write anything, the exact JavaScript call it shows (ai.interactions.create with model and input, and interaction.output_text) and the model it uses. Check https://aistudio.google.com/docs/latest-model for the model labelled "Default general-purpose". If either has changed since 2026-11-14 (gemini-4-hydrogen then), tell me and use the new one.
2. Don't install anything yourself. Give me the exact commands to make a package.json with "type": "module" and to install the only package, @google/genai, with npm install @google/genai, and I'll run them. Use Node's built-in http module for the server, so there's nothing else to install.
3. Write server.js: first it takes the key only from process.env.GEMINI_API_KEY, and if that's missing it stops with a plain message telling me to set it in this terminal window (Part 4 of the series shows how). It passes the key to the client explicitly (new GoogleGenAI with apiKey). It never prints, logs, returns or writes the key, and it never sends it to the browser.
4. The server listens only on 127.0.0.1 and port 3000. It serves one page from a separate public/index.html file at /, and one POST route, /api/scale, that takes JSON with a recipe (at most 4,000 characters) and a number of people (a whole number from 1 to 50), refuses anything else with a plain error, and sends one prompt to the model asking it to rescale the ingredient amounts.
5. public/index.html has a text box, a number box and a Scale button, and calls /api/scale with fetch. It contains no key and no call to Google. It shows the model's answer as plain text, never as HTML.
6. If the Gemini call fails, the server returns a short error without the key or the full error object, and logs only the error code and Google's message, and reminds me that 401 means a missing, wrong or expired key, 403 a permission or billing problem and 429 too many requests.
7. Write a .gitignore that covers .env, .env.*, and node_modules.
8. Show me every file and wait for my yes before saving them. I'll switch you out of plan mode so you can save.
9. Tell me to go through every line before I run it, and give me a short check: search every file for the key name and confirm it only appears in server.js, list the packages in package.json, and confirm nothing I type is saved anywhere.
Safety: work only in this folder, never put a key in any file (the example key EXAMPLE-NOT-A-REAL-KEY is the only key text allowed), don't run the app yourself, don't publish or deploy anything, and don't go online except to the two Google pages above.
Output: server.js, public/index.html, package.json, .gitignore, and a three-line summary of how to run it and open it in my browser at 127.0.0.1 on port 3000.
