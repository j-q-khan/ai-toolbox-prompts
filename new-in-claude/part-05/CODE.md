# Full code: Claude Update: Claude Whiteboards, Plan a Project on a Shared Board

The whiteboard request prompt, the made-up brainstorm and the setup checklist, written from Anthropic's help pages "Get started with Claude Whiteboards", "Share artifacts", "What are artifacts and how do I use them?", "Artifacts admin guide for Team and Enterprise plans" and "Use Claude Meetings" (checked 2026-11-26). They were written from the docs, not run for this video.

### 1. claude-whiteboards-plan-prompt.txt
```
# Paste the request below into any Claude chat, or go to the Artifacts tab, select the Whiteboards tile (labelled Whiteboard), and paste it there.
# Or select the microphone next to the send button and say it. To stop, select the microphone again or press Escape, then send.
# Claude Whiteboards is a beta on Pro, Max, Ultra, Team and Enterprise plans. Written from Anthropic's help page, Get started with Claude Whiteboards, checked 2026-11-26.
# The lines starting with # are notes for you: don't paste them.
# Fill in the parts in brackets. Claude works from what's on the board and doesn't use context from your connected apps, so put the dates and details in the request.
# Use made-up or approved details only. Remove anything private first.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Start a whiteboard to plan [what you're planning], with [the parts of the plan, separated by commas].
Group related ideas, put the steps in order, and connect the ones that depend on each other.

# Example, made up (the one in the video):
# Start a whiteboard to plan Test Bakery's summer menu, with three new drinks, a tasting day, posters and a price list.

# Then, on the board:
# Find the gaps. For example:
What's missing between the tasting day and the posters?
# Reorganize. For example:
Regroup the board by theme.
# Or:
Turn this board into a timeline.
# Focus on one area: drag across a part of the board, then ask about only that part. For example:
What would make more people come to the tasting day?
# When the thinking is done, turn it into a doc or deck. For example:
Turn this board into a summer menu plan.

# To save a picture: click Share, go to Export, and choose PNG. To keep working in another tool: use Send to (Lucid, Miro or Zoho Vani).
```

### 2. test-bakery-summer-brainstorm.txt
```
# Made-up brainstorm for the video's example, one idea per line as group: idea. Lines starting with # are notes.
# Paste the lines below into a Claude Whiteboards chat after "Start a whiteboard from this plan:", or use them with plan_outline.py from the build prompt.
Drinks: iced lemon tea
Drinks: strawberry lemonade
Drinks: cold brew
Tasting day: a Saturday
Tasting day: free samples
Tasting day: ask regulars to vote
Posters and price list: posters by the counter
Posters and price list: new price list
Question: when do we order supplies?
```

### 3. claude-whiteboards-setup-checklist.md
```
# Claude Whiteboards (beta): setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you use it?
- [ ] Your plan is Pro, Max, Ultra, Team or Enterprise. Anthropic: "Claude Whiteboards is available in beta on Pro, Max, Ultra, Team, and Enterprise plans on web, Claude Desktop, and Claude Mobile." It isn't on the Free plan.
- [ ] Not in Claude for Teachers yet.
- [ ] Not for organizations with HIPAA-ready configurations. With zero data retention for Claude Code: available in chat and Cowork, not covered by zero data retention, and not available in Claude Code.

## For the owner (Owners and Primary Owners, Team and Enterprise)
- [ ] Organization settings, then Capabilities: "Cloud code execution and file creation" is on (called "Create and edit files" in the updated Settings layout). Artifacts need it.
- [ ] Organization settings, then Artifacts: Artifacts is on, and Whiteboards (beta) is on. Team default: on. Enterprise default: off until an owner turns it on.
- [ ] To let people invite outside guests by email: Organization settings, then Artifacts, "Email invitations outside your organization". Team default: on. Enterprise default: off.
- [ ] Enterprise: custom roles can limit artifacts and templates to groups. Check that the people who need Whiteboards are included.

## Make a board
- [ ] In any chat: ask for a whiteboard (claude-whiteboards-plan-prompt.txt).
- [ ] Or: go to the Artifacts tab, select the Whiteboards tile (labelled "Whiteboard"), and describe what you want to work through, or dictate it.
- [ ] Dictate: select the microphone next to the send button. To stop, select it again or press Escape; your words stay in the box. Select send or press Return.
- [ ] Check: Claude groups related ideas, puts steps in order and connects the ones that depend on each other, using shapes, arrows and sections.
- [ ] Find the gaps: ask what's missing between two steps. Claude adds suggestions to the board for you to check.
- [ ] Reorganize: ask Claude to regroup the board by theme or turn it into a timeline. Anyone on the board can rearrange what's there.
- [ ] Focus on one area: drag across a part of the board to ask Claude about only that part.
- [ ] You can add pictures and videos to a board, but you can't import a board from a file.

## Share it
- [ ] Boards start private to you. Open the board on the web or in Claude Desktop and click "Share" (sharing can't be changed in Claude for iOS or Android).
- [ ] Team and Enterprise: add people from your organization and choose each one's access. Pro, Max and Ultra: "Only you" or "Anyone with the link", or invite people by email (beta).
- [ ] Access levels: "Can view" (open it and see its comments), "Commenter" (plus add comments), "Can edit" (plus make changes).
- [ ] Email invitations: the invitee needs a Claude account with the address you invited. Up to 50 people from outside your organization per artifact. Pending invitations expire after 30 days.
- [ ] People you invite from outside your organization: "Parts of the artifact that use Claude or your connectors don't work for them." On Pro, Max and Ultra, "outside your organization" means anyone other than you.
- [ ] Everyone on a board works on it at the same time. To see what a teammate is looking at, follow them around the board.

## Turn it into something else
- [ ] A doc or deck: ask Claude, for example "Turn this board into a summer menu plan."
- [ ] A picture: click "Share", go to "Export", and choose PNG.
- [ ] Another tool: use "Send to": Lucid, Miro and Zoho Vani ("and we're adding more over time").

## What it can't do (yet)
- [ ] "Claude works from what's on the board and doesn't use context from your connected apps." Say or paste the dates and details onto the board.
- [ ] No import of a board from a file.
- [ ] No size limit is stated on the help page.

## Usage and what's kept
- [ ] "Claude Whiteboards counts toward your plan's usage limits, like the rest of your work with Claude."
- [ ] In a Claude Meetings call (Team and Enterprise, beta, Google Meet): say "Claude, make a whiteboard"; Claude attaches it to the meeting page. "Docs and whiteboards made in a meeting are free through February 10, 2027."
- [ ] Every whiteboard you create is saved in the Artifacts tab. How long boards are kept: not stated on the Whiteboards help page (2026-11-26).

## If the Whiteboard tile isn't there
- [ ] Check the plan (not Free), then the owner's switches above, in order, then custom roles on Enterprise.
- [ ] On Pro, Max and Ultra: Settings, then Capabilities: "Cloud code execution and file creation" is on (called "Create and edit files" in the updated Settings layout). Artifacts need it.
- [ ] It works when your plan is on the board, a teammate's changes show up, and the board is in the Artifacts tab afterwards.

Sources: support.claude.com/en/articles/18324319-get-started-with-claude-whiteboards ; support.claude.com/en/articles/9547008 ; support.claude.com/en/articles/17153992 ; support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans ; support.claude.com/en/articles/18325154-use-claude-meetings ; claude.com/resources/articles/sheets-whiteboards-data
```
