# Full code: Claude for Excel: Install the Add-in and Your First Real Task



### 1. plant-shop-sales.csv
```
Date,Product,Quantity,Unit price,Total
2026-10-01,Snake plant,2,18,36
2026-10-02,Pothos,3,12,36
2026-10-03,Clay pot,5,6,30
2026-10-06,Fern,1,15,15
2026-10-07,Snake plant,1,18,18
2026-10-08,Pothos,4,12,58
2026-10-09,Fern,2,15,30
2026-10-10,Clay pot,3,6,18
2026-10-13,Snake plant,3,18,54
2026-10-14,Pothos,3,12,36
2026-10-15,Fern,4,15,60
2026-10-16,Clay pot,2,6,12
```

### 2. how-to-check.txt
```
Practice sheet: plant-shop-sales.csv (an invented shop; every number is made up)

Open it
- Download it from the link in the description: on the file's page, click "Download raw file".
- Optional: open it in Notepad (Windows) or TextEdit (Mac) first. It is plain text: 13 lines, no formulas, nothing hidden.
- Open it in Excel. If everything lands in column A, use Data, then From Text/CSV, and pick "Comma" as the delimiter.
- Save it as a workbook at once: File, then Save As, then "Save as type" (Windows) or "File Format" (Mac) = Excel Workbook (.xlsx).

What you should find
- 12 orders, 1 to 16 October 2026, in A2:E13.
- One typed total is wrong on purpose: E7 says 58, but 4 x 12 = 48.

Check Claude's work by hand
- One line: E2 should show 2 x 18 = 36, and its formula should multiply the quantity (column C) by the unit price (column D), for example =C2*D2.
- Grand total: select E2:E13. The Sum in the strip at the bottom of the Excel window should say 393 after the fix (403 before it).
- Totals by product, after the fix: Snake plant 108, Pothos 120, Fern 105, Clay pot 60.

Safety
- Only use Claude for Excel with trusted spreadsheets (Anthropic's warning).
- The add-in sends your conversations, and what Claude reads from the workbook, to Anthropic. Keep real client data out unless your employer allows it.
```
