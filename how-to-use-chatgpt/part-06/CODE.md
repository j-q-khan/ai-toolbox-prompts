# Full code: ChatGPT Free vs Go vs Plus: Which Plan Is Worth Paying For in 2026?

The plan checklist and the fill-in plan table, written from OpenAI's pricing and help pages (checked 2026-11-22), not run. Nothing was bought, signed up for or generated for this video.

### 1. chatgpt-plan-checklist.txt
```
# ChatGPT plan checklist: Free, Go, Plus or Pro?
# From How to Use ChatGPT, Part 6. Facts checked 2026-11-22 from OpenAI's pricing and help pages. Written from the docs, not run.
# How to save this file:
#   Windows: open Notepad, paste this text, choose File, Save as, set the box called Save as type to All files,
#   and name it chatgpt-plan-checklist.txt
#   Mac: open TextEdit, choose Format, Make Plain Text, paste this text, and save it as chatgpt-plan-checklist.txt
# How to use it: tick each line that's true for you. If any line under Go, Plus or Pro is ticked,
#   start with the highest of those plans and check it against the others; stay on Free only if
#   every Free line is ticked and nothing below it is.
# Plans and limits change: check https://chatgpt.com/pricing on the day you decide.

STAY ON FREE IF ALL OF THESE ARE TRUE
[ ] I mostly chat. (Free: "unlimited everyday text chats, subject to abuse-prevention safeguards")
[ ] Three file uploads a day is enough. (Free: "limited to 3 file uploads per day")
[ ] I make the odd picture. (Free: "Limited image creation")
[ ] I paste in less than about 12 pages of text at once. (Free, with Instant: "~12 pages of text")
[ ] Five files in each project is enough. (Free: 5 files per project)
[ ] Ads may appear, and that's fine with me. (Free and Go: "Ads may appear")

GO IS WORTH A LOOK IF ANY OF THESE ARE TRUE
[ ] Free's upload limit keeps stopping me. (Go: "More uploads")
[ ] I want more pictures. (Go: "More image creation")
[ ] I paste in long documents, up to about 40 pages at once. (Go, with Instant: "~40 pages of text", the same as Plus)
[ ] I want up to 25 files in each project. (Go and Plus: 25 files per project)
[ ] Ads may appear, and that's still fine with me.

PLUS IS WORTH A LOOK IF ANY OF THESE ARE TRUE
[ ] I want ChatGPT to think harder: the Medium and High stops on the Thinking slider. (Plus: "Medium and High: Included". Free and Go: "Not included")
[ ] I want no ads at all. ("Plus, Pro, Business, Enterprise, and Edu accounts will not have ads.")
[ ] I want "More complex and accurate image creation".
[ ] I want ChatGPT Work on the web and phone, not only the desktop app. (Free and Go: "Limited (desktop app)")
[ ] I want three hours of voice in a rolling 24 hours. (Plus: "3 hours". Go: OpenAI's pages disagree)

PRO IS WORTH A LOOK ONLY IF ANY OF THESE ARE TRUE
[ ] I'm on Plus and its limits stop me most days.
[ ] I need the Extra High or Pro stops on the Thinking slider. (Plus: "Not included")
[ ] I paste in more than about 40 pages at once. (Pro, with Instant: "~250 pages of text")
[ ] I want up to 40 files in each project.
[ ] Remember: "A Pro subscription does not include unlimited use of the GPT-6 Pro model."

BEFORE YOU PAY
[ ] I checked today's prices on https://chatgpt.com/pricing. (When checked on 2026-11-22, Free was $0, Go was $8 a month, Plus was $20 a month, Pro was $100, $200 or $500 a month, in US dollars.)
[ ] I know there's no yearly billing for Go, Plus or Pro: it's month by month.
[ ] I know that switching from Plus down to Go keeps Plus until the end of the billing cycle, with no refund. (Profile icon, then Settings, then Account)
[ ] Not sure? Fill in the last column of chatgpt-plans.csv (yes or no on each row) and use the build prompt to make a comparison page.
```

### 2. chatgpt-plans.csv
```
need,Free,Go,Plus,Pro,lowest_plan,source,checked,i_need_this
Everyday text chats,"Unlimited, subject to abuse-prevention safeguards","Unlimited, subject to abuse-prevention safeguards",Unlimited*,Unlimited*,Free,"Free tier FAQ; pricing page (*Usage must be reasonable and comply with our policies)",2026-11-22,
More than 3 file uploads a day,Limited to 3 file uploads per day,More uploads,Expanded messages and uploads,Yes,Go,Uploading files; pricing page,2026-11-22,
More pictures than Free,Limited image creation,More image creation,More complex and accurate image creation,"Unlimited and faster image creation (Unlimited subject to abuse guardrails)",Go,pricing page,2026-11-22,
Paste in more than about 12 pages at once,~12 pages of text,~40 pages of text,~40 pages of text,~250 pages of text,Go,"pricing page, GPT Instant input maximum (an approximation)",2026-11-22,
Paste in more than about 40 pages at once,~12 pages of text,~40 pages of text,~40 pages of text,~250 pages of text,Pro,"pricing page, GPT Instant input maximum (an approximation)",2026-11-22,
More than 5 files in a project,5 files per project,25 files per project,25 files per project,40 files per project,Go,Projects in ChatGPT,2026-11-22,
More than 25 files in a project,5 files per project,25 files per project,25 files per project,40 files per project,Pro,Projects in ChatGPT,2026-11-22,
More memory than Free,Limited memory and context,Longer memory,Expanded memory and context,Maximum memory and context,Go,pricing page,2026-11-22,
The Medium and High thinking stops,Not included,Not included,Included,Included,Plus,GPT-6 and other models in ChatGPT,2026-11-22,
The Extra High and Pro thinking stops,Not included,Not included,Not included,"Included (not unlimited use of GPT-6 Pro)",Pro,GPT-6 and other models in ChatGPT,2026-11-22,
No ads,Ads may appear,Ads may appear,Will not have ads,Will not have ads,Plus,Ads in ChatGPT,2026-11-22,
Three hours of voice in a rolling 24 hours,"Limited access, limits may change","Pages disagree: 3 hours, or the same as Free",3 hours,"More (15 hours on Pro 100; Unlimited, subject to abuse guardrails, on Pro 200)",Plus,ChatGPT Voice; What is ChatGPT Go,2026-11-22,
ChatGPT Work on the web and phone,Limited (desktop app),Limited (desktop app),"Desktop, web, and mobile","Desktop, web, and mobile",Plus,pricing page,2026-11-22,
"Price a month (was, when checked, US dollars)",$0,$8,$20,"$100, $200 or $500",,"learn.chatgpt.com/docs/pricing; About ChatGPT Pro tiers",2026-11-22,
```
