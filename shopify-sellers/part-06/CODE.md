# Full code: Meta Pixel Not Working on Shopify?

The code is built from Shopify's official docs and Anthropic's API docs, and needs a free Shopify development store to try.

### Setup commands (Shopify CLI 5.0.0, anthropic 2.4.0, 2026-11-03)
```
npm install -g @shopify/cli@latest
pip install anthropic
shopify store auth --store your-dev-store.myshopify.com --scopes read_reports
```

### API key (put your own key in place of the placeholder)
```
export ANTHROPIC_API_KEY="your-api-key-here"
```

### orders.graphql
```
query {
  shopifyqlQuery(query: "FROM sales SHOW total_sales, orders TIMESERIES day SINCE -30d UNTIL today ORDER BY day ASC") {
    tableData {
      columns {
        name
        dataType
        displayName
      }
      rows
    }
    parseErrors
  }
}
```

### Run the query
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file orders.graphql --output-file orders.json
```

### compare.py (save Meta's purchases by day as meta_purchases.csv)
```
import anthropic

client = anthropic.Anthropic()

with open("orders.json", encoding="utf-8") as f:
    shopify_data = f.read()
with open("meta_purchases.csv", encoding="utf-8-sig") as f:
    meta_data = f.read()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Below are Shopify orders by day and Meta purchases by day for the same dates. "
            "Find the date and purchase columns in the Meta file. Line the two up by date, "
            "show the gap for each day, label each day as Meta over-counting or under-counting, "
            "and say which pattern is most common.\n\nSHOPIFY:\n" + shopify_data + "\n\nMETA:\n" + meta_data,
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
```

### Run
```
python compare.py
```
