Paste this into Claude Code, Anthropic's coding assistant that works with the files in a folder on your computer, opened in a new folder holding only test-plan-prices.csv from this video's files (or your own file in the same layout). It builds a small Python script (you'll need Python 3 on your computer, and Claude Code can help you check) that totals what each business plan would cost for a team size you enter, from prices you typed in. It reads only the file you name, writes one new file beside it, and changes nothing else. Written for this video, checked 2026-11-21. Nothing here was run for the video.

Goal: write one Python script, seat_costs.py, that reads a file of per-seat plan prices and a team size, and writes a short table of what each plan would cost a month and a year for that team.
Input: one CSV file and a team size, both named on the command line, for example python seat_costs.py test-plan-prices.csv 4. Skip blank lines and lines starting with #. The file has the columns tool, plan, price_per_seat, billing, min_seats, max_seats, offer_ends, note. billing is yearly or monthly, min_seats and max_seats are whole numbers or empty, and offer_ends is a date written as YYYY-MM-DD or empty. NAME below means the price file's name without .csv.
Steps, in order:
1. Tell me in two sentences what the script will do and which file it will create, then wait for me to say go.
2. Use only Python's standard library, with its csv module for reading. No installs, no internet, no other files read.
3. For each line, work out the seats to pay for: the team size, or min_seats when the team is smaller, and say so in the line's Notes. If the team is bigger than max_seats, write "Over this plan's limit" in Notes instead of a cost.
4. Monthly cost is seats times price_per_seat. Yearly cost is the monthly cost times 12. Round both to cents.
5. If offer_ends is before today's date, write "Offer ended: check the price" in Notes. If it's within 60 days from today, write "Offer ends on" and the date.
6. Write NAME-costs-for-N.md, where N is the team size: a Markdown table with the columns Tool, Plan, Billing, Seats, Per seat, Monthly, Yearly, Notes, in the file's order, with the note column added to Notes. Start it with a line saying "Made from NAME.csv on" and today's date, for a team of N, and end it with "Prices change: check each company's own page before you buy."
7. Print the three lowest monthly costs on the screen.
8. The first line that isn't blank or a # line is the header: read the columns from it. If the team size isn't a whole number above 0, or any line has a price that isn't a number, a seat count that isn't a whole number, a billing word other than yearly or monthly, or a date that isn't YYYY-MM-DD, stop and tell me the line number, and write nothing.
9. Never overwrite a file that already exists: if the output file is there, stop and tell me.
10. Then run it once on the file I named with a team of 4, and show me the table.
Safety: read only the file I name. Don't change, move or delete it or anything else. Don't upload anything or call any website or API.
Output: seat_costs.py, the new table, and a three-line note saying what you created.
