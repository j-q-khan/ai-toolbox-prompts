# Claude build prompt: Meshy AI Free vs Paid: Pricing, Credits and Who Owns Your 3D Models

An offline "should I pay for Meshy this month?" helper for Claude Code: it totals the credits for what you plan to make, picks the cheapest plan that covers it, and prints the licence and the credit line for a shop listing. Checked against Meshy's docs, pricing page and Terms of Use on 2026-11-07. Not run by us. It never calls Meshy or uses a key. Not legal advice.

Use this in Claude Code (Pro or higher), in an empty test folder. Start in plan mode.

Goal: build a small, offline "should I pay for Meshy this month?" helper that reads what I plan to make, totals the credits, picks the cheapest plan that covers it, and prints the licence that applies plus the credit line to paste into a shop listing.
Inputs: a file called plan.csv next to the script, with the columns name, model, texture, selling. model is one of lite, standard or ultra2k; texture and selling are yes or no. If the file is missing, create it with four example rows: a dog figurine on lite, the same dog on standard, a planter on ultra2k with texture, and a dog figurine for sale on standard.
Numbers to use, from Meshy's docs and pricing page (checked 2026-11-07; re-check https://www.meshy.ai/pricing and https://docs.meshy.ai/en/webapp/pricing before you trust them):
- credits per try: lite 10, standard 20, ultra2k 25, texture adds 10
- plans: Free 100 credits a month at $0, Pro 1,000 at $20, Premium 3,000 at $40, Ultra 8,000 at $100 (Studio 5,500 shared at $70, plus $10 a month for each extra seat, is for teams; list it but don't pick it)
- Free only downloads untextured lite models, 10 a month; a standard or ultra2k model needs a paid plan to download
- licence: Free is CC BY 4.0, Meshy owns the model and you must credit Meshy; paid plans own their output (Meshy Terms of Use, section 3.2, last updated 2026-09-19)
Steps, in order:
1. Tell me which files you'll create and wait for my yes. Use Python 3 and the standard library only. Install nothing, make no network calls, and never call Meshy's API or use any key.
2. Write plan_month.py. Validate every row and print a clear error for a bad value instead of crashing.
3. Print a table: each row's credits, the total, and for each plan whether it fits, how many credits are left, and why Free is ruled out if it is (too many credits, a textured model, a non-lite model, or more than 10 downloads).
4. Print the cheapest plan that covers the month. If any row has selling = yes, also print the licence that plan gives, and on Free print this credit line to paste: Model created with Meshy – CC BY 4.0 License, followed by https://creativecommons.org/licenses/by/4.0/
5. End with the line: Not legal advice. Prices and credits as checked on 2026-11-07; check meshy.ai/pricing.
6. Run it on the example file and show me the output. Then explain how to edit plan.csv for my own month.
Safety: this folder only. Don't change any file except plan.csv and plan_month.py. Stop and ask me before doing anything not listed here.
Output: plan_month.py, plan.csv, and a three-line summary.
