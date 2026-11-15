# Full code: Claude Research Mode: When to Use It and How to Get a Good Report

A research request template and a source-check checklist written for this video from Anthropic's own help pages (checked 2026-11-14). Menu names are as the help pages gave them that day; check the linked page if a menu looks different.

### 1. research-request-template.txt
```
# Claude Research request template (from Anthropic's help pages, checked 2026-11-14)
# Turn on Research first: the + button at the bottom left of the chat, then Research
# (newer layout: you can also type /deep-research). Paid plans: Pro, Max, Ultra, Team, Enterprise.

Who I am and what I'm deciding: [e.g. a small bakery choosing between a deck, convection and combi oven]
What to compare: [e.g. running costs, space, upkeep, the breads each suits]
How to lay it out: [e.g. a three-sentence summary, a comparison table, the risks, a numbered source list]
Sources to favour: [e.g. makers' spec sheets and trade guides]
Sources to avoid or limits: [e.g. nothing older than two years; public web only]
What to work from: [e.g. "search the public web only" or "also check my connected apps" (web or desktop only)]
After the report: list the three claims the decision depends on most, each with its source.

# Filled-in example (made up):
# We're a small bakery choosing between a deck oven, a convection oven and a combi oven.
# Compare them on running costs, space, upkeep and the breads and pastries each suits.
# Give me a short summary, a comparison table and the main risks to check before buying.
# Favour makers' spec sheets and trade guides. Search the public web only.
```

### 2. research-source-check.md
```
# Checking a Claude Research report (from Anthropic's help pages, checked 2026-11-14)

## Before you start
- [ ] A paid plan (Pro, Max, Ultra, Team or Enterprise). On Free, use a normal chat with web search.
- [ ] Web search on: a checkmark next to Web search in the + menu (the newer layout has no toggle).
- [ ] Team or Enterprise: an Owner has turned on web search in Organization settings, then Capabilities.

## While it runs
- [ ] The blue indicator shows at the bottom of the chat window. Click it again to turn Research off.
- [ ] Answer any follow-up questions Claude asks before it starts.
- [ ] Research counts toward your usage limits and can use them up faster than a normal chat.

## When the report is back
- [ ] Pick the two or three claims your decision really rests on.
- [ ] Click the citation beside each one and check the page says the same thing.
- [ ] A link won't open? It happens; find the page another way before you rely on it.
- [ ] For an important decision, check it against a trusted source as well.

## Good to know
- [ ] Research runs on Claude Opus 5.5 (falls back to Opus 4.8), whatever model you picked.
- [ ] Started on a phone? It searches the web only and skips your connected apps, with no warning.
- [ ] During Research, Claude can use your connectors' tools without asking each time. Turn off any you don't want used.
- [ ] Not researching? Type: "Claude, please use the research tool to..." and your question.
- [ ] Help page: support.claude.com, Use research on Claude.
```
