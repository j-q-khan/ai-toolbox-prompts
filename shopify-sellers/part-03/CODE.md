# Full code: Shopify Fraud Prevention: Stop Fake Orders and Bots

The code is built from Shopify's official docs and Anthropic's Claude Code docs. Try it on a free Shopify development store, never on a store with real customers.

### Setup command (Shopify CLI 5.0.0, checked 2026-11-03)
```
npm install -g @shopify/cli@latest
```

### Sign in to your development store with view-only orders access, last 60 days (no key file: this opens a browser sign-in)
```
shopify store auth --store your-dev-store.myshopify.com --scopes read_orders
```

### risky-orders.graphql (Admin API 2026-10, no customer emails or IPs)
```
query RiskyOrders {
  orders(first: 50, sortKey: CREATED_AT, reverse: true, query: "risk_level:high OR risk_level:medium") {
    nodes {
      name
      createdAt
      test
      displayFinancialStatus
      billingAddressMatchesShippingAddress
      totalPriceSet {
        shopMoney {
          amount
          currencyCode
        }
      }
      risk {
        recommendation
        assessments {
          riskLevel
          facts {
            description
            sentiment
          }
        }
      }
    }
  }
}
```

### Run the report, then ask Claude Code to sum it up
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file risky-orders.graphql --output-file risky-orders.json
claude "Read risky-orders.json. Group the orders by recommendation, risk level and risk fact description, show the five most common facts in a table, and suggest Shopify Flow conditions to review. Don't change, cancel or refund anything."
```
