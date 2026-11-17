# Full code: Qwen 3.8 and Kimi K3: The Other Open Models and Their Licences

A licence table and a licence script written for this video from each model's own LICENSE file and card on Hugging Face, LM Studio's model pages and Hugging Face's model-card docs (checked 2026-11-17). The script was not run against Hugging Face; the output shown is an example. licence_check.py makes one request to Hugging Face's public model API, needs no key, and writes one file, MODEL-LICENCE.md. It reads the licence field the maker set; it is not legal advice. Test only.

### 1. licence-table.md
```
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
```

### 2. licence_check.py
```
# licence_check.py: look up a model's licence on Hugging Face and write it into MODEL-LICENCE.md
# in this folder, with the maker's page and today's date.
# Test only. Written from the Hugging Face Hub docs and API (checked 2026-11-17), not run against a real model.
# Standard library only. No key needed; it makes one request to huggingface.co and writes one file.
# It reads the licence field the maker set. It is not legal advice: open the LICENSE file and check it yourself.
#
# Run: python licence_check.py Qwen/Qwen3.5-4B      (on a Mac: python3 licence_check.py Qwen/Qwen3.5-4B)
import datetime
import json
import re
import sys
import urllib.error
import urllib.request

API = "https://huggingface.co/api/models/"  # the Hub's public model API
OUT = "MODEL-LICENCE.md"
DEFAULT_MODEL = "Qwen/Qwen3.5-4B"  # a small Qwen model under Apache-2.0 (checked 2026-11-17)


def fetch(model):
    req = urllib.request.Request(API + model, headers={"User-Agent": "licence-check"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        sys.exit(f"Hugging Face answered HTTP {err.code} for {model}. Check the name, e.g. Qwen/Qwen3.5-4B.")
    except (urllib.error.URLError, TimeoutError, ValueError) as err:
        sys.exit(f"Couldn't reach Hugging Face: {err}")


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*", model):
        sys.exit("Give the model as maker/name, e.g. Qwen/Qwen3.5-4B")
    data = fetch(model)
    card = data.get("cardData") or {}
    licence = card.get("license") or "not stated"
    if isinstance(licence, list):  # the field can hold a list
        licence = ", ".join(str(x) for x in licence)
    licence = str(licence)
    name = card.get("license_name")
    link = card.get("license_link")
    page = "https://huggingface.co/" + model
    if link and not str(link).startswith("http"):
        link = f"{page}/blob/main/{link}"  # a link like "LICENSE" points to the file in the repo
    lines = [
        f"# {OUT}",
        "",
        f"- Model: {model}",
        f"- Licence field on Hugging Face: {licence}",
    ]
    if name:
        lines.append(f"- Licence name: {name}")
    lines.append(f"- Licence file: {link or page + '/blob/main/LICENSE'}")
    lines.append(f"- Maker's page: {page}")
    lines.append(f"- Checked: {datetime.date.today().isoformat()}")
    lines.append("")
    if "other" in licence.split(", "):
        lines.append("This is a custom licence. Open the licence file and look for Model as a Service and for")
        lines.append("a rule about showing the model's name before you build a product on it.")
    elif licence == "not stated":
        lines.append("No licence field is set. Don't use the model until you've found its licence file.")
    else:
        lines.append("This is the licence the maker set in the model card. Open the licence file to confirm it.")
    lines.append("Not legal advice: check the licence file yourself.")
    text = "\n".join(lines) + "\n"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"Saved {OUT} in this folder.")


if __name__ == "__main__":
    main()
```

### 3. example-output.txt
```
Example output (not run against Hugging Face: the licence field is the one the Hub's API showed for Qwen/Qwen3.5-4B on 2026-11-17):
# MODEL-LICENCE.md

- Model: Qwen/Qwen3.5-4B
- Licence field on Hugging Face: apache-2.0
- Licence file: https://huggingface.co/Qwen/Qwen3.5-4B/blob/main/LICENSE
- Maker's page: https://huggingface.co/Qwen/Qwen3.5-4B
- Checked: 2026-11-17

This is the licence the maker set in the model card. Open the licence file to confirm it.
Not legal advice: check the licence file yourself.

Saved MODEL-LICENCE.md in this folder.
```
