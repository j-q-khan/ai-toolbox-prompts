# Claude Meetings (beta): setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you use it?
- [ ] Your workspace is on a Claude Team or Enterprise plan. Anthropic: "Claude Meetings is rolling out in beta on Team and Enterprise plans in Claude and Claude Desktop."
- [ ] Your organization doesn't use zero data retention (ZDR), a HIPAA-ready configuration or customer-managed encryption keys (CMEK). While it's in beta, it isn't available to those organizations.
- [ ] Your team meets on Google Meet. Anthropic: "Support is currently available for Google Meet, with other platforms coming soon."

## For the owner
- [ ] Organization settings, then Products, then Claude Meetings (beta). Choose: off, on for roles that include Meetings, or on for everyone. Team default: on for everyone. Enterprise default: off.
- [ ] Turn on Google Calendar for your organization. Anthropic: "An owner must enable Google Calendar for your organization first."
- [ ] Meetings with external guests: internal meetings only (the Enterprise default) or allowed (the Team default).
- [ ] Members' connectors in meetings: whether Claude can use members' connected tools during meetings.
- [ ] Owners and Primary Owners manage these. On Enterprise, custom roles can control access.

## Before every call
- [ ] Everyone on the call is okay with being transcribed (Anthropic's help page says this comes first, also before you turn on auto-join).
- [ ] For your first try, use a dummy meeting with people who know it's a trial, such as "Weekly planning (test)".

## Add Claude
- [ ] In Claude, on the web or in Claude Desktop, go to Meetings.
- [ ] Connect your Google Calendar.
- [ ] Select a meeting on your calendar.
- [ ] Click "Add Claude".
- [ ] Check: Claude appears as a participant and posts a notice in the call's chat.
- [ ] If Claude asks to come in, the host can let it in. If the host declines, Claude doesn't try that call again unless someone adds it.
- [ ] Auto-join (optional): Settings, then Capabilities, then Meetings, then Auto-join. All your meetings, or all except one-on-ones. Owners can't set it for you.

## During the call
- [ ] Ask out loud ("Claude", then your question) or type in the Meet chat. Claude answers in writing in the Meet chat by default.
- [ ] Anything Claude posts in the Meet chat is visible to everyone on the call.
- [ ] "Claude, make a doc." or "Claude, make a whiteboard." It attaches each one to the meeting page.
- [ ] Connected tools: Claude asks each person's permission the first time. For now, when someone asks out loud, it asks each time to confirm who's speaking.
- [ ] To pause: ask it to stop listening, or use the meeting page. To have it leave: ask it to leave, or select "Remove Claude" on the meeting page.
- [ ] Claude can stay for up to eight hours and warns you before it leaves.

## After the call
- [ ] The meeting page has the notes (a summary and any action items), the transcript and everything you made.
- [ ] People from your organization on the invite get a recap email with a link.
- [ ] For a checklist of who does what, paste the notes into meeting-notes-checklist-prompt.txt in a regular chat.
- [ ] In a regular chat, ask Claude about past meetings you have access to.

## What it keeps
- [ ] Anthropic: "It saves a transcript, summary, and screen descriptions, not audio."
- [ ] How long it's kept: not stated on any Anthropic page we checked (2026-11-26). Ask your owner before using it on real calls.

## Outside guests
- [ ] Not allowed: Claude stays out of calls when someone from outside your organization is invited, and leaves if one joins partway through, including another company's notetaker bot.
- [ ] Allowed: Claude listens and takes notes, and posts its notice in the call's chat but doesn't reply there. Guests don't get the meeting page or the recap email.
- [ ] Each person also has their own Meetings with external guests setting in Settings, then Capabilities, then Meetings.

## Cost in the beta (Anthropic's help page, 2026-11-26)
- [ ] Notes, transcripts, and answers that don't use your connected tools are included on Team and Enterprise plans.
- [ ] Docs and whiteboards made in a meeting are free through February 10, 2027.
- [ ] Using your connected tools counts toward your own usage and can lead to charges for your organization.

Sources: support.claude.com/en/articles/18325154-use-claude-meetings ; claude.com/resources/articles/claude-meetings
