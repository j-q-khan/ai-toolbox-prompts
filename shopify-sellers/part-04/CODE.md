# Full code: Shopify AI Product Descriptions at Scale

The code is built from Shopify's official docs and Anthropic's API docs, and needs a free Shopify development store to try.

### Setup commands (anthropic 2.4.0 on PyPI, 2026-11-03)
```
claude plugin install shopify-ai-toolkit@claude-plugins-official
mkdir descriptions && cd descriptions
python3 -m venv .venv && source .venv/bin/activate
pip install anthropic
```

### API key (put your own key in place of the placeholder)
```
export ANTHROPIC_API_KEY="your-api-key-here"
```

### describe.py (save your export as products_export.csv in the same folder)
```
import csv
import anthropic

client = anthropic.Anthropic()

PROMPT = """Write a product description for a Shopify store, using only these facts.
Add no materials, sizes, certifications or benefits that are not listed.
Write 80 to 120 words in plain sentences, in a [your brand voice] tone.
Reply with the description only.

Title: {title}
Type: {ptype}
Vendor: {vendor}
Tags: {tags}
Current description: {old}"""

rows = []
with open("products_export.csv", newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        if not row["Title"]:
            continue
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": PROMPT.format(
                        title=row["Title"],
                        ptype=row["Type"],
                        vendor=row["Vendor"],
                        tags=row["Tags"],
                        old=row["Description"],
                    ),
                }
            ],
        )
        text = ""
        for block in message.content:
            if block.type == "text":
                text += block.text
        rows.append({"URL handle": row["URL handle"], "Title": row["Title"], "Description": text})

with open("descriptions_to_check.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["URL handle", "Title", "Description"])
    writer.writeheader()
    writer.writerows(rows)
```

### Run
```
python describe.py
```
