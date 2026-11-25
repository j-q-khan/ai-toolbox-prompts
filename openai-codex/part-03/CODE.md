# Full code: ChatGPT Codex Cloud: Run a Task on Your GitHub Repo and Open a Pull Request

The task prompt, the review comments and the Codex Cloud checklist from this video, written from OpenAI's official Codex docs and help centre and GitHub's docs (checked 2026-11-24). They were written from the docs, not run for this video.

### 1. cloud-task-prompts.txt
```
# Use these on a GitHub test repo with nothing real in it, never on your only copy of real work.
# The lines starting with # are notes for you: don't paste them.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

# The task: type this in a new Codex Cloud task, started from your published environment.
Add a short section called "Opening hours" to README.md with one line: Monday to Saturday: 8 to 5. Change nothing else.

# Then review the changes and any test results, and open a pull request from the result when you're ready.
# On GitHub, under your repo's name, select Pull requests, open the pull request, then its Files changed tab, and check that only the Opening hours lines were added.

# A second look: post this as a comment on the pull request.
@codex review

# The same comment with a one-off focus.
@codex review for issues in the README
```

### 2. codex-cloud-checklist.md
```
# Codex Cloud: first task checklist (checked 2026-11-24)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save. Plans and prices change often: check https://learn.chatgpt.com/docs/pricing

## Your plan and sign-in (OpenAI's help centre and docs, checked 2026-11-24)
- [ ] "Codex Cloud is available to eligible Plus, all Pro tiers, Business, Enterprise, Healthcare, and Education accounts, subject to rollout and workspace settings. It is not included with Free or Go."
- [ ] Plus was $20 a month when checked 2026-11-24.
- [ ] Work or school account? "Your workspace's Codex cloud-access settings control whether you can use cloud tasks."
- [ ] "Codex cloud requires signing in with ChatGPT."
- [ ] "If you log in using an email and password, you must set up MFA on your account before accessing Codex cloud."

## A test repo on GitHub (GitHub's quickstart)
- [ ] Select + in the upper-right corner, then New repository.
- [ ] Name it (for example test-bakery), choose a visibility (this video uses private: "Private repositories are only accessible to you, people you explicitly share access with…"), toggle Add README to On, then Create repository.
- [ ] The README shows on the repo's front page.

## Create and publish an environment
- [ ] On chatgpt.com or in the ChatGPT desktop app: start a chat and choose Work in, then Cloud.
- [ ] Open Select environment, then Create environment.
- [ ] Select only your test repo. "Connect GitHub if prompted."
- [ ] Select Get started: "Codex inspects the repositories, installs dependencies and tools, and tests the workflow."
- [ ] "Supply missing access or information when asked."
- [ ] Codex can save the tested setup as an Install script: "commands to install dependencies and prepare development assets".
- [ ] Internet: "Turn on Enable all public internet access for full public access", or turn it off and "allow package managers or add specific hosts under Additional allowed domains". The page states no default: check yours. This video leaves full access off.
- [ ] From OpenAI's earlier Codex Cloud (Legacy) internet access page (the current page doesn't repeat it): the risks include "Prompt injection from untrusted web content". "Point Codex only to trusted resources and keep internet access as limited as possible."
- [ ] "Review the setup report, configuration, and files", then select Publish.
- [ ] After Environment published appears, select Start a new task.

## Your VM (OpenAI's VM table)
- [ ] Plus, Edu Plus: 2 vCPUs, 8 GiB memory, 8 GiB disk.
- [ ] Pro, Business, Enterprise: 4 vCPUs, 16 GiB memory, 32 GiB disk. Edu, Edu Pro: the same.
- [ ] Usage (pricing page): "Local messages and cloud chats share your plan's usage allowance." "Cloud tasks may use more of your allowance than local messages."

## The task
- [ ] Paste the task from cloud-task-prompts.txt.
- [ ] "Codex can edit files, run commands, and check its work." "Tasks in Codex Cloud can keep working while your computer is asleep."
- [ ] "Review changes and test results before committing or opening a pull request."
- [ ] Something off? Ask for the change in the same chat.
- [ ] "Saved state doesn't replace source control." "Commit important work or save the output you need."

## The pull request and a review
- [ ] Open a pull request from the result when you're ready.
- [ ] On GitHub: "Under your repository name, click Pull requests", then open the pull request.
- [ ] On GitHub: "The Files changed tab shows the diff that reviewers use to understand the proposed changes."
- [ ] Comment @codex review: "Wait for Codex to react (👀) and post a review."
- [ ] No reaction? "Confirm you turned on code review for the repository in Codex settings" (https://chatgpt.com/settings/code-review) and that the pull request belongs to a repository connected to Codex.
- [ ] One-off focus: "@codex review for issues in the README".

Sources: learn.chatgpt.com/docs/cloud ; learn.chatgpt.com/docs/environments/cloud-environments ; learn.chatgpt.com/docs/cloud/internet-access ; learn.chatgpt.com/docs/third-party/github ; learn.chatgpt.com/docs/auth ; learn.chatgpt.com/docs/pricing ; help.openai.com/en/articles/11369540 ; docs.github.com (Quickstart for repositories, About repositories, Pull requests, Reviewing proposed changes in a pull request)
```
