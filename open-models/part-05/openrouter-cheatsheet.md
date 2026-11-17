# OpenRouter cheat sheet (facts checked 2026-11-17)

Fees, limits, prices and the free model list change. Check each page named below before you rely on a line.

## 1. The key
- [ ] Make a key at openrouter.ai/settings/keys. Give it a name and a credit limit ("We recommend setting a credit limit on every key").
- [ ] Keys start with sk-or-v1-. Keep yours in a password manager. Never put it in code, a file in your folder, a chat or a screenshot.
- [ ] Set it for one window only, then run your script from that same window:
      Windows PowerShell:  $env:OPENROUTER_API_KEY = "sk-or-v1-..."
      Mac Terminal:        export OPENROUTER_API_KEY="sk-or-v1-..."
- [ ] Both last only until you shut that window. Typed this way, the key also lands in the shell's history file.
      To type it without it showing or being saved in history:
      Windows PowerShell:  $env:OPENROUTER_API_KEY = [Net.NetworkCredential]::new('', (Read-Host 'Paste key' -AsSecureString)).Password
      Mac Terminal:        read -rs OPENROUTER_API_KEY && export OPENROUTER_API_KEY
- [ ] If a key leaks, delete it on the keys page and make a new one.

## 2. What it costs (was ... when checked, 2026-11-17)
| Item | OpenRouter's words or figure | Page |
|---|---|---|
| Fee when you buy credits | 5.5% ($0.80 minimum); crypto 5% | openrouter.ai/docs/faq |
| Model prices | "We pass through the pricing of the underlying model providers without any markup" | openrouter.ai/docs/faq |
| Refunds | unused credits within 24 hours; "the platform fees are non-refundable" | openrouter.ai/docs/faq |
| Credits | may expire "after one year of purchase" | openrouter.ai/docs/faq |
| Free models | 50 requests per day; 1000 per day after buying at least 10 credits; 20 requests per minute | openrouter.ai/docs/api/reference/limits |
| Privacy settings | "There are separate settings for paid and free models" (openrouter.ai/settings/privacy) | openrouter.ai/docs/guides/privacy/provider-logging |
| Fallbacks | "a fallback to a paid model incurs charges even though the first model was :free" | openrouter.ai/docs/guides/routing/model-variants/free |

## 3. Model names and list prices, per million tokens in / out (models API, 2026-11-17)
| Model name in your code | In | Out |
|---|---|---|
| openrouter/free (Free Models Router) | $0 | $0 |
| deepseek/deepseek-v4.1-flash | $0.14 | $0.42 |
| deepseek/deepseek-v4-pro | $0.90 | $1.50 |
| qwen/qwen3.8-27b | $0.15 | $1.875 |
| moonshotai/kimi-k3 | $0.192 | $16.00 |
| moonshotai/kimi-k3.1-pro | $0.2403 | $8.4023 |
| anthropic/claude-haiku-5.5 | $0.10 | $0.50 |
| anthropic/claude-sonnet-5.5 | $2.00 | $10.00 |
| anthropic/claude-opus-5.5 | $4.00 | $20.00 |
On 2026-11-17, 14 models ended in :free (two music models were also priced at 0), and none was DeepSeek, Qwen, Kimi or Claude. These are OpenRouter's listed prices; each model's page shows its providers.

## 4. What OpenRouter logs, in its words
- [ ] "We log basic request metadata (timestamps, model used, token counts). Prompt and completion are not logged by default."
- [ ] Opt-in logging of prompts and completions gives "a 1% discount on usage costs".
- [ ] "Providers that do log, or where we have been unable to confirm their policy, will not be routed to unless the model training toggle is switched on." There are "separate settings for paid and free models".
- [ ] Exceptions (data collection page): "OpenRouter retains prompts only when you opt in, or when retention is needed for CSAM review, reporting, and related legal preservation. Requests to Safety Retention endpoints are the exception: OpenRouter or the provider may retain prompts and responses from any request, only to prevent abuse, and not for training."
- [ ] The provider that runs the model still receives your text. Follow your employer's rules on what you paste.

## 5. Claude Code, in each company's words (no setup here)
- [ ] Anthropic: "Anthropic doesn't endorse, maintain, or audit third-party gateway products, and doesn't support routing Claude Code to non-Claude models through any gateway."
- [ ] OpenRouter's Claude Code page: "Claude Code with OpenRouter is only guaranteed to work with the Anthropic first-party provider."

Sources: openrouter.ai/docs/faq ; openrouter.ai/docs/api_reference/authentication ; openrouter.ai/docs/api/reference/limits ; openrouter.ai/docs/guides/routing/model-variants/free ; openrouter.ai/docs/guides/privacy/data-collection ; openrouter.ai/api/v1/models ; openrouter.ai/docs/cookbook/coding-agents/claude-code-integration ; code.claude.com/docs/en/llm-gateway
