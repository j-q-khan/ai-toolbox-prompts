# Claude build prompt: Shopify Tariffs Explained

From "AI for Shopify Sellers", Part 9. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with a free Shopify development store only. Start in plan mode. This is not customs or legal advice: Claude never suggests an HS code or a duty rate.

Goal: build a repeatable HS code gap finder that lists every variant missing an HS code or country of origin, with a plain description and search words for a person to look up on the official tariff schedule.
Inputs: a Shopify development store, [your-dev-store].myshopify.com, with demo products. Admin GraphQL API version 2026-10. Optionally, the CSV from Settings, Taxes and duties, Manage, Update with CSV, Export (columns Product title, Variant SKU, Country of origin, HS code). My notes on each product's materials, function and main use: [paste or attach].
Steps, in order:
1. Check that Shopify CLI and the Shopify AI Toolkit plugin are installed. Show me each install command and wait for my yes.
2. Sign in with shopify store auth using only the read_products scope.
3. Write variants.graphql: productVariants(first: 100) with sku, displayName, product (title, productType, category fullName) and inventoryItem (harmonizedSystemCode, countryCodeOfOrigin). Validate it with the toolkit, run it with shopify store execute and save variants.json. Never add --allow-mutations.
4. Using code, list variants with no harmonizedSystemCode, a code that is not 6 to 13 digits, or no countryCodeOfOrigin. Group them by productType, then product title.
5. For each product, write a plain description a customs officer would need (material, how it works, main use) from my notes only, plus three search words for hts.usitc.gov and CBP's CROSS rulings search. Mark anything you had to guess.
6. Write hs-worksheet.csv (product title, variant SKU, problem, plain description, search words, code found by a person, source checked, date) with the last three columns left blank for me, and README.md with the run steps and the date.
Safety: work only inside this folder, development store only, never real client or customer data, read-only scope, never write a code or country back to the store, and never suggest a code, a rate or a legal conclusion. Ask before any write. Stop and ask me before running anything that changes data.
Output: variants.graphql, variants.json, hs-worksheet.csv, README.md, and a count of gaps.
