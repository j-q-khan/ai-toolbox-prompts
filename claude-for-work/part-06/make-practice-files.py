# make-practice-files.py: rebuilds the six Part 6 practice files byte for byte (an invented tea shop, no personal data).
# Usage: python make-practice-files.py 8 .   (seed 8, output folder). Standard library only; it writes six CSV files and nothing else.
import random, csv, calendar, sys, os
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 8
OUT = sys.argv[2] if len(sys.argv) > 2 else None
rng = random.Random(SEED)
PRODUCTS = [("Breakfast blend 100g", 8), ("Earl grey 100g", 9), ("Green sencha 100g", 11),
            ("Chai spice 100g", 10), ("Peppermint 50g", 6), ("Glass teapot", 34),
            ("Tea infuser", 7), ("Gift box", 28)]
WEIGHTS = [22, 18, 10, 14, 12, 5, 10, 9]
COUNTS = {1: 64, 2: 70, 3: 66, 4: 68, 5: 71, 6: 69}
oid = 1001
files = {}
for m in range(1, 7):
    days = calendar.monthrange(2027, m)[1]
    rows = []
    dates = sorted(rng.randint(1, days) for _ in range(COUNTS[m]))
    for d in dates:
        name, price = rng.choices(PRODUCTS, WEIGHTS)[0]
        q = rng.choices([1, 2, 3, 4], [50, 30, 14, 6])[0]
        rows.append([f"W-{oid}", f"2027-{m:02d}-{d:02d}", name, q, price, q * price])
        oid += 1
    files[m] = rows
# planted problem: the March export repeated eight orders at the end of the file
march = files[3]
picks = sorted(rng.sample(range(len(march)), 8))
files[3] = march + [list(march[i]) for i in picks]
hdr = ["order_id", "order_date", "product", "quantity", "unit_price", "order_total"]
tot = {m: sum(r[5] for r in rows) for m, rows in files.items()}
dup = sum(march[i][5] for i in picks)
print("seed", SEED, "raw", tot, "dup", dup, "true march", tot[3] - dup, "dupes", [march[i][0] for i in picks])
if OUT:
    os.makedirs(OUT, exist_ok=True)
    for m, rows in files.items():
        with open(os.path.join(OUT, f"orders-2027-{m:02d}.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n"); w.writerow(hdr); w.writerows(rows)
