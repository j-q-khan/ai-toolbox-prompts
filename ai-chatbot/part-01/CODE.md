# Full code: AI Chatbot for Your Website: How to Make One, and Which Kind to Pick



### 1. which-kind-checklist.txt
```
# Which kind of website chatbot? A checklist. From AI Chatbot, Part 1.
# Facts checked 2026-11-22 from the makers' own pages. Written from the docs, not run. Prices change: check each pricing page.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it which-kind-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as which-kind-checklist.txt
# How to use it: go down the three kinds, and pick the first one where every line is true for you.
# Then work through "Before it goes on your site" and tick every line.

KIND 1: A HOSTED CHATBOT BUILDER (the place most small businesses start)
[ ] I want it working this week, with nothing to install
[ ] I don't want to look after a server
[ ] I've checked the plan limits on the pricing page (for example: Tidio, Botpress, Chatbase, Intercom Fin)
[ ] I know what happens when I hit the limit (Botpress Free says "No top-ups or overages"; Tidio's 50 free Lyro conversations don't renew)

KIND 2: A PLUGIN FOR MY SITE'S SOFTWARE (for example, on WordPress)
[ ] My site runs on WordPress and I can install plugins
[ ] AI Engine (Meow Apps): I'm happy to sign up with an AI provider and pay them directly ("Its chatbots use your own API keys")
[ ] AI Engine: I know answering from my own site is Pro ("Get Pro, from $59/year" when checked)
[ ] Or Tidio's official plugin: I'll connect it to a Tidio account

KIND 3: ONE I HOST MYSELF (AI Chatbot, Parts 2 and 3: AnythingLLM and Dify)
[ ] I'm comfortable typing commands in a terminal
[ ] I'll keep the server running, backed up and updated
[ ] I've read the tool's licence, in the maker's own words

BEFORE IT GOES ON YOUR SITE (every kind)
[ ] It learns from my real pages: opening hours, prices, delivery, returns
[ ] Every file has selectable text (if I can't highlight the words, the bot can't use them)
[ ] My most-asked questions are added as question-and-answer pairs
[ ] I've tested 10 questions customers really send me, and checked every answer against my site
[ ] I've tested a question that isn't on my pages, and it says it doesn't know
[ ] Its first message says it's an AI, not a person (see first-message.txt)
[ ] It gives a way to reach a real person (email, phone or a form)
[ ] My AI provider key is never pasted into a web page or the embed code
[ ] Someone goes through its conversations every week and fixes the pages behind wrong answers
```

### 2. first-message.txt
```
# A first message, a fallback reply and a hand-over line for a website chatbot. From AI Chatbot, Part 1.
# Facts checked 2026-11-22. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it first-message.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as first-message.txt
# How to use it: swap Test Bakery, test@example.com and +1 555 0100 for your own business name and contact details,
# then paste each line into your chatbot builder's settings for its first message, its fallback reply and its hand-over.
# Why: the EU AI Act, Article 50(1), asks providers to make sure people "are informed that they are interacting with
# an AI system, unless this is obvious" (enforceable from 2 August 2026). This isn't legal advice.

FIRST MESSAGE
Hi, I'm Test Bakery's assistant, and I'm an AI, not a person. I answer from our website, and if you'd rather talk to someone, email test@example.com.

FALLBACK REPLY (when it doesn't know)
I don't have that information. Email test@example.com or call +1 555 0100 and the team will help.

HAND-OVER LINE (when the visitor asks for a person)
Of course. Leave your question and an email address here, or email test@example.com, and a person from Test Bakery will reply.
```
