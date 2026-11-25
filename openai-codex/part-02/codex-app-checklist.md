# Codex in the ChatGPT desktop app: first task checklist (checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. Prices change often: check https://learn.chatgpt.com/docs/pricing

## Install and sign in
- [ ] Windows: install the ChatGPT desktop app from the Microsoft Store (https://get.microsoft.com/installer/download/9PLM9XGG6VKS), or in PowerShell: winget install --id 9PLM9XGG6VKS -s msstore
- [ ] Mac: download the Mac version from https://chatgpt.com/download/
- [ ] Linux: "available in preview" (Ubuntu 24.04 LTS and 26.04 LTS, Debian 13, Fedora 43 and 44, Arch Linux): https://learn.chatgpt.com/docs/linux/linux-app
- [ ] Open the app and sign in with your ChatGPT account.

## What your plan gets (OpenAI's pricing page and help centre, checked 2026-11-24)
- [ ] Free (was $0 a month) and Go (was $8 a month): "GPT-6 Luna at Standard speed in the desktop app, subject to rollout".
- [ ] Codex Cloud "is not included with Free or Go" (help centre).
- [ ] Plus (was $20 a month): "Codex on the web, in the CLI, in the IDE extension, and on iOS".
- [ ] A key for OpenAI's API instead of a plan: "Codex in the CLI, SDK, or IDE extension", "No cloud-based features", billed at API prices.

## Open Codex on a test folder
- [ ] Open your test folder ("Start a chat, create a project, or open a folder."). Use a copy of something harmless.
- [ ] Then open the ChatGPT dropdown and select Codex, then New chat. In Codex, Ctrl+O (Windows) or Cmd+O (Mac) also opens a folder.
- [ ] Open the review tab: Ctrl+Shift+G (Windows) or Control+Shift+G (Mac). "The review pane requires a project inside a Git repository. If your project isn't a Git repository yet, the app prompts you to create one."
- [ ] Windows: "If you don't have Git installed natively on Windows, the app can't use some features." Git "Powers the review panel"; OpenAI's Windows guide gives: winget install --id Git.Git
- [ ] Git users: "Create Git checkpoints before and after a task so you can revert changes."

## Where it runs and what it may do
- [ ] Below the composer: Work in = This computer, and Worktree left unselected, so the chat runs Local ("work directly in your current project directory").
- [ ] Worktree, for later: "isolate changes in a Git worktree"; it needs a Git repository. "You can think of Local as the foreground and Worktree as the background."
- [ ] Permissions control below the composer: "For most work, start with Ask for approval."
- [ ] "Check the selected mode for the current chat; having a mode available doesn't mean it's selected."
- [ ] Don't use Full access: "Codex is not limited to your project directory and might perform unintentional destructive actions that can lead to data loss."

## The task and approval requests
- [ ] Prompt 1, then Prompt 2, from first-task-prompts.txt.
- [ ] If an approval request opens: look at what it asks, then Enter approves and Esc declines.
- [ ] If it offers scopes, "such as approving once or for the session, choose the narrowest scope that lets the task continue."
- [ ] On a Mac, folders like Music, Downloads or Desktop "require additional approval from the user" (that's macOS asking).

## Check the change
- [ ] Review pane: switch the diff pane to Last turn to see "only the changes of your last Codex turn".
- [ ] Only the new Cinnamon roll line? Keep it. Anything else? Undo it in the review pane.
- [ ] Optional: type /review in the composer and choose Review uncommitted changes: "Codex reports prioritized findings without changing your working tree."

## From the Codex CLI (Plus and up, or an API key)
- [ ] Type /app on Windows or a Mac: "The desktop app opens the same saved chat so you can continue there." If the app isn't installed or running, Codex shows an error asking you to install or launch it.

Sources: learn.chatgpt.com/docs/app ; learn.chatgpt.com/docs/windows/windows-app ; learn.chatgpt.com/docs/linux/linux-app ; learn.chatgpt.com/docs/quickstart ; learn.chatgpt.com/docs/environments/modes ; learn.chatgpt.com/docs/environments/git-worktrees ; learn.chatgpt.com/docs/permission-modes ; learn.chatgpt.com/docs/sandboxing ; learn.chatgpt.com/docs/reference/commands ; learn.chatgpt.com/docs/code-review ; learn.chatgpt.com/docs/reference/troubleshooting ; learn.chatgpt.com/docs/developer-commands?surface=cli ; learn.chatgpt.com/docs/codex/cli ; learn.chatgpt.com/docs/pricing ; help.openai.com/en/articles/11369540
