# Full code: Claude for Accounting: Reconciliations and Month-End Close



### 1. bank-statement.csv
```
Date,Description,Money in,Money out,Balance
2026-10-01,Opening balance,,,4200
2026-10-03,Card takings,1840,,6040
2026-10-06,Rent standing order,,1200,4840
2026-10-09,Cheque 1041,,1530,3310
2026-10-14,Card takings,2260,,5570
2026-10-17,Electricity direct debit,,185,5385
2026-10-21,Cheque 1042,,640,4745
2026-10-24,Card takings,1975,,6720
2026-10-28,Wages,,2400,4320
2026-10-31,Monthly account fee,,15,4305
2026-10-31,Interest paid,3,,4308
```

### 2. cash-book.csv
```
Date,Description,Reference,Money in,Money out,Balance
2026-10-01,Opening balance,,,,4200
2026-10-03,Card takings,Takings week 1,1840,,6040
2026-10-06,Rent,Lease,,1200,4840
2026-10-08,Wheel parts supplier,Cheque 1041,,1350,3490
2026-10-14,Card takings,Takings week 2,2260,,5750
2026-10-17,Electricity,Direct debit,,185,5565
2026-10-20,Brake parts supplier,Cheque 1042,,640,4925
2026-10-24,Card takings,Takings week 3,1975,,6900
2026-10-28,Wages,Payroll,,2400,4500
2026-10-30,Tyre supplier,Cheque 1043,,310,4190
2026-10-31,Takings banked,Deposit slip 118,1120,,5310
```

### 3. how-to-check.txt
```
Practice files: bank-statement.csv and cash-book.csv (an invented bike repair shop, October 2026; every number is made up)

Open them
- Download each from the link in the description: on the file's page, click "Download raw file".
- Optional: open them in Notepad (Windows) or TextEdit (Mac) first. Plain text: 12 lines each (a header and 11 lines), no formulas, nothing hidden.
- In Claude: new chat, the "+" button at the lower left of the message box, "Add files or photos", pick both files.

Layout
- bank-statement.csv: Date, Description, Money in, Money out, Balance. Opening 4200, closing 4308. 10 payments in and out.
- cash-book.csv: Date, Description, Reference, Money in, Money out, Balance. Opening 4200, closing 5310. 10 payments in and out.
- Gap before reconciling: 5310 - 4308 = 1002.

Matched pairs (7)
- Card takings 1840 (3 Oct), 2260 (14 Oct), 1975 (24 Oct); Rent 1200; Electricity 185; Cheque 1042 640 (20 Oct in the books, 21 Oct at the bank); Wages 2400.

Timing differences (no entry needed; they should show on November's statement)
- Outstanding cheque 1043, Tyre supplier, 310 (in the books 30 Oct, not yet at the bank).
- Deposit in transit, Deposit slip 118, 1120 (in the books 31 Oct, not yet at the bank).

Adjustments (need an entry in the books)
- Monthly account fee 15 (bank only).
- Interest paid 3 (bank only).

The planted mistake (try to find it before you look)
- Cheque 1041, Wheel parts supplier: the bank paid 1530, the cash book says 1350. Difference 180 (180 / 9 = 20: two digits swapped).
- For this practice, the supplier's invoice is for 1530, so the cash book is wrong, not the bank.

The reconciliation
- Bank: 4308 + 1120 (deposit in transit) - 310 (outstanding cheque) = 5118.
- Books: 5310 + 3 (interest) - 15 (fee) - 180 (cheque 1041) = 5118.
- Difference: 0.

Draft journal entries, 31 October 2026 (approve each one before typing it into your books)
- Debit Bank charges 15, Credit Bank 15: monthly account fee.
- Debit Bank 3, Credit Interest received 3: bank interest.
- Debit Parts 180, Credit Bank 180: correct cheque 1041 from 1350 to 1530 (invoice 1530).
- Debits equal credits in each entry. No entry for the outstanding cheque or the deposit in transit.

Check Claude's work by hand
- Re-add both sides: both should come to 5118, difference 0.
- Tick every match: 10 payments on each side, each with a partner or a reason, nothing counted twice.
- Each draft entry: debits = credits. Next month: cheque 1043 (310) and the 1120 deposit should show on November's bank statement.

Safety
- Not accounting, tax or financial advice. A qualified accountant checks anything real.
- What you paste goes to Anthropic. Blank out account numbers, card numbers and customer names, and follow your employer's rules.
```
