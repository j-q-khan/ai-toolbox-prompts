# Full code: Shopify Traffic but No Sales?

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

### funnel.graphql
```
query {
  shopifyqlQuery(query: "FROM sessions SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout, sessions_that_completed_checkout, conversion_rate WHERE human_or_bot_session = 'human' GROUP BY landing_page_path SINCE -30d UNTIL today ORDER BY sessions DESC LIMIT 20") {
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
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file funnel.graphql --output-file funnel.json
```

### diagnose.py
```
import anthropic

client = anthropic.Anthropic()

with open("funnel.json", encoding="utf-8") as f:
    data = f.read()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "This is a Shopify funnel for human sessions over the last 30 days, by landing page. "
            "For each page, work out the cart rate and the purchase rate. "
            "Name the three pages that lose the most visitors, say at which step, "
            "and suggest one fix for each. Show your working.\n\n" + data,
        }
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
```

### Run
```
python diagnose.py
```
