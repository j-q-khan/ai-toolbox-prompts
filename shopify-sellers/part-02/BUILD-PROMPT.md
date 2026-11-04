# Claude build prompt: How to Connect Claude to Shopify with MCP

From "AI for Shopify Sellers", Part 2. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: connect this Claude Code session to Shopify's official developer tools and prove it is pointed at my development store, not a real one.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with demo data only. Shopify CLI, the Shopify Dev MCP server (@shopify/dev-mcp) and Admin GraphQL API version 2026-10.
Steps, in order:
1. Show me the commands to install Shopify CLI and add the Dev MCP server (claude mcp add --transport stdio shopify-dev-mcp -- npx -y @shopify/dev-mcp@latest), and wait for my yes before running each one.
2. Ask me whether to turn off the Shopify AI Toolkit's usage data, and if I say yes, create the opt-out file the toolkit's README describes for my operating system.
3. Using the Dev MCP server, look up the Shop and ShopPlan objects for 2026-10 and write check-store.graphql returning shop name, myshopifyDomain, currencyCode, plan publicDisplayName and plan partnerDevelopment. Validate it before showing it to me.
4. Sign in with shopify store auth using only the read_products scope, then run the query with shopify store execute and save check-store.json. Never add --allow-mutations.
5. Read check-store.json. If partnerDevelopment is not true, stop and tell me, because you may be pointed at a real store.
6. Write CLAUDE.md for this folder with these rules: read-only queries only, validate every query with the Dev MCP server first, and before any change show what will change, how many items and how to undo it, then wait for my yes.
Safety: work only inside this folder, use the development store only, never real client or customer data, read-only scope first, and ask before any write. Stop and ask me before running anything that changes data.
Output: check-store.graphql, check-store.json, CLAUDE.md, and a short note with the store name, plan and whether it is a development store.
