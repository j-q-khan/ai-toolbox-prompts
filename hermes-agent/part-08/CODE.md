# Full code: Hermes Agent with Claude: API Key or Claude Subscription?

A checklist written for this video from the Hermes Agent docs and source (v0.23.1, published 2026-11-10), the hermes-official-plugins repo, and Anthropic's pricing, legal, terms and help pages, checked 2026-11-16. Prices and policies change; check the source links before you rely on a line. Nothing was installed or run.

### hermes-claude-checklist.md
```
# Hermes Agent with Claude: checklist (facts checked 2026-11-16)

Every line comes from the Hermes Agent docs or source (v0.23.1, published 2026-11-10),
the hermes-official-plugins repo, or Anthropic's own pages, with the source at the bottom.
Nothing here was installed or run. Not affiliated with Nous Research or Anthropic.
Part 2's safe choices still apply: Blank Slate, approvals on manual, a key with a spend limit.

## Which route fits you
- No Claude plan, Free or Pro: an Anthropic API key, billed per token from prepaid credit.
  Hermes docs: "Claude Pro subscribers cannot use this path" (the subscription sign-in);
  "use an ANTHROPIC_API_KEY instead".
- Max, Ultra or Team: an API key from the Console organization linked to your plan, so your
  plan's monthly API credits pay for it first (see "Monthly API credits").
- Hermes' built-in subscription sign-in: Hermes says it needs Max plus purchased extra usage
  credits; read "The subscription route" for both sides' words before you choose it.

## Prices (Anthropic pricing page, per million tokens, input / output, when checked 2026-11-16)
- Claude Opus 5.5 (claude-opus-5-5): was $4 / $20. Cache hits: $0.20.
- Claude Sonnet 5.5 (claude-sonnet-5-5): was $2 / $10. Cache hits: $0.10.
- Claude Haiku 5.5 (claude-haiku-5-5): was $0.10 / $0.50 for prompts up to 100,000 tokens,
  $0.50 / $2.50 over that.
- Claude Sonnet 4.6 (the model in Hermes' docs example): was $3 / $15.
- Every Hermes turn sends its instructions and tools as well as your message, and repeated text
  is billed at the cache-hit price when it is cached.

## Monthly API credits (Anthropic help page, checked 2026-11-16)
- Max $100 a month, Ultra $200, Team $20 per Standard seat and $100 per Premium seat
  (pooled, capped at $500). "Free, Pro, and Enterprise plans aren't eligible."
- New subscribers: seven days on the plan first.
- Claim: claude.ai > Settings > Billing (Team: Organization settings > Billing) >
  API credits > Link organization > choose or create a Console organization.
- "You can link only one Console organization… You can't change the linked organization
  yourself." Sign in to the Console with the same email you use on claude.ai.
- Covers: "The Claude API (Messages API and Message Batches API)", the Console Playground,
  Claude Managed Agents, the Claude Agent SDK.
- Doesn't cover: interactive Claude Code; "Extra usage in Claude, Claude Code, or Claude Cowork";
  Claude on Bedrock, Vertex AI or Foundry.
- No roll-over. When they run out: "API requests stop until your next monthly credits arrive.
  Usage is never charged to your Claude plan." (unless the organization bought credits or
  turned on auto-reload)

## The subscription route: both sides, word for word
Hermes docs (Integrations: Providers, Anthropic (Native), v0.23.1):
- "When you authenticate via hermes model → Anthropic OAuth (or via hermes auth add anthropic
  --type oauth), Hermes routes as Claude Code against your Anthropic account. It only works if
  you're on a Claude Max plan and have purchased extra usage credits. The base Max plan
  allowance (the usage included in Claude Code by default) is not consumed by Hermes — only
  the extra/overage credits you've added on top are. Claude Pro subscribers cannot use this path."
- Hermes' menu labels that option "1. Claude Pro/Max subscription (OAuth login)".
Nous Research's experimental plugin (hermes-official-plugins, claude-subscription-directsdk, v0.4.0):
- README: it "drives the unmodified official Claude Code executable as a request-scoped model
  client for your Claude Pro/Max subscription"; "This is a review build, not a full-parity or
  production-readiness claim."; "Subscription entitlement and extra-usage settings still belong to
  the account and native service." Not set up in the video.
Anthropic, Claude Code Legal and compliance (code.claude.com, read 2026-11-16):
- "OAuth authentication is intended exclusively for purchasers of Claude Free, Pro, Max, Ultra,
  Team, and Enterprise subscription plans and is designed to support ordinary use of Claude
  Code and other native Anthropic applications."
- "Developers building products or services that interact with Claude's capabilities,
  including those using the Agent SDK, should use API key authentication through Claude
  Console or a supported cloud provider. Anthropic does not permit third-party developers to
  offer Claude.ai login into their own applications, or to route requests through Free, Pro,
  Max, or Ultra plan credentials on behalf of their users."
- "Nor does it prevent an end user from signing in to the unmodified Claude Code binary with
  their own Claude subscription, including where a platform hosts Claude Code as described
  under Can customers offer Claude Code in their products? above."
- "Anthropic reserves the right to take measures to enforce these restrictions and may do so
  without prior notice."
Anthropic, Consumer Terms of Service (effective Oct 8, 2025), things you may not do:
- "Except when you are accessing our Services via an Anthropic API Key or where we otherwise
  explicitly permit it, to access the Services through automated or non-human means, whether
  through a bot, script, or otherwise."
Anthropic help, Use the Claude Agent SDK with your Claude plan:
- "Update June 15, 2026: We've paused the previously-announced changes to Claude Agent SDK
  usage. For now, nothing has changed: Claude Agent SDK, claude -p, and third-party app usage
  still draw from your subscription limits."
The video doesn't decide between these. Read both pages on the day you set this up.

## Set the key in Hermes (PowerShell on Windows, Terminal on Mac; the same commands)
1. Make a key at https://platform.claude.com/settings/keys (the page Hermes points to).
   API use is prepaid: buy a small amount of credit on the Billing page
   (platform.claude.com/settings/billing) and leave auto-reload off, so the credit is your limit.
2. Type:
     hermes model
   Choose Anthropic.
3. If you use Claude Code, you may see "Claude Code credentials: ✓ (auto-detected)" with
   "Use existing credentials" selected. Enter keeps that borrowed subscription login.
   Choose "Reauthenticate (new OAuth login)" instead.
   (If a key is already saved, the screen shows it here instead; "Use existing credentials"
   then keeps the key.)
4. At "Choose authentication method", type 2 (Anthropic API key (pay-per-token)).
5. Paste the key at "API key (sk-ant-...):". It may show nothing as you paste.
   You should see: ✓ API key saved.   (Hermes saves it as ANTHROPIC_API_KEY in its .env file.)
6. Pick claude-opus-5-5 from the list. If you want claude-sonnet-5-5 and it isn't listed,
   type the name.
   You should see: Default model set to: claude-opus-5-5 (via Anthropic)
7. Start a chat:
     hermes

## Borrowed Claude Code logins (Hermes docs, Security: Borrowed CLI logins)
- Default: auth.adopt_external_logins: true. With no login of its own, Hermes can borrow
  Claude Code's ~/.claude/.credentials.json (or Keychain entry) and refresh it.
- "Once two programs hold one token family, whichever refreshes first invalidates the other's copy."
- Turn it off:
     hermes config set auth.adopt_external_logins false
  "With the switch off Hermes never reads or refreshes those files."

## What "Hermes with Claude Code" can mean
1. The borrowed login above.
2. The importer:  hermes import-agent claude-code --dry-run   (preview only)
   then:          hermes import-agent claude-code
   Copies CLAUDE.md (into memory), permission rules, MCP servers and skills from ~/.claude.
   "Credential files (~/.claude/.credentials.json, …) are never read."
3. The bundled claude-code skill: Hermes hands coding jobs to the Claude Code program
   ("Delegate coding to Claude Code CLI"), which uses Claude Code's own login.

## Keep the cost down (Hermes docs, Configuring models)
- Stay on one model through a long chat: "A one-turn switch breaks the provider's prompt-cache
  prefix twice (switching out and back)… the next turn re-pays full input cost".

## Sources (checked 2026-11-16)
- Hermes docs, Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers#anthropic-native
- Hermes docs, Borrowed CLI logins: https://hermes-agent.nousresearch.com/docs/user-guide/security#borrowed-cli-logins
- Hermes docs, Import from Other Agents: https://hermes-agent.nousresearch.com/docs/user-guide/import-from-other-agents
- Hermes docs, Configuring models: https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models
- Hermes source (tag v0.23.1): hermes_cli/model_setup_flows.py, hermes_cli/model_setup_flows_common.py,
  agent/anthropic_credentials.py at https://github.com/NousResearch/hermes-agent
- Claude Subscription DirectSDK: https://github.com/NousResearch/hermes-official-plugins/tree/main/claude-subscription-directsdk
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Claude Code legal and compliance: https://code.claude.com/docs/en/legal-and-compliance
- Consumer Terms: https://www.anthropic.com/legal/consumer-terms
- Monthly API credits: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans
- Paying for API usage: https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage
- Agent SDK with your plan: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan
- Releases: https://github.com/NousResearch/hermes-agent/releases
```
