# monthly_totals.py: example of the kind of script Claude Code writes for Prompt 3 (Example output, not run by us).
# Test-only: put it in a throwaway folder that holds only the six practice order files, read every line, then run:
#   python monthly_totals.py
# It reads orders-*.csv in this folder, counts each order number once, totals each month,
# writes monthly-totals.csv next to them and prints what it did. It deletes nothing and installs nothing.
import csv
import glob
from collections import defaultdict

first = {}                  # order number -> the first line seen with it
repeats = []                # order numbers seen again
totals = defaultdict(int)   # "2027-03" -> total in dollars

for path in sorted(glob.glob("orders-*.csv")):
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            order = row["order_id"]
            if order in first:
                same = "identical" if row == first[order] else "DIFFERENT, check by hand"
                repeats.append(f"{order} ({same})")
                continue
            first[order] = row
            totals[row["order_date"][:7]] += int(row["order_total"])

with open("monthly-totals.csv", "w", newline="", encoding="utf-8") as f:
    out = csv.writer(f)
    out.writerow(["month", "total"])
    for month in sorted(totals):
        out.writerow([month, totals[month]])

print(f"{len(first)} orders, {len(repeats)} repeated lines skipped")
for r in repeats:
    print("  repeat:", r)
for month in sorted(totals):
    print(month, totals[month])
