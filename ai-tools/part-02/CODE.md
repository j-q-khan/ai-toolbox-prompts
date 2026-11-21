# Full code: Free AI Tools: What You Really Get Without Paying

The limits sheet and the two made-up test files for this video, written from each company's own pages (checked 2026-11-21). They were written from the docs, not run for this video.

### 1. limits-without-paying.md
```
# What you get without paying: the limits sheet (facts checked 2026-11-21)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as limits-without-paying.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every line below is from the company's own page on 2026-11-21, in its own words where quoted. Nothing was signed up for, installed or run. Plans and limits change often: check each page before you rely on it. "Free" and "unlimited" appear here only inside a company's own words.

| Tool (maker) | What the plan you don't pay for gives, in the maker's words | The catch | Where you see it | Source |
|---|---|---|---|---|
| ChatGPT (OpenAI) | "ChatGPT is free to use." "Free users have unlimited everyday text chats, subject to abuse-prevention safeguards." | "Limited messages with uploads", "Limited image creation", "Limited voice chats", "Limited deep research"; "Ads may appear in the Free tier in certain countries." | "ChatGPT will notify you when you reach an applicable limit." | https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq and https://chatgpt.com/pricing |
| Claude (Anthropic) | "$0", "Free for everyone" | "Limited usage every 5 hours and every week"; "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are." Uploads: 500MB per file, up to 20 files per chat. | No message count is published | https://claude.com/pricing |
| Gemini (Google) | "$0 / month with a Google Account": "Image generation and editing", "Deep Research", "Gemini Notebook" | "Your limit refreshes every 5 hours until you reach your weekly limit."; a "daily quota" of images, no number; up to 10 files in one prompt, 100 MB each, video 2 GB | No message count is published | https://gemini.google/us/subscriptions/?hl=en |
| Microsoft Copilot (Microsoft) | "a limited free version of Copilot" | "subject to available capacity and limits"; "When you hit a limit, you can choose to upgrade to a paid option or come back later." | When you hit a limit | https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals |
| Perplexity (Perplexity) | Free "includes basic searches, three Pro Searches (more thorough, multi-step searches) a day, and one Research query (a full report on a complex topic) a month." (blog, 13 October 2026) | "File uploads are not unlimited on Free, Pro, or Max plans."; the allowance "resets on a rolling weekly basis" | 3 Pro Searches a day, 1 Research query a month | https://www.perplexity.ai/hub/blog/ai-costs |
| Gemini Notebook, was NotebookLM (Google) | "Gemini Notebook without an AI plan": "Sign up at no charge by using your gmail account." | 100 notebooks, 50 sources per notebook (not counting notes); "the quota refreshes every 5 hours until you reach your weekly limit" | Settings at the top right, then Usage; a message at the bottom of the chat | https://support.google.com/notebooklm/answer/16213268 and https://support.google.com/gemininotebook/answer/17670842 |
| Notion AI (Notion) | "Trial of Notion AI" (Free and Plus plans) | After the trial: "an upgrade to the Business or Enterprise Plan is necessary to continue using AI features"; "Anytime you click Try again, that counts as an additional AI response." | A message when the trial is used up | https://www.notion.com/help/complimentary-ai-responses and https://www.notion.com/pricing (prices shown in euros when checked) |

## The first paid step (US prices, was this when checked, 2026-11-21)
| Plan | Price | In the maker's words | Source |
|---|---|---|---|
| Google AI Plus | $4.99 a month | "Get double the usage limits" | https://gemini.google/us/subscriptions/?hl=en |
| ChatGPT Go | $8 a month | "This plan may include ads." | https://learn.chatgpt.com/docs/pricing |
| Microsoft 365 Personal | $9.99 a month ($6.99 first-month offer) | "higher usage than free" | https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals |
| Google AI Pro | $19.99 a month | | https://gemini.google/us/subscriptions/?hl=en |
| ChatGPT Plus | $20 a month | | https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus |
| Claude Pro | $20 a month, or $17 a month billed yearly ($200 up front) | "More usage than Free" | https://claude.com/pricing |
| Perplexity Pro | $20 a month (Perplexity's blog, October 2026) | | https://www.perplexity.ai/hub/blog/ai-costs |

## Before you pay
- [ ] Is the same limit stopping the same job every week?
- [ ] Is it in the one app you use most?
- [ ] Is there a smaller paid step that lifts that limit?
- [ ] Have you checked the company's own pricing page today?
- [ ] In ChatGPT, is it "Chat memory full"? Start a new chat and paste only the paragraph you're working on.
```

### 2. test-limits.csv
```
# Made-up limits for trying the build prompt. Only the two Perplexity lines are real numbers (Perplexity's blog, 13 October 2026); every other number is made up, because those companies publish no count.
# To keep a copy: paste this into Notepad and save it as test-limits.csv with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you: the script skips them.
tool,what,limit,period,note
Perplexity,Pro Search,3,day,From Perplexity's blog
Perplexity,Research query,1,month,From Perplexity's blog
Claude,long chats,6,day,Made-up number: Anthropic publishes no count
Gemini,pictures,10,day,Made-up number: Google publishes no count
Notion AI,AI responses,20,month,Made-up number: Notion publishes no trial size
```

### 3. test-usage.csv
```
# A made-up usage log for Test Bakery, for trying the build prompt. Change the dates to this week's to see warnings.
# To keep a copy: paste this into Notepad and save it as test-usage.csv with the box called Save as type set to All files. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# The lines starting with # are notes for you: the script skips them.
date,tool,what,count,used_for
2026-11-20,Perplexity,Pro Search,2,Checking flour storage advice
2026-11-21,Perplexity,Pro Search,3,Comparing oven cleaning methods
2026-11-21,Perplexity,Research query,1,Report on bank holiday opening rules
2026-11-21,Claude,long chats,5,Drafting the supplier email and the rota
2026-11-21,Gemini,pictures,4,Pictures of a loaf for the website
2026-11-19,Notion AI,AI responses,12,Summarising staff meeting notes
2026-11-21,ChatGPT,text chats,9,Everyday questions
```
