# Full code: How to Win Shopify Chargebacks

The code is built from Shopify's official docs and Anthropic's Claude Code docs, and needs a free Shopify development store to try.

### Setup commands
```
npm install -g @shopify/cli@5.0.0
claude plugin install shopify-ai-toolkit@claude-plugins-official
mkdir chargeback-tracker
cd chargeback-tracker
shopify store auth --store your-dev-store.myshopify.com --scopes read_shopify_payments_disputes,read_orders
```

### disputes.graphql
```
query {
  disputes(first: 25, reverse: true) {
    nodes {
      id
      type
      status
      initiatedAt
      evidenceDueBy
      evidenceSentOn
      amount { amount currencyCode }
      reasonDetails { reason networkReasonCode }
      order { name displayFulfillmentStatus }
    }
  }
}
```

### CLAUDE.md
```
# Chargeback tracker
- Use only disputes.json. Never change the store or contact customers.
- Keep status NEEDS_RESPONSE, sorted by evidenceDueBy, soonest first.
- Show order name, type, reason, amount, due date and days left.
- Add the evidence Shopify lists for that reason, for example:
  - FRAUDULENT: fulfillment date, billing details, IP and country, tracking.
  - PRODUCT_NOT_RECEIVED: fulfillment date, tracking, delivery proof.
  - PRODUCT_UNACCEPTABLE: tracking, product page and photos.
- Say what is missing. Never invent evidence. Write checklist.md.
```

### Run
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --json --query-file disputes.graphql --output-file disputes.json
claude "Make the chargeback checklist from disputes.json"
```
