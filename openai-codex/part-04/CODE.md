# Full code: OpenAI Codex in VS Code: Set Up the Extension and Make Your First Change

The test file, the prompts and the "Codex not showing" fix checklist from this video, written from OpenAI's official Codex docs, the extension's Marketplace listing and Visual Studio Code's docs (checked 2026-11-24). They were written from the docs, not run for this video.

### 1. hours.txt
```
Monday to Saturday: 8 to 5
```

### 2. codex-vscode-prompts.txt
```
# Use these on a test folder with nothing real in it, never on your only copy of real work.
# The lines starting with # are notes for you: don't paste them.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.
# Save hours.txt from this video into a folder called Test Bakery, open that folder in Visual Studio Code
# with File, then Open Folder, open hours.txt, and check the permissions control below the composer says Ask for approval.

# The job: type this in the Codex composer.
Add a line for Sunday, 9 to 1, to hours.txt. Change nothing else.

# Then look at the summary and the changed lines. Keep the edits you want.
# Not right? Ask for a follow-up in the same chat, for example:
Put hours.txt back the way it was before your last change.
```

### 3. codex-vscode-fix-checklist.md
```
# Codex extension not showing in Visual Studio Code: fix checklist (checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. Plans and prices change often: check https://learn.chatgpt.com/docs/pricing

## The right extension (Marketplace listing, checked 2026-11-24)
- [ ] Name: "Codex – OpenAI's coding agent". Publisher: OpenAI. Item ID: openai.chatgpt.
- [ ] Plans: "Codex works with Plus, Pro, Business, Edu, and Enterprise ChatGPT plans." Plus was $20 a month when checked 2026-11-24.
- [ ] Free and Go: OpenAI's pricing page lists Codex "in the desktop app, subject to rollout".
- [ ] The extension's manifest asks for Visual Studio Code 1.96.2 or newer.

## 1. Open it from the Command Palette (OpenAI's Codex docs)
- [ ] "choose the Codex icon. If it is not visible, open the Command Palette and run Codex: Open Codex Sidebar."
- [ ] Command Palette: Ctrl (Control)+Shift+P on Windows, Cmd (Command)+Shift+P on a Mac.

## 2. Installed but switched off? (Microsoft's Visual Studio Code docs, not OpenAI's)
- [ ] Open the Extensions view: the Extensions icon in the Activity Bar. "By default, the Extensions view shows the extensions you currently have installed".
- [ ] Marked Disabled? Choose Enable from the menu that opens from its gear: "You can re-enable it with the Enable or Enable (Workspace) commands in the dropdown menu."

## 3. Out of date? (Microsoft's Visual Studio Code docs)
- [ ] An Update button beside it? Select it, then Restart Extensions when asked: "The update installs, and you're prompted to restart the extension host (Restart Extensions)."

## 4. Not installed? (the Marketplace listing and Microsoft's Visual Studio Code docs)
- [ ] In the Extensions view, search Codex, pick "Codex – OpenAI's coding agent" by OpenAI, and select Install.
- [ ] The first time you install from a new publisher, Visual Studio Code asks you to confirm you trust it: check it says OpenAI.
- [ ] "After the installation completes, the Install button changes to the Manage gear button."

## 5. Opens but you can't sign in?
- [ ] "On the signed-out screen, select Sign in with ChatGPT, then complete the browser flow."
- [ ] Check your plan against the list at the top.

## 6. Still stuck?
- [ ] OpenAI's troubleshooting page: "Find existing issues on the Codex GitHub repo." https://github.com/openai/codex/issues
- [ ] Sidebar works but something inside fails? Type /feedback in the composer: "Open the feedback dialog to submit feedback and optionally include logs."
- [ ] "If you share logs, review them first to confirm they don't contain sensitive information."

## Cursor or Windsurf
- [ ] OpenAI's docs: "VS Code and compatible editors use the Codex extension". Menus may look different there.
- [ ] Windsurf: windsurf.com redirected to devin.ai/desktop when checked 2026-11-24 ("Windsurf is now Devin Desktop").

## Once it works (OpenAI's Codex docs)
- [ ] "For most work, start with Ask for approval." "Having a mode available doesn't mean it's selected."
- [ ] "Create Git checkpoints before and after a task so you can revert changes."
- [ ] "If you revert or change an edit, tell Codex so it doesn't overwrite your edit when it works on the next prompt."

Sources: learn.chatgpt.com/docs/codex/ide ; learn.chatgpt.com/docs/developer-commands?surface=ide ; learn.chatgpt.com/docs/auth ; learn.chatgpt.com/docs/permission-modes ; learn.chatgpt.com/docs/prompting ; learn.chatgpt.com/docs/reference/troubleshooting ; learn.chatgpt.com/docs/pricing ; marketplace.visualstudio.com/items?itemName=openai.chatgpt ; code.visualstudio.com/docs/configure/extensions/extension-marketplace ; devin.ai/blog/windsurf-is-now-devin-desktop
```
