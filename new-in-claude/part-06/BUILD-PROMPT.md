Paste this into Claude Code, Anthropic's coding tool, in a new, empty test folder (not a real repository). It drafts a Claude Approvals policy file in observe mode for a made-up test repository, keeps Claude's Code Review check under advisory so automatic reviews carry on, and adds a small checker that looks for the documented keys, tested on made-up files only, and it changes nothing until you agree. Written from Anthropic's docs "Claude Approvals", "Set up Claude Approvals" and the policy file reference, checked 2026-11-26. Nothing here was run for the video.

Goal: draft approvals.draft.yml, a Claude Approvals policy for a made-up repository called test-org/test-repo, in observe mode, plus check_policy.py, a small Python script that checks a policy draft for the things Anthropic's docs say matter before it goes near a real repository.
Context: Claude Approvals (public beta, Claude Team and Enterprise plans, GitHub only) follows a policy file saved at .claude/approvals.yml on a repository's default branch. Anthropic's docs say adding a policy file can stop automatic Code Reviews unless a rule names claude/code_review, and that observe mode is still billed. This draft is named approvals.draft.yml and kept out of any .claude folder, so it can't act as a policy anywhere. Use made-up names only.
Steps, in order:
1. Tell me your plan in a few lines and wait for my OK. Don't create, change or delete any file before I say yes.
2. Create approvals.draft.yml with exactly these lines, copied from Anthropic's starter policy "Keep two people on each change" (without the three leading spaces this list adds), and nothing else:
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
3. Write check_policy.py with the Python standard library only (no YAML package, no installs). It takes a file path, reads it as plain text, and reports PASS or FAIL for each check: a line "version: 1"; a line "mode: observe"; a "rules:" line; every rule (each line starting with "  - purpose:") followed by a "paths:" line and a "verdict:" line before the next rule; "claude/code_review" on an "advisory:" line or inside an "if:" line; and no "claude: approves" anywhere. It prints which line failed and exits with code 1 if any check fails.
4. If the file is missing or empty, print a clear message and exit with code 1. Never change the file it checks.
5. Create two made-up test files, test-good.yml (a copy of approvals.draft.yml) and test-no-review.yml (the same, without the advisory line), and run check_policy.py on all three. Show me the output: approvals.draft.yml and test-good.yml must pass, and test-no-review.yml must fail on the claude/code_review check.
6. Add a short README.md: what each file is; that approvals.draft.yml becomes a policy only when someone saves it as .claude/approvals.yml on a repository's default branch; to try it first on a test repository, in observe mode, after branch protection is set up; that observe mode is billed; that the checker is a text check, not Anthropic's validator, and Claude comments on the pull request that adds a real policy file; and a reminder to follow your organization's rules.
Safety: work only inside this folder. Don't create a .claude folder or any file named approvals.yml. No network access, no installs, no git commands, no GitHub calls. Don't install or configure the Claude GitHub App, and don't run /ship or /steward. Ask before every file you create.
Output: the five files, the checker's output for the three test files, and a two-line note of what you did.
