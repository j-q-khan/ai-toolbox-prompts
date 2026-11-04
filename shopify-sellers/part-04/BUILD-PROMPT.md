# Claude build prompt: Shopify AI Product Descriptions at Scale

From "AI for Shopify Sellers", Part 4. Checked 2026-11-03. Copy everything below into Claude Code.

Use this in Claude Code (Pro or higher), in an empty test folder, with an export from a free Shopify development store and a throwaway Anthropic API key with a low spending limit. Start in plan mode.

Goal: draft a description for every product in my Shopify export through Anthropic's Message Batches API at half price, with structured outputs, and write a file I can check and re-import.
Inputs: products_export.csv, exported from Products, Export, All products, Plain CSV file. Columns used: URL handle, Title, Type, Vendor, Tags, Description. Variant lines have an empty Title and are skipped. Model: claude-haiku-5-5. Python with the anthropic package.
Steps, in order:
1. Read the Claude docs pages for Message Batches and structured outputs (output_config.format with a json_schema) and tell me the exact request shape you will use.
2. Write describe_batch.py. For each product line, build one batch request whose custom_id maps to the URL handle (keep a lookup file if a handle is too long or has other characters the custom_id rules don't allow).
3. Use a JSON schema with two fields: description (80 to 120 words, only the facts in that line, in a [your brand voice] tone) and guesses (a list of anything not stated in the facts).
4. Test first: send the first 5 products as normal requests and show me the results. Wait for my yes before submitting the full batch.
5. Submit the batch, poll until it ends, and match each result to its handle by custom_id.
6. Write descriptions_to_check.csv with exactly three columns, URL handle, Title, Description, and review.csv with URL handle, guesses and any errored or expired request.
7. Write README.md with the run steps and what it cost.
Safety: work only inside this folder, use only the dev store export, never real client or customer data, never connect to any store, and keep the API key in an environment variable, never in a file. Nothing is imported: I check every line and import myself with Overwrite products with matching handles, on a dev store first. Stop and ask me before running anything that changes data.
Output: describe_batch.py, descriptions_to_check.csv, review.csv, README.md, and a short summary with the counts.
