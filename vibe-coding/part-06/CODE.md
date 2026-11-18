# Full code: Lovable vs Claude Code: Which Should a Non-Coder Use?

The prompt from this video and a side-by-side sheet, written from Lovable's and Anthropic's official pages (checked 2026-11-17). They were written from the docs, not run for this video.

### 1. same-app-prompt.txt
```
# Paste the prompt below into Lovable (the box on your dashboard, with Build picked)
# or into Claude Code (opened in a new, empty folder). It builds the same tiny page in either tool.
# Made-up details only. Written from Lovable's and Claude Code's docs, checked 2026-11-17.
# To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files.
# On a Mac: open TextEdit, choose Format, then Make Plain Text, before you paste and save.

# The prompt:
Build a one-page pre-order page for Test Bakery, a made-up neighbourhood bakery, with made-up details only.
Show three breads with prices: Sourdough loaf $6, Cinnamon roll $3, Rye bread $5, each with a plus and a minus button and a number that starts at 0.
Show a running total at the bottom that updates as the numbers change, and a Clear button that sets everything back to 0.
Use a warm, friendly style with large text, and make it work on a phone as well as a laptop.
No sign-in, no database, no payments, no forms that send data anywhere, and no outside services.
Tell me what you'll build first and wait for my OK, then check that the buttons, the total and Clear all work.
```

### 2. lovable-vs-claude-code-sheet.md
```
# Lovable vs Claude Code for non-coders: side-by-side sheet (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

Disclosure: this channel's videos are made with Claude's help, so every line below comes from each company's own pages, with the date checked.

## What each one is
- Lovable: a website where you describe an app in a chat and it builds it: "a working application that includes frontend, backend, database, authentication, and integrations, all backed by editable code" (Lovable docs).
- Claude Code: Anthropic's coding assistant. It "reads your codebase, edits files, runs commands" and is "Available in your terminal, IDE, desktop app, and browser" (Claude Code docs).

## Where it runs, and what you install
- Lovable: runs in your web browser. A desktop app for macOS and Windows is "available on all plans, including Free, at no extra cost."
- Claude Code, desktop app: "launch Claude, sign in, and click the Code tab". "The app includes Claude Code, so you don't need to install the CLI separately. A paid subscription is required."
- Claude Code, terminal: an install command (see Claude Code for Beginners on this channel).
- Claude Code, browser (claude.ai/code): "no local setup"; "Cloud sessions work with existing GitHub repositories." Cloud sessions are on Pro, Max, Ultra and Team plans.

## Who owns the code
- Lovable's terms (updated 2026-08-28): you own your Customer Data, "including the applications, websites, or other projects you build", and "any AI Output generated for you through the Services, subject to any third-party rights in the underlying models". You also grant Lovable "a worldwide, perpetual, royalty-free license to use, copy, modify, process, analyze, and otherwise exploit your Customer Data for our business purposes". Lovable may use Customer Data to train AI models; "You may tell us at any time that you do not want your Customer Data used for model training."
- Anthropic's Consumer Terms (effective 2025-10-08): "we assign to you all our right, title, and interest (if any) in Outputs." Training: "unless you opt out of training through your account settings."
- Where the code lives: Claude Code works on files in your folder (or on GitHub, in the browser). Lovable stores it for you; Git sync with GitHub, GitLab or Bitbucket is on every plan, both ways; "Edit code" and "Download code" are on Pro and up.

## How you publish
- Lovable: click Publish in the top-right corner of the editor, next to Share; you get an address ending in lovable.app, and Lovable hosts it ("no servers to set up, and HTTPS included"). Custom domains: Pro and up.
- Claude Code: can publish an artifact, "one self-contained page with no backend", on claude.ai, private until you share it, on Pro, Max, Ultra, Team and Enterprise. "An artifact is a static page. It can't authenticate viewers itself." "For a hosted internal tool with a backend, deploy it on your own infrastructure instead."

## What each one costs (was ... when checked, 2026-11-17)
- Lovable free plan: 5 build credits a day, up to 30 a month ("5/day, 30/month", Lovable docs, Subscription plans); the pricing page adds "monthly grants of 20 Cloud credits" (lovable.dev/pricing).
- Lovable Pro: from $25 a month for 100 credits, or $250 a year; higher credit tiers cost more. Lovable Business: from $50 a month for 100 credits (Lovable docs, Subscription plans).
- Lovable chat: Chat mode messages are "covered first by the daily chat allowance".
- Claude Free plan: $0, no Claude Code.
- Claude Pro: $20 a month, or $17 a month with annual billing ($200 up front). Max: $100 a month. Ultra: $200 a month. Usage limits every 5 hours and every week (claude.com/pricing).

## Who might pick which
- Lovable: you've never coded and want one place that builds, saves data, handles logins and publishes, starting on its free plan.
- Claude Code: you already pay for Claude, want your code as files on your own computer, or have code to change, and you're happy to sort out hosting.
- Both: Lovable's GitHub sync works both ways on every plan, and its docs say you can then "work locally" and "deploy outside Lovable", so you could start in Lovable and bring in Claude Code later.

## Before you type anything
- Use made-up details like Test Bakery and test@example.com. For work, follow your employer's rules.
- Check each company's training setting in your account.

Sources: docs.lovable.dev/introduction/subscription-plans (Lovable pricing) ; lovable.dev/pricing ; docs.lovable.dev (introduction/welcome, introduction/welcome, integrations/desktop-app, features/publish, integrations/github, features/chat-mode) ; lovable.dev/terms ; claude.com/pricing ; code.claude.com/docs/en (overview, web-quickstart, claude-code-on-the-web, artifacts) ; anthropic.com/legal/consumer-terms
```
