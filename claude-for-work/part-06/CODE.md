# Full code: Claude for Data Analysis: Chat, Cowork or Claude Code?



### 1. monthly_totals.py
```
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
```

### 2. how-to-check.txt
```
Practice files: orders-2027-01.csv to orders-2027-06.csv (six monthly order files for an invented tea shop, Wrenfield Tea; every order, product and number is made up; there are no customer names, emails or phone numbers in them, on purpose)

Open them
- Download each from the link in the description: on the file's page, click "Download raw file".
- Each line is one order: order_id, order_date, product, quantity, unit_price, order_total (quantity x unit_price, whole dollars).
- 416 lines in all: 408 different orders, plus 8 March orders listed twice (the planted problem).
- Optional: open them in Notepad (Windows) or TextEdit (Mac) first. Plain text, no formulas, nothing hidden.

The planted problem (try to find it before you look)
- The March file has 74 order lines but only 66 different order numbers.
- Its last 8 lines (lines 68 to 75 of the file, counting the header as line 1) repeat 8 earlier March orders word for word:
  W-1137 $16, W-1143 $136, W-1155 $7, W-1157 $16, W-1158 $68, W-1180 $36, W-1183 $28, W-1185 $8.
- They add $315 to March: 16 + 136 + 7 + 16 + 68 + 36 + 28 + 8 = 315.

Monthly totals (whole dollars)
  Month     As the file stands   Without repeats
  January          1,193              1,193
  February         1,568              1,568
  March            1,842              1,527
  April            1,272              1,272
  May              1,484              1,484
  June             1,587              1,587
  Six months       8,946              8,631
- As the files stand, March looks like the best month. Without the repeats, June is first ($1,587), February second ($1,568), March third ($1,527).

1. Chat (Prompt 1, the March file, explore-data skill)
- Expect Claude to report 74 order lines, 66 different order numbers, 8 repeated lines that are identical, March $1,842 as it stands and $1,527 without the repeats.

2. Cowork (Prompt 2, a folder holding only the six files, set to Manual)
- Before you start: the permission setting in the message box is Manual ("Manually approve" on some screens). Auto is the default on Pro, Max, Ultra and Team.
- With Manual on, Claude asks you to Allow or Deny its actions. Expect one new spreadsheet, monthly-summary.xlsx, matching the table above, and the six original files unchanged.

3. Claude Code (Prompt 3, a throwaway folder holding only the six files)
- Start it in Manual mode: claude --permission-mode manual
- Before you say yes to creating the script, check: it opens only orders-*.csv in this folder, it writes one new file (monthly-totals.csv) and deletes nothing, and a repeated order number is skipped and listed, not added twice.
- Expected output (Example output, written from the files, not run by us):
  408 orders, 8 repeated lines skipped
    repeat: W-1137 (identical)
    repeat: W-1143 (identical)
    repeat: W-1155 (identical)
    repeat: W-1157 (identical)
    repeat: W-1158 (identical)
    repeat: W-1180 (identical)
    repeat: W-1183 (identical)
    repeat: W-1185 (identical)
  2027-01 1193
  2027-02 1568
  2027-03 1527
  2027-04 1272
  2027-05 1484
  2027-06 1587

Check one total by hand (any route)
- Open orders-2027-03.csv in Excel, or import it in Google Sheets (File, then Import). Click an empty cell outside column F (for example H2) and type =SUM(F:F). It adds the order_total column: 1842. (Typed inside column F, it would add itself and give an error.)
- The last 8 lines are the copies: 16 + 136 + 7 + 16 + 68 + 36 + 28 + 8 = 315.
- 1,842 - 315 = 1,527, the corrected March. If Claude's number is different, ask it to show its working.
- To find repeats in your own files: sort by order_id and the copies sit side by side, or put =COUNTIF(A:A,A2) in an empty column and fill it down; any 2 is an order number that appears twice.

Check the chart
- Bar charts should start at zero (the data plugin's data-visualization skill: "Bar charts start at zero: Always.").
- With the axis starting at 1,500, June's bar (1,587) looks over three times March's (1,527): 87 above the axis against 27. From zero they are about 4% apart (60 / 1,527).

Safety
- What you paste or connect goes to Anthropic. Keep customer details (names, emails, phone numbers, card numbers) out, and follow your employer's rules.
- Cowork and recent versions of Claude Code start on Auto. For work files, set Manual so they ask before they act.
- Give Cowork and Claude Code a folder that holds only the files for the task, and keep backups.
- Read every script before it runs. Run the example script only in a throwaway folder with these practice files.
```

### 3. orders-2027-03.csv
```
order_id,order_date,product,quantity,unit_price,order_total
W-1135,2027-03-01,Peppermint 50g,2,6,12
W-1136,2027-03-02,Earl grey 100g,2,9,18
W-1137,2027-03-02,Breakfast blend 100g,2,8,16
W-1138,2027-03-02,Chai spice 100g,2,10,20
W-1139,2027-03-03,Chai spice 100g,1,10,10
W-1140,2027-03-04,Chai spice 100g,2,10,20
W-1141,2027-03-05,Earl grey 100g,1,9,9
W-1142,2027-03-05,Green sencha 100g,4,11,44
W-1143,2027-03-05,Glass teapot,4,34,136
W-1144,2027-03-06,Breakfast blend 100g,1,8,8
W-1145,2027-03-08,Tea infuser,1,7,7
W-1146,2027-03-09,Breakfast blend 100g,1,8,8
W-1147,2027-03-09,Breakfast blend 100g,1,8,8
W-1148,2027-03-10,Earl grey 100g,1,9,9
W-1149,2027-03-10,Breakfast blend 100g,1,8,8
W-1150,2027-03-10,Earl grey 100g,1,9,9
W-1151,2027-03-10,Earl grey 100g,3,9,27
W-1152,2027-03-11,Tea infuser,2,7,14
W-1153,2027-03-11,Chai spice 100g,1,10,10
W-1154,2027-03-12,Gift box,2,28,56
W-1155,2027-03-12,Tea infuser,1,7,7
W-1156,2027-03-12,Breakfast blend 100g,2,8,16
W-1157,2027-03-12,Breakfast blend 100g,2,8,16
W-1158,2027-03-12,Glass teapot,2,34,68
W-1159,2027-03-12,Peppermint 50g,3,6,18
W-1160,2027-03-12,Green sencha 100g,1,11,11
W-1161,2027-03-13,Green sencha 100g,2,11,22
W-1162,2027-03-14,Gift box,1,28,28
W-1163,2027-03-15,Glass teapot,1,34,34
W-1164,2027-03-15,Breakfast blend 100g,1,8,8
W-1165,2027-03-15,Tea infuser,1,7,7
W-1166,2027-03-15,Earl grey 100g,1,9,9
W-1167,2027-03-16,Breakfast blend 100g,2,8,16
W-1168,2027-03-16,Peppermint 50g,2,6,12
W-1169,2027-03-16,Breakfast blend 100g,1,8,8
W-1170,2027-03-16,Glass teapot,4,34,136
W-1171,2027-03-17,Gift box,4,28,112
W-1172,2027-03-18,Breakfast blend 100g,3,8,24
W-1173,2027-03-19,Earl grey 100g,3,9,27
W-1174,2027-03-19,Green sencha 100g,3,11,33
W-1175,2027-03-19,Tea infuser,2,7,14
W-1176,2027-03-21,Green sencha 100g,1,11,11
W-1177,2027-03-21,Chai spice 100g,1,10,10
W-1178,2027-03-21,Breakfast blend 100g,1,8,8
W-1179,2027-03-21,Breakfast blend 100g,2,8,16
W-1180,2027-03-21,Earl grey 100g,4,9,36
W-1181,2027-03-22,Chai spice 100g,4,10,40
W-1182,2027-03-22,Green sencha 100g,2,11,22
W-1183,2027-03-22,Gift box,1,28,28
W-1184,2027-03-22,Breakfast blend 100g,2,8,16
W-1185,2027-03-23,Breakfast blend 100g,1,8,8
W-1186,2027-03-24,Chai spice 100g,2,10,20
W-1187,2027-03-24,Peppermint 50g,1,6,6
W-1188,2027-03-24,Breakfast blend 100g,1,8,8
W-1189,2027-03-24,Earl grey 100g,1,9,9
W-1190,2027-03-25,Breakfast blend 100g,2,8,16
W-1191,2027-03-26,Gift box,3,28,84
W-1192,2027-03-26,Green sencha 100g,1,11,11
W-1193,2027-03-26,Earl grey 100g,2,9,18
W-1194,2027-03-27,Tea infuser,3,7,21
W-1195,2027-03-28,Breakfast blend 100g,1,8,8
W-1196,2027-03-29,Peppermint 50g,2,6,12
W-1197,2027-03-29,Earl grey 100g,2,9,18
W-1198,2027-03-30,Tea infuser,1,7,7
W-1199,2027-03-30,Breakfast blend 100g,1,8,8
W-1200,2027-03-31,Green sencha 100g,1,11,11
W-1137,2027-03-02,Breakfast blend 100g,2,8,16
W-1143,2027-03-05,Glass teapot,4,34,136
W-1155,2027-03-12,Tea infuser,1,7,7
W-1157,2027-03-12,Breakfast blend 100g,2,8,16
W-1158,2027-03-12,Glass teapot,2,34,68
W-1180,2027-03-21,Earl grey 100g,4,9,36
W-1183,2027-03-22,Gift box,1,28,28
W-1185,2027-03-23,Breakfast blend 100g,1,8,8
```
