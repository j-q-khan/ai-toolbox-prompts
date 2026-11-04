# Full code: Shopify Inventory Sync with Amazon and Etsy

The code is built from Shopify's official docs and Anthropic's Claude Code docs, and needs a free Shopify development store to try.

### Setup commands
```
npm install -g @shopify/cli@latest
curl -fsSL https://claude.ai/install.sh | bash
shopify store create dev --name "Sync test" --demo-data
shopify store auth --store your-dev-store.myshopify.com --scopes read_products,read_inventory
```

### variants.graphql
```
query {
  productVariants(first: 250) {
    nodes {
      sku
      displayName
      inventoryQuantity
      inventoryPolicy
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

### Pull the Shopify data
```
shopify store execute --store your-dev-store.myshopify.com --version 2026-10 --query-file variants.graphql --output-file shopify-variants.json
```

### .claude/skills/sync-check/SKILL.md
```
---
description: Compares Shopify, Etsy and Amazon stock by SKU and flags overselling risks.
disable-model-invocation: true
allowed-tools: Read Write
---
Read shopify-variants.json, etsy-listings.csv and amazon-all-listings.txt (tab-separated).
Use sku and inventoryQuantity from Shopify, SKU and Quantity from Etsy, seller-sku and quantity from Amazon.
Trim spaces from every SKU. Match SKUs exactly. Never merge codes that differ only in capitals.
Write sync-report.csv with columns: sku, shopify_qty, etsy_qty, amazon_qty, problem.
Problem is one of: missing on a channel, blank SKU, duplicate SKU, capitals differ, marketplace higher than Shopify, Shopify sells when out of stock (inventoryPolicy CONTINUE).
Change no file except sync-report.csv.
```

### Run
```
claude
/sync-check
```
