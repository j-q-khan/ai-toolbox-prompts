# Claude build prompt: Shopify Fraud Prevention: Stop Fake Orders and Bots

From "AI for Shopify Sellers", Part 3. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode. This is a defensive review of my own orders: it never cancels, refunds or contacts anyone.

Goal: build a repeatable risk report of my store's recent high and medium risk orders, with a dashboard and suggested Shopify Flow rules for me to review.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with test orders only. Admin GraphQL API version 2026-10. Optionally, an Orders CSV export from the same store with only these columns kept: Name, Created at, Total, Discount Code, Shipping Country, Risk Level.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_orders scope.
3. Write risky-orders.graphql: the 50 newest orders matching risk_level:high OR risk_level:medium, with name, createdAt, test, displayFinancialStatus, billingAddressMatchesShippingAddress, the total in shop money, and risk recommendation, riskLevel and fact descriptions. No emails, names, phone numbers or IP addresses. Validate it with the toolkit against 2026-10.
4. Run it with shopify store execute and save risky-orders.json. Never add --allow-mutations.
5. If the CSV is present, first check that it has no Email, Phone, Billing Name, Shipping Name, street or Device ID column; if it does, stop and tell me.
6. Using code, count orders per hour, per discount code and per shipping country, and the five most common risk facts. Write risk-summary.csv and dashboard.html (one page, no outside scripts) with those counts and the high-risk orders highlighted.
7. Write flow-ideas.md: Shopify Flow conditions to review that use the Order risk analyzed trigger and only add tags or send internal emails.
Safety: work only inside this folder, development store and test data only, never real client or customer data, read-only scope, and never cancel, refund, capture or tag anything. Ask before any write. Stop and ask me before running anything that changes data.
Output: risky-orders.graphql, risky-orders.json, risk-summary.csv, dashboard.html, flow-ideas.md, and a five-line summary.
