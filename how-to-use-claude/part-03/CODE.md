# Full code: Claude Projects Explained: Set Up Your First Project the Right Way

A Project setup checklist and an instructions template written for this video from Anthropic's own help pages (checked 2026-11-14). Menu names are as the help pages gave them that day; check the linked page if a menu looks different.

### 1. claude-project-setup-checklist.md
```
# Claude Projects: setup checklist (from Anthropic's help pages, checked 2026-11-14)

## Before you start
- [ ] A Claude account. Free can have up to 5 Projects; paid plans list Projects without that cap.
- [ ] One job you repeat (a weekly newsletter, customer replies, a course). One Project per job.

## Create it
- [ ] Click Projects in the sidebar on the left (or go to claude.ai/projects).
- [ ] Click + New Project (top right).
- [ ] Give it a short name and, if you like, a description. Claude can't see either, so put nothing important there.
- [ ] Team or Enterprise only: choose who can see it.

## Add project knowledge (the files)
- [ ] On the right side of the Project's page, click + in project knowledge.
- [ ] Upload what you'd otherwise paste every time: price lists, style notes, examples you like.
- [ ] Each file up to 30 MB, and all the files together must fit what Claude can hold at once (paid plans go further, below).
- [ ] Paid plans: when the files outgrow what Claude can hold at once, it searches them instead (up to 10x more).

## Add project instructions
- [ ] Click Set project instructions, type how Claude should work, click Save instructions.
- [ ] Keep them short. Change them whenever Claude does something you don't like.

## Check it worked
- [ ] Start a new chat inside the Project and ask for the job.
- [ ] The answer uses a fact from your files and follows your instructions, with nothing pasted.

## Avoid the classic mistake
- [ ] A file attached inside one chat stays in that chat. Anything the Project should always know goes in project knowledge.
- [ ] Move an existing chat in: the arrow next to the chat's name, then Add to project.

## Good to know
- [ ] Star it for quick access: the star icon at the top right of the Project puts it in your starred items in the sidebar.
- [ ] Each Project has its own memory. To keep it fully apart, turn off "Use account memory" under Memory on the Project's page.
- [ ] Files in a Project are cached and count less against your usage limit when reused (the cache expires after a while unused).
- [ ] A new version of Projects is in beta, starting in Claude Code. Help pages: support.claude.com
```

### 2. project-instructions-template.txt
```
You're helping with: [the one job, e.g. our weekly customer newsletter]
Who it's for: [the readers, e.g. regular customers of a small bakery]
Style: [e.g. warm, short sentences, British spelling, no jargon]
Always: [e.g. use prices from menu-and-prices.txt; end with our opening hours]
Never: [e.g. invent prices or offers that aren't in the files]
If something's missing from the files, ask me instead of guessing.
```
