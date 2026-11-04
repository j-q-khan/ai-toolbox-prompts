# Claude build prompt: Meta Pixel Not Working on Shopify?

From "AI for Shopify Sellers", Part 6. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: find every leftover Meta pixel snippet in a copy of my theme, and line up Shopify orders with Meta purchases by day, so I can see which fix to try first.
Inputs: a Shopify development store, [your-dev-store].myshopify.com. A copy of its published theme, pulled with Shopify CLI. meta_purchases.csv, my daily Purchase counts exported from Meta for the same 30 days (find the date and purchases columns yourself and tell me which you used). Admin GraphQL API version 2026-10.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. In a subfolder named theme-copy, run shopify theme pull --store [your-dev-store] --live. This only downloads files. Never run shopify theme push, publish or delete.
3. Search every file in theme-copy for fbq, connect.facebook.net and any 15 or 16 digit pixel ID. Write pixel-snippets.md with file, line number and the matching line, and say which ones look like a second pixel next to the Facebook and Instagram app. Change no theme file.
4. Sign in with shopify store auth using only the read_reports scope. Write orders.graphql with the ShopifyQL query FROM sales SHOW total_sales, orders TIMESERIES day SINCE -30d UNTIL today ORDER BY day ASC, validate it with the toolkit, run it with shopify store execute and save orders.json. Never add --allow-mutations.
5. Using code, join orders.json and meta_purchases.csv by date, and write gaps.csv with date, Shopify orders, Meta purchases, gap, and over or under. Compare counts, not revenue.
6. Write summary.md: the most common pattern, and the first thing to check (Meta high: a duplicate pixel or view-through purchases; Meta low: blocked events or missing consent). Never suggest a way around the cookie banner.
Safety: work only inside this folder, development store only, totals only with no customer names or emails, read-only scopes, and ask before any write. Stop and ask me before running anything that changes data.
Output: pixel-snippets.md, orders.graphql, orders.json, gaps.csv, summary.md.
