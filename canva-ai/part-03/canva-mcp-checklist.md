# Claude Canva MCP: Claude Code and Cowork checklist (facts checked 2026-11-17)

To keep a copy: paste this into Notepad and save it with the box called Save as type set to All files. On a Mac, open TextEdit, choose Format, then Make Plain Text, before you paste and save.

## Before you start
- [ ] The Canva connector is connected on claude.ai (Part 1 of this series): Customize, then Connectors.
- [ ] Claude Code is installed, or you have Cowork (Anthropic: available on paid plans).
- [ ] A work account: follow your employer's rules first. Each person signs in to Canva for themselves. On Team and Enterprise plans, an owner enables connectors first (Anthropic's help page).
- [ ] Anthropic: connecting a service grants Claude "permission to access and potentially modify data within that service based on your account permissions".

## Claude Code
- [ ] Start it: `claude` in PowerShell (Windows) or Terminal (Mac).
- [ ] Type `/mcp`. Anthropic's docs: "Servers from claude.ai appear in the list with indicators showing they come from claude.ai." The entry may be named with a prefix: the docs' own examples are `claude.ai Slack` and `claude.ai Claude Docs`.
- [ ] Not there? Type `/status`. Connectors are fetched only with a claude.ai subscription login. They aren't loaded, "even if you previously ran `/login`", when `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `apiKeyHelper` is active, with a third-party provider such as Amazon Bedrock, with an Anthropic profile, or with a `claude setup-token` token.
- [ ] Fix (Anthropic's docs): unset that environment variable, remove the `apiKeyHelper` setting or switch off the profile, then `/login` and select your claude.ai account. How to unset a variable depends on how it was set; this video doesn't cover it.
- [ ] Connectors you have never signed in to may be collapsed behind a "Show unused connectors" entry at the end of the claude.ai section.
- [ ] Check: paste list-canva-tools-prompt.txt. You should get tool names back. Nothing changes.
- [ ] Shortcut: in `/mcp` you can switch a connector off for the current project (folder) only.

## Cowork
- [ ] Anthropic: "Web connectors are available for all users on Claude, Cowork, Claude Desktop, and Claude Mobile".
- [ ] Control which connectors Claude can use from the "+" menu in the chat box, or Customize, then Connectors.
- [ ] Modes: Cowork has three. To approve every "Needs approval" action yourself, use Manual (mode selector in the chat box). Tools you set to "Always allow" are approved in every mode; "Blocked" tools are denied.

## Canva's plugin (canva-sdks/canva-skills)
- [ ] Published by Canva on GitHub, Apache License 2.0, marked "Anthropic verified" on Anthropic's plugin listing. Not installed or run for this video.
- [ ] Six skills: edit-design, resize-for-social-media, bulk-create, brand-check, get-design-feedback, implement-feedback.
- [ ] Install lines, typed inside Claude Code: `/plugin marketplace add canva-sdks/canva-skills` then `/plugin install canva@canva-skills`.
- [ ] The second line opens a panel first. Anthropic's docs: "A plugin can run hooks and MCP servers, so read the pane before you install."
- [ ] The repo then says: "Connect the `canva` MCP server and sign in to Canva when prompted."
- [ ] bulk-create and autofill, as written, not resolved: the plugin listing says "The bulk-create skill requires a Canva Enterprise plan" and the repo says "Requires Canva Enterprise for autofill"; Canva's tool docs say "Autofill is available to users on Canva Pro, Business, and Enterprise plans."
- [ ] resize-for-social-media: the skill's own file says "Do not require user approval between steps". Canva's docs say resizing makes a copy and "The original is unchanged", and that it's marked Pro and above, with a limited trial on the Free plan.

## Limits (Canva's developer docs)
- [ ] Rate limits are in requests a minute: generate-design 20, export-design 20, resize-design 20, autofill-design 60, generate-image 10.
- [ ] Tools without their own limit share a default cap of 300 requests a minute per user, "counted across all of that user's MCP clients".
- [ ] Pro and above (Canva Pro, Business and Enterprise): autofill, Brand Kits and Brand Templates, resizing. No Canva price is given here; see https://www.canva.com/pricing/
- [ ] Anthropic's listing shows 17 Canva tools and Canva's table 46, so Claude may not offer every tool. Nothing here was tested.

## Not this one
- [ ] The Canva Dev MCP server (`canva-dev`) "provides AI-powered development assistance for Canva apps". It needs Node.js v24 or later and is for people building Canva apps. It isn't the connector.

Sources: code.claude.com/docs/en/mcp ; code.claude.com/docs/en/discover-plugins ; support.claude.com/en/articles/11176164 ; support.claude.com/en/articles/13345190 ; claude.com/connectors/canva ; claude.com/marketplace/plugins/canva ; github.com/canva-sdks/canva-skills ; canva.dev/docs/apps/mcp/tools ; canva.dev/docs/apps/mcp/tools/autofill-design ; canva.dev/docs/apps/mcp/tools/resize-design ; canva.dev/docs/apps/dev-mcp-server
