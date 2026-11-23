# Full code: AI Chatbot for WhatsApp: Answer Customers Automatically



### 1. whatsapp-bot-instructions.txt
```
# Instructions for a business WhatsApp chatbot. From AI Chatbot, Part 4.
# Facts checked 2026-11-22 from Meta's and Tidio's own pages. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it whatsapp-bot-instructions.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as whatsapp-bot-instructions.txt
# How to use it: swap Test Bakery, +1 555 0100 and test@example.com for your own details. Paste the INSTRUCTIONS part
# where your chatbot takes instructions (in Tidio: Lyro's Guidance, under Behavior; in Meta Business Agent: the
# instructions you add under Tools). Paste the MESSAGES into the matching settings, or keep them for your team.
# Why: Meta's WhatsApp Business Messaging Policy says "You may use automation when responding during the 24-hour window,
# but must also have available prompt, clear, and direct escalation paths" (last updated September 23, 2026).
# This isn't legal advice.

INSTRUCTIONS
You are Test Bakery's WhatsApp assistant. You are an AI, not a person, and you say so in your first reply.
Answer only questions about Test Bakery: opening hours, our cakes and prices, delivery, and how to order.
Answer only from the information Test Bakery has given you. If it isn't there, say you don't know and offer a person.
Never invent prices, hours, addresses, discounts or policies.
Hand the chat to a person when: the customer asks for a person, the question is about a refund, a complaint,
an allergy or a payment problem, or you don't know the answer.
Reply in one message, not several short ones.
Never ask for card numbers, passwords or other private details.
If someone replies STOP, send the opt-out reply and nothing else.

MESSAGES
First reply:
Hi, I'm Test Bakery's assistant, and I'm an AI, not a person. I answer questions about Test Bakery. To talk to someone, call +1 555 0100 or email test@example.com.

Hand-over:
I'll pass you to a person at Test Bakery now. We're here Tuesday to Saturday, 8am to 4pm, and we'll reply in this chat.

Fallback (when it doesn't know):
I don't have that information. Call +1 555 0100 or email test@example.com, and the team will help.

Opt-out reply:
Done. You won't get any more WhatsApp messages from Test Bakery.

OPT-IN WORDING (for your website form or shop counter, before you message anyone)
[ ] Yes, I'd like WhatsApp messages from Test Bakery about my orders and offers. Reply STOP at any time to stop.
# Meta's opt-in rules: "Businesses must clearly state that a person is opting in to receive communication from the
# business." "Businesses must clearly state the business's name that a person is opting in to receive messages from."
```

### 2. whatsapp-setup-checklist.txt
```
# Before you connect WhatsApp: a setup checklist. From AI Chatbot, Part 4.
# Facts checked 2026-11-22 from Meta's, Tidio's and Botpress's own pages. Written from the docs, not run.
# Prices and rules change: check Meta's pricing page and Messaging Policy before you start.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it whatsapp-setup-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as whatsapp-setup-checklist.txt
# How to use it: pick your route, then tick every line under it and under EVERY ROUTE.

ROUTE 1: META BUSINESS AGENT, IN THE WHATSAPP BUSINESS APP
[ ] My number is registered in the WhatsApp Business app
[ ] I can see Meta Business Agent under Tools (Meta: "Available to eligible businesses in select markets")
[ ] I've read what the app says about price before I tap Confirm (Meta's product page shows no price)
[ ] I've added my website, catalog and price lists for it to learn from
[ ] I've tested it like a customer and rewritten any answer I didn't like
[ ] I've flagged topics it must hand to me (refunds, complaints, allergies, payments)

ROUTE 2: A BUILDER ON THE WHATSAPP BUSINESS PLATFORM (for example Tidio)
[ ] The number is owned by my business, has a country and area code, and can receive a call or a text
[ ] It isn't my personal number (Tidio: "You should not use your personal phone number.")
[ ] If the number is on the WhatsApp or WhatsApp Business app: I've checked whether my builder offers what Meta calls
    Coexistence; if it doesn't, I've deleted that WhatsApp account first (Tidio: "Uninstalling the app does not
    release the number.")
[ ] I can log in to Facebook with access to my Meta Business Account (or I'll create one in the signup window)
[ ] I have my company's legal name and official address ready (Tidio asks for both)
[ ] Tidio: Settings, then Channels, then WhatsApp, then Integrate WhatsApp
[ ] Tidio: Lyro has knowledge added, and WhatsApp is switched on in Lyro's Channels section
[ ] Tidio: I know whether Lyro answers always or only when my team is offline (Channels, Live conversations tab)
[ ] Tidio: I know my Lyro allowance (every account gets "50 free Lyro AI conversations", "a one-time quota")
[ ] Botpress or another builder: I know my bot can't send until Meta has verified my business

EVERY ROUTE: PERMISSION, A PERSON, COSTS
[ ] I only message people who gave me their number and agreed to hear from my business (opt-in)
[ ] My opt-in wording names my business and says how to stop (see whatsapp-bot-instructions.txt)
[ ] I stop messaging anyone who asks me to, on or off WhatsApp
[ ] Customers can reach a person: a hand-over in the chat, a phone number, an email or a support form
[ ] The bot answers only about my business, and says it's an AI in its first reply
[ ] I know the limit: since 1 October 2026, Meta gives each business phone number "one free tier of 1,000 delivered
    service messages per month"; past that, a reply only goes out if someone is set up to pay (the next two lines)
[ ] Tidio route: "You are charged by Tidio, not by WhatsApp or Meta directly"; on a paid plan Tidio bills Meta's fees
    at month end with "no markup"; on Tidio for free, sending stops at 1,000 messages a month
[ ] Builder that has me pay Meta directly: a payment method is in Meta's Billing Hub before the bot goes on
[ ] I know the 24-hour customer service window: after it ends I can only send an approved template, and templates
    are charged on their own (Tidio: "Template messages have separate category-based charges.")
[ ] The bot answers in one message, not several short ones
[ ] I've messaged the business number from another phone and checked the answers against my real details
[ ] Someone reads the bot's conversations every week and fixes the information behind wrong answers
```
