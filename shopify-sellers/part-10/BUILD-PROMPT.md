# Claude build prompt: Shopify Inventory Sync with Amazon and Etsy

From "AI for Shopify Sellers", Part 10. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store and small made-up Etsy and Amazon files. Start in plan mode.

Goal: build a repeatable SKU sync check across Shopify, Etsy and Amazon, saved as a Claude Code skill and as a ZIP I can upload to the Claude app for a teammate.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with demo data. Admin GraphQL API version 2026-10. etsy-listings.csv (columns SKU, Quantity, Title, from Etsy's Download Data) and amazon-all-listings.txt (tab-separated, columns seller-sku, quantity, from the All Listings Report). If those files don't exist, make small made-up ones that reuse the dev store's SKUs, with one blank SKU, one duplicate and one that differs only in capitals, and show them to me.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_products and read_inventory scopes.
3. Write variants.graphql: productVariants(first: 250) with sku, displayName, inventoryQuantity and inventoryPolicy, plus pageInfo. Validate it with the toolkit, run it with shopify store execute and save shopify-variants.json. If hasNextPage is true, tell me before paging. Never add --allow-mutations.
4. Write .claude/skills/sync-check/SKILL.md: trim spaces, match SKUs exactly, never merge codes that differ only in capitals, and write sync-report.csv with sku, shopify_qty, etsy_qty, amazon_qty, problem (missing on a channel, blank SKU, duplicate SKU, capitals differ, marketplace higher than Shopify, inventoryPolicy CONTINUE).
5. Run /sync-check and show me sync-report.csv.
6. Make a claude.ai copy of the skill in a folder named sync-check with name and description in its frontmatter and no Claude Code-only settings, and zip it as sync-check.zip for Customize, Skills, Upload a skill. Tell me what to check before uploading.
Safety: work only inside this folder, development store and made-up files only, never real client or customer data, never order exports, read-only scopes, and change no file except the ones listed. Never update stock or SKUs anywhere. Stop and ask me before running anything that changes data.
Output: variants.graphql, shopify-variants.json, the skill, sync-report.csv, sync-check.zip, and a short summary of problems found.
