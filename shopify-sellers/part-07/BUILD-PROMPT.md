# Claude build prompt: How to Win Shopify Chargebacks

From "AI for Shopify Sellers", Part 7. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode. Nothing here can promise a win: the bank decides.

Goal: build a repeatable chargeback tracker that lists open disputes soonest first, with the evidence Shopify lists for each reason, as a checklist and a one-page dashboard.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, that uses Shopify Payments (a dev store may return no disputes; if so, make three made-up disputes in a file named sample-disputes.json and say so). Admin GraphQL API version 2026-10. My evidence notes in evidence-rules.md, which I will paste from Shopify's chargeback reasons page.
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_shopify_payments_disputes and read_orders scopes.
3. Write disputes.graphql: disputes(first: 25, reverse: true) with id, type, status, initiatedAt, evidenceDueBy, evidenceSentOn, amount, reasonDetails (reason, networkReasonCode) and order (name, displayFulfillmentStatus). Validate it with the toolkit, run it with shopify store execute and save disputes.json. Never add --allow-mutations.
4. Using code, keep status NEEDS_RESPONSE, work out days left to evidenceDueBy, and sort soonest first.
5. For each dispute, match the reason to evidence-rules.md and list the evidence to gather, in Shopify's order: direct proof, customer acknowledgment, policy, context. Say what is missing. Never invent evidence.
6. Write checklist.md and dashboard.html (one page, no outside scripts): days left per dispute, reason, amount, and evidence still missing.
7. Write CLAUDE.md with these rules, so the next run follows them.
Safety: work only inside this folder, development store or made-up data only, never real client or customer data, read-only scopes, never submit evidence, accept a dispute, refund or contact anyone, and ask before any write. Stop and ask me before running anything that changes data.
Output: disputes.graphql, disputes.json or sample-disputes.json, checklist.md, dashboard.html, CLAUDE.md.
