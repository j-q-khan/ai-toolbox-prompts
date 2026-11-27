Paste this into Claude Code, Anthropic's coding tool, in a new, empty test folder. It builds a small script that turns a plain list of budget items into a sample sheet as a CSV file you can import into Claude Sheets, with the money left and totals worked out and checked, tested on made-up numbers only, and it changes nothing until you agree. Written from Anthropic's help page "Get started with Claude Sheets", checked 2026-11-26. Nothing here was run for the video.

Goal: build a small Python script, budget_csv.py, that turns a plain text list of budget items into a sample budget sheet saved as a CSV file, with a Left column (planned minus actual) and a Total line, ready to import into Claude Sheets.
Context: Claude Sheets (beta, on Pro, Max, Ultra, Team and Enterprise plans) can import a CSV file, and Anthropic's help page says to give Claude the numbers you already have so the sheet is built from your own data. Sheets can't pull live data from connected apps, so a CSV file you import is how numbers get in. Use made-up numbers only.
Steps, in order:
1. Tell me your plan in a few lines and wait for my OK. Don't create, change or delete any file before I say yes.
2. Create sample-items.txt with made-up items for "Test Bakery", one per line as name, planned, actual: "Flour, 400, 380", "Butter, 300, 340", "Boxes, 150, 120". Use no real names, companies or emails, and no currency signs.
3. Write budget_csv.py with the Python standard library only. It takes the items file's path and an output path as arguments, and reads each non-empty line as a name and two whole numbers.
4. If a line doesn't have exactly three parts, or a number isn't a whole number of zero or more, stop and say which line is wrong instead of writing anything.
5. Write a CSV file with the header Item, Planned, Actual, Left, one line per item where Left is Planned minus Actual (it can be below zero), and a last line Total with the sums of the three number columns. Write plain numbers, not formulas, so it imports the same everywhere.
6. Check the result before writing: the Total of Left must equal the Total of Planned minus the Total of Actual. If it doesn't, stop and say so.
7. If the file has no items, print a clear message and write nothing. Never overwrite an existing output file: stop and tell me.
8. Run it on sample-items.txt only, writing test-bakery-budget.csv, and show me the file. For the made-up items it must show Left values of 20, -40 and 30, and a Total line of 850, 840 and 10.
9. Add a short README.md: how to run it on Windows and Mac, that it never sends anything anywhere, how to bring the CSV into Claude Sheets (Anthropic's help page lists the option "Import a CSV file" but doesn't say where it sits), that Claude Sheets needs a Pro plan or above, and a reminder to remove private details from real numbers and to follow your organization's rules before using it.
Safety: work only inside this folder. No network access, no installs, no other packages. Don't open or upload real company files. Ask before every file you create.
Output: the four files, test-bakery-budget.csv made from the made-up items, and a two-line note of what you did.
