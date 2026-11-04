# Full code: Shopify Tariffs Explained

The code is built from Shopify's official docs and Anthropic's Claude Code docs, and needs a free Shopify development store to try.

### Setup commands
```
npm install -g @shopify/cli@5.0.0
claude plugin install shopify-ai-toolkit@claude-plugins-official
mkdir hs-gaps
cd hs-gaps
shopify store auth --store your-dev-store.myshopify.com --scopes read_products
```

### variants.graphql
```
query {
  productVariants(first: 100) {
    nodes {
      sku
      displayName
      product { title productType category { fullName } }
      inventoryItem { harmonizedSystemCode countryCodeOfOrigin }
    }
  }
}
```

### CLAUDE.md
```
# HS code gap finder
- Use only variants.json. Never change the store.
- List variants with no harmonizedSystemCode or no countryCodeOfOrigin.
- Group them by productType, then product title.
- For each, write a plain description: material, function, main use.
- Add three search words for the official tariff schedule.
- Never suggest an HS code or a duty rate. A person checks every code.
- Write the result to hs-worksheet.md.
```

### Run
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --json --query-file variants.graphql --output-file variants.json
claude "Make the HS worksheet from variants.json"
```
