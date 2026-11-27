# Research with Claude: a source-check checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.
Written for the video from Anthropic's own pages. Nothing was signed up for, searched or run for it. Settings and plans change, so open each source before you rely on a line. Prices are what the page showed when checked, in US dollars, before tax.

## 1. A research prompt to copy
Search the web. [Your question]. Find studies, research papers and other sources from the last five years. Put a link beside every claim. For each claim, give the exact quote from the source that supports it, and leave out any claim you can't find a quote for. If you're not sure, say so.

- The first line follows Anthropic: "If you want to ensure that Claude uses web search, include "Search the web" or "Use web search" in your prompt to Claude."
- The last two lines follow Anthropic's guide to reducing hallucinations: "have Claude verify each claim by finding a supporting quote after it generates a response. If it can't find a quote, it must retract the claim." and "Explicitly give Claude permission to admit uncertainty."
- Source: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

## 2. Before you ask
- [ ] Web search is on: the "+" button in the lower left corner of the chat window, then "Web search". "A checkmark will appear next to "Web search" when it's enabled."
- [ ] No Web search in that menu? Anthropic: "If you have the new Claude experience, there's no web search toggle. Claude searches the web when it helps."
- [ ] On a Team or Enterprise plan: "An Owner or Primary Owner must first enable web search for the entire workspace in Organization settings" (then Capabilities).
- [ ] Web search is on every plan, Free included (pricing page, "Web search" row). Source: https://support.claude.com/en/articles/10684626-enable-and-use-web-search

## 3. If you use Research
- [ ] Paid plans only: "Research is available for users with paid Claude plans (Pro, Max, Ultra, Team, or Enterprise)". Claude Pro was $20 a month billed monthly, or $17 a month with the yearly plan ($200 billed up front). Source: https://claude.com/pricing
- [ ] Web search is on: "You must have web search turned on for research to function."
- [ ] You checked which connectors are on for this chat (the "+" button, then hover over "Connectors"; each app has its own switch for that conversation): "During research, Claude can use tools from your connectors automatically, without asking for approval each time."
- [ ] Research's report has citations too, so check them the same way as in section 4. Anthropic: "The research feature can synthesize information across multiple sources with proper citations and produces a longer final report."
- [ ] Sources: https://support.claude.com/en/articles/11088861-use-research-on-claude and https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research and https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities

## 4. Check every citation
- [ ] Check 1: click the link. Does the page open? ("Occasionally, website links may not function.")
- [ ] Check 2: search the page for a key word from the claim (in Google Chrome: Ctrl + F on Windows, Command + F on a Mac). Does the sentence around it say what Claude claimed?
- [ ] Is it the same claim, or something smaller, older, or written by someone selling the very thing?
- [ ] Note the date on the page, and who published it. Anthropic: "Use authoritative sources for critical decisions."
- [ ] Keep it, rewrite the claim to match its source, or drop it.
- [ ] Why: "Claude can write things that might look correct but are very mistaken." and "When working with web search results, users should review Claude's cited sources." Source: https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on

My citations (fill in):
| No. | Claim | Link | Opens? | Says what's claimed? | Who published it | Date on the page | Date I checked | Keep, rewrite or drop |
|---|---|---|---|---|---|---|---|---|
| 3 (example) | Most customers pay more for local flowers | town-survey.example | yes | partly: one town's shoppers only | a made-up town survey | 2025 | 2026-11-26 | rewrite |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

## 5. Before you use the answer
- [ ] Every claim you're keeping has a citation that opens and says it.
- [ ] For a rule your business has to follow, you opened the official source itself.
- [ ] Nothing went into a customer email or a money decision before these checks. Anthropic: "Users should not rely on Claude as a singular source of truth and should carefully scrutinize any high-stakes advice given by Claude."
