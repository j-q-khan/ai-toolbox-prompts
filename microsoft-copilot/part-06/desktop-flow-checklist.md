# Power Automate for desktop: your first desktop flow, test file to a new workbook (checked 2026-11-17)
# Windows 10 or 11 only: no Mac, no ARM. Made-up test file only, in a test folder.
# Run it attended, while you watch. Follow your employer's rules on what you may install and automate.

## 0. What you need
- [ ] Windows 10 or 11 on a PC without an ARM processor
- [ ] Excel installed on that PC
- [ ] test-orders.csv from this folder (five made-up orders)
- [ ] Power Automate for desktop: build 2611 (10 November 2026) was the latest when checked

## 1. Install it (one way only, never both)
- [ ] Windows 11: search the Windows search bar for Power Automate; it downloads and opens the first time you select it
- [ ] Or the Microsoft Store version: no admin rights needed, updates itself
- [ ] Or the installer from Microsoft's download page (Setup.Microsoft.PowerAutomate.exe): needs admin rights
- [ ] Windows 10: download it first (Microsoft Store or the installer below)
- [ ] At work: ask the people who run your computers which install they allow
- [ ] Which one do you have? In the Windows apps list, "Power Automate for desktop" is the installer version and "Power Automate" is the Store version

## 2. What you can use
- [ ] Windows 11, no paid plan: attended desktop flows for personal productivity, in the default environment only
- [ ] Sharing flows, or starting them from the cloud: the Power Automate Premium plan
- [ ] Windows Home: flows run on your own PC; they can't be started from the cloud
- [ ] Unattended flows (nobody at the PC): the Power Automate Process plan, one per machine; not built here

## 3. Test folder
- [ ] Make a folder called Desktop flow test inside Documents
- [ ] Save test-orders.csv into it
- [ ] Shut test-orders.csv in Excel before you run the flow

## 4. New flow
- [ ] In the main Power Automate window, select New flow, type a name, select Create
- [ ] The flow designer opens: the Actions pane on the left, the workspace in the middle

## 5. Action 1: File, then Read from CSV file
- [ ] File path: pick Desktop flow test\test-orders.csv with the file button at the end of the box
- [ ] First line contains column names: off (the headings come across as the first line)
- [ ] Advanced, Columns separator: Custom
- [ ] Custom separator: , (one comma)
- [ ] Variables produced: CSVTable
- [ ] Select Save to add the action

## 6. Action 2: Excel, then Launch Excel
- [ ] Launch Excel: With a blank document
- [ ] Make instance visible: on (so you can watch)
- [ ] Variables produced: ExcelInstance

## 7. Action 3: Excel, then Write to Excel worksheet
- [ ] Excel instance: %ExcelInstance%
- [ ] Value to write: %CSVTable% (pick it with the {x} button)
- [ ] Write mode: On specified cell
- [ ] Column: 1
- [ ] Row: 1

## 8. Action 4: Excel, then Close Excel
- [ ] Before closing Excel: Save document as
- [ ] Document format: Excel Workbook (.xlsx)
- [ ] Document path: the same folder as in step 5, with the name test-orders-copy (copy the folder part from step 5's File path)
- [ ] Never save over test-orders.csv
- [ ] Select Save in the designer's toolbar

## 9. Know how to stop it, before you run it
- [ ] In the designer: Stop, beside Run in the toolbar
- [ ] Started from the main Power Automate window: Stop on the flow's line in My flows, or on the notification or monitoring window (Settings, Flow run control, picks which one shows)
- [ ] Settings, Flow run control: set your own stop shortcut (Microsoft documents no default one)

## 10. Run it and check it
- [ ] Select Run and watch: Excel opens a blank workbook, fills it, saves it and shuts
- [ ] Open test-orders-copy.xlsx in your test folder (no file? add .xlsx to the end of Document path and run again)
- [ ] Check one order by hand against test-orders.csv, for example 1003, Stapler, 2, 7

## 11. Later
- [ ] The recorder (designer toolbar, Recorder): captures clicks and typing in apps with no ready-made action; loops can't be captured; expect to delete extra steps
- [ ] Right-click the flow in the main window, Properties: give it its own keyboard shortcut

Sources: learn.microsoft.com "Install Power Automate"; "Prerequisites and limitations"; "Power Automate licensing FAQ"; "Power Automate for desktop console"; "Runtime notifications"; "Run desktop flows via keyboard shortcuts"; "Create desktop flows"; "Convert a CSV file into an Excel spreadsheet"; "File actions reference"; "Excel actions reference"; "Record desktop flows"; "Run unattended desktop flows"; "Released versions of Power Automate for desktop"
