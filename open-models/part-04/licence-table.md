# Qwen 3.8 and Kimi K3: licence table (facts checked 2026-11-17)

Licences and model pages change. Open each LICENSE file named below and check it yourself before you rely on a line. This is a summary of the licence files, not legal advice.

## 1. Which sizes fit a home computer
| Model | Size, per its card | Memory LM Studio lists | At home? |
|---|---|---|---|
| Qwen3.5 and Qwen3.6 sizes (Part 2) | 0.8B to 35B-A3B | 2 GB (2B) to 20 GB (35B-A3B) | Yes, the small ones |
| Qwen3.8-27B | 27B | 16 GB minimum | Yes, with 16 GB or more |
| Qwen3.8-Flash-Next | 125B (6B activated) | 96 GB minimum | Not on most home computers |
| Qwen3.8-2.4T-A95B | 2.4T (95B activated) | no page | No: data-centre hardware |
| Kimi-K3, Kimi-K3.1-Pro | 2.8T (104B activated) | no page | No: rent it |
| Kimi-K2.7-Code | 1T (32B activated) | no page | No: rent it |

## 2. Licence and business rule
| Model | Licence (its LICENSE file) | Model as a Service rule |
|---|---|---|
| Qwen3.8-27B | Apache License 2.0 | None |
| Qwen3.5 and Qwen3.6 sizes | Apache License 2.0 | None |
| Qwen3.8-Flash-Next | Qwen Community License 1.0 | A Model as a Service or "AI Work Assistant" business needs "a separate license from Qwen" for any commercial purpose. No revenue limit. |
| Qwen3.8-2.4T-A95B | Qwen3.8-Max License | The same, only when aggregate revenue "exceeds US$50,000,000 ... during any consecutive twelve (12) months". |
| Kimi-K3, Kimi-K3.1-Pro | Kimi K3 License, Kimi K3.1-Pro License | A Model as a Service business above "20 million US dollars ... in total over any consecutive 12 months" must "enter into a separate agreement with Moonshot AI". |
| Kimi-K2.7-Code | Modified MIT License | None. The only change from MIT is the name rule below. |

## 3. In every custom licence above (not Apache 2.0): show the model's name
- [ ] Qwen Community and Qwen3.8-Max, clause 1: a product with "more than 100,000,000 monthly active users or US$ 20,000,000 ... monthly revenue" must display the "respective model name ... prominently ... on the user interface".
- [ ] Kimi K3 and K3.1-Pro, section 3, and Kimi-K2.7-Code: more than 100 million monthly active users, or more than 20 million US dollars in monthly revenue: display "Kimi K3", "Kimi K3.1-Pro" or "Kimi K2.7 Code".

## 4. What "Model as a Service" means, in the licences' words
- [ ] Qwen: "giving a third party access to language model inference or fine-tuning (e.g., via API or a hosted endpoint) in a manner that allows such third parties to exercise meaningful control over the inputs, parameters, or training data. This does not include the mere relaying of requests to models hosted by other third parties."
- [ ] Qwen, "AI Work Assistant": "an independent AI-powered product primarily designed for AI-assisted coding or office productivity", not a single-purpose tool, an assistant for another domain, or a feature of a product whose main purpose is something else.
- [ ] Kimi: the same first sentence ("e.g., via API"), and it "does not include (a) end-user products with model capabilities solely embedded within specific features or harnesses, or (b) mere relaying of requests to models hosted by others."

## 5. The exceptions
- [ ] Qwen (Community and Max): the Model as a Service rule "shall not apply to the licensee's internal Use of the Software, provided that such Use does not make the Software, its outputs, or its underlying model capabilities available to any third party."
- [ ] Kimi (K3 and K3.1-Pro, section 4): sections 2 and 3 "do not apply to: (a) internal use of the Software, defined as any use that does not make the Software, its outputs, or its underlying capabilities available to third parties; or (b) any use of the Software accessed through Moonshot AI's official products or certified inference partners."
- [ ] Apache License 2.0, section 2: "a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license". Section 4 asks you to pass on a copy of the licence and keep its notices.

## 6. Before you build on one
- [ ] On the model's Hugging Face page, check the licence it shows. "other" means a custom licence: open the LICENSE file.
- [ ] Search the LICENSE file for "Model as a Service" and "displayed".
- [ ] Moonshot's API is at platform.kimi.ai (platform.moonshot.ai redirects there, checked 2026-11-17).

Sources: huggingface.co/Qwen/Qwen3.8-27B (LICENSE) ; huggingface.co/Qwen/Qwen3.8-Flash-Next (LICENSE) ; huggingface.co/Qwen/Qwen3.8-2.4T-A95B (LICENSE) ; huggingface.co/moonshotai/Kimi-K3 (LICENSE) ; huggingface.co/moonshotai/Kimi-K3.1-Pro (LICENSE) ; huggingface.co/moonshotai/Kimi-K2.7-Code (LICENSE) ; huggingface.co/api/models?author=Qwen ; lmstudio.ai/models/qwen/qwen3.8-27b ; lmstudio.ai/models/qwen/qwen3.8-flash-next ; huggingface.co/docs/hub/model-cards
