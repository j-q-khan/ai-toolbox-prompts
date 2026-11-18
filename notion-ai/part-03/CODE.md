# Full code: Notion AI Meeting Notes: Set It Up and Get Your Summary

The prompt from this video and the steps as a checklist, written from Notion's help centre and pricing page (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. meeting-page-prompt.txt
```
# Paste this into Notion AI (click the face in the bottom corner of Notion to open the Notion Agent chat), then send it.
# It asks first, then makes one new private page you can reuse for a meeting: the consent reminder as its first line, a dummy agenda, and a line showing where to type /meet.
# It changes nothing else. It does not start AI Meeting Notes: Notion's help page says the Notion Agent can't, so you type /meet yourself.
# On Notion's Free and Plus plans each response in Notion AI uses some of your trial of Notion AI.
# Written from Notion's help centre, checked 2026-11-17, not run.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Leave these lines starting with # out when you paste.

Goal: make one new private page I can reuse as a meeting page, with dummy text only. Change nothing else in my workspace.
Steps, in order:
1. Tell me in two sentences what you will make and where, and wait for me to answer yes. Write nothing until I do.
2. Make one new private page called "Weekly sync, dummy notes".
3. Make this the first line of the page, in bold: "Before we start: tell everyone that Notion AI Meeting Notes will transcribe this meeting, and get a yes from each person. Capturing what people say may need their consent, depending on where you are. If anyone says no, don't start."
4. Under it, add the heading "Meeting details" with three lines: "Team: Test Bakery (dummy)", "Date:" left empty, and "Who is here:" left empty.
5. Add the heading "Agenda" with three numbered lines: "Opening day at Test Bakery (dummy)", "Flour order (dummy)", "Next steps (dummy)".
6. Add the heading "Meeting notes go here" with one line: "In Notion's desktop app, type /meet on the empty line below this one, write the agenda under Notes, then select Start transcribing once everyone has agreed."
7. Add the heading "After the meeting" with four to-do lines: "The summary appeared", "Checked two points against the transcript with the citations", "Chose who can open this note with Share", "Deleted the transcript if it isn't needed".
8. Stop there.
Rules: don't start, add or imitate AI Meeting Notes, a transcript or a summary, and don't invent anything that was said. No real names, emails or phone numbers. Don't edit, move, share or delete any other page or database, and don't search my other pages for this. No web search and no changes to permissions or settings. If anything is unclear, ask me before you write.
Output: the page, and one line that says nothing else was changed.
```

### 2. notion-meeting-notes-checklist.md
```
# Notion AI Meeting Notes: checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Plans, limits and dates change. Check each line again at notion.com/help/ai-meeting-notes before you rely on it. This is not legal advice.

## What you need
- [ ] A plan that includes it: "You must be on Notion's Business or Enterprise Plan to use AI Meeting Notes." On Free and Plus the pricing page shows Meeting notes as "Limited Trial".
- [ ] For video calls: Notion's desktop app, version 4.7.0 or higher. On a Mac, macOS 13 or later. On Windows, the latest version.
- [ ] To be online: "AI Meeting Notes is not currently supported while offline."
- [ ] For work meetings: your employer's rules on what may be transcribed, and where the notes may be kept.

## Which device hears what
- [ ] Desktop app: your system audio and your microphone, so it hears everyone on a video call.
- [ ] Browser: your microphone only. With headphones on, sound from the call is not captured. Without headphones, and with the volume up, it may be.
- [ ] Phone app: the phone's microphone only. With headphones or earbuds, Notion won't hear the other people.
- [ ] So: desktop app for video calls; browser or phone when everyone is in one room.

## Start the notes
- [ ] Open a page in the desktop app and type /meet. A meeting notes block appears on the page.
- [ ] Or, on a new empty page: click the Meet pill at the bottom of the page (named in Notion's guide).
- [ ] Other ways in: the Meetings tab in the sidebar (one sentence of Notion's help page calls it the Meeting notes tab), or the notification the desktop app shows when you join a video call. These make the notes as their own page.
- [ ] The first time: Notion asks for access to your system audio and screen recording permissions. Notion says this is how it transcribes the other people while you wear headphones.
- [ ] Before the meeting: type your agenda under Notes. Notion takes these notes into account when it writes the summary.

## Consent, before you start
- [ ] Capturing what people say may need their consent, depending on where you are. Tell everyone in the meeting before you start.
- [ ] Notion's page: "We recommend complying with the strictest consent laws and always obtaining consent from all participants".
- [ ] Three ways to ask: (1) Text: click the slider icon at the top of the block, hover over Consent, copy the message and paste it into the call's chat. (2) Voice: the speaker button at the bottom of the block plays the message; it plays through your computer speakers, not your call's microphone, so unmute your speakers and unplug headphones. (3) Say it yourself. Notion's example: "Alright if I record and transcribe this meeting using Notion AI Meeting Notes?"
- [ ] Selecting Start transcribing confirms that everyone in the meeting has given their consent.
- [ ] If someone joins late, stop and ask them too. If someone says no, don't transcribe.
- [ ] Workspace owners: Settings, then Meeting notes, has "Enforce consent for all workspace members".

## Transcribe, stop, and check that it worked
- [ ] Select Start transcribing. Keep typing under Notes if you want to.
- [ ] When the meeting is over, select Stop. The summary starts on its own.
- [ ] Check: the summary appears, with key points and action items, and the transcript is there too. A summary needs at least 300 transcribed characters, roughly a minute of talking.
- [ ] Click a citation in the summary to jump to the line of the transcript it came from. Check two points this way: a transcript can mishear words.
- [ ] To change the layout: Instructions at the bottom of the block, change it from Auto, then Retry summary.

## Limits (checked 2026-11-17)
- [ ] Languages listed in the FAQ: English, Chinese, Spanish, French, German, Japanese, Korean, Portuguese, Russian, Thai, Vietnamese, Danish, Finnish, Norwegian, Dutch and Swedish.
- [ ] Speaker labels: the page tells this two ways (a longer list of supported languages in one place, "English only" in the FAQ). Look at your own transcript before you count on names.
- [ ] A daily limit of 10 hours per user.
- [ ] Audio files you can upload instead: AAC, M4A, MP3 and WAV (the settings icon at the top of the block, then Upload audio).

## Credits, from 1 December 2026
- [ ] Notion's credits page: "AI meeting notes uses Auto and will begin consuming monthly Standard credit allowance on December 1, 2026. A one hour meeting is estimated to use ~10 Standard credits."
- [ ] Each Business member gets 1,500 Standard credits a month (Part 2 of this series covers credits).
- [ ] Our arithmetic, not Notion's: one hour of meetings every working day is about 200 to 220 Standard credits a month.

## Privacy, in Notion's words
- [ ] "By default, your customer data is not used to train models."
- [ ] "Sub-processors do not store audio."
- [ ] "Free, Plus, and Business: AI provider retains your data for 30 days or fewer, then deletes it."
- [ ] Each meeting note has its own sharing settings: select Share at the top of the note to choose who can open it.

## Switch off, or tidy up, afterwards
- [ ] Delete a transcript: click the slider icon at the top of the block, then Delete transcript.
- [ ] Delete the dummy meeting page when you're done: select the three dots at the very top right of the page, then Delete.
- [ ] Stop the pop-up when you join calls: Settings, then Notifications, then switch off Desktop meeting detection notifications.
- [ ] Workspace owners can switch the feature off: Settings, then Meeting notes, then switch off Enable Meeting notes for workspace.

Sources: notion.com/help/ai-meeting-notes ; notion.com/help/guides/preserve-perfect-meeting-memory-with-ai-meeting-notes ; notion.com/help/standard-select-and-notion-credits-eligible-features ; notion.com/help/notion-ai-security-practices ; notion.com/pricing ; notion.com/help/notion-agent
```
