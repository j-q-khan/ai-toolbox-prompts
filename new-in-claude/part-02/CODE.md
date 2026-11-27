# Full code: Claude Motion: Turn a Chat Into an Animated Explainer Video

The explainer request prompt and the setup checklist, written from Anthropic's help pages "Get started with Claude Motion", "Artifacts admin guide for Team and Enterprise plans" and "Share artifacts" (checked 2026-11-26). They were written from the docs, not run for this video.

### 1. motion-explainer-prompt.txt
```
# Paste the request below into a Claude chat after choosing Output, then Motion, in the message box.
# Or go to the Artifacts tab, select a Motion template, and paste it there.
# Claude Motion is a beta on Team and Enterprise plans. Written from Anthropic's help page, Get started with Claude Motion, checked 2026-11-26.
# The lines starting with # are notes for you: don't paste them.
# Fill in the four parts in brackets. Anthropic's help page says to say who will watch it, where it will play, and roughly how long it should be.
# Attach the report, data or images you want Claude to use, so the animation is built from your own material. Remove anything private first.
# Motion doesn't use a video generation model, so it doesn't create realistic footage or people. Ask for words, numbers, charts and shapes.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Make a [length, for example 30-second] explainer of [what it explains], for [who will watch], to play [where it will play].
Use the attached file for every word and number. Don't add facts that aren't in it.
Show one step per scene, with big, short text that can be taken in at a glance, and simple shapes or charts, no people.
Keep the same colours and style in every scene, and end on a scene that sums up the steps.

# Example, made up (the one in the video):
# Make a 30-second explainer of Test Bakery's three onboarding steps, for new starters, to play on their first morning.

# Then change one detail at a time in the same chat, for example:
Slow down the second scene.
Change step 2's title to Meet your buddy.

# When it looks right: click Export and choose MP4. Animations start private to you. To share one, open it and click Share.
```

### 2. claude-motion-setup-checklist.md
```
# Claude Motion (beta): setup checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can you use it?
- [ ] Your workspace is on a Claude Team or Enterprise plan. Anthropic: "Claude Motion is available in beta on Team and Enterprise plans."
- [ ] No Team or Enterprise plan? Claude Design (still designs) is on every Claude plan, including Free, per Anthropic's October 8, 2026 article.

## For the owner (Owners and Primary Owners)
- [ ] Organization settings, then Capabilities: "Cloud code execution and file creation" is on (Anthropic's admin guide says this comes first).
- [ ] Organization settings, then Artifacts: Artifacts is on.
- [ ] Organization settings, then Artifacts, under Templates: Motion (beta) is on. Team default: on. Enterprise default: off.
- [ ] Enterprise: custom roles can limit Motion to specific groups. Check that the people who need it have the Motion capability.
- [ ] Sharing outside the organization: External sharing (anyone with the link) and email invitations outside your organization are two separate settings in Organization settings, then Artifacts. Turning on one doesn't turn on the other.
- [ ] HIPAA-ready configurations: an Owner can turn on Motion after accepting the terms, but it isn't covered under the Business Associate Agreement, so keep protected health information out of it.

## Make an animation
- [ ] In any chat, on the web or in Claude Desktop: select "Output" in the message box and choose "Motion". (Anthropic's article also shows typing "/motion" in the message box to bring up the Motion option.)
- [ ] Or: go to the Artifacts tab, select a Motion template, and describe the animation you want.
- [ ] Say who will watch it, where it will play, and roughly how long it should be (motion-explainer-prompt.txt).
- [ ] Attach the report, data or images you want Claude to use. Use made-up or approved material only.
- [ ] Check: the animation plays like a short video beside your chat.

## Change it
- [ ] Ask in the chat for one change at a time, like "Slow down the second scene". The rest stays as it was.
- [ ] Or adjust the animation yourself in the editor.
- [ ] Motion doesn't use a video generation model, so it doesn't create realistic footage or people.

## Export and share
- [ ] To download: click "Export" and choose MP4.
- [ ] Longest length and picture size: not stated on any Anthropic page we checked (2026-11-26). Watch the file through once before you send it.
- [ ] Animations start private to you. To share one, open it and click "Share".
- [ ] Team and Enterprise choices: "Only people invited", "Anyone at" your organization, or "Anyone with the link" (only when an Owner has turned on External sharing or allowed that artifact). Greyed out? Ask an Owner or Primary Owner.

## Usage and what's kept
- [ ] "Claude Motion counts toward your plan's usage limits, like the rest of your work with Claude. Longer or more complex animations use more of your limit than a typical message."
- [ ] Every animation you create is saved in the Artifacts tab.
- [ ] Admin guide: "Uploaded assets are stored persistently, and fall under the same data retention and deletion policies as other Anthropic products for organizations." On Enterprise, a custom retention period can cover artifacts.

## If Motion isn't there
- [ ] Check the plan (Team or Enterprise), then the three switches above, in order, then custom roles on Enterprise.
- [ ] It works when Motion shows up under Output, your test animation plays beside the chat, and it's in the Artifacts tab.

Sources: support.claude.com/en/articles/17454997-get-started-with-claude-motion ; support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans ; support.claude.com/en/articles/9547008 ; claude.com/resources/articles/dashboards-and-motion
```
