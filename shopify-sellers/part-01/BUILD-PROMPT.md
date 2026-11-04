# Claude build prompt: How to Use AI for Shopify

From "AI for Shopify Sellers", Part 1. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: build a repeatable low-stock snapshot for my Shopify development store, with a one-page dashboard of the result.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with demo data only. Admin GraphQL API version 2026-10. No real store and no customer data.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin (shopify-ai-toolkit@claude-plugins-official) are installed. Show me each install command and wait for my yes before running it.
2. Sign in with shopify store auth using only the read_products scope.
3. Write low-stock.graphql with productsCount, then products(first: 10, sortKey: INVENTORY_TOTAL) returning title, status and totalInventory. Validate it with the toolkit against 2026-10 before running it.
4. Run it with shopify store execute and save low-stock.json. Never add --allow-mutations.
5. From low-stock.json, write low-stock.csv (title, status, total inventory) and dashboard.html: one page, no outside scripts, a bar chart of the ten products by stock, active products with zero stock highlighted, and the run date.
6. Write README.md with the exact commands to repeat the run next week.
Safety: work only inside this folder, use the read-only scope, use the development store only, never use real client or customer data, and ask before any write to the store or any file outside this folder. Stop and ask me before running anything that changes data.
Output: low-stock.graphql, low-stock.json, low-stock.csv, dashboard.html, README.md, and a three-line summary of what the snapshot shows.
