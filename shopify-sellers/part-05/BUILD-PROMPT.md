# Claude build prompt: Shopify Traffic but No Sales?

From "AI for Shopify Sellers", Part 5. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: build a repeatable funnel checker that shows which landing pages lose human visitors, at which step, as a CSV and a one-page dashboard.
Inputs: a Shopify development store, [your-dev-store].myshopify.com. Admin GraphQL API version 2026-10 and ShopifyQL. If the API route is blocked, use instead a CSV I export from Analytics, Sessions by landing page, filtered to Human sessions, with columns landing page path, sessions, sessions with cart additions, sessions that reached checkout, sessions that completed checkout.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_reports scope.
3. Write funnel.graphql with a shopifyqlQuery: FROM sessions, SHOW sessions, sessions_with_cart_additions, sessions_that_reached_checkout, sessions_that_completed_checkout, conversion_rate, WHERE human_or_bot_session = 'human', GROUP BY landing_page_path, SINCE -30d UNTIL today, ORDER BY sessions DESC, LIMIT 50. Validate it with the toolkit, run it with shopify store execute, and save funnel.json. Never add --allow-mutations. If it fails on access, stop and ask me for the CSV.
4. Using code, work out each page's cart rate, checkout rate and completion rate, and the step where it loses the most visitors.
5. Write funnel-report.csv and dashboard.html (one page, no outside scripts): pages ranked by sessions lost, a bar per funnel step, and the worst step labelled.
6. For the top five pages, write fix-list.md with one plain check per page (price with shipping, delivery time, returns, sizing, page speed). Mark each as a check, not a proven cause.
Safety: work only inside this folder, development store only, never customer names or emails, read-only scope, and ask before any write. Stop and ask me before running anything that changes data.
Output: funnel.graphql, funnel.json or the CSV used, funnel-report.csv, dashboard.html, fix-list.md, and a short summary.
