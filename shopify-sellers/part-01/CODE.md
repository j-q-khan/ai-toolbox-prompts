# Full code: How to Use AI for Shopify

The code is built from Shopify's official docs and Anthropic's Claude Code docs. Try it on a free Shopify development store, never on a store with real customers.

### Setup commands (Shopify CLI 5.0.0 and the Shopify AI Toolkit plugin, checked 2026-11-03)
```
npm install -g @shopify/cli@latest
claude plugin install shopify-ai-toolkit@claude-plugins-official
```

### Sign in to your development store with view-only product access (no key file: this opens a browser sign-in)
```
shopify store auth --store your-dev-store.myshopify.com --scopes read_products
```

### low-stock.graphql (Admin API 2026-10)
```
query LowStock {
  productsCount {
    count
  }
  products(first: 10, sortKey: INVENTORY_TOTAL) {
    nodes {
      title
      status
      totalInventory
    }
  }
}
```

### Run
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file low-stock.graphql --output-file low-stock.json
```
