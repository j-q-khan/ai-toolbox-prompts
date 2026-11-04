# Claude build prompt: Replace Shopify Apps with Claude Code

From "AI for Shopify Sellers", Part 11. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: set up a safe theme sandbox where Claude Code can replace one small app job, [the job, for example a free-shipping banner], with a theme section, without any way to push or publish.
Inputs: a Shopify development store, [your-dev-store], created with demo data. Its theme name: [theme name]. My app list, one line each: name, monthly price, the one job it does. Optionally, a design I made in Claude Design and handed off to Claude Code.
Steps, in order:
1. Check that Shopify CLI, Git and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sort my app list into: built-in setting, Shopify Flow workflow, small theme change, Shopify Function, or keep the app. Anything touching payments, taxes or customer data goes in keep. Write app-sort.md and wait for me to pick one job.
3. Show me, then run after my yes: shopify theme duplicate for a backup named Backup before Claude, then shopify theme pull into a folder named my-theme, then git init and a first commit.
4. Write CLAUDE.md (one small change at a time, explain before changing, prefer a new section or snippet, run shopify theme check after every change, never push, publish or delete a theme) and .claude/settings.json with deny rules for shopify theme push, publish and delete and anything with allow-live.
5. Build the job as a new section, following the Claude Design handoff if there is one. Run shopify theme check, fix errors, and commit with a clear message.
6. Tell me the shopify theme dev command to preview it, and the push command with --unpublished for me to run myself.
Safety: work only inside this folder and the development store, never real client or customer data, never edit the published theme, and ask before any write to the store. Stop and ask me before running anything that changes data.
Output: app-sort.md, the theme folder with Git history, CLAUDE.md, .claude/settings.json, the new section, and a list of every file touched.
