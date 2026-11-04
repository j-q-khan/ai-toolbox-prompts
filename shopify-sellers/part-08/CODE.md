# Full code: Shopify Order Tracking with an AI Chatbot

The code is built from Shopify's official docs and Anthropic's Claude Code docs, and needs a free Shopify development store to try.

### Setup commands
```
npm install -g @shopify/cli@5.0.0
claude plugin install shopify-ai-toolkit@claude-plugins-official
mkdir late-shipments
cd late-shipments
shopify store auth --store your-dev-store.myshopify.com --scopes read_orders
```

### orders.graphql
```
query {
  orders(first: 50, reverse: true) {
    nodes {
      name
      createdAt
      displayFulfillmentStatus
      statusPageUrl
      fulfillments(first: 5) {
        displayStatus
        inTransitAt
        estimatedDeliveryAt
        trackingInfo(first: 1) { company number url }
      }
    }
  }
}
```

### CLAUDE.md
```
# Late shipment finder
- Use only orders.json. Never change the store and never send messages.
- Flag orders UNFULFILLED or PARTIALLY_FULFILLED for more than 2 days.
- Flag fulfillments with displayStatus DELAYED, ATTEMPTED_DELIVERY, FAILURE or NOT_DELIVERED.
- Flag fulfillments whose estimatedDeliveryAt has passed and are not DELIVERED.
- For each, show the order name, days since createdAt, status and tracking.
- Draft a short message with the statusPageUrl. For unshipped orders, offer the choice to wait or cancel for a prompt refund.
- Write the result to late-orders.md.
```

### Run
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --json --query-file orders.graphql --output-file orders.json
claude "Find the late shipments in orders.json"
```
