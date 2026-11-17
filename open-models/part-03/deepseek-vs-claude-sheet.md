# DeepSeek V4 vs Claude: comparison sheet (facts checked 2026-11-16)

Prices and policies change. Re-check each line on the page named beside it before you rely on it.
This channel's videos are made with Claude's help, so both sides are quoted from their own pages.

## 1. Price per 1M tokens, US dollars (was, when checked on 2026-11-16)
| Model | Input | Output | Source |
|---|---|---|---|
| DeepSeek-V4.1-Flash (`deepseek-flash`), peak | $0.30 | $1.20 | api-docs.deepseek.com/quick_start/pricing |
| DeepSeek-V4.1-Flash, off-peak | $0.15 | $0.60 | same |
| DeepSeek-V4-Pro (`deepseek-v4-pro`), peak | $1.32 | $3.96 | same |
| DeepSeek-V4-Pro, off-peak | $0.66 | $1.98 | same |
| Claude Haiku 5.5, prompts up to 100,000 tokens | $0.10 | $0.50 | docs.claude.com/en/docs/about-claude/pricing |
| Claude Haiku 5.5, prompts over 100,000 tokens | $0.50 | $2.50 | same |
| Claude Sonnet 5.5 | $2 | $10 | same |
| Claude Opus 5.5 | $4 | $20 | same |
| Claude Fable 5.2 | $8 | $40 | same |

- [ ] DeepSeek input above is the cache-miss price. Cache hits were $0.003 / $0.006 (Flash, off-peak / peak) and $0.022 / $0.044 (Pro).
- [ ] Claude cache hits ("Hits and refreshes"): Haiku 5.5 $0.01, Sonnet 5.5 $0.10, Opus 5.5 $0.20, Fable 5.2 $0.20. Claude also lists cache-write prices above the input price (Haiku 5.5: $0.125 for 5-minute writes); DeepSeek's page lists none.
- [ ] DeepSeek: "Off-peak rates are half of the peak rates. Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full."
- [ ] Anthropic: "The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens."
- [ ] Claude's monthly chat plans are a different thing from these per-token prices.

## 2. Privacy, in each company's own words
### DeepSeek
- [ ] Privacy Policy, "Last Update: Feb 10, 2026": "To provide you with our services, we directly collect, process and store your Personal Data in People's Republic of China."
- [ ] Same policy: "We retain Personal Data for as long as necessary to provide our Services and for the other purposes set out in this Privacy Policy."
- [ ] Same policy lists "the right to opt-out of using your Personal Data for training our models or optimizing our technologies.", among rights introduced with "Depending on where you live and subject to exceptions provided under applicable data protection laws, you may have certain rights".
- [ ] Same policy lists, among its uses: "to train and improve our technology, such as our machine learning models and algorithms." No separate line was found, in it or in the Open Platform Terms, for API inputs (checked 2026-11-16).
- [ ] Open Platform Terms of Service (effective April 29, 2026), 5.5: "We will collect and process the personal information you provide as the data subject in accordance with the "DeepSeek Privacy Policy"."
### Anthropic
- [ ] Privacy Policy (effective Sep 10, 2026), section 5, Data Transfers: "Anthropic is a global company, and when you access our Services, your personal data is transferred to our servers in the US, or to other countries outside the European Economic Area ("EEA") and the UK for the purposes outlined in Section 2 of this Privacy Policy". (The same policy says it doesn't apply to content processed for customers of Anthropic's business offerings.)
- [ ] Privacy Center, "Is my data used for model training?" (commercial customers, August 18, 2026): "By default, we will not use your inputs or outputs from our commercial products (e.g. Claude for Work, Anthropic API, Claude Gov, etc.) to train our models."
- [ ] Privacy Center, data retention (commercial, July 1, 2026): "For Anthropic API users, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except:" (longer-retention services you control, such as the Files API, and Usage Policy enforcement).
- [ ] Privacy Policy (effective Sep 10, 2026), for the Claude apps: "We may use your Inputs and Outputs to train and improve Anthropic AI models, unless you opt out through your account settings." It adds: "Even if you opt-out, we will use Inputs and Outputs for model improvement when" (for example, chats flagged for safety review).
### Either one
- [ ] Follow your employer's rules about what you paste.
- [ ] Keep passwords, API keys and other secrets out of every chatbot and API prompt.

## 3. The US notice (Federal Register, 2026-10-20, Department of Homeland Security)
- [ ] Title: "Notice of Order Regarding Exclusion and Removal of DeepSeek Products From Federal Civilian Executive Branch Information Technology Systems and Procurements".
- [ ] It orders "(1) exclusion of information technology products and services developed by Hangzhou DeepSeek Artificial Intelligence Co., Ltd (DeepSeek), to include affiliated entities as defined in 48 CFR 2.101, from federal civilian agency procurements; and (2) removal of all DeepSeek and DeepSeek-affiliate products, and third-party products and services developed using DeepSeek implementations, from civilian agency information technology."
- [ ] Scope: federal civilian agency IT and procurement. If you work for one, follow your agency.
- [ ] The notice text doesn't mention open weights run on your own computer. (The signed order is attached as scanned page images; read it at regulations.gov, docket DHS-2026-0628.)

## 4. Running the open weights yourself
- [ ] DeepSeek-V4.1-Flash and DeepSeek-V4-Pro weights: MIT licence ("This repository and the model weights are licensed under the MIT License.").
- [ ] DeepSeek-V4-Pro: 1.6T parameters, 49B activated (V4 preview card, huggingface.co/deepseek-ai/DeepSeek-V4-Pro). The -0813 card's vLLM example "serves the model with vLLM on a single 4×GB300 node."
- [ ] DeepSeek-V4.1-Flash: "552B backbone parameters", 8B activated during prefill and 16B during decode.
- [ ] For scale (Part 2): LM Studio lists 16 GB as the minimum system memory for Qwen3.6-27B. Neither DeepSeek V4 model fits a home computer (our reasoning from those figures).
- [ ] Another company hosting the open weights has its own privacy terms: read them too.

Sources: api-docs.deepseek.com/quick_start/pricing ; cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html ; cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html ; huggingface.co/deepseek-ai/DeepSeek-V4-Pro ; huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 ; huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash ; docs.claude.com/en/docs/about-claude/pricing ; privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training ; privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data ; anthropic.com/legal/privacy ; federalregister.gov/documents/2026/10/20/2026-21447
