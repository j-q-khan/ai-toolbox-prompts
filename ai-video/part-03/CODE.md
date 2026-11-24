# Full code: AI Video Free: What the Free AI Video Generators Really Give You

The free-plan checklist and the two spreadsheet files for this video, written from the makers' own pages (checked 2026-11-23). They were written from the docs, not run, and nothing was generated for this video.

### 1. free-ai-video-plans-checklist.md
```
# What the free AI video plans really give you: checklist (facts checked 2026-11-23)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files, as free-ai-video-plans-checklist.md. On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Every quote below is from the maker's own page on 2026-11-23. Nothing was signed up for, run or generated. Plans, credits and prices change: check each page on the day you sign up.

## Four questions to ask any plan you don't pay for
- [ ] Do the credits come back (daily), or do you get one batch (once)? Do they expire?
- [ ] What can the plan make? Is the model you want on it?
- [ ] Is there a watermark on what you download?
- [ ] Can you sell what you make on this plan (commercial use)?

## Flow (Google)
- [ ] Credits: "With no subscription, you receive only 50 Google Flow credits per day". Unused credits "don't roll over". https://support.google.com/flow/answer/16526234
- [ ] Makes: "Access basic video generation"; "All users can access Omni Flash models"; 3 to 10 s without a subscription. https://support.google.com/flow/answer/16352836
- [ ] Peak hours: "roughly 2 PM to 5 PM UTC, you may not be able to generate videos without a subscription."
- [ ] Watermark: invisible SynthID on every output; a visible one via the "Visible watermarking" toggle under your profile picture, automatic in India, South Korea and Vietnam unless on the Ultra 20x plan. https://support.google.com/flow/answer/16353333
- [ ] Selling: the help page quotes only "Google won't claim ownership over that content". Check Google's terms: https://policies.google.com/terms
- [ ] First paid step, when checked: Google AI Plus "$4.99 / month", plus 200 Flow credits a month. https://gemini.google/us/subscriptions/?hl=en

## Kling
- [ ] Credits: "Claim your daily free credits on KlingAI" (no amount given). Basic: "free forever", "No monthly Credits". https://kling.ai/explore/kling_ai_daily_free_credits
- [ ] Watermark: "free-tier exports generally include a watermark. Watermark removal is a membership benefit."
- [ ] Selling: Basic "generated content is not for commercial use" (credit guide, July 28, 2026); the same guide lists Standard, Pro, Premier and Ultra as "generated content is for commercial use". Terms: "without our written permission, you may not use ... the Output for any commercial purposes." https://kling.ai/docs/user-policy
- [ ] Price: the live plan page didn't load for us; check it yourself.

## Runway
- [ ] Credits: "125 one-time credits"; "a one-time deposit of 125 credits that doesn't expire". https://runway.com/pricing
- [ ] Makes: "Users can create images and voiceovers ... and work with existing video through upscaling and scene building". Gen-4.5 is listed on Standard and up, not Free. "Runway shows the total cost before you generate."
- [ ] Watermark: "Images made on the Free plan carry a small Runway watermark." Standard lists "No watermarks".
- [ ] Selling: "Can I use the output commercially? Yes." "you own your work on every plan, including the Free plan." https://runway.com/product/ai-video-generator
- [ ] First paid step, when checked: Standard $15 a month, or $12 a month billed yearly, 625 credits a month.

## Hailuo (MiniMax)
- [ ] Credits: "a one-time welcome package of free credits. These credits will expire three days after being granted." (terms last updated 7/14/2025) https://hailuoai.video/doc/payment-policy.html
- [ ] Watermark: "Free Users : Video downloads will include a watermark."
- [ ] Selling: "personal, non-commercial use only" (terms last modified 08/19/2026). https://hailuoai.video/doc/terms-of-service.html The older paid terms (7/14/2025) say that on a paid plan "you retain any and all intellectual property rights to such content, including the right to use it for commercial purposes."
- [ ] Price: no current price page loaded for us; check it yourself.

## Luma
- [ ] Credits: no unpaid plan on the pricing page; "Free trial credits included on all plans". https://lumalabs.ai/llm-info
- [ ] Selling: only Outputs "produced during an active Subscription Term under Customer's paid subscription"; trial output "may only be used for your internal evaluation and testing". Trials run "during the period designated by Luma (not to exceed 14 days unless otherwise agreed upon by the parties in writing)"; the terms don't say whether that covers the trial credits. https://lumalabs.ai/legal/terms-of-service
- [ ] Watermark: Luma may "embed watermarks"; you may not remove them.
- [ ] First paid step, when checked: Plus $30 a month, or $25 a month billed yearly, "Commercial use". https://lumalabs.ai/pricing
```

### 2. plans.csv
```
# The five plans from this video, for the Claude build prompt (facts checked 2026-11-23).
# To keep a copy: paste this into Notepad and save it as plans.csv with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Lines starting with # are notes for you, and the script skips them. Empty allowance = the maker doesn't say: fill in what your account shows.
# renews: daily, once or trial. started: the date you got the credits (YYYY-MM-DD), so expiry counts from it. commercial: yes, no or check.
generator,plan,allowance,renews,started,expires_after_days,watermark,commercial
Flow,no subscription,50,daily,,,invisible SynthID and a visible toggle,check
Kling,Basic,,daily,,,generally on free-tier exports,no
Runway,Free,125,once,,,on Free plan images,yes
Hailuo,free user welcome package,,once,,3,on free downloads,no
Luma,trial credits,,trial,,,may be built in,no
```

### 3. usage.csv
```
# Made-up practice rows for the Claude build prompt: replace them with your own.
# To keep a copy: paste this into Notepad and save it as usage.csv with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# date is YYYY-MM-DD. for_sale is yes or no.
date,generator,credits_spent,for_sale,what
2026-11-23,Flow,5,no,candle test at 360p
2026-11-23,Flow,15,yes,candle clip at 720p for a shop ad
2026-11-23,Runway,60,no,first test
2026-11-23,Hailuo,10,yes,beach clip for a reel
```
