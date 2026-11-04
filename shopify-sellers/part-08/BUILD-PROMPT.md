# Claude build prompt: Shopify Order Tracking with an AI Chatbot

From "AI for Shopify Sellers", Part 8. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode.

Goal: build a repeatable late-shipment finder that lists unshipped and delayed orders and drafts one honest message per order, for me to check and send myself.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with test orders only. Admin GraphQL API version 2026-10. My promised shipping time: [days]. My real processing times, carriers and delay steps: [paste].
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_orders scope.
3. Write orders.graphql: orders(first: 50, reverse: true) with name, createdAt, displayFulfillmentStatus, statusPageUrl, and fulfillments(first: 5) with displayStatus, inTransitAt, estimatedDeliveryAt and trackingInfo(first: 1) company, number and url. No customer names, emails or phone numbers. Validate it with the toolkit, run it with shopify store execute and save orders.json. Never add --allow-mutations.
4. Using code, flag orders UNFULFILLED or PARTIALLY_FULFILLED for more than [days] days, fulfillments with displayStatus DELAYED, ATTEMPTED_DELIVERY, FAILURE or NOT_DELIVERED, and fulfillments whose estimatedDeliveryAt has passed without DELIVERED.
5. Write late-orders.csv with order name, days since createdAt, status, carrier and tracking number.
6. Draft one short message per flagged order in drafts.md, using only my facts and the statusPageUrl. For unshipped orders, give the customer the choice to agree to the delay or cancel for a prompt full refund. Never guess a delivery date.
7. Write shipping-faq.md from my processing times, carriers and delay steps only, for me to publish as a page the Inbox agent can draw on.
Safety: work only inside this folder, development store and test orders only, never real client or customer data, read-only scope, and never send a message, change an order or cancel anything. Ask before any write. Stop and ask me before running anything that changes data.
Output: orders.graphql, orders.json, late-orders.csv, drafts.md, shipping-faq.md, and a count of flagged orders.
