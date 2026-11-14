# Claude build prompt: How to Use Nano Banana Pro in Google AI Studio: Make and Edit Images

Part 5 of the Google AI Studio series. Copy everything below the line into Claude Code.
What it builds follows Google's official Gemini API docs (checked 2026-11-13). Try it in a test folder first, and read every file it writes before you use it; it asks before it writes anything, and you run the install yourself. Nano Banana Pro is not on the free tier, so every picture costs money.

---

Use this in Claude Code, in a new, empty test folder (never your home folder). Start in plan mode.
Goal: build a tiny Python app that makes one picture with Nano Banana Pro through the Gemini API, tells me what it will cost before it sends anything, and saves the picture in this folder. It gets my key only from the GEMINI_API_KEY environment variable. Use a throwaway key with billing on, a spend cap and a billing alert, and dummy prompts only: no photos of real people, no real brands.
Steps, in order:
1. Look up two Google pages and tell me what you find before you write anything: the model name and the Python example for client.interactions.create with response_format and output_image on https://aistudio.google.com/docs/image-generation, and the Nano Banana Pro prices on https://aistudio.google.com/docs/pricing (per picture at 1K, 2K and 4K, the text and thinking price, the input picture price, and whether the free tier still says "Not available"). If the model name or a price has changed, tell me and use the new one.
2. Don't install anything yourself. Give me the exact commands to make a virtual environment in this test folder and install the only package, google-genai, with pip install -U google-genai, and I'll run them.
3. Write image_app.py: first it reads the key only from the environment variable GEMINI_API_KEY, and if that's missing it stops with a plain message telling me to set it in this terminal window (Part 4 of the series shows how). It passes the key to the client explicitly (genai.Client(api_key=...)). It never prints, logs or writes the key.
4. It takes a prompt and a size (1K, 2K or 4K, always with a capital K; default 2K) and an aspect ratio (default 1:1) from the command line, checks them against the lists on Google's page, and refuses anything else.
5. Before sending, it prints the model, the size and the price from step 1 for one picture, says that thinking is charged on top, and waits for me to type yes. Anything else stops it with "Nothing was sent."
6. It sends one request to the model with client.interactions.create and response_format type image, then saves output_image (or, if that's empty, the first image block in interaction.steps, as Google's gemini-3-pro-image example reads it) to a new file in this folder with a name that never overwrites an existing file. If no image comes back, or the request fails, it prints the error code and Google's message without the key, and reminds me that 401 means a missing, wrong or expired key, 403 a permission or billing problem, 429 too many requests, and that Nano Banana models aren't on the free tier.
7. Write a .gitignore that covers .env, .env.*, the virtual environment folder and *.png.
8. Show me both files and wait for my yes before saving them. I'll switch you out of plan mode so you can save.
9. Tell me to read every line before I run it, and remind me: every picture costs money (say the price again), every picture carries an invisible SynthID watermark, and Google's Prohibited Use Policy applies, so no fake pictures of real people or events, and only photos I have the rights to.
Safety: work only in this folder, never put a key in any file (the example key EXAMPLE-NOT-A-REAL-KEY is the only key text allowed), don't run the app yourself, and don't go online except to the two Google pages above.
Output: image_app.py, .gitignore, and a three-line summary of how to run it, with one example command that uses a dummy prompt.
