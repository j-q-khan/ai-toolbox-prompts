# Full code: Claude Update: Claude Ship, PR Steward and Claude Approvals Explained

Anthropic's documented example policy, the documented two-people starter policy, the documented example classifier and the rollout checklist, written from Anthropic's docs "Claude Ship", "PR Steward", "What PR Steward can access", "Set up PR Steward", "Claude Approvals", "Set up Claude Approvals", "Claude Approvals policy file reference", "Claude Approvals classifiers", "Claude Code GitHub Actions" and the help page on the Enterprise promotional credits (checked 2026-11-26). The three YAML files are copied exactly from the docs, after our own comment lines at the top. They were written from the docs, not run for this video.

### 1. approvals.example.yml
```
# Anthropic's example policy, copied exactly from code.claude.com/docs/en/approvals (checked 2026-11-26). The lines from "# .claude/approvals.yml" down are the docs' own.
# To use it, save it as .claude/approvals.yml in a TEST repository's root, in a pull request of its own, and merge it into the default branch.
# Set up branch protection first. Observe mode is billed. Claude Approvals is a public beta on Team and Enterprise plans, GitHub only.
# .claude/approvals.yml
version: 1
mode: observe
rules:
  - purpose: "A change takes two people, and Claude doesn't approve."
    paths: ["**"]
    verdict: { claude: comments, seats: 2 }
    advisory: [claude/code_review]
```

### 2. approvals-two-people-starter.example.yml
```
# Anthropic's starter policy "Keep two people on each change", copied exactly from code.claude.com/docs/en/approvals-setup (checked 2026-11-26). The lines from "# .claude/approvals.yml" down are the docs' own.
# The second rule asks for two people on any change under .claude/, which includes the policy file. Enforcing it needs two people with write access.
# To use it, save it as .claude/approvals.yml in a TEST repository, as above. Delete "mode: observe" only when the check's titles match what your reviewers decide.
# .claude/approvals.yml
version: 1
mode: observe
rules:
  - purpose: "A change takes two people."
    paths: ["**"]
    verdict: { claude: comments, seats: 2 }
    advisory: [claude/code_review]
  - purpose: "A change to the review rules takes two people."
    paths: ["**/.claude/**"]
    nested: inherit
    verdict: { claude: comments, seats: 2 }
```

### 3. change_risk-def.example.yml
```
# Anthropic's example classifier definition, copied exactly from code.claude.com/docs/en/approvals-classifiers (checked 2026-11-26). The lines from "# .claude/classifiers/change_risk/def.yml" down are the docs' own.
# To use it, save it as .claude/classifiers/change_risk/def.yml on a TEST repository's default branch, and list repo/change_risk under advisory in a rule that has a verdict.
# Each run is billed, also in observe mode. With no budget key, a run's cost cap is 10 US dollars (the maximum is also 10), and the docs say the bill can be higher.
# .claude/classifiers/change_risk/def.yml
version: 1
description: "How risky is this change to ship?"
model: opus
prompt: |
  Rate how risky this change is to ship.
  high: it touches sign-in, billing or a data migration.
  medium: it changes behavior a user can see.
  low: anything else.
  When two ratings fit, pick the higher.
outputs:
  risk: { type: ordinal, values: [low, medium, high] }
```

### 4. claude-ship-rollout-checklist.md
```
# Claude Ship: rollout checklist (facts checked 2026-11-26)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Can your organisation use it?
- [ ] A Claude Team or Enterprise plan. "Claude Ship is for organizations on Team and Enterprise plans."
- [ ] Not with Zero Data Retention, the HIPAA configuration, or customer-managed encryption keys. Claude Approvals also can't start with FERPA or Access Transparency settings.
- [ ] Hosts: Claude Approvals works on github.com, including GitHub Enterprise Cloud. PR Steward works on github.com or a connected GitHub Enterprise Server instance on port 443.
- [ ] Status, when checked: the docs say "Code Review is generally available. PR Steward and Claude Approvals are in public beta." The product page says "Claude Ship is available in beta". The article and product page say "an admin" turns agents on; the docs say you need an Owner role.
- [ ] Anthropic's warning: "Claude Ship uses AI and may miss bugs, security vulnerabilities, or other issues."

## Before you turn anything on
- [ ] Claude side: an Owner role, usage credits, and the GitHub connector on in Organization settings, then Connectors.
- [ ] GitHub side: an owner of the GitHub organization installs the Claude GitHub App and links it to your Claude organization. A repository admin adds branch rules. A private repository needs a paid GitHub plan.
- [ ] The app's permissions (you accept all of them; "GitHub doesn't let you accept a subset"): Actions read and write; Administration read; Checks read and write; Contents read and write; Dependabot alerts read; Discussions read and write; Issues read and write; Members read; Merge queues read; Metadata read; Pull requests read and write; Repository creation read and write; Repository hooks read and write; Statuses read; Workflows read and write.
- [ ] Branch rules on the default branch: require a pull request with at least one approval; dismiss stale approvals on new commits, or require approval of the most recent push; keep the Claude GitHub App off the bypass list; protect other branches PR Steward shouldn't push to, and block force pushes where you don't want them.
- [ ] Pick ONE test repository.

## Turn on one agent at a time, in this order (Organization settings, then Claude Ship)
- [ ] 1. Code Review. Adding a repository can start billed reviews. Set a monthly spend limit in Organization settings, then Usage.
- [ ] 2. PR Steward. Set "Runs for" (All eligible authors, or Listed users only to pilot). Turn on the Steward switch. Set PR Steward's monthly limit in Organization settings, then Usage, under Services ("PR Steward has no spend limit of its own until you set one"). In the repository's Edit dialog, set Steward to "Manual (@claude steward)" and set the Steward spend cap in US dollars.
- [ ] Test PR Steward: on a test pull request, comment @claude steward. The label claude-pr-steward-watching and a comment headed "Claude PR Steward" appear. To stop it, remove the label or comment @claude stop.
- [ ] PR Steward pushes commits and replies without asking first. It skips drafts (unless the repository is set to On (including drafts), or, in a Manual repository, someone starts it on the draft), pull requests from forks, pull requests a bot opened, and authors without write access.
- [ ] What it won't do: "Steward is designed not to approve or merge pull requests." In Anthropic-hosted sessions, Anthropic's service refuses approving, changing branch protection, rulesets or statuses, writing check runs, deleting a branch, and pushing tags. Merging, auto-merge and force-pushing are left to GitHub's branch rules. In a self-hosted environment, Claude can reach GitHub with any GitHub credential a session can read, and Anthropic's service can't refuse an approval made that way.
- [ ] Only when its fixes match what your reviewers would do: set the repository to On. PR Steward can be on in up to 256 repositories.
- [ ] 3. Claude Approvals. In a pull request of its own, add .claude/approvals.yml (approvals.example.yml or approvals-two-people-starter.example.yml) in observe mode, and merge when Claude comments that it "found the policy file in this change valid". Then open another pull request: a "Claude Approvals" check appears with a title that starts "(observe mode)".
- [ ] Keep claude/code_review in a rule that matches the files you want reviewed (under advisory, or in an if), or automatic Code Reviews normally stop on files the policy covers, in observe mode too.
- [ ] Observe mode is billed (reviews and classifier runs). Set the classifier runs' spend limit in Organization settings, then Usage, under Services. "Claude Approvals has no base charge."
- [ ] Who can turn it on: "anyone who can merge a policy file into the default branch". An Owner can turn it off for the whole organization (Block globally in the Approve setting on the Claude Ship page).
- [ ] Watch for merges without a person: the check blocks only where it's a required GitHub check; seats: 1 lets the author alone fill it; claude: approves starts no review by itself; auto-merge or a merge queue with no person's approval can merge "without anyone acting".
- [ ] Optional helper: type /claude-approvals at the Claude Code prompt in your repository, followed by what you want, and Claude writes or changes the policy file (Claude Code v2.1.331 or later). Check the result in observe mode.

## Enforce, only when the observe-mode titles match your reviewers
- [ ] Delete the mode: observe line and merge that change.
- [ ] Five minutes later, comment @claude approvals rerun on each open pull request whose check title starts "(observe mode)" or "Observe mode ended".
- [ ] In GitHub, require the status check "Claude Approvals", and set its source to the Claude app ("If you allow any source, GitHub accepts a check named Claude Approvals from elsewhere"). By API, the Claude app's ID is 1236702.
- [ ] Confirm: a pull request that changes a file under .claude/ shows "Waiting on human review from any person (1/2)", and GitHub lists the check as required.

## Billing, when checked on 2026-11-26
- [ ] "Each agent is billed on token usage through your organization's usage credits, separately from your plan's included usage."
- [ ] Turning off usage credits doesn't stop an agent that's on.
- [ ] Enterprise promotional credits (help page, updated November 23, 2026): eligible Enterprise organizations, claimed once by an Owner or Primary Owner on the Claude Ship settings page, from October 15, 2026 through January 15, 2027 (23:59 UTC); between $10,000 and $50,000, based on active Claude Code seats; used within 30 days of claiming. Organizations that claimed the earlier free Code Review offer can't claim this one.

## Turning it off, in this order
- [ ] 1. Claude Approvals first (a policy can start billed reviews where Code Review is off): turn on dismissing stale approvals, stop requiring the check, turn Approvals off, then dismiss Claude's approving reviews on open pull requests.
- [ ] 2. PR Steward. 3. Code Review.
- [ ] Suspend or uninstall the Claude GitHub App, or unlink the GitHub organization, only after Approvals is off.
- [ ] These steps leave the /ship and /steward commands on; they're turned off separately in managed settings.

Sources: code.claude.com/docs/en/claude-ship ; code.claude.com/docs/en/pr-steward ; code.claude.com/docs/en/pr-steward-security ; code.claude.com/docs/en/pr-steward-setup ; code.claude.com/docs/en/approvals ; code.claude.com/docs/en/approvals-setup ; code.claude.com/docs/en/approvals-policy ; code.claude.com/docs/en/approvals-classifiers ; code.claude.com/docs/en/github-actions ; claude.com/resources/articles/introducing-claude-ship ; claude.com/product/claude-ship ; support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise
```
