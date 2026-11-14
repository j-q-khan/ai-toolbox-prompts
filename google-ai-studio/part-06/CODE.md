# Full code: Google AI Studio Build Mode: Make a Web App With Vibe Coding

A checklist written for this video from Google's Build mode, publishing, key and vibe coding pages (checked 2026-11-14). It's a plain text file; there's nothing to install or run, and nothing in it was tested against a real app.

### code-checklist.txt
```
Build mode code checklist (Google AI Studio). Go through it before you share or publish.
Sources, checked 2026-11-14: aistudio.google.com/docs/aistudio-build-mode,
aistudio.google.com/docs/aistudio-deploying, aistudio.google.com/docs/api-key,
aistudio.google.com/docs/terms, cloud.google.com/discover/what-is-vibe-coding

1. The key
   [ ] Search every file in the Code tab for GEMINI_API_KEY. It should appear only in server files.
   [ ] No file in the browser half (the React front end) calls Google directly.
   [ ] No key, password or token is typed into any file. People you share with can see the code.
   [ ] A spend cap and a billing alert are set on the key's account (Part 4).

2. Packages
   [ ] Open package.json. List every package and ask the agent what each one is for.
   [ ] Remove any package nobody can explain.

3. Data
   [ ] List everything the app sends, and where: the Gemini call, any other website, any storage.
   [ ] The app stores nothing personal. Free-tier prompts can be used to improve Google's products.
   [ ] Nothing a visitor types is shown back as HTML (ask the agent to show it as plain text).

4. Behaviour
   [ ] Click through every button yourself. A message saying it's fixed is not a test.
   [ ] Try a wrong input: an empty box, a huge number, a very long text.
   [ ] Ask the agent to explain each file in plain words, then check its answer against the code.

5. Before you publish
   [ ] You know who can open it: Publish gives a public link anyone can open.
   [ ] A published app uses your key for every visitor's Gemini calls (Google's Build page).
   [ ] On a free key, what visitors type falls under the free terms (used to improve Google's products).
   [ ] Users in the UK, Switzerland or the European Economic Area: Google's terms allow only paid services.
   [ ] Google's terms also bar apps aimed at, or likely used by, people under 18.
   [ ] Unpublish apps you stop looking after.
```
