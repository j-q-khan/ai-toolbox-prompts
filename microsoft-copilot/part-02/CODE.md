# Full code: Copilot in Excel Tutorial: Formulas, Charts and Data Analysis (2026)

A test file and a prompt sheet written for this video from Microsoft's Copilot in Excel help pages (checked 2026-11-17). Nothing here was run through Copilot for this video; use them on a test copy only.

### 1. gift-shop-sales.csv
```
Order ID,Date,Product,Quantity,Unit Price
1001,2026-10-01,Mug,3,12.50
1002,2026-10-02,Notebook,5,8.00
1003,2026-10-03,Candle,2,15.00
1004,2026-10-04,Tote bag,1,18.00
1005,2026-10-06,Mug,4,12.50
1006,2026-10-07,Candle,7,15.00
1007,2026-10-08,Notebook,2,8.00
1008,2026-10-09,Tote bag,3,18.00
1009,2026-10-10,Mug,1,12.50
1010,2026-10-13,Candle,3,15.00
1011,2026-10-14,Notebook,7,8.00
1012,2026-10-15,Tote bag,2,18.00
1013,2026-10-16,Mug,6,12.50
1014,2026-10-17,Candle,1,15.00
1015,2026-10-20,Notebook,3,8.00
1016,2026-10-21,Tote bag,4,18.00
```

### 2. excel-copilot-prompt-sheet.md
```
# Copilot in Excel: prompt sheet (checked 2026-11-17)
# Use a test copy and made-up data only. Follow your employer's rules.

## 0. Set up (once)
- [ ] Download gift-shop-sales.csv: in the GitHub folder, select the file, then the Download raw file button
- [ ] Open gift-shop-sales.csv in Excel, then File → Save As → Excel Workbook (.xlsx)
- [ ] Click any cell in the data, then Home → Format as Table, pick a style, tick "My table has headers", select OK
- [ ] Copilot opens in edit mode and changes the workbook directly: work on this test copy

## 1. Formula column (Copilot button, lower right corner; edit mode)
Add a column that calculates the total for each order, quantity times unit price.

## 2. Explain it (click the first Total cell first)
Explain the formula in the selected cell.

## 3. Chart
Create a column chart of the Total column, added up by product.

## 4. Refine the chart (same box)
Make it a bar chart sorted from highest to lowest.

## 5. Question (switch the pane to chat mode, so nothing changes)
Using the Total column, which product had the highest total sales, and which had the lowest?

## 6. Check one result by hand
- [ ] Filter the Product column to Candle: 2 + 7 + 3 + 1 = 13 sold, at $15 each = $195
- [ ] Compare with Copilot's chart and answer (expected from this file: Candle highest, Notebook lowest at $136)
- [ ] No match? Don't use it. Ask again with the column names spelled out

## Copilot not showing in Excel?
- [ ] Look in the lower right corner of the workbook: the button moved there (older videos show it on the Home tab); right click it, Move to ribbon, if you prefer
- [ ] Windows: File → Account → Update License, then restart Excel
- [ ] Mac: Excel menu → About Excel → More Info → Refresh License, then restart Excel
- [ ] Home plan: only the person who owns the Microsoft 365 Personal, Family or Premium plan gets Copilot, not the people it's shared with
- [ ] Work account: check the label under your name in the Copilot app; Semi-Annual Enterprise Channel doesn't get Copilot features, so ask the people who run your work accounts
- [ ] You don't need OneDrive or AutoSave on: Copilot in Excel runs with AutoSave on or off
- [ ] Copilot won't edit? Formulas → Calculation Options must be set to Automatic

Sources: support.microsoft.com "Get started with Copilot in Excel"; "Copilot in Excel tips"; "Get data insights with Copilot in Excel"; "Visualize your data with Copilot in Excel"; "Frequently asked questions about Copilot in Excel"; "How to find and enable missing Copilot button"; "Create and format tables"
```
