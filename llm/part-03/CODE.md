# Full code: LLM Models Compared: Which Is Best, and How to Read the Rankings

The model-picking checklist from this video, written from the ranking sites' and makers' own pages, checked 2026-11-23. It was written from the docs, not run.

### model-picking-checklist.md
```
# Model-picking checklist (facts checked 2026-11-23)
# From the video LLM Models Compared: Which Is Best, and How to Read the Rankings
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as model-picking-checklist.md.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Rankings and prices change. Everything below is as written when checked, on 2026-11-23. Check each page again on your day.

## 1. Your task
- [ ] What's the job? Chat and writing / coding / an app answering lots of small requests / something else.
- [ ] How will you use it? A chat app (a monthly plan) or the API (you pay per million tokens, in and out).

## 2. Your budget
- [ ] API prices per million tokens, in / out, when checked, on 2026-11-23:
  - Claude Opus 5.5: $4 / $20 (platform.claude.com/docs/en/about-claude/pricing)
  - Claude Haiku 5.5: $0.10 / $0.50 for prompts up to 100,000 tokens; $0.50 / $2.50 over that
  - GPT-6.2 Astra: $8 / $40; GPT-6 Luna: $0.10 / $0.50 (developers.openai.com/api/docs/pricing, short context, up to 272K input tokens)
  - Gemini 4 Carbon: $2 / $10 through 30 November 2026, then $4 / $20 from 1 December 2026 (aistudio.google.com/docs/pricing)
  - Gemini 4 Hydrogen: $1.50 / $7.50; its free tier was listed as "Free of charge"
  - DeepSeek V4 Pro: $1.32 / $3.96 in peak hours; "Off-peak rates are half of the peak rates." (api-docs.deepseek.com/quick_start/pricing)
- [ ] Lots of small, repeated jobs? Start with the small model. Anthropic calls Claude Haiku 5.5 "For high-volume, latency-sensitive tasks"; OpenAI calls GPT-6 Luna "Our most efficient model for focused, high-volume tasks."
- [ ] Don't need answers straight away? Anthropic's Batch API: "a 50 percent discount on both input and output tokens".

## 3. Your privacy
- [ ] Must what you type stay on your own computer? Only a model whose files you download and run yourself does that.
- [ ] Any company's API, DeepSeek's included, receives what you send it.
- [ ] Open doesn't mean small: DeepSeek-V4-Pro's model card lists "1.6T parameters", far beyond a home computer. For models that fit 8 or 16 GB, see the Run Open Models series: https://youtu.be/KFtS8D7-yus

## 4. Which board to check
- [ ] Arena (arena.ai/leaderboard), formerly LMArena: blind votes. "Only votes made while the models are anonymous count toward official rankings". Check the board for your job (Text, WebDev and others).
- [ ] Artificial Analysis (artificialanalysis.ai): its own tests. Intelligence Index v5.0.1: "Knowledge Work (25%), Coding (25%), Science (25%), and General (25%)".
- [ ] Skip Hugging Face's Open LLM Leaderboard: "the leaderboard is officially retiring!" (13 March 2025).
- [ ] When checked, on 2026-11-23: Arena's text board top was Gemini 4 Carbon (High). Artificial Analysis's index top was Claude Fable 5.2 (Max), 65, and each maker's best was Anthropic 65, OpenAI 62, Google 61. These change often: check the date on the board you look at.

## 5. What a board can't tell you
- [ ] Whether it's right for your job: votes show which answer people preferred, not whether it was right.
- [ ] Whether a gap matters: a few points apart is a tie.
- [ ] Whether it's current: check the date, and whether the test set changed ("GDPval-AA was removed from the Intelligence Index in v5.0").
- [ ] What it costs you, and where your data goes: check the maker's pricing page and terms yourself.

## Sources (all fetched 2026-11-23)
- arena.ai/faq ; arena.ai/blog/lmarena-is-now-arena ; arena.ai/leaderboard/text
- artificialanalysis.ai/methodology/intelligence-benchmarking ; artificialanalysis.ai/leaderboards/models
- huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/1135
- platform.claude.com/docs/en/about-claude/models/overview ; platform.claude.com/docs/en/about-claude/pricing
- developers.openai.com/api/docs/models ; developers.openai.com/api/docs/pricing
- aistudio.google.com/docs/models ; aistudio.google.com/docs/pricing
- api-docs.deepseek.com/quick_start/pricing ; huggingface.co/deepseek-ai/DeepSeek-V4-Pro
```
