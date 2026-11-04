# Full code: How to Connect Claude to Shopify with MCP

The code is built from Shopify's official docs and Anthropic's Claude Code docs. Try it on a free Shopify development store, never on a store with real customers.

### Setup commands (Shopify CLI 5.0.0 and Shopify Dev MCP 1.18.0, checked 2026-11-03; restart Claude Code after the second line)
```
npm install -g @shopify/cli@latest
claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest
claude mcp list
```

### Optional: turn off the toolkit's usage data (macOS or Linux; on Windows, make an empty file named opt-out in a shopify-ai-toolkit folder inside %APPDATA%)
```
mkdir -p ~/.config/shopify-ai-toolkit && touch ~/.config/shopify-ai-toolkit/opt-out
```

### Sign in to your development store with view-only access (no key file: this opens a browser sign-in)
```
shopify store auth --store your-dev-store.myshopify.com --scopes read_products
```

### check-store.graphql (Admin API 2026-10)
```
query CheckStore {
  shop {
    name
    myshopifyDomain
    currencyCode
    plan {
      publicDisplayName
      partnerDevelopment
    }
  }
}
```

### Run
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file check-store.graphql --output-file check-store.json
```
